# 📱 Google Play Reviews Scraper

<div align="center">

**🌍 Language / Idioma / Langue / Sprache / Lingua**

[![🇺🇸 English](https://img.shields.io/badge/🇺🇸-English-blue?style=for-the-badge)](README.md)
[![🇧🇷 Português](https://img.shields.io/badge/🇧🇷-Português-green?style=for-the-badge)](README_PT.md)
[![🇪🇸 Español](https://img.shields.io/badge/🇪🇸-Español-red?style=for-the-badge)](README_ES.md)
[![🇫🇷 Français](https://img.shields.io/badge/🇫🇷-Français-blue?style=for-the-badge)](README_FR.md)
[![🇩🇪 Deutsch](https://img.shields.io/badge/🇩🇪-Deutsch-black?style=for-the-badge)](README_DE.md)
[![🇮🇹 Italiano](https://img.shields.io/badge/🇮🇹-Italiano-green?style=for-the-badge)](README_IT.md)

---

![Google Play Reviews Scraper](img/google-play.png)

**Professionelles Tool zum Extrahieren und Analysieren von App-Bewertungen aus dem Google Play Store**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)](https://windows.microsoft.com)

</div>

---

## 🎯 **Was macht es?**

Extrahiert **ALLE** verfügbaren Bewertungen von jeder Google Play Store App schnell, organisiert und zuverlässig. Ideal für:

- 📊 **Marktanalyse** und Wettbewerbsforschung
- 🔍 **UX-Forschung** und Benutzerfeedback-Analyse  
- 📈 **Überwachung** des App-Rufs
- 🎯 **Insights** für Produktentwicklung
- 📋 **Berichte** und Präsentationen

---

## 🚀 **Schnelle Installation**

### 🖥️ **Plattform-Kompatibilität**

| Plattform | Grafische Oberfläche | Kommandozeile | Ausführbare Datei |
|-----------|----------------------|---------------|-------------------|
| 🪟 **Windows** | ✅ Vollständige Unterstützung | ✅ Unterstützt | ✅ Verfügbar |
| 🍎 **macOS** | ❌ Nur Terminal | ✅ Unterstützt | ❌ Nicht verfügbar |
| 🐧 **Linux** | ❌ Nur Terminal | ✅ Unterstützt | ❌ Nicht verfügbar |

> **Hinweis**: Die grafische Benutzeroberfläche ist nur für Windows verfügbar. Mac- und Linux-Benutzer müssen die Kommandozeilenversion verwenden.

### Option 1: Ausführbare Datei (Nur Windows)
1. Laden Sie die ausführbare Datei von der [Releases-Seite](../../releases) herunter
2. Führen Sie `GooglePlayReviewScraper.exe` aus
3. Fertig! Python muss nicht installiert werden

### Option 2: Quellcode (Alle Plattformen)
```bash
# Repository klonen
git clone https://github.com/ihr-benutzername/google-play-reviews-scraper.git
cd google-play-reviews-scraper

# Abhängigkeiten installieren
pip install -r requirements.txt

# Windows: GUI ausführen
python app_gui.py

# Mac/Linux: Kommandozeile verwenden
python review_scraper.py --url "https://play.google.com/store/apps/details?id=com.whatsapp"
```

**Windows-Benutzer**: Die Benutzeroberfläche öffnet sich auf Portugiesisch. Verwenden Sie den Flaggen-Selektor in der oberen rechten Ecke, um die Sprache zu ändern!
**Mac/Linux-Benutzer**: Verwenden Sie die Kommandozeilenschnittstelle mit den unten gezeigten Parametern.

---

## 💻 **Moderne Grafische Benutzeroberfläche**

![Google Play Reviews Scraper Screenshot](img/google-play-reviews-scraper.png)

### 🎬 **Anwendung in Aktion**
![Google Play Reviews Scraper Demo](img/google-play-reviews-scraper.gif)

### ✨ Interface-Funktionen:
- 🎨 **Modernes Material Design** intuitive Benutzeroberfläche
- 🌍 **Mehrsprachig** mit Flaggen-Selektor (6 Sprachen)
- 📋 **URL einfügen** direkt aus dem Browser
- ⚙️ **Einfache Einstellungen** (Land, Sprache, Ordner)
- 📊 **Echtzeit-Fortschritt** mit visueller Fortschrittsleiste
- 📁 **Automatisches Öffnen** generierter Dateien
- 📜 **Sanftes Scrollen** für kleine Bildschirme
- ℹ️ **"Über"-Modal** mit Entwicklerinformationen
- 🎯 **Benutzerdefiniertes Symbol** in der Taskleiste

### 🌍 **Mehrsprachiges System**
- **🇺🇸 English**
- **🇧🇷 Português**
- **🇪🇸 Español**
- **🇫🇷 Français**
- **🇩🇪 Deutsch** (Standard)
- **🇮🇹 Italiano**

**Selektor mit echten Flaggen**: Klicken Sie auf die Flagge in der oberen rechten Ecke, um die Sprache sofort zu ändern!

---

## 📖 **Wie zu verwenden**

### 1️⃣ **App finden**
Gehen Sie zum Google Play Store und finden Sie die gewünschte App. Beispiel:
```
https://play.google.com/store/apps/details?id=com.whatsapp
```

### 2️⃣ **URL einfügen**
- Öffnen Sie Google Play Reviews Scraper
- Fügen Sie die vollständige URL in das Feld ein
- Die App-ID wird automatisch extrahiert

### 3️⃣ **Konfigurieren (Optional)**
- **Land**: `de` (Deutschland), `us` (USA), `br` (Brasilien)...
- **Sprache**: `de` (Deutsch), `en` (Englisch), `pt` (Portugiesisch)...
- **Ordner**: Wählen Sie, wo die Dateien gespeichert werden sollen

### 4️⃣ **Ausführen**
Klicken Sie auf "Sammlung Starten" und warten Sie. Der Prozess ist automatisch!

---

## 🛠️ **Kommandozeilenschnittstelle**

### 🎬 **Terminal-Demonstration**
![Google Play Reviews Scraper Terminal Demo](img/google-play-reviews-scraper-terminal.gif)

### 🍎🐧 **Für Mac/Linux-Benutzer (Erforderlich)**

Da die grafische Benutzeroberfläche exklusiv für Windows ist, müssen Mac- und Linux-Benutzer die Kommandozeile verwenden:

```bash
# Grundlegende Verwendung
python review_scraper.py --url "https://play.google.com/store/apps/details?id=com.whatsapp"

# Mit benutzerdefinierten Einstellungen
python review_scraper.py \
  --app-id "com.whatsapp" \
  --country "de" \
  --lang "de" \
  --output "whatsapp_reviews"

# Hilfe erhalten
python review_scraper.py --help
```

### 🪟 **Für Windows-Benutzer (Optional)**

Windows-Benutzer können auch die Kommandozeile für die Automatisierung verwenden:

```bash
# Grundlegendes Beispiel
python review_scraper.py --url "https://play.google.com/store/apps/details?id=com.whatsapp"

# Mit benutzerdefinierten Einstellungen
python review_scraper.py \
  --app-id "com.whatsapp" \
  --country "us" \
  --lang "en" \
  --output "whatsapp_usa_reviews"

# Vollständige Hilfe
python review_scraper.py --help
```

### **Verfügbare Parameter:**
```
--url, -u          Vollständige App-URL
--app-id, -a       App-ID (z.B.: com.whatsapp)
--country, -c      Ländercode (Standard: de)
--lang, -l         Sprachcode (Standard: de)
--output, -o       Name der Ausgabedateien
--help, -h         Diese Hilfe anzeigen
```

---

## 🌍 **Unterstützte Sprachen in der Benutzeroberfläche**

Die Anwendung unterstützt **6 Sprachen** mit vollständiger Übersetzung der Benutzeroberfläche:

| Flagge | Code | Sprache | Status |
|--------|------|---------|--------|
| 🇺🇸 | `en` | **English** | ✅ Vollständig |
| 🇧🇷 | `pt` | **Português** | ✅ Vollständig |
| 🇪🇸 | `es` | **Español** | ✅ Vollständig |
| 🇫🇷 | `fr` | **Français** | ✅ Vollständig |
| 🇩🇪 | `de` | **Deutsch** | ✅ Standard |
| 🇮🇹 | `it` | **Italiano** | ✅ Vollständig |

**Wie zu verwenden**: Klicken Sie auf die Flagge in der oberen rechten Ecke der Benutzeroberfläche, um die Sprache sofort zu ändern!

### 🎯 **Was übersetzt wird:**
- ✅ Alle Schaltflächen und Beschriftungen
- ✅ Abschnittstitel
- ✅ Status- und Protokollnachrichten
- ✅ Vollständiges "Über"-Modal
- ✅ Platzhalter und Tooltips
- ✅ Fehlermeldungen

---

## 🚀 **Neuigkeiten der aktuellen Version**

### ✨ **Implementierte Funktionen**
- 🌍 **Vollständiges mehrsprachiges System** (6 Sprachen)
- 🎨 **Material Design Interface** modern und responsiv
- 🏳️ **Flaggen-Selektor** mit echten PNG-Bildern (24x24px)
- 📜 **Sanftes Scrollen** für Bildschirme jeder Größe
- 🎯 **Benutzerdefiniertes Google Play-Symbol** in der Taskleiste
- ℹ️ **"Über"-Modal** mit Projektinformationen
- 🔄 **Sofortige Übersetzung** der gesamten Benutzeroberfläche
- 📊 **Visuelle und informative** Fortschrittsleisten

---

<div align="center">

**Entwickelt mit ❤️ von [DSiqueira](https://dsiqueira.com)**

⭐ **Wenn dieses Projekt nützlich war, hinterlassen Sie einen Stern!** ⭐

</div>