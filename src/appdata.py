"""Per-user storage: settings and usage stats live in the OS app-data folder.

Writing next to the executable fails when the app is installed under
Program Files, so everything goes to:

- Windows: %APPDATA%\\GooglePlayReviewsScraper
- macOS:   ~/Library/Application Support/GooglePlayReviewsScraper
- Linux:   $XDG_CONFIG_HOME/google-play-reviews-scraper (~/.config/...)
"""

from __future__ import annotations

import json
import logging
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

log = logging.getLogger("gplay_reviews")

APP_NAME = "GooglePlayReviewsScraper"


def user_data_dir() -> Path:
    override = os.environ.get("GPRS_DATA_DIR")
    if override:
        path = Path(override)
    elif sys.platform == "win32":
        path = Path(os.environ.get("APPDATA") or Path.home() / "AppData" / "Roaming") / APP_NAME
    elif sys.platform == "darwin":
        path = Path.home() / "Library" / "Application Support" / APP_NAME
    else:
        base = os.environ.get("XDG_CONFIG_HOME") or Path.home() / ".config"
        path = Path(base) / "google-play-reviews-scraper"
    path.mkdir(parents=True, exist_ok=True)
    return path


def resource_path(*parts: str) -> Path:
    """Locate bundled assets both from source and inside a PyInstaller build."""
    base = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parent.parent))
    return base.joinpath(*parts)


class JsonStore:
    """A small dict persisted as JSON. Failures are logged, never raised."""

    def __init__(self, filename: str, defaults: dict[str, Any]):
        self.path = user_data_dir() / filename
        self.data = dict(defaults)
        try:
            if self.path.exists():
                self.data.update(json.loads(self.path.read_text(encoding="utf-8")))
        except (OSError, ValueError) as exc:
            log.warning("Could not read %s: %s", self.path, exc)

    def __getitem__(self, key: str) -> Any:
        return self.data[key]

    def get(self, key: str, default: Any = None) -> Any:
        return self.data.get(key, default)

    def update(self, **values: Any) -> None:
        self.data.update(values)
        self.save()

    def save(self) -> None:
        try:
            tmp = self.path.with_suffix(".tmp")
            tmp.write_text(json.dumps(self.data, ensure_ascii=False, indent=2), encoding="utf-8")
            tmp.replace(self.path)
        except OSError as exc:
            log.warning("Could not write %s: %s", self.path, exc)


def default_output_dir() -> str:
    docs = Path.home() / "Documents"
    return str((docs if docs.is_dir() else Path.home()) / "Google Play Reviews")


def load_settings() -> JsonStore:
    return JsonStore(
        "settings.json",
        {
            "ui_language": None,      # None = detect from OS on first run
            "country": "br",
            "review_language": "pt",
            "output_dir": default_output_dir(),
            "formats": ["csv", "json"],
            "appearance": "system",   # system | light | dark
            "show_log": False,
        },
    )


class TimeStats:
    """Cumulative "time saved" counter shown after each collection."""

    SECONDS_PER_REVIEW = 30  # rough cost of copying one review by hand

    def __init__(self) -> None:
        self.store = JsonStore(
            "time_stats.json",
            {
                "total_reviews_collected": 0,
                "total_time_saved_seconds": 0,
                "total_sessions": 0,
                "first_use": None,
                "last_use": None,
            },
        )

    def add_session(self, reviews_count: int) -> int:
        if reviews_count <= 0:
            return 0
        saved = reviews_count * self.SECONDS_PER_REVIEW
        now = datetime.now().isoformat(timespec="seconds")
        d = self.store.data
        d["total_reviews_collected"] += reviews_count
        d["total_time_saved_seconds"] += saved
        d["total_sessions"] += 1
        d["first_use"] = d["first_use"] or now
        d["last_use"] = now
        self.store.save()
        return saved

    @property
    def total_reviews(self) -> int:
        return self.store["total_reviews_collected"]

    @property
    def total_seconds(self) -> int:
        return self.store["total_time_saved_seconds"]

    @property
    def total_sessions(self) -> int:
        return self.store["total_sessions"]


def format_duration(seconds: int) -> str:
    seconds = int(seconds)
    if seconds < 60:
        return f"{seconds}s"
    if seconds < 3600:
        m, s = divmod(seconds, 60)
        return f"{m}min {s}s" if s else f"{m}min"
    h, rem = divmod(seconds, 3600)
    m = rem // 60
    return f"{h}h {m}min" if m else f"{h}h"
