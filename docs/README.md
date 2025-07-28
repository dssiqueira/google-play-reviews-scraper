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

**Professional tool to extract and analyze app reviews from Google Play Store**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)](https://windows.microsoft.com)

</div>

---

## 🎯 **What does it do?**

Extracts **ALL** available reviews from any Google Play Store app quickly, organized and reliably. Perfect for:

- 📊 **Market analysis** and competition research
- 🔍 **UX research** and user feedback analysis  
- 📈 **App reputation** monitoring
- 🎯 **Product development** insights
- 📋 **Reports** and presentations

---

## 🚀 **Quick Installation**

### 🖥️ **Platform Compatibility**

| Platform | GUI Interface | Command Line | Executable |
|----------|---------------|--------------|------------|
| 🪟 **Windows** | ✅ Full support | ✅ Supported | ✅ Available |
| 🍎 **macOS** | ❌ Terminal only | ✅ Supported | ❌ Not available |
| 🐧 **Linux** | ❌ Terminal only | ✅ Supported | ❌ Not available |

> **Note**: The graphical interface is currently Windows-only. Mac and Linux users can use the command-line version.

### Option 1: Executable (Windows Only)
1. Download the executable from [releases page](../../releases)
2. Run `GooglePlayReviewScraper.exe`
3. Done! No need to install Python

### Option 2: Source Code (All Platforms)
```bash
# Clone the repository
git clone https://github.com/your-username/google-play-reviews-scraper.git
cd google-play-reviews-scraper

# Install dependencies
pip install -r requirements.txt

# Windows: Run GUI
python app_gui.py

# Mac/Linux: Use command line
python review_scraper.py --url "https://play.google.com/store/apps/details?id=com.whatsapp"
```

**Windows users**: Interface opens in Portuguese. Use the flag selector in the top-right corner to change language!
**Mac/Linux users**: Use the command-line interface with the parameters shown below.

---

## 💻 **Modern Graphical Interface**

![Google Play Reviews Scraper Screenshot](../assets/screenshots/google-play-reviews-scraper.png)

### 🎬 **Application in Action**
![Google Play Reviews Scraper Demo](../assets/screenshots/google-play-reviews-scraper.gif)

### ✨ Interface Features:
- 🎨 **Modern Material Design** intuitive interface
- 📋 **Paste URL** directly from browser
- ⚙️ **Simple settings** (country, language, folder)
- ⏱️ **Real-time progress**
- 📁 **Auto-open** generated files
- ℹ️ **Developer information** modal
- 🌍 **Multi-language** with flag selector (6 languages)
- 📜 **Smooth scrolling** for small screens
- 🎯 **Custom icon** in taskbar

### 🌍 **Multi-language System**
- **🇺🇸 English** (Default)
- **🇧🇷 Português**
- **🇪🇸 Español** 
- **🇫🇷 Français**
- **🇩🇪 Deutsch**
- **🇮🇹 Italiano**

**Real flag selector**: Click the flag in the top-right corner to change language instantly!

---

## 📖 **How to Use**

### 1️⃣ **Find the App**
Go to Google Play Store and find the desired app. Example:
```
https://play.google.com/store/apps/details?id=com.whatsapp
```

### 2️⃣ **Paste the URL**
- Open Google Play Reviews Scraper
- Paste the complete URL in the field
- App ID will be extracted automatically

### 3️⃣ **Configure (Optional)**
- **Country**: `us` (USA), `br` (Brazil), `uk` (United Kingdom)...
- **Language**: `en` (English), `pt` (Portuguese), `es` (Spanish)...
- **Folder**: Choose where to save files

### 4️⃣ **Execute**
Click "Start Collection" and wait. The process is automatic!

---

## 📊 **Extracted Data**

For each collected review, you get:

| Field | Description | Example |
|-------|-------------|---------|
| **user_name** | User name | "John Silva" |
| **content** | Review text | "Excellent app, very useful!" |
| **score** | Rating (1-5 stars) | 5 |
| **date** | Review date | "2024-01-15" |
| **thumbs_up** | Number of likes | 12 |
| **reply_content** | Developer response | "Thanks for the feedback!" |
| **reply_date** | Response date | "2024-01-16" |
| **app_version** | App version | "2.24.1.78" |

---

## 📁 **Generated Files**

### 📄 **CSV (Excel/Spreadsheets)**
```
whatsapp_messenger_reviews.csv
```
- Perfect for analysis in Excel, Google Sheets
- Automatic filters and charts
- Easy sharing

### 📋 **JSON (Programming)**
```json
{
  "user_name": "Maria Santos",
  "content": "Best messaging app!",
  "score": 5,
  "date": "2024-01-15",
  "thumbs_up": 8,
  "reply_content": null,
  "app_version": "2.24.1.78"
}
```

---

## 🎯 **Practical Example: WhatsApp**

### **Input:**
```
URL: https://play.google.com/store/apps/details?id=com.whatsapp
Country: Brazil (br)
Language: Portuguese (pt)
```

### **Output:**
```
🔍 Processing: WhatsApp Messenger
📱 Developer: WhatsApp LLC
⭐ Rating: 4.2/5 (2.1M reviews)

📊 Collecting reviews...
✅ Page 1: 40 reviews
✅ Page 2: 40 reviews
...
✅ Page 250: 35 reviews

🎉 Collection completed!
📈 Total collected: 9.847 reviews

📊 Statistics:
⭐ Average rating: 4.18
📈 Distribution:
  5★: 6.234 (63.3%) ████████████████████████████████
  4★: 1.456 (14.8%) ███████████████
  3★: 892 (9.1%)    █████████
  2★: 567 (5.8%)    ██████
  1★: 698 (7.1%)    ███████

💾 Files saved:
📄 whatsapp_messenger_reviews.csv (2.1 MB)
📋 whatsapp_messenger_reviews.json (3.4 MB)
```

---

## 🛠️ **Command Line Interface**

### � ***Terminal Usage Demo**
![Google Play Reviews Scraper Terminal Demo](../assets/screenshots/google-play-reviews-scraper-terminal.gif)

### 🍎🐧 **For Mac/Linux Users (Required)**

Since the GUI is Windows-only, Mac and Linux users must use the command line:

```bash
# Basic usage
python review_scraper.py --url "https://play.google.com/store/apps/details?id=com.whatsapp"

# With custom settings
python review_scraper.py \
  --app-id "com.whatsapp" \
  --country "us" \
  --lang "en" \
  --output "whatsapp_reviews"

# Get help
python review_scraper.py --help
```

### 🪟 **For Windows Users (Optional)**

Windows users can also use the command line for automation:

```bash
# Basic example
python review_scraper.py --url "https://play.google.com/store/apps/details?id=com.whatsapp"

# With custom settings
python review_scraper.py \
  --app-id "com.whatsapp" \
  --country "us" \
  --lang "en" \
  --output "whatsapp_usa_reviews"

# Complete help
python review_scraper.py --help
```

### **Available Parameters:**
```
--url, -u          Complete app URL
--app-id, -a       App ID (ex: com.whatsapp)
--country, -c      Country code (default: us)
--lang, -l         Language code (default: en)
--output, -o       Output file names
--help, -h         Show this help
```

---

## 🌍 **Supported Interface Languages**

The application supports **6 languages** with complete interface translation:

| Bandeira | Código | Idioma | Status |
|----------|--------|--------|--------|
| 🇧🇷 | `pt` | **Português** | ✅ Padrão |
| 🇺🇸 | `en` | **English** | ✅ Completo |
| 🇪🇸 | `es` | **Español** | ✅ Completo |
| 🇫🇷 | `fr` | **Français** | ✅ Completo |
| 🇩🇪 | `de` | **Deutsch** | ✅ Completo |
| 🇮🇹 | `it` | **Italiano** | ✅ Completo |

**How to use**: Click the flag in the top-right corner of the interface to change language instantly!

### 🎯 **What is translated:**
- ✅ All buttons and labels
- ✅ Section titles
- ✅ Status and log messages
- ✅ Complete "About" modal
- ✅ Placeholders and tooltips
- ✅ Error messages

---

## 🔧 **Generate Executable**

To create your own executable:

```bash
# Run the build script
python build_simple.py

# The executable will be created at:
dist/GooglePlayReviewScraper.exe
```

## 📁 **Project Structure**

```
google-play-reviews-scraper/
├── 📄 app_gui.py              # Main graphical interface
├── 📄 review_scraper.py       # Scraping logic
├── 📄 translations.py         # Multi-language system
├── 📄 build_simple.py         # Script to generate executable
├── 📄 requirements.txt        # Python dependencies
├── 📄 README.md              # Documentation
├── 📄 LICENSE                # MIT License
└── 📁 img/                   # Visual resources
    ├── 🖼️ google-play.png     # Application icon
    ├── 🖼️ google-play.ico     # Windows icon
    ├── 🇧🇷 br.png             # Brazil flag
    ├── 🇺🇸 en.png             # USA/England flag
    ├── 🇪🇸 es.png             # Spain flag
    ├── 🇫🇷 fr.png             # France flag
    ├── 🇩🇪 al.png             # Germany flag
    └── 🇮🇹 it.png             # Italy flag
```

### 🔑 **Main Files**
- **`app_gui.py`**: Modern interface with Material Design
- **`translations.py`**: Complete translation system
- **`review_scraper.py`**: Review extraction engine
- **`img/`**: High-quality icons and flags

---

## 📈 **Use Cases**

### 🏢 **For Companies**
- Monitor competitor app feedback
- Analyze user sentiment
- Identify recurring issues
- Track feature releases

### 🎓 **For Researchers**
- UX and behavior studies
- Mobile market analysis
- Academic research
- Machine learning datasets

### 👨‍💻 **For Developers**
- Feedback on your own apps
- Competition analysis
- Identify reported bugs
- Insights for improvements

---

## 🔗 **Complementary Tools**

### 📊 **Advanced Analysis**
After extracting the data, use our analysis tool:

**[Review Stats Pro](https://review-stats-pro.lovable.app/)**
- Interactive charts
- Sentiment analysis
- Temporal comparison
- Automatic reports

---

## ⚡ **Performance and Features**

| Metric | Value |
|--------|-------|
| **Speed** | ~200 reviews/minute |
| **Accuracy** | 99.9% of data |
| **Limit** | No review limit |
| **Stability** | Automatic retry |
| **Languages** | 6 supported languages |
| **Interface** | Responsive Material Design |

### 🎨 **Interface Features**
- **Responsive design**: Works on any resolution
- **Smart scrolling**: Smooth navigation on small screens  
- **Custom icon**: Google Play in taskbar
- **Visual feedback**: Progress bars and real-time status
- **Accessibility**: Hover effects and appropriate cursor
- **Informative modal**: About project and developer

---

## 🛡️ **Legal Considerations**

- ✅ Public data from Google Play Store
- ✅ Respects robots.txt and rate limits
- ✅ No login or authentication required
- ⚠️ Use responsibly and respect terms of use

---

## 🤝 **Contributing**

Contributions are welcome! 

1. Fork the project
2. Create a branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request

---

## 📞 **Support**

Need help? Get in touch:

- 🌐 **Website**: [dsiqueira.com](https://dsiqueira.com)
- 📧 **Email**: contato@dsiqueira.com
- 💬 **Issues**: [GitHub Issues](../../issues)

---

## 📄 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

## 🚀 **Current Version Features**

### ✨ **Implemented Features**
- 🌍 **Complete multi-language system** (6 languages)
- 🎨 **Modern and responsive** Material Design interface
- 🏳️ **Flag selector** with real PNG images (24x24px)
- 📜 **Smooth scrolling** for screens of any size
- 🎯 **Custom Google Play icon** in taskbar
- ℹ️ **"About" modal** with project information
- 🔄 **Instant translation** of entire interface
- 📊 **Visual and informative** progress bars

### 🎯 **Technical Improvements**
- **Modular architecture**: Clear separation between interface and logic
- **Translation system**: Easy to add new languages
- **Resource management**: Optimized image loading
- **Error handling**: Fallbacks for compatibility
- **Performance**: Fluid and responsive interface

---

**Developed with ❤️ by [DSiqueira](https://dsiqueira.com)**

⭐ **If this project was useful, leave a star!** ⭐

</div>