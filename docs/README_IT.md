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

## ⚡ Avvio Rapido

### 🎯 **Opzione 1: Applicazione GUI (Consigliata)**

```bash
# 1. Clonare il repository
git clone https://github.com/your-username/google-play-reviews-scraper.git
cd google-play-reviews-scraper

# 2. Installare le dipendenze
pip install -r requirements.txt

# 3. Avviare la GUI
python src/app_gui.py
```

### 🔧 **Opzione 2: Riga di Comando**

```bash
# Estrarre recensioni da una singola app
python src/review_scraper.py --url "https://play.google.com/store/apps/details?id=com.whatsapp"

# Elaborazione in batch di più app
python src/review_scraper.py --batch lista_app.txt --output risultati/
```

### 📦 **Opzione 3: Modulo Python**

```python
from src.review_scraper import GooglePlayReviewScraper

scraper = GooglePlayReviewScraper()
reviews = scraper.scrape_reviews("com.whatsapp")
print(f"{len(reviews)} recensioni estratte!")
```

---

## 📖 Caratteristiche

<div align="center">

| 🎯 **Caratteristiche Principali** | 🎨 **Interfaccia** | 📊 **Output** | 🌍 **Multi-Lingua** |
|:---:|:---:|:---:|:---:|
| Estrae **TUTTE** le recensioni | GUI moderna con temi | Esportazione CSV e JSON | 6 lingue supportate |
| **Elaborazione in batch** | Progresso tempo reale | Analisi dettagliate | Auto-rilevamento lingua |
| **Filtraggio intelligente** | Drag & drop URL | Statistiche tempo | Traduzioni personalizzate |
| **Limitazione velocità** | Coda multi-app | Gestione errori | Supporto RTL |

</div>

### 🚀 **Cosa lo rende speciale?**

- **🎯 Estrazione Completa**: Ottiene TUTTE le recensioni disponibili, non solo quelle recenti
- **⚡ Super Veloce**: Scraping ottimizzato con limitazione intelligente della velocità  
- **🎨 Interfaccia Bella**: GUI moderna con temi chiaro/scuro
- **📊 Analisi Ricche**: Statistiche dettagliate e tracciamento del tempo
- **🔄 Elaborazione in Batch**: Gestisce più app simultaneamente
- **🌍 Multi-Lingua**: Interfaccia disponibile in 6 lingue
- **📱 Rilevamento Intelligente**: Auto-rileva info app e gestisce errori elegantemente
- **💾 Formati Multipli**: Esporta in CSV, JSON con campi personalizzabili
- **🛡️ Robusto**: Gestisce problemi di rete, limiti di velocità e casi estremi

---

## 🛠️ Installazione

### 📋 **Requisiti**

- **Python 3.7+** (3.9+ consigliato)
- **Connessione internet** per lo scraping
- **2GB RAM** minimo (4GB+ per grandi dataset)

### 📦 **Installazione Rapida**

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