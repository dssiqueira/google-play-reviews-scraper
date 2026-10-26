<div align="center">

<img src="assets/icons/google-play.png" width="72" alt="">

# Google Play Reviews Scraper

**Collect Google Play Store reviews into CSV, JSON or Excel — from a desktop app or the terminal.**

[🇺🇸 English](README.md) · [🇧🇷 Português](docs/README_PT.md) · [🇪🇸 Español](docs/README_ES.md) · [🇫🇷 Français](docs/README_FR.md) · [🇩🇪 Deutsch](docs/README_DE.md) · [🇮🇹 Italiano](docs/README_IT.md)

[![Tests](https://github.com/dssiqueira/google-play-reviews-scraper/actions/workflows/tests.yml/badge.svg)](https://github.com/dssiqueira/google-play-reviews-scraper/actions/workflows/tests.yml)
[![Python](https://img.shields.io/badge/python-3.9%2B-3776AB?logo=python&logoColor=white)](https://python.org)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

<img src="assets/screenshots/app-light.png" width="720" alt="The app collecting reviews for four apps">

</div>

## Features

- **Queue several apps** — paste Play Store URLs or package ids, even many at once (one per line).
- **Collect what you need** — everything, the latest *N* per app, or only reviews since a date.
- **CSV, JSON and Excel** — CSV opens in Excel with accents intact; JSON includes app metadata.
- **Stop any time** — stopping is instant and keeps what was already collected.
- **Resilient** — network hiccups are retried with backoff instead of silently cutting the collection short.
- **Rating summary** — average and 1–5★ distribution when a run finishes.
- **Light & dark mode**, 6 interface languages (PT, EN, ES, FR, DE, IT), remembers your settings.
- **Same app on Windows, macOS and Linux**, plus a scriptable CLI and a Python API.

<div align="center">
<img src="assets/screenshots/app-dark-summary.png" width="600" alt="Summary after a run, in dark mode">
</div>

## Quick start

### Windows — no Python needed

Download the installer or the `.exe` from [Releases](https://github.com/dssiqueira/google-play-reviews-scraper/releases) and run it.

### From source (Windows, macOS, Linux)

```bash
git clone https://github.com/dssiqueira/google-play-reviews-scraper.git
cd google-play-reviews-scraper
pip install -r requirements.txt

python src/app_gui.py         # desktop app
python src/review_scraper.py  # interactive terminal mode
```

> **Linux:** Tk is a separate package on most distros — `sudo apt install python3-tk` (Debian/Ubuntu) or `sudo dnf install python3-tkinter` (Fedora).

## Command line

```bash
# one app, by id or URL
python src/review_scraper.py com.whatsapp
python src/review_scraper.py "https://play.google.com/store/apps/details?id=com.whatsapp"

# several apps, US store in English, max 1,000 each, since Jan 1st, as CSV + Excel
python src/review_scraper.py com.whatsapp com.instagram.android \
    --country us --lang en --max 1000 --since 2026-01-01 --format csv,xlsx --output-dir data/
```

| Option | Default | |
|---|---|---|
| `APP ...` | — | Play Store URLs or app ids |
| `-c, --country` | `br` | Store country (`us`, `gb`, `de`, …) |
| `-l, --lang` | `pt` | Review language (`en`, `es`, …) |
| `-n, --max` | all | Max reviews per app |
| `--since` | — | Only reviews on/after `YYYY-MM-DD` |
| `-f, --format` | `csv,json` | Any of `csv`, `json`, `xlsx` |
| `-d, --output-dir` | `.` | Where files are written |
| `-o, --output` | app name | File name prefix (single app only) |
| `-v, --verbose` | off | Show retries and debug info |

Files are named after the app, e.g. `whatsapp_messenger_reviews.csv`.

## Python API

```python
from review_scraper import GooglePlayReviewScraper

scraper = GooglePlayReviewScraper(country="us", lang="en")
result = scraper.scrape("com.whatsapp", max_reviews=500,
                        on_progress=lambda done, total: print(done, total))

print(result.title, len(result.reviews), result.complete)
print(scraper.statistics(result.reviews))   # total, average, 1-5★ distribution
scraper.save_reviews(result.reviews, result.app_info, output_dir="data", formats=["csv", "xlsx"])
```

`scrape()` also takes `since=date(...)` and a `cancel_event=threading.Event()` you can set from another thread.

## Output

Each review has the same columns in every format:

| Column | Example |
|---|---|
| `review_id` | `gp:AOqpTOH…` |
| `user_name` | `Maria S.` |
| `content` | `Great app, but…` |
| `score` | `4` |
| `thumbs_up_count` | `12` |
| `at` | `2026-10-01T14:32:10` |
| `reply_content` / `reply_at` | developer reply, if any |
| `app_version` | `2.26.4.71` |

The JSON file wraps the reviews with `collection_info` (date, country, language) and the full `app_info` from the store. See [`examples/`](examples).

Want charts and sentiment analysis? Upload the JSON to **[Review Stats Pro](https://review-stats-pro.lovable.app/)**.

## Good to know

- **How many reviews can I get?** As many as Google Play serves for that country/language — usually fewer than the total shown on the store page, which counts every language. The progress counter shows that total as `~N`.
- **Where are my settings?** In your user app-data folder (`%APPDATA%\GooglePlayReviewsScraper` on Windows, `~/Library/Application Support/…` on macOS, `~/.config/google-play-reviews-scraper` on Linux).
- **Is this allowed?** It reads public review pages, like a browser does. Reviews include user names, so handle the data responsibly (LGPD/GDPR) and respect Google Play's terms.

## Development

```bash
pip install -r requirements-dev.txt
pytest                      # tests run offline against a fake Play Store
ruff check src tests
python build.py             # standalone app in dist/
python build.py --installer # Windows: also builds the Inno Setup installer
```

```
src/
  review_scraper.py   scraping core + CLI
  app_gui.py          desktop app (CustomTkinter)
  translations.py     UI strings for 6 languages
  appdata.py          settings and stats in the user's app-data folder
assets/               icons, theme, screenshots
tests/                pytest suite
build.py              PyInstaller build (+ installer.iss for Windows)
```

Translations live in `src/translations.py`; a test checks every language has every key. Contributions welcome — open an [issue](https://github.com/dssiqueira/google-play-reviews-scraper/issues) or a PR.

## License

[MIT](LICENSE) © Douglas Siqueira

Made by [Douglas Siqueira](https://dsiqueira.com/sobre) · [dsiqueira.com](https://dsiqueira.com)
