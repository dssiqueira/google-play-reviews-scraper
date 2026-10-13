<div align="center">

<img src="../assets/icons/google-play.png" width="72" alt="">

# Google Play Reviews Scraper

**Raccogli le recensioni del Google Play Store in CSV, JSON o Excel — da app desktop o da terminale.**

[🇺🇸 English](../README.md) · [🇧🇷 Português](README_PT.md) · [🇪🇸 Español](README_ES.md) · [🇫🇷 Français](README_FR.md) · [🇩🇪 Deutsch](README_DE.md) · [🇮🇹 Italiano](README_IT.md)

<img src="../assets/screenshots/app-light.png" width="720" alt="L'app mentre raccoglie le recensioni di quattro app">

</div>

## Funzionalità

- **Coda con più app** — incolla URL del Play Store o ID di pacchetto, anche molti insieme (uno per riga).
- **Solo quello che ti serve** — tutto, le ultime *N* per app, o solo le recensioni da una data.
- **CSV, JSON ed Excel** — il CSV si apre in Excel con gli accenti corretti; il JSON include i metadati dell'app.
- **Ferma quando vuoi** — l'arresto è immediato e conserva quanto già raccolto.
- **Robusto** — gli errori di rete vengono ritentati invece di interrompere la raccolta in silenzio.
- **Riepilogo dei voti** — media e distribuzione da 1 a 5★ alla fine.
- **Tema chiaro e scuro**, interfaccia in 6 lingue, ricorda le tue impostazioni.
- **La stessa app su Windows, macOS e Linux**, più CLI e API Python.

<div align="center">
<img src="../assets/screenshots/app-dark-summary.png" width="600" alt="">
</div>

## Per iniziare

### Windows — senza Python

Scarica l'installer o l'`.exe` da [Releases](https://github.com/dssiqueira/google-play-reviews-scraper/releases) ed eseguilo.

### Dal codice sorgente

```bash
git clone https://github.com/dssiqueira/google-play-reviews-scraper.git
cd google-play-reviews-scraper
pip install -r requirements.txt

python src/app_gui.py         # app desktop
python src/review_scraper.py  # modalità interattiva da terminale
```

> **Linux:** Tk è spesso un pacchetto separato — `sudo apt install python3-tk` (Debian/Ubuntu).

## Riga di comando

```bash
# un'app, per ID o URL
python src/review_scraper.py com.whatsapp

# più app, store USA in inglese, max 1.000 ciascuna, dal 1° gennaio, in CSV + Excel
python src/review_scraper.py com.whatsapp com.instagram.android \
    --country us --lang en --max 1000 --since 2026-01-01 --format csv,xlsx
```

Tutte le opzioni, l'API Python e il formato dei dati sono nel [README in inglese](../README.md).

## Buono a sapersi

- **Quante recensioni posso ottenere?** Quante ne fornisce Google Play per quel paese/lingua — di solito meno del totale nella scheda, che conta tutte le lingue.
- **È consentito?** Legge pagine pubbliche, come un browser. Le recensioni contengono nomi utente: tratta i dati in modo responsabile (GDPR) e rispetta i termini di Google Play.

Grafici e analisi del sentiment? Carica il JSON su **[Review Stats Pro](https://review-stats-pro.lovable.app/)**.

## Licenza

[MIT](../LICENSE) © Douglas Siqueira
