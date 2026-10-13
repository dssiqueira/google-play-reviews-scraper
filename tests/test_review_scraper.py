"""Unit tests for the scraper core. The Play Store is faked; no network needed."""

import json
import sys
import threading
from datetime import date, datetime, timedelta
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import review_scraper as rs  # noqa: E402
from review_scraper import GooglePlayReviewScraper, Review, clean_filename, parse_app_id  # noqa: E402


# --------------------------------------------------------------------------- #
# Fake Play Store
# --------------------------------------------------------------------------- #
class Token:
    def __init__(self, token):
        self.token = token


class FakeStore:
    """Mimics google_play_scraper: newest first, pages of `count`, and on a
    network error returns an empty page with a None token (like the real lib)."""

    def __init__(self, total=450, fail_pages=(), title="My App"):
        self.total = total
        self.fail_pages = set(fail_pages)   # page numbers that fail once
        self.title = title
        self.calls = 0
        self.start = datetime(2026, 10, 1)

    def app(self, app_id, lang, country):
        return {"appId": app_id, "title": self.title, "reviews": self.total}

    def reviews(self, app_id, lang, country, sort, count, continuation_token=None):
        self.calls += 1
        offset = continuation_token.token if continuation_token else 0
        page = offset // 200
        if page in self.fail_pages:
            self.fail_pages.discard(page)
            return [], Token(None)  # what the real library does on errors
        end = min(offset + 200, self.total)
        raw = [
            {
                "reviewId": f"r{i}", "userName": f"user{i}", "content": f"review {i}",
                "score": i % 5 + 1, "thumbsUpCount": i, "at": self.start - timedelta(days=i),
                "replyContent": None, "repliedAt": None, "appVersion": "1.0",
            }
            for i in range(offset, end)
        ]
        return raw, Token(end if end < self.total else None)


@pytest.fixture
def store(monkeypatch):
    fake = FakeStore()
    monkeypatch.setattr(rs, "app", fake.app)
    monkeypatch.setattr(rs, "reviews", fake.reviews)
    return fake


@pytest.fixture
def scraper():
    return GooglePlayReviewScraper(delay=0, max_retries=1, empty_page_retries=2)


@pytest.fixture(autouse=True)
def no_sleep(monkeypatch):
    monkeypatch.setattr(rs.time, "sleep", lambda s: None)


# --------------------------------------------------------------------------- #
# Input parsing
# --------------------------------------------------------------------------- #
@pytest.mark.parametrize("text", [
    "com.whatsapp",
    "  com.whatsapp  ",
    "https://play.google.com/store/apps/details?id=com.whatsapp",
    "https://play.google.com/store/apps/details?id=com.whatsapp&hl=pt_BR&gl=br",
    "play.google.com/store/apps/details?hl=en&id=com.whatsapp",
])
def test_parse_app_id_accepts_urls_and_ids(text):
    assert parse_app_id(text) == "com.whatsapp"


@pytest.mark.parametrize("text", ["", "whatsapp", "https://play.google.com/store/apps", "1com.x", "com..x"])
def test_parse_app_id_rejects_garbage(text):
    with pytest.raises(ValueError):
        parse_app_id(text)


def test_clean_filename():
    assert clean_filename("WhatsApp Messenger: Chat & Calls!") == "whatsapp_messenger_chat_calls"
    assert clean_filename("???") == "app"
    assert len(clean_filename("x" * 100)) == 40


# --------------------------------------------------------------------------- #
# Scraping
# --------------------------------------------------------------------------- #
def test_collects_everything(store, scraper):
    progress = []
    result = scraper.scrape("com.my.app", on_progress=lambda d, t: progress.append((d, t)))
    assert len(result.reviews) == 450
    assert result.complete and not result.error
    assert progress[-1] == (450, 450)
    assert len({r.review_id for r in result.reviews}) == 450
    assert isinstance(result.reviews[0], Review)
    assert result.reviews[0].at == "2026-10-01T00:00:00"


def test_max_reviews(store, scraper):
    result = scraper.scrape("com.my.app", max_reviews=250)
    assert len(result.reviews) == 250 and result.complete


