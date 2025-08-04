<div align="center">

# 📱 Google Play Reviews Scraper

![Google Play Reviews Scraper](assets/icons/google-play.png)

**🚀 Professional tool to extract and analyze app reviews from Google Play Store**

*Extract thousands of reviews in minutes with a beautiful, modern interface*

---

## 🌍 **Choose Your Language / Escolha seu Idioma**

[![🇺🇸 English](https://img.shields.io/badge/🇺🇸-English-4285f4?style=for-the-badge&labelColor=white)](README.md)
[![🇧🇷 Português](https://img.shields.io/badge/🇧🇷-Português-00a86b?style=for-the-badge&labelColor=white)](docs/README_PT.md)
[![🇪🇸 Español](https://img.shields.io/badge/🇪🇸-Español-ea4335?style=for-the-badge&labelColor=white)](docs/README_ES.md)
[![🇫🇷 Français](https://img.shields.io/badge/🇫🇷-Français-4285f4?style=for-the-badge&labelColor=white)](docs/README_FR.md)
[![🇩🇪 Deutsch](https://img.shields.io/badge/🇩🇪-Deutsch-333333?style=for-the-badge&labelColor=white)](docs/README_DE.md)
[![🇮🇹 Italiano](https://img.shields.io/badge/🇮🇹-Italiano-00a86b?style=for-the-badge&labelColor=white)](docs/README_IT.md)

---

[![Python](https://img.shields.io/badge/Python-3.7+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Cross--Platform-lightgrey?style=for-the-badge)](https://github.com)
[![GUI](https://img.shields.io/badge/Interface-Modern_GUI-blue?style=for-the-badge)](src/app_gui.py)

**[🎬 See Demo](#-demo) • [⚡ Quick Start](#-quick-start) • [📖 Features](#-features) • [🛠️ Installation](#️-installation)**

---

</div>

## 🎬 Demo

<div align="center">

### 🖥️ Modern Interface
*Beautiful, intuitive GUI with multi-language support*

![Interface Preview](assets/screenshots/google-play-reviews-scraper.png)

### ⚡ Application in Action
*See the scraper working with real-time progress*

![Application Demo](assets/screenshots/google-play-reviews-scraper.gif)

### 📊 Command Line Interface
*Also available via terminal for automation*

![Terminal Demo](assets/screenshots/google-play-reviews-scraper-terminal.gif)

</div>

---

## ⚡ Quick Start

### 🎯 **Option 1: GUI Application (Recommended)**

```bash
# 1. Clone the repository
git clone https://github.com/dssiqueira/google-play-reviews-scraper.git
cd google-play-reviews-scraper

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the GUI
python src/app_gui.py
```

### 🔧 **Option 2: Command Line**

```bash
# Extract reviews from a single app
python src/review_scraper.py --url "https://play.google.com/store/apps/details?id=com.whatsapp"

# Batch process multiple apps
python src/review_scraper.py --batch apps_list.txt --output results/
```

### 📦 **Option 3: Python Module**

```python
from src.review_scraper import GooglePlayReviewScraper

scraper = GooglePlayReviewScraper()
reviews = scraper.scrape_reviews("com.whatsapp")
print(f"Extracted {len(reviews)} reviews!")
```

---

## 📖 Features

<div align="center">

| 🎯 **Core Features** | 🎨 **Interface** | 📊 **Output** | 🌍 **Multi-Language** |
|:---:|:---:|:---:|:---:|
| Extract **ALL** reviews | Modern GUI with themes | CSV & JSON export | 6 languages supported |
| **Batch processing** | Real-time progress | Detailed analytics | Auto-detect locale |
| **Smart filtering** | Drag & drop URLs | Time statistics | Custom translations |
| **Rate limiting** | Multi-app queue | Error handling | RTL support |

</div>

### 🚀 **What makes it special?**

- **🎯 Complete Extraction**: Gets ALL available reviews, not just recent ones
- **⚡ Lightning Fast**: Optimized scraping with intelligent rate limiting  
- **🎨 Beautiful Interface**: Modern GUI with light/dark themes
- **📊 Rich Analytics**: Detailed statistics and time tracking
- **🔄 Batch Processing**: Handle multiple apps simultaneously
- **🌍 Multi-Language**: Interface available in 6 languages
- **📱 Smart Detection**: Auto-detects app info and handles errors gracefully
- **💾 Multiple Formats**: Export to CSV, JSON with customizable fields
- **�️e Robust**: Handles network issues, rate limits, and edge cases

---

## 🛠️ Installation

### 📋 **Requirements**

- **Python 3.7+** (3.9+ recommended)
- **Internet connection** for scraping
- **2GB RAM** minimum (4GB+ for large datasets)

### 📦 **Quick Installation**

```bash
git clone https://github.com/dssiqueira/google-play-reviews-scraper.git
cd google-play-reviews-scraper
pip install -r requirements.txt
python src/app_gui.py
```

---

## 🎯 Use Cases

### 💼 **Perfect for:**

- **📊 Market Researchers** - Analyze competitor apps and market trends
- **🎯 Product Managers** - Gather user feedback for feature planning  
- **� U*X Researchers** - Understand user pain points and preferences
- **📈 App Developers** - Monitor app performance and user satisfaction
- **🏢 Business Analysts** - Generate insights for strategic decisions
- **🎓 Students & Academics** - Collect data for research projects

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**🚀 Developed with ❤️ for the community**

**If this project helped you, please consider giving it a ⭐!**

[![GitHub stars](https://img.shields.io/github/stars/dssiqueira/google-play-reviews-scraper?style=social)](../../stargazers)
[![GitHub forks](https://img.shields.io/github/forks/dssiqueira/google-play-reviews-scraper?style=social)](../../network/members)

</div>