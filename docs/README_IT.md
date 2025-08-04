<div align="center">

# 📱 Google Play Reviews Scraper

![Google Play Reviews Scraper](../assets/icons/google-play.png)

**🚀 Strumento professionale per estrarre e analizzare recensioni di app dal Google Play Store**

*Estrai migliaia di recensioni in pochi minuti con un'interfaccia moderna e bella*

---

## 🌍 **Scegli la tua Lingua / Choose Your Language**

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
[![GUI](https://img.shields.io/badge/Interface-GUI_Moderna-blue?style=for-the-badge)](../src/app_gui.py)

**[🎬 Vedi Demo](#-demo) • [⚡ Avvio Rapido](#-avvio-rapido) • [📖 Caratteristiche](#-caratteristiche) • [🛠️ Installazione](#️-installazione)**

---

</div>

## 🎬 Demo

<div align="center">

### 🖥️ Interfaccia Moderna
*Interfaccia bella e intuitiva con supporto multi-lingua*

![Anteprima Interfaccia](../assets/screenshots/interface-preview.png)

### ⚡ Elaborazione in Batch
*Elabora più app simultaneamente con progresso in tempo reale*

![Elaborazione in Batch](../assets/screenshots/batch-processing.gif)

### 📊 Formati di Output Ricchi
*Esporta in CSV, JSON con analisi dettagliate*

![Formati di Output](../assets/screenshots/output-formats.png)

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
## ⚡ Avvio Rapido

### 🎯 **Opzione 1: Applicazione GUI (Consigliata)**

```bash
# 1. Clonare il repository
git clone https://github.com/your-username/google-play-reviews-scraper.git
cd google-play-reviews-scraper

# 2. Installare le dipendenze
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
git clone https://github.com/your-username/google-play-reviews-scraper.git
cd google-play-reviews-scraper
pip install -r requirements.txt
python src/app_gui.py
```

---

## 🎯 Casi d'Uso

### 💼 **Perfetto per:**

- **📊 Ricercatori di Mercato** - Analizzare app concorrenti e tendenze di mercato
- **🎯 Product Manager** - Raccogliere feedback utenti per pianificazione funzionalità  
- **🔍 Ricercatori UX** - Comprendere punti dolenti e preferenze utenti
- **📈 Sviluppatori App** - Monitorare performance e soddisfazione utenti
- **� Analgisti Business** - Generare insights per decisioni strategiche
- **🎓 Studenti e Accademici** - Raccogliere dati per progetti di ricerca

---

## 🌍 **Documentazione Completa in Altre Lingue**

<div align="center">

**📖 Documentazione completa con guide dettagliate, esempi e tutorial:**

[![🇺🇸 Complete English Documentation](https://img.shields.io/badge/🇺🇸-Complete_Documentation-4285f4?style=for-the-badge)](../README.md)
[![🇧� Documuentação Completa em Português](https://img.shields.io/badge/🇧🇷-Documentação_Completa-00a86b?style=for-the-badge)](README_PT.md)
[![🇪🇸 Documentación Completa en Español](https://img.shields.io/badge/🇪🇸-Documentación_Completa-ea4335?style=for-the-badge)](README_ES.md)
[![🇫🇷 Documentation Complète en Français](https://img.shields.io/badge/🇫🇷-Documentation_Complète-4285f4?style=for-the-badge)](README_FR.md)
[![🇩🇪 Vollständige Dokumentation auf Deutsch](https://img.shields.io/badge/🇩🇪-Vollständige_Dokumentation-333333?style=for-the-badge)](README_DE.md)

**📋 [Vedi Tutte le Lingue e Guida alla Traduzione](LANGUAGES.md)**

</div>

---

## � Licenza

Questo progetto è sotto licenza **MIT** - vedi il file [LICENSE](../LICENSE) per i dettagli.

---

<div align="center">

**🚀 Sviluppato con ❤️ per la comunità**

**Se questo progetto ti ha aiutato, considera di dargli una ⭐!**

[![GitHub stars](https://img.shields.io/github/stars/your-username/google-play-reviews-scraper?style=social)](../../stargazers)
[![GitHub forks](https://img.shields.io/github/forks/your-username/google-play-reviews-scraper?style=social)](../../network/members)

</div>