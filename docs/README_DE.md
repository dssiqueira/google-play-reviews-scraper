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

![Interface Vorschau](../assets/screenshots/google-play-reviews-scraper.png)

### ⚡ Anwendung in Aktion
*Sehen Sie den Scraper mit Echtzeit-Fortschritt arbeiten*

![Anwendungs-Demo](../assets/screenshots/google-play-reviews-scraper.gif)

### 📊 Kommandozeilen-Interface
*Auch über Terminal für Automatisierung verfügbar*

![Terminal-Demo](../assets/screenshots/google-play-reviews-scraper-terminal.gif)

</div>

---

## ⚡ Schnellstart

### 🖥️ **Plattform-Kompatibilität**

| Plattform | Grafische Oberfläche | Kommandozeile | Hinweise |
|:---------:|:--------------------:|:-------------:|:---------|
| 🪟 **Windows** | ✅ Vollständige Unterstützung | ✅ Unterstützt | Moderne GUI mit allen Funktionen |
| 🍎 **macOS** | ✅ Native Oberfläche | ✅ Unterstützt | Für macOS-Design optimiert |
| 🐧 **Linux** | ⚠️ Basis-GUI | ✅ Unterstützt | GUI verfügbar, aber CLI empfohlen |

### 🎯 **Option 1: GUI-Anwendung (Empfohlen)**

#### **🚀 Ein-Befehl-Installation**
```bash
git clone https://github.com/dssiqueira/google-play-reviews-scraper.git
cd google-play-reviews-scraper
python install.py
```

#### **🔧 Manuelle Installation**
```bash
# Windows: python src/app_gui.py
# macOS: python src/app_gui_mac.py  
# Linux: python src/app_gui.py
```

### 🔧 **Option 2: Kommandozeile**

```bash
# Bewertungen einer einzelnen App extrahieren
python src/review_scraper.py --url "https://play.google.com/store/apps/details?id=com.whatsapp"

# Batch-Verarbeitung mehrerer Apps
python src/review_scraper.py --batch apps_liste.txt --output ergebnisse/
```

### 📦 **Option 3: Python-Modul**

```python
from src.review_scraper import GooglePlayReviewScraper

scraper = GooglePlayReviewScraper()
reviews = scraper.scrape_reviews("com.whatsapp")
print(f"{len(reviews)} Bewertungen extrahiert!")
```

---

## 📈 **Review Stats Pro - Professionelle Analyse**

Nach der Extraktion von Bewertungen analysieren Sie Ihre Daten mit unserer professionellen Plattform:

**🔗 [Review Stats Pro](https://review-stats-pro.lovable.app/)**

### ✨ **Funktionen:**
- 📊 **Sentiment-Analyse** - Verstehen Sie Benutzeremotionen
- 📈 **Trend-Erkennung** - Identifizieren Sie zeitliche Muster
- 🔍 **Schlüsselwort-Extraktion** - Finden Sie die meist erwähnten Themen
- 📊 **Interaktive Diagramme** - Professionelle Visualisierungen

### 💡 **Arbeitsablauf:**
1. Bewertungen mit diesem Tool extrahieren
2. JSON zu Review Stats Pro hochladen
3. Sofortige professionelle Analysen erhalten

---

## 📖 Funktionen

<div align="center">

| 🎯 **Kernfunktionen** | 🎨 **Interface** | 📊 **Ausgabe** | 🌍 **Multi-Sprache** |
|:---:|:---:|:---:|:---:|
| Extrahiert **ALLE** Bewertungen | Moderne GUI mit Themes | CSV & JSON Export | 6 Sprachen unterstützt |
| **Batch-Verarbeitung** | Echtzeit-Fortschritt | Detaillierte Analysen | Auto-Spracherkennung |
| **Intelligente Filterung** | Drag & Drop URLs | Zeit-Statistiken | Benutzerdefinierte Übersetzungen |
| **Rate Limiting** | Multi-App-Warteschlange | Fehlerbehandlung | RTL-Unterstützung |

</div>

### 🚀 **Was macht es besonders?**

- **🎯 Vollständige Extraktion**: Erhält ALLE verfügbaren Bewertungen, nicht nur die neuesten
- **⚡ Blitzschnell**: Optimiertes Scraping mit intelligenter Geschwindigkeitsbegrenzung  
- **🎨 Schöne Oberfläche**: Moderne GUI mit hellen/dunklen Themes
- **📊 Reiche Analysen**: Detaillierte Statistiken und Zeitverfolgung
- **🔄 Batch-Verarbeitung**: Behandelt mehrere Apps gleichzeitig
- **🌍 Multi-Sprache**: Oberfläche in 6 Sprachen verfügbar
- **📱 Intelligente Erkennung**: Erkennt App-Infos automatisch und behandelt Fehler elegant
- **💾 Mehrere Formate**: Exportiert zu CSV, JSON mit anpassbaren Feldern
- **🛡️ Robust**: Behandelt Netzwerkprobleme, Rate Limits und Grenzfälle

---

## 🛠️ Installation

### 📋 **Anforderungen**

- **Python 3.7+** (3.9+ empfohlen)
- **Internetverbindung** für Scraping
- **2GB RAM** minimum (4GB+ für große Datensätze)

### 📦 **Schnelle Installation**

```bash
git clone https://github.com/dssiqueira/google-play-reviews-scraper.git
cd google-play-reviews-scraper
pip install -r requirements.txt
python src/app_gui.py
```

---

## 🎯 Anwendungsfälle

### 💼 **Perfekt für:**

- **📊 Marktforscher** - Konkurrenz-Apps und Markttrends analysieren
- **🎯 Product Manager** - Benutzerfeedback für Feature-Planung sammeln  
- **🔍 UX-Forscher** - Benutzerschmerzen und Präferenzen verstehen
- **📈 App-Entwickler** - App-Performance und Benutzerzufriedenheit überwachen
- **🏢 Business-Analysten** - Insights für strategische Entscheidungen generieren
- **🎓 Studenten & Akademiker** - Daten für Forschungsprojekte sammeln

---
---

## ?? Lizenz

Dieses Projekt steht unter der **MIT-Lizenz** - siehe die [LICENSE](../LICENSE) Datei f�r Details.

---

<div align="center">

**?? Mit ?? f�r die Community entwickelt**

**Wenn dieses Projekt Ihnen geholfen hat, geben Sie ihm bitte einen ?!**

[![GitHub stars](https://img.shields.io/github/stars/dssiqueira/google-play-reviews-scraper?style=social)](../../stargazers)
[![GitHub forks](https://img.shields.io/github/forks/dssiqueira/google-play-reviews-scraper?style=social)](../../network/members)

</div>
