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

![Interface Preview](assets/screenshots/interface-preview.png)

### ⚡ Batch Processing
*Process multiple apps simultaneously with real-time progress*

![Batch Processing](assets/screenshots/batch-processing.gif)

### 📊 Rich Output Formats
*Export to CSV, JSON with detailed analytics*

![Output Formats](assets/screenshots/output-formats.png)

</div>

---

## ⚡ Quick Start

### 🎯 **Option 1: GUI Application (Recommended)**

```bash
# 1. Clone the repository
git clone https://github.com/your-username/google-play-reviews-scraper.git
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
- **🛡️ Robust**: Handles network issues, rate limits, and edge cases

---

## �️ Instaellation

### 📋 **Requirements**

- **Python 3.7+** (3.9+ recommended)
- **Internet connection** for scraping
- **2GB RAM** minimum (4GB+ for large datasets)

### � *o*Dependencies**

```bash
# Core dependencies (automatically installed)
google-play-scraper  # Google Play Store API
pandas              # Data processing
tkinter            # GUI framework (usually pre-installed)
```

### � **Insltallation Methods**

#### **Method 1: Git Clone (Recommended)**
```bash
git clone https://github.com/your-username/google-play-reviews-scraper.git
cd google-play-reviews-scraper
pip install -r requirements.txt
```

#### **Method 2: Direct Download**
```bash
# Download ZIP from GitHub
# Extract to desired folder
cd google-play-reviews-scraper-main
pip install -r requirements.txt
```

#### **Method 3: Virtual Environment (Advanced)**
```bash
python -m venv scraper_env
source scraper_env/bin/activate  # Linux/Mac
# or
scraper_env\Scripts\activate     # Windows

pip install -r requirements.txt
```

### ✅ **Verify Installation**

```bash
# Test the scraper
python src/review_scraper.py --help

# Launch GUI
python src/app_gui.py
```

---

## 📊 Usage Examples

### 🎯 **GUI Usage**

1. **Launch the application**
   ```bash
   python src/app_gui.py
   ```

2. **Add apps to queue**
   - Paste Google Play Store URL
   - Click "Add" to queue
   - Repeat for multiple apps

3. **Configure settings**
   - Choose country/language
   - Set output directory
   - Select export format

4. **Start extraction**
   - Click "Start Scraping"
   - Monitor real-time progress
   - Access results via buttons

### 🔧 **Command Line Usage**

```bash
# Basic usage
python src/review_scraper.py --url "https://play.google.com/store/apps/details?id=com.whatsapp"

# Advanced options
python src/review_scraper.py \
  --url "https://play.google.com/store/apps/details?id=com.whatsapp" \
  --country "us" \
  --language "en" \
  --output "whatsapp_reviews" \
  --format "both"

# Batch processing
python src/review_scraper.py --batch apps_list.txt --output results/
```

### 🐍 **Python Integration**

```python
from src.review_scraper import GooglePlayReviewScraper

# Initialize scraper
scraper = GooglePlayReviewScraper(country='us', lang='en')

# Extract reviews
reviews = scraper.scrape_reviews('com.whatsapp')

# Process results
print(f"Total reviews: {len(reviews)}")
for review in reviews[:5]:  # Show first 5
    print(f"⭐ {review['score']}/5 - {review['content'][:100]}...")
