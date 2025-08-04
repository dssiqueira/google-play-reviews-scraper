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

![Google Play Reviews Scraper](../assets/icons/google-play.png)

**Strumento professionale per estrarre e analizzare recensioni di app dal Google Play Store**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)](https://windows.microsoft.com)

</div>

---

## 🎯 **Cosa fa?**

Estrae **TUTTE** le recensioni disponibili da qualsiasi app del Google Play Store in modo rapido, organizzato e affidabile. Ideale per:

- 📊 **Analisi di mercato** e ricerca della concorrenza
- 🔍 **Ricerca UX** e analisi del feedback degli utenti  
- 📈 **Monitoraggio** della reputazione delle app
- 🎯 **Insights** per lo sviluppo di prodotti
- 📋 **Report** e presentazioni

---

## 🚀 **Installazione Rapida**

### 🖥️ **Compatibilità delle Piattaforme**

| Piattaforma | Interfaccia Grafica | Riga di Comando | Eseguibile |
|-------------|---------------------|-----------------|------------|
| 🪟 **Windows** | ✅ Supporto completo | ✅ Supportato | ✅ Disponibile |
| 🍎 **macOS** | ✅ **NUOVO!** Interfaccia Nativa | ✅ Supportato | ❌ Non disponibile |
| 🐧 **Linux** | ❌ Solo terminale | ✅ Supportato | ❌ Non disponibile |

> **✨ NUOVO**: macOS ora ha un'interfaccia visuale nativa con 6 lingue e design nativo!

### Opzione 1: Eseguibile (Solo Windows)
1. Scarica l'eseguibile dalla [pagina delle release](../../releases)
2. Esegui `GooglePlayReviewScraper.exe`
3. Fatto! Non è necessario installare Python

### Opzione 2: Interfaccia Visuale (Windows & macOS)
```bash
# Clona il repository
git clone https://github.com/tuo-utente/google-play-reviews-scraper.git
cd google-play-reviews-scraper

# Installa le dipendenze
pip install -r requirements.txt

# Windows: Esegui l'interfaccia grafica
python app_gui.py

# macOS: Esegui l'interfaccia nativa
cd src && python3 app_gui_mac.py
```

### Opzione 3: Riga di Comando (Tutte le Piattaforme)
```bash
# Dopo aver clonato e installato le dipendenze
python review_scraper.py --url "https://play.google.com/store/apps/details?id=com.whatsapp"
```

**🪟 Utenti Windows**: L'interfaccia si aprirà in Portoghese. Usa il selettore di bandiere nell'angolo in alto a destra per cambiare lingua!
**🍎 Utenti macOS**: Interfaccia nativa con 6 lingue, font SF Pro e integrazione Finder!
**🐧 Utenti Linux**: Utilizza l'interfaccia a riga di comando con i parametri mostrati di seguito.

---

## 💻 **Interfaccia Grafica Moderna**

![Google Play Reviews Scraper Screenshot](../assets/screenshots/google-play-reviews-scraper.png)

### 🎬 **Applicazione in Azione**
![Google Play Reviews Scraper Demo](../assets/screenshots/google-play-reviews-scraper.gif)

### ✨ Caratteristiche dell'Interfaccia:
- 🎨 **Design Material Design** moderno e intuitivo
- 🌍 **Multi-lingua** con selettore di bandiere (6 lingue)
- 📋 **Incolla URL** direttamente dal browser
- ⚙️ **Impostazioni semplici** (paese, lingua, cartella)
- 📊 **Progresso in tempo reale** con barra visuale
- 📁 **Apertura automatica** dei file generati
- 📜 **Scorrimento fluido** per schermi piccoli
- ℹ️ **Modal "Informazioni"** con informazioni dello sviluppatore
- 🎯 **Icona personalizzata** nella barra delle applicazioni

### 🌍 **Sistema Multi-lingua**
- **🇺🇸 English**
- **🇧🇷 Português**
- **🇪🇸 Español**
- **🇫🇷 Français**
- **🇩🇪 Deutsch**
- **🇮🇹 Italiano** (Predefinito)

**Selettore con bandiere reali**: Clicca sulla bandiera nell'angolo in alto a destra per cambiare lingua istantaneamente!

---

## 🛠️ **Interfaccia a Riga di Comando**

### 🎬 **Dimostrazione del Terminal**
![Google Play Reviews Scraper Terminal Demo](../assets/screenshots/google-play-reviews-scraper-terminal.gif)

### 🍎🐧 **Per Utenti Mac/Linux (Obbligatorio)**

Poiché l'interfaccia grafica è esclusiva per Windows, gli utenti Mac e Linux devono utilizzare la riga di comando:

```bash
# Uso di base
python review_scraper.py --url "https://play.google.com/store/apps/details?id=com.whatsapp"

# Con impostazioni personalizzate
python review_scraper.py \
  --app-id "com.whatsapp" \
  --country "it" \
  --lang "it" \
  --output "whatsapp_reviews"

# Ottenere aiuto
python review_scraper.py --help
```

### 🪟 **Per Utenti Windows (Opzionale)**

Gli utenti Windows possono anche utilizzare la riga di comando per l'automazione:

```bash
# Esempio di base
python review_scraper.py --url "https://play.google.com/store/apps/details?id=com.whatsapp"

# Con impostazioni personalizzate
python review_scraper.py \
  --app-id "com.whatsapp" \
  --country "us" \
  --lang "en" \
  --output "whatsapp_usa_reviews"

# Aiuto completo
python review_scraper.py --help
```

### **Parametri Disponibili:**
```
--url, -u          URL completa dell'app
--app-id, -a       ID dell'app (es: com.whatsapp)
--country, -c      Codice del paese (predefinito: it)
--lang, -l         Codice della lingua (predefinito: it)
--output, -o       Nome dei file di output
--help, -h         Mostra questo aiuto
```

---

## 📖 **Come Usare**

### 1️⃣ **Trova l'App**
Vai su Google Play Store e trova l'app desiderata. Esempio:
```
https://play.google.com/store/apps/details?id=com.whatsapp
```

### 2️⃣ **Incolla l'URL**
- Apri Google Play Reviews Scraper
- Incolla l'URL completo nel campo
- L'ID dell'app verrà estratto automaticamente

### 3️⃣ **Configura (Opzionale)**
- **Paese**: `it` (Italia), `us` (USA), `br` (Brasile)...
- **Lingua**: `it` (Italiano), `en` (Inglese), `pt` (Portoghese)...
- **Cartella**: Scegli dove salvare i file

### 4️⃣ **Esegui**
Clicca su "Inizia Raccolta" e aspetta. Il processo è automatico!

---

## 🌍 **Lingue Supportate nell'Interfaccia**

L'applicazione supporta **6 lingue** con traduzione completa dell'interfaccia:

| Bandiera | Codice | Lingua | Stato |
|----------|--------|--------|-------|
| 🇺🇸 | `en` | **English** | ✅ Completo |
| 🇧🇷 | `pt` | **Português** | ✅ Completo |
| 🇪🇸 | `es` | **Español** | ✅ Completo |
| 🇫🇷 | `fr` | **Français** | ✅ Completo |
| 🇩🇪 | `de` | **Deutsch** | ✅ Completo |
| 🇮🇹 | `it` | **Italiano** | ✅ Predefinito |

**Come usare**: Clicca sulla bandiera nell'angolo in alto a destra dell'interfaccia per cambiare lingua istantaneamente!

### 🎯 **Cosa viene tradotto:**
- ✅ Tutti i pulsanti e le etichette
- ✅ Titoli delle sezioni
- ✅ Messaggi di stato e registro
- ✅ Modal "Informazioni" completo
- ✅ Placeholder e tooltip
- ✅ Messaggi di errore

---

## 🚀 **Novità della Versione Attuale**

### ✨ **Funzionalità Implementate**
- 🌍 **Sistema multi-lingua completo** (6 lingue)
- 🎨 **Interfaccia Material Design** moderna e responsiva
- 🏳️ **Selettore di bandiere** con immagini PNG reali (24x24px)
- 📜 **Scorrimento fluido** per schermi di qualsiasi dimensione
- 🎯 **Icona personalizzata** Google Play nella barra delle applicazioni
- ℹ️ **Modal "Informazioni"** con informazioni del progetto
- 🔄 **Traduzione istantanea** di tutta l'interfaccia
- 📊 **Barre di progresso** visuali e informative

---

<div align="center">

**Sviluppato con ❤️ da [DSiqueira](https://dsiqueira.com)**

⭐ **Se questo progetto è stato utile, lascia una stella!** ⭐

</div>