"""Desktop app for Google Play Reviews Scraper (Windows, macOS and Linux).

Threading model: scraping runs in a worker thread that never touches Tk.
It posts events to a queue that the UI thread drains every few ms, and it
is stopped through a ``threading.Event`` checked between every batch.
"""

from __future__ import annotations

import logging
import os
import queue
import subprocess
import sys
import threading
import webbrowser
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from tkinter import filedialog, messagebox
from typing import Optional

import customtkinter as ctk

from appdata import TimeStats, format_duration, load_settings, resource_path
from review_scraper import (
    GooglePlayReviewScraper,
    ScrapeResult,
    parse_app_id,
)
from translations import LANGUAGES, Translator, code_from_choice, detect_language

__version__ = "2.0.0"
REPO_URL = "https://github.com/dssiqueira/google-play-reviews-scraper"

THEME_FILE = resource_path("assets", "theme.json")
ctk.set_default_color_theme(str(THEME_FILE))
APP_COLORS = ctk.ThemeManager.theme["_app"]
MUTED = APP_COLORS["muted"]

FORMAT_LABELS = {"csv": "CSV", "json": "JSON", "xlsx": "Excel"}
APPEARANCES = ("system", "light", "dark")
POLL_MS = 60


def open_path(path: Path | str) -> None:
    """Open a file or folder with the OS default handler."""
    path = str(path)
    if sys.platform == "win32":
        os.startfile(path)  # noqa: S606 - local file chosen by the user
    elif sys.platform == "darwin":
        subprocess.Popen(["open", path])
    else:
        subprocess.Popen(["xdg-open", path])


def font(size: int = 13, weight: str = "normal") -> ctk.CTkFont:
    return ctk.CTkFont(size=size, weight=weight)


# --------------------------------------------------------------------------- #
# Queue model
# --------------------------------------------------------------------------- #
@dataclass
class QueueItem:
    app_id: str
    state: str = "pending"            # pending | running | done | partial | error | skipped
    detail: str = ""
    title: str = ""
    files: dict[str, Path] = field(default_factory=dict)
    result: Optional[ScrapeResult] = None


class QueueRow(ctk.CTkFrame):
    DOT = {
        "pending": MUTED, "running": APP_COLORS["warning"], "done": APP_COLORS["accent"],
        "partial": APP_COLORS["warning"], "error": APP_COLORS["danger"], "skipped": MUTED,
    }

    def __init__(self, master, app: App, item: QueueItem):
        super().__init__(master, fg_color=APP_COLORS["inset"], corner_radius=8)
        self.app, self.item = app, item
        self.grid_columnconfigure(1, weight=1)

        self.dot = ctk.CTkLabel(self, text="●", width=18, font=font(14))
        self.dot.grid(row=0, column=0, rowspan=2, padx=(10, 4), pady=6)
        self.name = ctk.CTkLabel(self, text="", anchor="w", font=font(13, "bold"))
        self.name.grid(row=0, column=1, sticky="ew", pady=(6, 0))
        self.sub = ctk.CTkLabel(self, text="", anchor="w", font=font(12), text_color=MUTED)
        self.sub.grid(row=1, column=1, sticky="ew", pady=(0, 6))

        self.open_btn = ctk.CTkButton(
            self, width=64, height=26, font=font(12),
            command=lambda: self.app.open_result(self.item),
        )
        self.remove_btn = ctk.CTkButton(
            self, text="✕", width=28, height=26, font=font(12),
            fg_color="transparent", hover_color=APP_COLORS["neutral_hover"], text_color=MUTED,
            text_color_disabled=APP_COLORS["faint"],
            command=lambda: self.app.remove_app(self.item.app_id),
        )
        self.remove_btn.grid(row=0, column=3, rowspan=2, padx=(4, 8))
        self.refresh()

    def refresh(self) -> None:
        t, it = self.app.t, self.item
        self.name.configure(text=it.title or it.app_id)
        sub = {
            "pending": t("status_pending"),
            "running": it.detail or t("status_running"),
            "done": it.detail,
            "partial": it.detail,
            "error": t("status_error", it.detail),
            "skipped": t("status_skipped"),
        }[it.state]
        if it.title and it.title != it.app_id:
            sub = f"{it.app_id} · {sub}"
        self.sub.configure(text=sub)
        self.dot.configure(text_color=self.DOT[it.state])

        self.open_btn.configure(text=t("open"))
        if it.files:
            self.open_btn.grid(row=0, column=2, rowspan=2, padx=(4, 0))
        else:
            self.open_btn.grid_remove()
        self.remove_btn.configure(state="disabled" if self.app.running else "normal")


