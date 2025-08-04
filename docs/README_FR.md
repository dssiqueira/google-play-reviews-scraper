<div align="center">

# 📱 Google Play Reviews Scraper

![Google Play Reviews Scraper](../assets/icons/google-play.png)

**🚀 Outil professionnel pour extraire et analyser les avis d'applications du Google Play Store**

*Extrayez des milliers d'avis en quelques minutes avec une interface moderne et belle*

---

## 🌍 **Choisissez votre Langue / Choose Your Language**

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
[![GUI](https://img.shields.io/badge/Interface-GUI_Moderne-blue?style=for-the-badge)](../src/app_gui.py)

**[🎬 Voir Démo](#-démo) • [⚡ Démarrage Rapide](#-démarrage-rapide) • [📖 Fonctionnalités](#-fonctionnalités) • [🛠️ Installation](#️-installation)**

---

</div>

## 🎬 Démo

<div align="center">

### 🖥️ Interface Moderne
*Interface belle et intuitive avec support multi-langues*

![Aperçu Interface](../assets/screenshots/interface-preview.png)

### ⚡ Traitement par Lots
*Traite plusieurs applications simultanément avec progression en temps réel*

![Traitement par Lots](../assets/screenshots/batch-processing.gif)

### 📊 Formats de Sortie Riches
*Exporte vers CSV, JSON avec analyses détaillées*

![Formats de Sortie](../assets/screenshots/output-formats.png)

</div>

---

## ⚡ Démarrage Rapide

### 🎯 **Option 1: Application GUI (Recommandée)**

```bash
# 1. Cloner le dépôt
git clone https://github.com/your-username/google-play-reviews-scraper.git
cd google-play-reviews-scraper

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Lancer la GUI
python src/app_gui.py
```

### 🔧 **Option 2: Ligne de Commande**

```bash
# Extraire les avis d'une seule application
python src/review_scraper.py --url "https://play.google.com/store/apps/details?id=com.whatsapp"

# Traitement par lots de plusieurs applications
python src/review_scraper.py --batch liste_apps.txt --output resultats/
```

### 📦 **Option 3: Module Python**

```python
from src.review_scraper import GooglePlayReviewScraper

scraper = GooglePlayReviewScraper()
reviews = scraper.scrape_reviews("com.whatsapp")
print(f"{len(reviews)} avis extraits!")
```

---

## 📖 Fonctionnalités

<div align="center">

| 🎯 **Fonctionnalités Principales** | 🎨 **Interface** | 📊 **Sortie** | 🌍 **Multi-Langues** |
|:---:|:---:|:---:|:---:|
| Extrait **TOUS** les avis | GUI moderne avec thèmes | Export CSV et JSON | 6 langues supportées |
| **Traitement par lots** | Progression temps réel | Analyses détaillées | Auto-détection langue |
| **Filtrage intelligent** | Glisser-déposer URLs | Statistiques temps | Traductions personnalisées |
| **Limitation de débit** | File d'attente multi-apps | Gestion d'erreurs | Support RTL |

</div>

### 🚀 **Ce qui le rend spécial?**

- **🎯 Extraction Complète**: Obtient TOUS les avis disponibles, pas seulement les récents
- **⚡ Super Rapide**: Scraping optimisé avec limitation intelligente de débit  
- **🎨 Interface Belle**: GUI moderne avec thèmes clair/sombre
- **📊 Analyses Riches**: Statistiques détaillées et suivi du temps
- **🔄 Traitement par Lots**: Gère plusieurs applications simultanément
- **🌍 Multi-Langues**: Interface disponible en 6 langues
- **📱 Détection Intelligente**: Auto-détecte les infos de l'app et gère les erreurs élégamment
- **💾 Formats Multiples**: Exporte vers CSV, JSON avec champs personnalisables
- **🛡️ Robuste**: Gère les problèmes réseau, limites de débit et cas extrêmes

---

## 🛠️ Installation

### 📋 **Prérequis**

- **Python 3.7+** (3.9+ recommandé)
- **Connexion internet** pour le scraping
- **2GB RAM** minimum (4GB+ pour gros datasets)

### 📦 **Installation Rapide**

```bash
git clone https://github.com/your-username/google-play-reviews-scraper.git
cd google-play-reviews-scraper
pip install -r requirements.txt
python src/app_gui.py
```

---

## 🎯 Cas d'Usage

### 💼 **Parfait pour:**

- **📊 Chercheurs de Marché** - Analyser les applications concurrentes et tendances
- **🎯 Chefs de Produit** - Collecter les retours utilisateurs pour planification  
- **🔍 Chercheurs UX** - Comprendre les points de douleur et préférences
- **📈 Développeurs d'Apps** - Surveiller performance et satisfaction utilisateurs
- **🏢 Analystes Business** - Générer des insights pour décisions stratégiques
- **🎓 Étudiants et Académiques** - Collecter données pour projets de recherche

---

## 🌍 **Documentation Complète dans d'Autres Langues**

<div align="center">

**📖 Documentation complète avec guides détaillés, exemples et tutoriels:**

[![🇺🇸 Complete English Documentation](https://img.shields.io/badge/🇺🇸-Complete_Documentation-4285f4?style=for-the-badge)](../README.md)
[![🇧🇷 Documentação Completa em Português](https://img.shields.io/badge/🇧🇷-Documentação_Completa-00a86b?style=for-the-badge)](README_PT.md)
[![🇪🇸 Documentación Completa en Español](https://img.shields.io/badge/🇪🇸-Documentación_Completa-ea4335?style=for-the-badge)](README_ES.md)
[![🇩🇪 Vollständige Dokumentation auf Deutsch](https://img.shields.io/badge/🇩🇪-Vollständige_Dokumentation-333333?style=for-the-badge)](README_DE.md)
[![🇮🇹 Documentazione Completa in Italiano](https://img.shields.io/badge/🇮🇹-Documentazione_Completa-00a86b?style=for-the-badge)](README_IT.md)

**📋 [Voir Toutes les Langues et Guide de Traduction](LANGUAGES.md)**

</div>

---

## 📄 Licence

Ce projet est sous licence **MIT** - voir le fichier [LICENSE](../LICENSE) pour les détails.

---

<div align="center">

**🚀 Développé avec ❤️ pour la communauté**

**Si ce projet vous a aidé, considérez lui donner une ⭐!**

[![GitHub stars](https://img.shields.io/github/stars/your-username/google-play-reviews-scraper?style=social)](../../stargazers)
[![GitHub forks](https://img.shields.io/github/forks/your-username/google-play-reviews-scraper?style=social)](../../network/members)

</div>