```

---

## �  Output Examples

### 📄 **CSV Output**
```csv
userName,score,content,thumbsUpCount,reviewCreatedVersion,at,appVersion
John Doe,5,"Amazing app! Love the new features",42,1.2.3,2024-01-15,1.2.3
Jane Smith,4,"Good but needs improvement in UI",15,1.2.2,2024-01-14,1.2.3
...
```

### � **JSON Output**
```json
{
  "app_info": {
    "title": "WhatsApp Messenger",
    "appId": "com.whatsapp",
    "score": 4.1,
    "reviews_count": 50000000
  },
  "extraction_info": {
    "total_reviews": 1500,
    "extraction_date": "2024-01-15T10:30:00Z",
    "time_taken": "2m 34s"
  },
  "reviews": [
    {
      "userName": "John Doe",
      "score": 5,
      "content": "Amazing app! Love the new features",
      "thumbsUpCount": 42,
      "at": "2024-01-15T08:20:00Z"
    }
  ]
}
```

### 📊 **Statistics Generated**
- **Total reviews extracted**
- **Average rating**
- **Rating distribution (1-5 stars)**
- **Extraction time and speed**
- **Most helpful reviews**
- **Recent vs older reviews ratio**

---

## 🌍 **Complete Documentation in Other Languages**

<div align="center">

**📖 Full documentation with detailed guides, examples, and tutorials:**

[![🇧🇷 Documentação Completa em Português](https://img.shields.io/badge/🇧🇷-Documentação_Completa-00a86b?style=for-the-badge)](docs/README_PT.md)
[![🇪🇸 Documentación Completa en Español](https://img.shields.io/badge/🇪🇸-Documentación_Completa-ea4335?style=for-the-badge)](docs/README_ES.md)
[![🇫🇷 Documentation Complète en Français](https://img.shields.io/badge/🇫🇷-Documentation_Complète-4285f4?style=for-the-badge)](docs/README_FR.md)
[![🇩🇪 Vollständige Dokumentation auf Deutsch](https://img.shields.io/badge/🇩🇪-Vollständige_Dokumentation-333333?style=for-the-badge)](docs/README_DE.md)
[![🇮🇹 Documentazione Completa in Italiano](https://img.shields.io/badge/🇮🇹-Documentazione_Completa-00a86b?style=for-the-badge)](docs/README_IT.md)

*Each language version includes localized examples, cultural context, and region-specific guidance*

**📋 [View All Languages & Translation Guide](docs/LANGUAGES.md)**

</div>

---

## 📁 Project Structure

```
📦 google-play-reviews-scraper/
├── 📂 src/                          # 🐍 Source code
│   ├── app_gui.py                   # 🖥️ Modern GUI application
│   ├── review_scraper.py            # ⚙️ Core scraping engine
│   ├── translations.py              # 🌍 Multi-language support
│   └── time_stats.py                # 📊 Performance analytics
├── 📂 assets/                       # 🎨 Visual resources
│   ├── icons/                       # 🎯 Application icons
│   │   ├── google-play.png          # 📱 Main app icon
│   │   └── google-play.ico          # 🖼️ Windows icon
│   ├── flags/                       # 🏳️ Language flags (24x24px)
│   │   ├── br.png                   # 🇧🇷 Brazil
│   │   ├── en.png                   # 🇺🇸 English
│   │   └── ...                      # 🌍 Other languages
│   └── screenshots/                 # 📸 Demo images
├── 📂 docs/                         # 📖 Documentation
│   ├── README.md                    # 🇺🇸 English docs
│   ├── README_PT.md                 # 🇧🇷 Portuguese docs
│   └── TRANSLATIONS.md              # 🌍 Translation guide
├── 📂 examples/                     # 📋 Sample outputs
│   ├── sample_reviews.csv           # 📊 CSV example
│   ├── sample_reviews.json          # 📄 JSON example
│   └── README.md                    # 📝 Examples guide
├── 📄 requirements.txt              # 📦 Python dependencies
├── 📄 LICENSE                       # ⚖️ MIT License
└── 📄 README.md                     # 📖 This file
```

---

## 🎯 Use Cases

<div align="center">

| 🏢 **Business** | 🔬 **Research** | 📱 **Development** | 📊 **Analytics** |
|:---:|:---:|:---:|:---:|
| Competitor analysis | User behavior studies | Feature feedback | Market trends |
| Market research | Academic research | Bug reports | Sentiment analysis |
| Brand monitoring | UX research | App store optimization | Performance metrics |
| Customer insights | Survey data | User testing | Reputation management |

</div>

### 💼 **Perfect for:**

- **📊 Market Researchers** - Analyze competitor apps and market trends
- **🎯 Product Managers** - Gather user feedback for feature planning  
- **🔍 UX Researchers** - Understand user pain points and preferences
- **📈 App Developers** - Monitor app performance and user satisfaction
- **🏢 Business Analysts** - Generate insights for strategic decisions
- **🎓 Students & Academics** - Collect data for research projects

---

## 🌍 Multi-Language Support

<div align="center">

**🇺🇸 English** • **🇧🇷 Português** • **🇪🇸 Español** • **🇫🇷 Français** • **🇩🇪 Deutsch** • **🇮🇹 Italiano**

*Interface automatically adapts to your system language*

</div>

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### 🐛 **Report Issues**
- Found a bug? [Open an issue](../../issues)
- Include steps to reproduce
- Provide system information

### 💡 **Suggest Features**
- Have an idea? [Start a discussion](../../discussions)
- Explain the use case
- Provide mockups if possible

### 🔧 **Code Contributions**
```bash
# 1. Fork the repository
# 2. Create a feature branch
git checkout -b feature/amazing-feature