# --------------------------------------------------------------------------- #
# Main window
# --------------------------------------------------------------------------- #
class App(ctk.CTk):
    def __init__(self) -> None:
        self.settings = load_settings()
        self.stats = TimeStats()
        self.t = Translator(self.settings.get("ui_language") or detect_language())
        ctk.set_appearance_mode(self.settings.get("appearance", "system"))

        super().__init__()
        self.title("Google Play Reviews Scraper")
        self.geometry("1000x740")
        self.minsize(880, 720)
        self._set_icon()

        self.items: list[QueueItem] = []
        self.rows: dict[str, QueueRow] = {}
        self.running = False
        self.cancel_event = threading.Event()
        self.events: queue.Queue[tuple] = queue.Queue()
        self.log_visible = bool(self.settings.get("show_log"))

        self.grid_columnconfigure(0, weight=3, uniform="cols")
        self.grid_columnconfigure(1, weight=2, uniform="cols")
        self.grid_rowconfigure(1, weight=1)

        self._build_header()
        self._build_apps_card()
        self._build_options_card()
        self._build_progress_card()
        self._attach_library_logs()
        self.apply_texts()
        self._render_queue()

        self.bind("<Return>", lambda e: self.add_from_entry())
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.after(POLL_MS, self._drain_events)

    # -- setup ------------------------------------------------------------ #
    def _set_icon(self) -> None:
        try:
            if sys.platform == "win32":
                self.iconbitmap(str(resource_path("assets", "icons", "google-play.ico")))
            else:
                from tkinter import PhotoImage
                self._icon = PhotoImage(file=str(resource_path("assets", "icons", "google-play.png")))
                self.iconphoto(True, self._icon)
        except Exception:  # noqa: BLE001 - a missing icon is not fatal
            pass

    def _logo(self) -> Optional[ctk.CTkImage]:
        try:
            from PIL import Image
            img = Image.open(resource_path("assets", "icons", "google-play.png"))
            return ctk.CTkImage(light_image=img, dark_image=img, size=(40, 40))
        except Exception:  # noqa: BLE001
            return None

    def _build_header(self) -> None:
        bar = ctk.CTkFrame(self, fg_color="transparent")
        bar.grid(row=0, column=0, columnspan=2, sticky="ew", padx=20, pady=(16, 10))
        bar.grid_columnconfigure(1, weight=1)

        logo = self._logo()
        ctk.CTkLabel(bar, text="", image=logo, width=40).grid(row=0, column=0, rowspan=2, padx=(0, 12))
        ctk.CTkLabel(bar, text="Google Play Reviews Scraper", font=font(21, "bold"), anchor="w").grid(
            row=0, column=1, sticky="w")
        self.subtitle = ctk.CTkLabel(bar, text="", font=font(13), text_color=MUTED, anchor="w")
        self.subtitle.grid(row=1, column=1, sticky="w")

        tools = ctk.CTkFrame(bar, fg_color="transparent")
        tools.grid(row=0, column=2, rowspan=2, sticky="e")

        self.lang_menu = ctk.CTkOptionMenu(
            tools, values=list(LANGUAGES.values()), width=124, command=self.on_language,
        )
        self.lang_menu.set(LANGUAGES[self.t.language])
        self.lang_menu.pack(side="left", padx=(0, 8))

        self.theme_seg = ctk.CTkSegmentedButton(tools, command=self.on_appearance)
        self.theme_seg.pack(side="left", padx=(0, 8))

        self.about_btn = ctk.CTkButton(
            tools, width=36, text="?", font=font(14, "bold"),
            fg_color=APP_COLORS["neutral"], hover_color=APP_COLORS["neutral_hover"],
            text_color=ctk.ThemeManager.theme["CTkLabel"]["text_color"],
            command=self.show_about,
        )
        self.about_btn.pack(side="left")

    def _card(self, row: int, column: int, **grid) -> ctk.CTkFrame:
        card = ctk.CTkFrame(self)
        card.grid(row=row, column=column, sticky="nsew", **grid)
        return card

    def _build_apps_card(self) -> None:
        card = self._card(1, 0, padx=(20, 8), pady=(0, 12))
        card.grid_columnconfigure(0, weight=1)
        card.grid_rowconfigure(3, weight=1)

        self.apps_title = ctk.CTkLabel(card, text="", font=font(15, "bold"), anchor="w")
        self.apps_title.grid(row=0, column=0, columnspan=2, sticky="w", padx=16, pady=(14, 8))

        self.entry = ctk.CTkEntry(card, height=36)
        self.entry.grid(row=1, column=0, sticky="ew", padx=(16, 8))
        self.entry.bind("<<Paste>>", self._on_paste)
        self.add_btn = ctk.CTkButton(card, height=36, width=100, command=self.add_from_entry)
        self.add_btn.grid(row=1, column=1, padx=(0, 16))

        self.hint = ctk.CTkLabel(card, text="", font=font(12), text_color=MUTED, anchor="w",
                                 justify="left", wraplength=520)
        self.hint.grid(row=2, column=0, columnspan=2, sticky="ew", padx=18, pady=(4, 6))

        self.queue_frame = ctk.CTkScrollableFrame(card, fg_color="transparent")
        self.queue_frame.grid(row=3, column=0, columnspan=2, sticky="nsew", padx=8)
        self.queue_frame.grid_columnconfigure(0, weight=1)
        self.empty_label = ctk.CTkLabel(self.queue_frame, text="", font=font(13), text_color=MUTED)

        self.log_box = ctk.CTkTextbox(card, font=ctk.CTkFont(family="Courier", size=12), wrap="word")
        self.log_box.configure(state="disabled")
        self._place_log()

        foot = ctk.CTkFrame(card, fg_color="transparent")
        foot.grid(row=4, column=0, columnspan=2, sticky="ew", padx=16, pady=(6, 12))
        foot.grid_columnconfigure(0, weight=1)
        self.queue_count = ctk.CTkLabel(foot, text="", font=font(12), text_color=MUTED, anchor="w")
        self.queue_count.grid(row=0, column=0, sticky="w")
        self.clear_btn = ctk.CTkButton(
            foot, height=26, width=10, font=font(12), fg_color="transparent",
            hover_color=APP_COLORS["neutral_hover"], text_color=MUTED,
            text_color_disabled=APP_COLORS["faint"], command=self.clear_queue,
        )
        self.clear_btn.grid(row=0, column=1, sticky="e")

    def _field_label(self, parent, row: int) -> ctk.CTkLabel:
        label = ctk.CTkLabel(parent, text="", font=font(12, "bold"), text_color=MUTED, anchor="w")
        label.grid(row=row, column=0, columnspan=2, sticky="w", padx=16, pady=(10, 2))
        return label

    def _build_options_card(self) -> None:
        card = self._card(1, 1, padx=(8, 20), pady=(0, 12))
        card.grid_columnconfigure((0, 1), weight=1)
        s = self.settings

        self.options_title = ctk.CTkLabel(card, text="", font=font(15, "bold"), anchor="w")
        self.options_title.grid(row=0, column=0, columnspan=2, sticky="w", padx=16, pady=(14, 0))

        self.country_label = self._field_label(card, 1)
        self.country_box = ctk.CTkComboBox(card, height=34, command=lambda _: self._save_options())
        self.country_box.grid(row=2, column=0, columnspan=2, sticky="ew", padx=16)

        self.rlang_label = self._field_label(card, 3)
        self.rlang_box = ctk.CTkComboBox(
            card, height=34, values=self.t.review_language_choices(),
            command=lambda _: self._save_options(),
        )
        self.rlang_box.set(self.t.review_language_label(s["review_language"]))
        self.rlang_box.grid(row=4, column=0, columnspan=2, sticky="ew", padx=16)

        self.limit_label = ctk.CTkLabel(card, text="", font=font(12, "bold"), text_color=MUTED, anchor="w")
        self.limit_label.grid(row=5, column=0, sticky="w", padx=(16, 4), pady=(10, 2))
        self.since_label = ctk.CTkLabel(card, text="", font=font(12, "bold"), text_color=MUTED, anchor="w")
        self.since_label.grid(row=5, column=1, sticky="w", padx=(4, 16), pady=(10, 2))
        self.limit_entry = ctk.CTkEntry(card, height=34)
        self.limit_entry.grid(row=6, column=0, sticky="ew", padx=(16, 4))
        self.since_entry = ctk.CTkEntry(card, height=34)
        self.since_entry.grid(row=6, column=1, sticky="ew", padx=(4, 16))

        self.formats_label = self._field_label(card, 7)
        fmt_row = ctk.CTkFrame(card, fg_color="transparent")
        fmt_row.grid(row=8, column=0, columnspan=2, sticky="w", padx=16)
        self.format_vars: dict[str, ctk.BooleanVar] = {}
        for fmt, label in FORMAT_LABELS.items():
            var = ctk.BooleanVar(value=fmt in s["formats"])
            ctk.CTkCheckBox(
                fmt_row, text=label, variable=var, width=80, checkbox_width=20, checkbox_height=20,
                command=self._save_options,
            ).pack(side="left", padx=(0, 6))
            self.format_vars[fmt] = var

        self.folder_label = self._field_label(card, 9)
        self.folder_value = ctk.CTkLabel(
            card, text="", anchor="w", justify="left", font=font(12), fg_color=APP_COLORS["inset"],
            corner_radius=8, height=34, wraplength=330,
        )
        self.folder_value.grid(row=10, column=0, columnspan=2, sticky="ew", padx=16)
        btns = ctk.CTkFrame(card, fg_color="transparent")
        btns.grid(row=11, column=0, columnspan=2, sticky="ew", padx=16, pady=(8, 16))
        btns.grid_columnconfigure((0, 1), weight=1)
        neutral = dict(fg_color=APP_COLORS["neutral"], hover_color=APP_COLORS["neutral_hover"],
                       text_color=ctk.ThemeManager.theme["CTkLabel"]["text_color"],
                       text_color_disabled=APP_COLORS["faint"], height=32)
        self.choose_btn = ctk.CTkButton(btns, command=self.choose_folder, **neutral)
        self.choose_btn.grid(row=0, column=0, sticky="ew", padx=(0, 4))
        self.open_folder_btn = ctk.CTkButton(
            btns, command=lambda: self.open_output_dir(), **neutral)
        self.open_folder_btn.grid(row=0, column=1, sticky="ew", padx=(4, 0))
        self._show_folder()

        card.grid_rowconfigure(12, weight=1)  # push content to the top

    def _build_progress_card(self) -> None:
        card = self._card(2, 0, columnspan=2, padx=20, pady=(0, 20))
        card.grid_columnconfigure(0, weight=1)
        self.progress_card = card

        self.status = ctk.CTkLabel(card, text="", font=font(14, "bold"), anchor="w")
        self.status.grid(row=0, column=0, sticky="ew", padx=(18, 8), pady=(14, 0))
        self.counter = ctk.CTkLabel(card, text="", font=font(13), text_color=MUTED, anchor="e")
        self.counter.grid(row=0, column=1, sticky="e", padx=(8, 18), pady=(14, 0))

        self.bar = ctk.CTkProgressBar(card, height=10)
        self.bar.grid(row=1, column=0, columnspan=2, sticky="ew", padx=18, pady=(10, 12))
        self._bar_value(0)

        actions = ctk.CTkFrame(card, fg_color="transparent")
        actions.grid(row=2, column=0, columnspan=2, sticky="ew", padx=18, pady=(0, 14))
        actions.grid_columnconfigure(0, weight=1)
        self.log_toggle = ctk.CTkButton(
            actions, width=10, height=30, font=font(12), fg_color="transparent",
            hover_color=APP_COLORS["neutral_hover"], text_color=MUTED, command=self.toggle_log,
        )
        self.log_toggle.grid(row=0, column=0, sticky="w")
        self.main_btn = ctk.CTkButton(
            actions, height=42, width=220, font=font(15, "bold"), command=self.on_main_button,
        )
        self.main_btn.grid(row=0, column=1, sticky="e")


    def _attach_library_logs(self) -> None:
        """Forward the scraper's warnings (retries, failures) to the log panel."""
        app = self

        class Handler(logging.Handler):
            def emit(self, record: logging.LogRecord) -> None:
                app.events.put(("log", record.getMessage()))

        handler = Handler(level=logging.WARNING)
        logger = logging.getLogger("gplay_reviews")
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

    # -- texts ------------------------------------------------------------ #
    def apply_texts(self) -> None:
        t = self.t
        self.subtitle.configure(text=t("subtitle"))
        self.theme_seg.configure(values=[t("theme_system"), t("theme_light"), t("theme_dark")])
        self.theme_seg.set(t(f"theme_{self.settings.get('appearance', 'system')}"))
        self.apps_title.configure(text=t("apps_title"))
        self.entry.configure(placeholder_text=t("url_placeholder"))
        self.add_btn.configure(text=t("add"))
        self._hint(t("paste_hint"))
        self.empty_label.configure(text=t("queue_empty"))
        self.clear_btn.configure(text=t("clear"))
        self.options_title.configure(text=t("options_title"))
        self.country_label.configure(text=t("country"))
        self.country_box.configure(values=t.country_choices())
        self.country_box.set(t.country_label(self.settings["country"]))
        self.rlang_label.configure(text=t("review_language"))
        self.limit_label.configure(text=t("limit"))
        self.since_label.configure(text=t("since"))
        self.limit_entry.configure(placeholder_text=t("limit_placeholder"))
        self.since_entry.configure(placeholder_text=t("since_placeholder"))
        self.formats_label.configure(text=t("formats"))
        self.folder_label.configure(text=t("folder"))
        self.choose_btn.configure(text=t("choose"))
        self.open_folder_btn.configure(text=t("open_folder"))
        self.log_toggle.configure(text=("▾ " + t("hide_log")) if self.log_visible else ("▸ " + t("show_log")))
        self._style_main_button()
        if not self.running:
            self.status.configure(text=t("ready"))
        self._update_queue_count()
        for row in self.rows.values():
            row.refresh()

    def _style_main_button(self) -> None:
        if self.running:
            stopping = self.cancel_event.is_set()
            self.main_btn.configure(
                text=self.t("stopping") if stopping else self.t("stop"),
                fg_color=APP_COLORS["danger"], hover_color=APP_COLORS["danger_hover"],
                state="disabled" if stopping else "normal",
            )
        else:
            theme = ctk.ThemeManager.theme["CTkButton"]
            self.main_btn.configure(
                text=self.t("start"), fg_color=theme["fg_color"],
                hover_color=theme["hover_color"], state="normal",
            )

    def _hint(self, text: str, error: bool = False) -> None:
        self.hint.configure(text=text, text_color=APP_COLORS["danger"] if error else MUTED)

    # -- header actions --------------------------------------------------- #
    def on_language(self, name: str) -> None:
        code = next(c for c, n in LANGUAGES.items() if n == name)
        self.lang_menu.set(name)
        self.t.set_language(code)
        self.settings.update(ui_language=code)
        self.apply_texts()

    def on_appearance(self, label: str) -> None:
        mode = next(m for m in APPEARANCES if self.t(f"theme_{m}") == label)
        ctk.set_appearance_mode(mode)
        self.settings.update(appearance=mode)

    # -- queue ------------------------------------------------------------ #
    def _on_paste(self, _event) -> str:
        try:
            text = self.clipboard_get()
        except Exception:  # noqa: BLE001 - empty / non-text clipboard
            return ""
        if "\n" in text.strip():
            self.add_inputs(text.splitlines())
            return "break"
        return ""

    def add_from_entry(self) -> None:
        text = self.entry.get()
        if text.strip():
            self.add_inputs(text.split())

    def add_inputs(self, lines: list[str]) -> None:
        added, problems = 0, []
        known = {it.app_id for it in self.items}
        for line in (ln.strip() for ln in lines):
            if not line:
                continue
            try:
                app_id = parse_app_id(line)
            except ValueError:
                problems.append(self.t("invalid_input", line[:60]))
                continue
            if app_id in known:
                problems.append(self.t("already_queued", app_id))
                continue
            known.add(app_id)
            self.items.append(QueueItem(app_id))
            added += 1

        if added:
            self.entry.delete(0, "end")
            self._render_queue()
        if problems:
            more = f"  (+{len(problems) - 1})" if len(problems) > 1 else ""
            self._hint(problems[0] + more, error=True)
        else:
            self._hint(self.t("paste_hint"))

    def remove_app(self, app_id: str) -> None:
        if self.running:
            return
        self.items = [it for it in self.items if it.app_id != app_id]
        self._render_queue()

    def clear_queue(self) -> None:
        if self.running:
            return
        self.items.clear()
        self._render_queue()

    def _render_queue(self) -> None:
        for app_id in list(self.rows):
            if app_id not in {it.app_id for it in self.items}:
                self.rows.pop(app_id).destroy()
        for i, item in enumerate(self.items):
            row = self.rows.get(item.app_id)
            if row is None:
                row = self.rows[item.app_id] = QueueRow(self.queue_frame, self, item)
            row.grid(row=i, column=0, sticky="ew", padx=4, pady=3)
        if self.items:
            self.empty_label.grid_forget()
        else:
            self.empty_label.grid(row=0, column=0, pady=40)
        self._update_queue_count()

    def _update_queue_count(self) -> None:
        n = len(self.items)
        self.queue_count.configure(
            text=self.t("queue_count_one") if n == 1 else self.t("queue_count_many", n) if n else "")
        state = "disabled" if self.running or not n else "normal"
        self.clear_btn.configure(state=state)

    def _refresh_row(self, item: QueueItem) -> None:
        row = self.rows.get(item.app_id)
        if row:
            row.refresh()

    # -- options ---------------------------------------------------------- #
    def _save_options(self) -> None:
        self.settings.update(
            country=code_from_choice(self.country_box.get()) or self.settings["country"],
            review_language=code_from_choice(self.rlang_box.get()) or self.settings["review_language"],
            formats=[f for f, v in self.format_vars.items() if v.get()],
        )

    def _show_folder(self) -> None:
        self.folder_value.configure(text="  " + self.settings["output_dir"])

    def choose_folder(self) -> None:
        folder = filedialog.askdirectory(initialdir=self.settings["output_dir"])
        if folder:
            self.settings.update(output_dir=folder)
            self._show_folder()

    def open_output_dir(self) -> None:
        folder = Path(self.settings["output_dir"])
        folder.mkdir(parents=True, exist_ok=True)
        open_path(folder)

    def open_result(self, item: QueueItem) -> None:
        for fmt in ("xlsx", "csv", "json"):
            if fmt in item.files and item.files[fmt].exists():
                open_path(item.files[fmt])
                return

    def _read_options(self) -> Optional[dict]:
        """Validate the form; show an error and return None if invalid."""
        t = self.t
        if not self.items:
            return self._error(t("err_no_apps"))

        limit_raw = self.limit_entry.get().strip().replace(".", "").replace(",", "")
        limit = None
        if limit_raw:
            if not limit_raw.isdigit() or int(limit_raw) <= 0:
                return self._error(t("err_limit"))
            limit = int(limit_raw)

        since_raw = self.since_entry.get().strip()
        since = None
        if since_raw:
            try:
                since = date.fromisoformat(since_raw)
            except ValueError:
                return self._error(t("err_since"))

        formats = [f for f, v in self.format_vars.items() if v.get()]
        if not formats:
            return self._error(t("err_no_format"))

        out = Path(self.settings["output_dir"]).expanduser()
        try:
            out.mkdir(parents=True, exist_ok=True)
        except OSError as exc:
            return self._error(t("err_folder", exc))

        self._save_options()
        return {
            "country": self.settings["country"],
            "lang": self.settings["review_language"],
            "max_reviews": limit,
            "since": since,
            "formats": formats,
            "output_dir": out,
        }

    def _error(self, message: str) -> None:
        messagebox.showerror(self.t("error_title"), message, parent=self)
        return None

    # -- run -------------------------------------------------------------- #
    def on_main_button(self) -> None:
        if self.running:
            self.cancel_event.set()
            self._style_main_button()
            self.status.configure(text=self.t("stopping"))
        else:
            self.start()

    def start(self) -> None:
        opts = self._read_options()
        if not opts:
            return
        for it in self.items:
            it.state, it.detail, it.files, it.result = "pending", "", {}, None
        self.running = True
        self.cancel_event.clear()
        self._set_inputs_enabled(False)
        self._style_main_button()
        self._bar_value(0)
        self.counter.configure(text="")
        self._clear_log()
        for row in self.rows.values():
            row.refresh()

        app_ids = [it.app_id for it in self.items]
        threading.Thread(target=self._worker, args=(app_ids, opts), daemon=True).start()

    def _worker(self, app_ids: list[str], opts: dict) -> None:
        """Runs off the UI thread. Talks to the UI only through self.events."""
        post = self.events.put
        scraper = GooglePlayReviewScraper(country=opts["country"], lang=opts["lang"])
        for index, app_id in enumerate(app_ids):
            if self.cancel_event.is_set():
                post(("skipped", index))
                continue
            post(("app_start", index))
            try:
                result = scraper.scrape(
                    app_id,
                    max_reviews=opts["max_reviews"],
                    since=opts["since"],
                    cancel_event=self.cancel_event,
                    on_progress=lambda done, total, i=index: post(("progress", i, done, total)),
                )
                files = {}
                if result.reviews:
                    files = scraper.save_reviews(
                        result.reviews, result.app_info,
                        output_dir=opts["output_dir"], formats=opts["formats"],
                    )
                post(("app_done", index, result, files))
            except Exception as exc:  # noqa: BLE001 - report and move on
                post(("app_failed", index, str(exc)))
        post(("finished",))

    def _drain_events(self) -> None:
        try:
            while True:
                event = self.events.get_nowait()
                getattr(self, f"_on_{event[0]}")(*event[1:])
        except queue.Empty:
            pass
        self.after(POLL_MS, self._drain_events)

    # event handlers (UI thread) ----------------------------------------- #
    def _on_log(self, message: str) -> None:
        self._log(message)

    def _on_app_start(self, index: int) -> None:
        item = self.items[index]
        item.state = "running"
        self._refresh_row(item)
        self.status.configure(text=self.t("app_progress", index + 1, len(self.items), item.title or item.app_id))
        self._log(self.t("log_start", item.app_id, self.settings["country"], self.settings["review_language"]))
        self._set_bar(index, 0.0)

    def _on_progress(self, index: int, done: int, total: Optional[int]) -> None:
        t, item = self.t, self.items[index]
        text = t("count_progress_total", t.num(done), t.num(total)) if total else t("count_progress", t.num(done))
        self.counter.configure(text=text)
        item.detail = text
        self._refresh_row(item)
        self._set_bar(index, min(done / total, 0.99) if total else 0.0)

    def _on_app_done(self, index: int, result: ScrapeResult, files: dict) -> None:
        t, item = self.t, self.items[index]
        item.title = result.title
        item.files = files
        item.result = result
        n = len(result.reviews)
        if not n and result.error:
            item.state, item.detail = "error", result.error[:80]
            self._log(t("log_error", item.app_id, result.error))
        elif result.complete:
            item.state, item.detail = "done", t("status_done", t.num(n))
            self._log(t("log_done", result.title, t.num(n)))
        else:
            reason = t("log_cancelled") if result.cancelled else (result.error or "")
            item.state, item.detail = "partial", t("status_partial", t.num(n))
            self._log(t("log_partial", result.title, reason))
        for path in files.values():
            self._log(t("log_saved", path))
        self._refresh_row(item)
        self.status.configure(text=self.t("app_progress", index + 1, len(self.items), item.title))
        self._set_bar(index, 1.0)

    def _on_app_failed(self, index: int, error: str) -> None:
        item = self.items[index]
        item.state, item.detail = "error", error[:80]
        self._log(self.t("log_error", item.app_id, error))
        self._refresh_row(item)
        self._set_bar(index, 1.0)

    def _on_skipped(self, index: int) -> None:
        item = self.items[index]
        item.state = "skipped"
        self._refresh_row(item)

    def _on_finished(self) -> None:
        t = self.t
        cancelled = self.cancel_event.is_set()
        results = [it.result for it in self.items if it.files and it.result]
        total = sum(len(r.reviews) for r in results)

        self.running = False
        self.cancel_event.clear()
        self._set_inputs_enabled(True)
        self._style_main_button()
        for row in self.rows.values():
            row.refresh()

        if not total:
            self.status.configure(text=t("finished_nothing"))
            self._bar_value(0)
            return
        if cancelled:
            self.status.configure(text=t("finished_cancelled", t.num(total)))
        else:
            self.status.configure(text=t("finished", t.num(total), len(results)))
            self._bar_value(1)
        saved = self.stats.add_session(total)
        self.after(250, lambda: SummaryDialog(self, results, total, saved))

    # -- helpers ---------------------------------------------------------- #
    def _set_bar(self, index: int, fraction: float) -> None:
        n = max(len(self.items), 1)
        self._bar_value((index + fraction) / n)

    def _bar_value(self, value: float) -> None:
        # CTkProgressBar draws a dot at 0; paint the fill like the track instead
        color = APP_COLORS["neutral"] if value <= 0 else APP_COLORS["accent"]
        self.bar.configure(progress_color=color)
        self.bar.set(value)

    def _set_inputs_enabled(self, enabled: bool) -> None:
        state = "normal" if enabled else "disabled"
        for w in (self.entry, self.add_btn, self.country_box, self.rlang_box, self.limit_entry,
                  self.since_entry, self.choose_btn, self.lang_menu):
            w.configure(state=state)
        self._update_queue_count()

    def toggle_log(self) -> None:
        self.log_visible = not self.log_visible
        self._place_log()
        self.settings.update(show_log=self.log_visible)
        self.apply_texts()

    def _place_log(self) -> None:
        """The log takes the queue's spot in the Apps card while visible."""
        if self.log_visible:
            self.queue_frame.grid_remove()
            self.log_box.grid(row=3, column=0, columnspan=2, sticky="nsew", padx=16, pady=(0, 4))
        else:
            self.log_box.grid_remove()
            self.queue_frame.grid()

    def _log(self, message: str) -> None:
        from time import strftime
        self.log_box.configure(state="normal")
        self.log_box.insert("end", f"{strftime('%H:%M:%S')}  {message}\n")
        self.log_box.see("end")
        self.log_box.configure(state="disabled")

    def _clear_log(self) -> None:
        self.log_box.configure(state="normal")
        self.log_box.delete("1.0", "end")
        self.log_box.configure(state="disabled")

    def show_about(self) -> None:
        AboutDialog(self)

    def on_close(self) -> None:
        self.cancel_event.set()
        self.destroy()


