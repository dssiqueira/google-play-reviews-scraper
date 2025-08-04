<div align="center">

# 📱 Google Play Reviews Scraper

![Google Play Reviews Scraper](../assets/icons/google-play.png)

**🚀 Professionelles Tool zum Extrahieren und Analysieren von App-Bewertungen aus dem Google Play Store**

*Extrahieren Sie Tausende von Bewertungen in Minuten mit einer schönen, modernen Oberfläche*

---

## 🌍 **Wählen Sie Ihre Sprache / Choose Your Language**

[![🇺🇸 English](https://img.shields.io/badge/🇺🇸-English-4285f4?style=for-the-badge&labelColor=white)](../README.md)
[![🇧🇷 Português](https://img.shields.io/badge/🇧🇷-Português-00a86b?style=for-the-badge&labelColor=white)](README_PT.md)
[![🇪🇸 Español](https://img.shields.io/badge/🇪🇸-Español-ea4335?style=for-the-badge&labelColor=white)](README_ES.md)
[![🇫🇷 Français](https://img.shields.io/badge/🇫🇷-Français-4285f4?style=for-the-badge&labelColor=white)](README_FR.md)
[![🇩🇪 Deutsch](https://img.shields.io/badge/🇩🇪-Deutsch-333333?style=for-the-badge&labelColor=white)](README_DE.md)
[![🇮🇹 Italiano](https://img.shields.io/badge/🇮🇹-Italiano-00a86b?style=for-the-badge&labelColor=white)](README_IT.md)

---

[![Python](https://img.shields.io/badge/Python-3.7+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](../LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Cross--Platform-lightgrey?style=for-the-badge)](https://github.com)
[![GUI](https://img.shields.io/badge/Interface-Moderne_GUI-blue?style=for-the-badge)](../src/app_gui.py)

**[🎬 Demo Ansehen](#-demo) • [⚡ Schnellstart](#-schnellstart) • [📖 Funktionen](#-funktionen) • [🛠️ Installation](#️-installation)**

---

</div>

## 🎬 Demo

<div align="center">

### 🖥️ Moderne Oberfläche
*Schöne, intuitive GUI mit mehrsprachiger Unterstützung*

![Interface Vorschau](../assets/screenshots/interface-preview.png)

### ⚡ Batch-Verarbeitung
*Verarbeitet mehrere Apps gleichzeitig mit Echtzeit-Fortschritt*

![Batch-Verarbeitung](../assets/screenshots/batch-processing.gif)

### 📊 Reichhaltige Ausgabeformate
*Export nach CSV, JSON mit detaillierten Analysen*

![Ausgabeformate](../assets/screenshots/output-formats.png)

</div>

---

## ⚡ Schnellstart

### 🎯 **Option 1: GUI-Anwendung (Empfohlen)**

```bash
# 1. Repository klonen
git clone https://github.com/your-username/google-play-reviews-scraper.git
cd google-play-reviews-scraper

# 2. Abhängigkeiten installieren
pip install -r requirements.txt

# 3. GUI starten
python src/app_gui.py
```

### 🔧 **Option 2: Kommandozeile**

```bash
# Bewertungen einer einzelnen App extrahieren
python src/review_scraper.py --url "https://play.google.com/store/apps/details?id=com.whatsapp"

# Batch-Verarbeitung mehrerer Apps
python src/review_scraper.py --batch app_liste.txt --output ergebnisse/
```

### 📦 **Option 3: Python-Modul**

```python
from src.review_scraper import GooglePlayReviewScraper

scraper = GooglePlayReviewScraper()
reviews = scraper.scrape_reviews("com.whatsapp")
print(f"{len(reviews)} Bewertungen extrahiert!")
```

---

## 📖 Funktionen

<div align="center">

| 🎯 **Hauptfunktionen** | 🎨 **Oberfläche** | 📊 **Ausgabe** | 🌍 **Mehrsprachig** |
|:---:|:---:|:---:|:---:|
| Extrahiert **ALLE** Bewertungen | Moderne GUI mit Themes | CSV & JSON Export | 6 Sprachen unterstützt |
| **Batch-Verarbeitung** | Echtzeit-Fortschritt | Detaillierte Analysen | Auto-Spracherkennung |
| **Intelligente Filterung** | Drag & Drop URLs | Zeitstatistiken | Benutzerdefinierte Übersetzungen |
| **Rate Limiting** | Multi-App-Warteschlange | Fehlerbehandlung | RTL-Unterstützung |

</div>

### 🚀 **Was macht es besonders?**

- **🎯 Vollständige Extraktion**: Erhält ALLE verfügbaren Bewertungen, nicht nur die neuesten
- **⚡ Blitzschnell**: Optimiertes Scraping mit intelligentem Rate Limiting  
- **🎨 Schöne Oberfläche**: Moderne GUI mit Hell-/Dunkel-Themes
- **📊 Reichhaltige Analysen**: Detaillierte Statistiken und Zeitverfolgung
- **🔄 Batch-Verarbeitung**: Verarbeitet mehrere Apps gleichzeitig
- **🌍 Mehrsprachig**: Oberfläche in 6 Sprachen verfügbar
- **📱 Intelligente Erkennung**: Erkennt App-Infos automatisch und behandelt Fehler elegant
- **💾 Mehrere Formate**: Export nach CSV, JSON mit anpassbaren Feldern
- **🛡️ Robust**: Behandelt Netzwerkprobleme, Rate Limits und Grenzfälle

---

## 🛠️ Installation

### 📋 **Voraussetzungen**

- **Python 3.7+** (3.9+ empfohlen)
- **Internetverbindung** für Scraping
- **2GB RAM** minimum (4GB+ für große Datensätze)

### 📦 **Schnelle Installation**

```bash
git clone https://github.com/your-username/google-play-reviews-scraper.git
cd google-play-reviews-scraper
pip install -r requirements.txt
python src/app_gui.py
```

---

## 🎯 Anwendungsfälle

### 💼 **Perfekt für:**

- **📊 Marktforscher** - Konkurrenz-Apps und Markttrends analysieren
- **🎯 Produktmanager** - Nutzerfeedback für Feature-Planung sammeln  
- **🔍 UX-Forscher** - Schmerzpunkte und Nutzerpräferenzen verstehen
- **📈 App-Entwickler** - Performance und Nutzerzufriedenheit überwachen
- **🏢 Business-Analysten** - Insights für strategische Entscheidungen generieren
- **🎓 Studenten und Akademiker** - Daten für Forschungsprojekte sammeln

---

## 🌍 **Vollständige Dokumentation in anderen Sprachen**

<div align="center">

**📖 Vollständige Dokumentation mit detaillierten Anleitungen, Beispielen und Tutorials:**

[![🇺🇸 Complete English Documentation](https://img.shields.io/badge/🇺🇸-Complete_Documentation-4285f4?style=for-the-badge)](../README.md)
[![🇧🇷 Documentação Completa em Português](https://img.shields.io/badge/🇧🇷-Documentação_Completa-00a86b?style=for-the-badge)](README_PT.md)
[![🇪🇸 Documentación Completa en Español](https://img.shields.io/badge/🇪🇸-Documentación_Completa-ea4335?style=for-the-badge)](README_ES.md)
[![🇫🇷 Documentation Complète en Français](https://img.shields.io/badge/🇫🇷-Documentation_Complète-4285f4?style=for-the-badge)](README_FR.md)
[![🇮🇹 Documentazione Completa in Italiano](https://img.shields.io/badge/🇮🇹-Documentazione_Completa-00a86b?style=for-the-badge)](README_IT.md)

**📋 [Alle Sprachen und Übersetzungsanleitung anzeigen](LANGUAGES.md)**

</div>

---

## 📄 Lizenz

Dieses Projekt steht unter der **MIT-Lizenz** - siehe die [LICENSE](../LICENSE) Datei für Details.

---

<div align="center">

**🚀 Mit ❤️ für die Community entwickelt**

**Wenn dieses Projekt Ihnen geholfen hat, geben Sie ihm bitte einen ⭐!**

[![GitHub stars](https://img.shields.io/github/stars/your-username/google-play-reviews-scraper?style=social)](../../stargazers)
[![GitHub forks](https://img.shields.io/github/forks/your-username/google-play-reviews-scraper?style=social)](../../network/members)

</div>