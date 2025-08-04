# 📱 Google Play Reviews Scraper

<div align="center">

**🌍 Language / Idioma / Langue / Sprache / Lingua**

[![🇺🇸 English](https://img.shields.io/badge/🇺🇸-English-blue?style=for-the-badge)](docs/README.md)
[![🇧🇷 Português](https://img.shields.io/badge/🇧🇷-Português-green?style=for-the-badge)](docs/README_PT.md)
[![🇪🇸 Español](https://img.shields.io/badge/🇪🇸-Español-red?style=for-the-badge)](docs/README_ES.md)
[![🇫🇷 Français](https://img.shields.io/badge/🇫🇷-Français-blue?style=for-the-badge)](docs/README_FR.md)
[![🇩🇪 Deutsch](https://img.shields.io/badge/🇩🇪-Deutsch-black?style=for-the-badge)](docs/README_DE.md)
[![🇮🇹 Italiano](https://img.shields.io/badge/🇮🇹-Italiano-green?style=for-the-badge)](docs/README_IT.md)

---

![Google Play Reviews Scraper](assets/icons/google-play.png)

**Professional tool to extract and analyze app reviews from Google Play Store**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)](#-quick-start)

</div>

---

## 🚀 **Quick Start**

### **🪟 Windows Users (Recommended)**
1. Download the executable from [releases page](../../releases)
2. Run `GooglePlayReviewScraper.exe`
3. Done! No Python installation required

### **🍎 macOS Users (Visual Interface)**
```bash
# Clone the repository
git clone https://github.com/your-username/google-play-reviews-scraper.git
cd google-play-reviews-scraper

# Install dependencies
pip install -r requirements.txt

# Run the macOS visual interface
cd src && python3 app_gui_mac.py
```

**✨ macOS Features:**
- 🌍 **6 languages**: Portuguese, English, Spanish, French, German, Italian
- 🎨 **Native macOS design** with SF Pro fonts
- 🖱️ **Trackpad support** and native scroll
- 📁 **Finder integration** for easy file access

### **🐧 Linux Users (Command Line)**
```bash
# Clone the repository
git clone https://github.com/your-username/google-play-reviews-scraper.git
cd google-play-reviews-scraper

# Install dependencies
pip install -r requirements.txt

# Run the command line interface
python src/review_scraper.py --url "https://play.google.com/store/apps/details?id=com.whatsapp"
```

---

## 📖 **Full Documentation**

Choose your language for complete documentation:

- **🇺🇸 [English Documentation](docs/README.md)**
- **🇧🇷 [Documentação em Português](docs/README_PT.md)**
- **🇪🇸 [Documentación en Español](docs/README_ES.md)**
- **🇫🇷 [Documentation en Français](docs/README_FR.md)**
- **🇩🇪 [Deutsche Dokumentation](docs/README_DE.md)**
- **🇮🇹 [Documentazione Italiana](docs/README_IT.md)**

---

## 📁 **Project Structure**

```
google-play-reviews-scraper/
├── 📁 src/                          # Source code
│   ├── app_gui.py                   # GUI application
│   ├── review_scraper.py            # Scraping engine
│   └── translations.py              # Translation system
├── 📁 docs/                         # Documentation
│   ├── README.md                    # English docs
│   ├── README_PT.md                 # Portuguese docs
│   └── ...                          # Other languages
├── 📁 assets/                       # Visual resources
│   ├── icons/                       # App icons
│   ├── flags/                       # Language flags
│   └── screenshots/                 # Screenshots & demos
├── 📁 build/                        # Build scripts
├── 📁 examples/                     # Sample output files
│   ├── sample_app_reviews.csv       # Sample CSV output
│   ├── sample_app_reviews.json      # Sample JSON output
│   └── README.md                    # Examples documentation
├── requirements.txt                 # Python dependencies
└── LICENSE                          # MIT License
```

---

## 🎯 **What does it do?**

Extracts **ALL** available reviews from any Google Play Store app quickly, organized and reliably. Perfect for:

- 📊 **Market analysis** and competition research
- 🔍 **UX research** and user feedback analysis  
- 📈 **App reputation** monitoring
- 🎯 **Product development** insights
- 📋 **Reports** and presentations

---

## 💻 **Interface Preview**

![Google Play Reviews Scraper Screenshot](assets/screenshots/google-play-reviews-scraper.png)

### 🎬 **Application in Action**
![Google Play Reviews Scraper Demo](assets/screenshots/google-play-reviews-scraper.gif)

---

## 🛠️ **Command Line Preview**

### 🎬 **Terminal Usage Demo**
![Google Play Reviews Scraper Terminal Demo](assets/screenshots/google-play-reviews-scraper-terminal.gif)

---

## 📄 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Developed with ❤️ by [DSiqueira](https://dsiqueira.com)**

⭐ **If this project was useful, leave a star!** ⭐

</div>