def test_since_stops_at_older_reviews(store, scraper):
    result = scraper.scrape("com.my.app", since=date(2026, 9, 22))
    # reviews are one per day starting 2026-10-01 -> 10 days inclusive
    assert len(result.reviews) == 10
    assert store.calls == 1  # no pointless extra pages


def test_empty_page_from_network_error_is_retried(store, scraper):
    """The real library hides network errors as an empty last page."""
    store.fail_pages = {1}
    result = scraper.scrape("com.my.app")
    assert len(result.reviews) == 450 and result.complete


def test_exceptions_are_retried_then_reported(monkeypatch, scraper):
    store = FakeStore()
    monkeypatch.setattr(rs, "app", store.app)
    state = {"n": 0}

    def flaky(*args, **kwargs):
        state["n"] += 1
        if state["n"] > 1:  # first page works, everything after explodes
            raise ConnectionError("boom")
        return store.reviews(*args, **kwargs)

    monkeypatch.setattr(rs, "reviews", flaky)
    result = scraper.scrape("com.my.app")
    assert len(result.reviews) == 200          # keeps what it had
    assert not result.complete and "boom" in result.error


def test_cancel_stops_between_pages(store, scraper):
    cancel = threading.Event()
    result = scraper.scrape(
        "com.my.app", cancel_event=cancel,
        on_progress=lambda done, total: cancel.set(),
    )
    assert len(result.reviews) == 200
    assert result.cancelled and not result.complete


def test_network_down_reports_error(monkeypatch, scraper):
    def down(*a, **k):
        raise OSError("Tunnel connection failed")

    monkeypatch.setattr(rs, "app", down)
    monkeypatch.setattr(rs, "reviews", lambda *a, **k: ([], Token(None)))
    result = scraper.scrape("com.my.app")
    assert not result.reviews and "Tunnel" in result.error


def test_backwards_compatible_api(store, scraper):
    reviews, info = scraper.extract_all_reviews("com.my.app")
    assert len(reviews) == 450 and info["title"] == "My App"
    assert scraper.extract_app_id_from_url("https://play.google.com/store/apps/details?id=a.b") == "a.b"


# --------------------------------------------------------------------------- #
# Saving
# --------------------------------------------------------------------------- #
def test_save_all_formats(store, scraper, tmp_path):
    result = scraper.scrape("com.my.app", max_reviews=30)
    files = scraper.save_reviews(result.reviews, result.app_info, output_dir=tmp_path,
                                 formats=["csv", "json", "xlsx"])
    assert set(files) == {"csv", "json", "xlsx"}
    assert files["csv"].name == "my_app_reviews.csv"

    payload = json.loads(files["json"].read_text(encoding="utf-8"))
    assert payload["collection_info"]["total_reviews"] == 30
    assert payload["reviews"][0]["review_id"] == "r0"

    import pandas as pd
    assert len(pd.read_csv(files["csv"])) == 30
    assert len(pd.read_excel(files["xlsx"])) == 30


def test_save_creates_folder_and_rejects_unknown_format(scraper, tmp_path):
    rows = [{"review_id": "1", "score": 5}]
    target = tmp_path / "new" / "folder"
    assert scraper.save_reviews(rows, {"title": "X"}, output_dir=target, formats=["json"])
    assert (target / "x_reviews.json").exists()
    with pytest.raises(ValueError):
        scraper.save_reviews(rows, {}, output_dir=tmp_path, formats=["pdf"])


def test_statistics():
    rows = [{"score": s} for s in (5, 5, 4, 1, 0)]
    stats = GooglePlayReviewScraper.statistics(rows)
    assert stats["total"] == 4 and stats["average"] == 3.75
    assert stats["distribution"] == {1: 1, 2: 0, 3: 0, 4: 1, 5: 2}


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #
def test_cli(store, tmp_path, capsys):
    code = rs.main(["com.my.app", "--max", "40", "-f", "csv,xlsx", "-d", str(tmp_path)])
    assert code == 0
    assert sorted(p.name for p in tmp_path.iterdir()) == ["my_app_reviews.csv", "my_app_reviews.xlsx"]
    assert "40 reviews" in capsys.readouterr().out


def test_cli_rejects_bad_input(capsys):
    assert rs.main(["not an app"]) == 2