# --------------------------------------------------------------------------- #
# Dialogs
# --------------------------------------------------------------------------- #
class Dialog(ctk.CTkToplevel):
    def __init__(self, app: App, title: str, width: int, height: int):
        super().__init__(app)
        self.app = app
        self.title(title)
        self.resizable(False, False)
        app.update_idletasks()
        x = app.winfo_rootx() + (app.winfo_width() - width) // 2
        y = app.winfo_rooty() + (app.winfo_height() - height) // 3
        self.geometry(f"{width}x{height}+{max(x, 0)}+{max(y, 0)}")
        self.transient(app)
        self.bind("<Escape>", lambda e: self.destroy())
        self.after(50, self._grab)

    def _grab(self) -> None:
        try:
            self.grab_set()
            self.focus_force()
        except Exception:  # noqa: BLE001 - window may not be viewable yet
            pass


class SummaryDialog(Dialog):
    def __init__(self, app: App, results: list[ScrapeResult], total: int, saved_seconds: int):
        t = app.t
        super().__init__(app, t("done_title"), 460, 545)
        stats = GooglePlayReviewScraper.statistics(r for res in results for r in res.reviews)

        body = ctk.CTkFrame(self)
        body.pack(fill="both", expand=True, padx=16, pady=16)

        ctk.CTkLabel(body, text="✓", font=font(34, "bold"), text_color=APP_COLORS["accent"]).pack(pady=(18, 0))
        ctk.CTkLabel(body, text=t("done_headline", t.num(total)), font=font(22, "bold")).pack()
        ctk.CTkLabel(body, text=t("done_apps", len(results)), text_color=MUTED).pack()

        rating = ctk.CTkFrame(body, fg_color=APP_COLORS["inset"])
        rating.pack(fill="x", padx=20, pady=(16, 8))
        head = ctk.CTkFrame(rating, fg_color="transparent")
        head.pack(fill="x", padx=14, pady=(10, 2))
        ctk.CTkLabel(head, text=t("avg_rating"), font=font(12, "bold"), text_color=MUTED).pack(side="left")
        ctk.CTkLabel(head, text=f"{stats['average']:.2f} ★", font=font(20, "bold")).pack(side="right")
        for star in range(5, 0, -1):
            share = stats["distribution"][star] / stats["total"] if stats["total"] else 0
            line = ctk.CTkFrame(rating, fg_color="transparent")
            line.pack(fill="x", padx=14, pady=1)
            ctk.CTkLabel(line, text=f"{star}★", width=30, anchor="w", font=font(12)).pack(side="left")
            ctk.CTkLabel(line, text=f"{share * 100:.0f}%", width=40, anchor="e", font=font(12),
                         text_color=MUTED).pack(side="right")
            bar = ctk.CTkProgressBar(line, height=8,
                                     progress_color=APP_COLORS["accent"] if share else APP_COLORS["neutral"])
            bar.set(share)
            bar.pack(side="left", fill="x", expand=True, padx=8)
        ctk.CTkFrame(rating, height=10, fg_color="transparent").pack()

        ctk.CTkLabel(body, text=t("done_time", format_duration(saved_seconds)), font=font(14, "bold")).pack(
            pady=(8, 0))
        ctk.CTkLabel(body, text=t("done_compare"), font=font(12), text_color=MUTED).pack()
        st = app.stats
        ctk.CTkLabel(
            body, text=t("done_totals", t.num(st.total_reviews), format_duration(st.total_seconds),
                         st.total_sessions),
            font=font(11), text_color=MUTED, wraplength=380,
        ).pack(pady=(6, 0))

        row = ctk.CTkFrame(body, fg_color="transparent")
        row.pack(side="bottom", fill="x", padx=20, pady=16)
        row.grid_columnconfigure((0, 1), weight=1)
        ctk.CTkButton(row, text=t("open_folder"), height=36, command=lambda: (app.open_output_dir(), self.destroy())
                      ).grid(row=0, column=0, sticky="ew", padx=(0, 4))
        ctk.CTkButton(row, text=t("close"), height=36, fg_color=APP_COLORS["neutral"],
                      hover_color=APP_COLORS["neutral_hover"],
                      text_color=ctk.ThemeManager.theme["CTkLabel"]["text_color"],
                      command=self.destroy).grid(row=0, column=1, sticky="ew", padx=(4, 0))


class AboutDialog(Dialog):
    def __init__(self, app: App):
        t = app.t
        super().__init__(app, t("about"), 400, 330)
        body = ctk.CTkFrame(self)
        body.pack(fill="both", expand=True, padx=16, pady=16)
        logo = app._logo()
        ctk.CTkLabel(body, text="", image=logo).pack(pady=(22, 6))
        ctk.CTkLabel(body, text="Google Play Reviews Scraper", font=font(17, "bold")).pack()
        ctk.CTkLabel(body, text=f"v{__version__} · MIT", text_color=MUTED).pack()
        ctk.CTkLabel(body, text=t("about_text"), wraplength=320, justify="center").pack(pady=(12, 4))
        ctk.CTkLabel(body, text=t("about_author"), text_color=MUTED).pack()
        ctk.CTkButton(body, text=t("about_github"), height=34,
                      command=lambda: webbrowser.open(REPO_URL)).pack(pady=(14, 18))


def main() -> None:
    if sys.platform == "win32":
        try:  # crisp icon in the taskbar instead of the generic Python one
            import ctypes
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("dssiqueira.GooglePlayReviewsScraper")
        except Exception:  # noqa: BLE001
            pass
    App().mainloop()


if __name__ == "__main__":
    main()