# 3. Make your changes
# 4. Test thoroughly
python -m pytest tests/

# 5. Submit a pull request
```

### 🌍 **Translations**
Help us support more languages! See [translations guide](docs/TRANSLATIONS.md).

---

## 📞 Support

### 🆘 **Need Help?**

- **📖 Documentation**: Check our [detailed guides](docs/)
- **💬 Discussions**: Join our [community discussions](../../discussions)
- **🐛 Issues**: Report bugs in [issues section](../../issues)
- **📧 Email**: Contact us at support@example.com

### ❓ **FAQ**

<details>
<summary><strong>🔍 How many reviews can I extract?</strong></summary>

The tool extracts ALL available reviews from Google Play Store. This can range from hundreds to millions depending on the app's popularity.

</details>

<details>
<summary><strong>⚡ How fast is the extraction?</strong></summary>

Speed varies by app size and network conditions. Typical rates:
- Small apps (< 1K reviews): 30-60 seconds
- Medium apps (1K-10K reviews): 2-5 minutes  
- Large apps (10K+ reviews): 5-30 minutes

</details>

<details>
<summary><strong>🌍 Which countries/languages are supported?</strong></summary>

All countries and languages supported by Google Play Store. The tool automatically handles localization and regional differences.

</details>

<details>
<summary><strong>🛡️ Is this legal?</strong></summary>

Yes! The tool only accesses publicly available data from Google Play Store, similar to viewing reviews in a web browser.

</details>

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### 🔓 **What this means:**
- ✅ **Commercial use** allowed
- ✅ **Modification** allowed  
- ✅ **Distribution** allowed
- ✅ **Private use** allowed
- ❌ **No warranty** provided
- ❌ **No liability** assumed

---

## 🏆 Acknowledgments

### 🙏 **Special Thanks**

- **[google-play-scraper](https://github.com/JoMingyu/google-play-scraper)** - Core scraping functionality
- **[pandas](https://pandas.pydata.org/)** - Data processing and analysis
- **[tkinter](https://docs.python.org/3/library/tkinter.html)** - GUI framework
- **Community contributors** - Bug reports, feature requests, and translations

### 🌟 **Inspiration**

This project was created to democratize access to app store data for researchers, developers, and businesses who need insights but lack the resources for expensive analytics tools.

---

<div align="center">

## ⭐ **Star History**

[![Star History Chart](https://api.star-history.com/svg?repos=your-username/google-play-reviews-scraper&type=Date)](https://star-history.com/#your-username/google-play-reviews-scraper&Date)

---

**🚀 Developed with ❤️ for the community**

**If this project helped you, please consider giving it a ⭐!**

*Your support motivates us to keep improving and adding new features*

[![GitHub stars](https://img.shields.io/github/stars/your-username/google-play-reviews-scraper?style=social)](../../stargazers)
[![GitHub forks](https://img.shields.io/github/forks/your-username/google-play-reviews-scraper?style=social)](../../network/members)
[![GitHub watchers](https://img.shields.io/github/watchers/your-username/google-play-reviews-scraper?style=social)](../../watchers)

</div>