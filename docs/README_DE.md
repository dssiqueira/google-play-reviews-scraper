<div align="center">

<img src="../assets/icons/google-play.png" width="72" alt="">

# Google Play Reviews Scraper

**Google-Play-Store-Bewertungen als CSV, JSON oder Excel sammeln — per Desktop-App oder Terminal.**

[🇺🇸 English](../README.md) · [🇧🇷 Português](README_PT.md) · [🇪🇸 Español](README_ES.md) · [🇫🇷 Français](README_FR.md) · [🇩🇪 Deutsch](README_DE.md) · [🇮🇹 Italiano](README_IT.md)

<img src="../assets/screenshots/app-light.png" width="720" alt="Die App sammelt Bewertungen für vier Apps">

</div>

## Funktionen

- **Mehrere Apps in der Warteschlange** — Play-Store-URLs oder Paket-IDs einfügen, auch viele auf einmal (eine pro Zeile).
- **Nur was du brauchst** — alles, die neuesten *N* pro App oder nur Bewertungen ab einem Datum.
- **CSV, JSON und Excel** — die CSV öffnet sich in Excel mit korrekten Umlauten; das JSON enthält die App-Metadaten.
- **Jederzeit stoppen** — sofort, und bereits Gesammeltes bleibt erhalten.
- **Robust** — Netzwerkfehler werden wiederholt, statt das Sammeln stillschweigend abzubrechen.
- **Bewertungsübersicht** — Durchschnitt und 1–5★-Verteilung am Ende.
- **Hell- und Dunkelmodus**, Oberfläche in 6 Sprachen, merkt sich deine Einstellungen.
- **Dieselbe App unter Windows, macOS und Linux**, dazu CLI und Python-API.

<div align="center">
<img src="../assets/screenshots/app-dark-summary.png" width="600" alt="">
</div>

## Schnellstart

### Windows — ohne Python

Installer oder `.exe` unter [Releases](https://github.com/dssiqueira/google-play-reviews-scraper/releases) herunterladen und starten.

### Aus dem Quellcode

```bash
git clone https://github.com/dssiqueira/google-play-reviews-scraper.git
cd google-play-reviews-scraper
pip install -r requirements.txt

python src/app_gui.py         # Desktop-App
python src/review_scraper.py  # interaktiver Terminal-Modus
```

> **Linux:** Tk ist meist ein eigenes Paket — `sudo apt install python3-tk` (Debian/Ubuntu).

## Kommandozeile

```bash
# eine App, per ID oder URL
python src/review_scraper.py com.whatsapp

# mehrere Apps, US-Store auf Englisch, max. 1.000 pro App, seit 1. Januar, als CSV + Excel
python src/review_scraper.py com.whatsapp com.instagram.android \
    --country us --lang en --max 1000 --since 2026-01-01 --format csv,xlsx
```

Alle Optionen, die Python-API und das Datenformat stehen im [englischen README](../README.md).

## Gut zu wissen

- **Wie viele Bewertungen bekomme ich?** So viele, wie Google Play für dieses Land/diese Sprache liefert — meist weniger als die Gesamtzahl im Store, die alle Sprachen zählt.
- **Ist das erlaubt?** Das Tool liest öffentliche Seiten, wie ein Browser. Bewertungen enthalten Nutzernamen: Geh verantwortungsvoll mit den Daten um (DSGVO) und beachte die Bedingungen von Google Play.

Diagramme und Stimmungsanalyse? Lade das JSON bei **[Review Stats Pro](https://review-stats-pro.lovable.app/)** hoch.

## Lizenz

[MIT](../LICENSE) © Douglas Siqueira
