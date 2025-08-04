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

![Aperçu Interface](../assets/screenshots/google-play-reviews-scraper.png)

### ⚡ Application en Action
*Voyez le scraper fonctionner avec progression en temps réel*

![Démo de l'Application](../assets/screenshots/google-play-reviews-scraper.gif)

### 📊 Interface en Ligne de Commande
*Également disponible via terminal pour l'automatisation*

![Démo du Terminal](../assets/screenshots/google-play-reviews-scraper-terminal.gif)

</div>

---

## ⚡ Démarrage Rapide

### 🖥️ **Compatibilité des Plateformes**

| Plateforme | Interface Graphique | Ligne de Commande | Notes |
|:----------:|:-------------------:|:-----------------:|:------|
| 🪟 **Windows** | ✅ Support Complet | ✅ Supporté | GUI moderne avec toutes les fonctionnalités |
| 🍎 **macOS** | ✅ Interface Native | ✅ Supporté | Optimisée pour le design macOS |
| 🐧 **Linux** | ⚠️ GUI Basique | ✅ Supporté | GUI disponible mais CLI recommandé |

### 🎯 **Option 1: Application GUI (Recommandée)**

#### **🚀 Installation en Une Commande**
```bash
git clone https://github.com/dssiqueira/google-play-reviews-scraper.git
cd google-play-reviews-scraper
python install.py
```

#### **🔧 Installation Manuelle**
```bash
# Windows: python src/app_gui.py
# macOS: python src/app_gui_mac.py  
# Linux: python src/app_gui.py
```

### 🔧 **Option 2: Ligne de Commande**

```bash
# Extraire les avis d'une seule app
python src/review_scraper.py --url "https://play.google.com/store/apps/details?id=com.whatsapp"

# Traitement par lots de plusieurs apps
python src/review_scraper.py --batch liste_apps.txt --output resultats/
```

### 📦 **Option 3: Module Python**

```python
from src.review_scraper import GooglePlayReviewScraper

scraper = GooglePlayReviewScraper()
reviews = scraper.scrape_reviews("com.whatsapp")
print(f"Extrait {len(reviews)} avis!")
```

---

## 📈 **Review Stats Pro - Analyse Professionnelle**

Après avoir extrait les avis, analysez vos données avec notre plateforme professionnelle:

**🔗 [Review Stats Pro](https://review-stats-pro.lovable.app/)**

### ✨ **Fonctionnalités:**
- 📊 **Analyse de Sentiment** - Comprendre les émotions des utilisateurs
- 📈 **Détection de Tendances** - Identifier les modèles temporels
- 🔍 **Extraction de Mots-clés** - Trouver les sujets les plus mentionnés
- 📊 **Graphiques Interactifs** - Visualisations professionnelles

### 💡 **Flux de travail:**
1. Extraire les avis avec cet outil
2. Télécharger le JSON vers Review Stats Pro
3. Obtenir des analyses professionnelles instantanées

---

## 📖 Fonctionnalités

<div align="center">

| 🎯 **Fonctionnalités Principales** | 🎨 **Interface** | 📊 **Sortie** | 🌍 **Multi-Langue** |
|:---:|:---:|:---:|:---:|
| Extrait **TOUS** les avis | GUI moderne avec thèmes | Export CSV et JSON | 6 langues supportées |
| **Traitement par lots** | Progrès en temps réel | Analyses détaillées | Auto-détection de langue |
| **Filtrage intelligent** | Glisser-déposer URLs | Statistiques de temps | Traductions personnalisées |
| **Limitation de débit** | File d'attente multi-apps | Gestion d'erreurs | Support RTL |

</div>

### 🚀 **Qu'est-ce qui le rend spécial ?**

- **🎯 Extraction Complète**: Obtient TOUS les avis disponibles, pas seulement les récents
- **⚡ Super Rapide**: Scraping optimisé avec limitation intelligente de débit  
- **🎨 Belle Interface**: GUI moderne avec thèmes clair/sombre
- **📊 Analyses Riches**: Statistiques détaillées et suivi du temps
- **🔄 Traitement par Lots**: Gère plusieurs apps simultanément
- **🌍 Multi-Langue**: Interface disponible en 6 langues
- **📱 Détection Intelligente**: Auto-détecte les infos de l'app et gère les erreurs élégamment
- **💾 Formats Multiples**: Exporte en CSV, JSON avec champs personnalisables
- **🛡️ Robuste**: Gère les problèmes réseau, limites de débit et cas extrêmes

---

## 🛠️ Installation

### 📋 **Prérequis**

- **Python 3.7+** (3.9+ recommandé)
- **Connexion internet** pour le scraping
- **2GB RAM** minimum (4GB+ pour de gros datasets)

### 📦 **Installation Rapide**

```bash
git clone https://github.com/dssiqueira/google-play-reviews-scraper.git
cd google-play-reviews-scraper
pip install -r requirements.txt
python src/app_gui.py
```

---

## 🎯 Cas d'Usage

### 💼 **Parfait pour:**

- **📊 Chercheurs de Marché** - Analyser les apps concurrentes et tendances du marché
- **🎯 Product Managers** - Recueillir les retours utilisateurs pour la planification de fonctionnalités  
- **🔍 Chercheurs UX** - Comprendre les points de douleur et préférences des utilisateurs
- **📈 Développeurs d'Apps** - Surveiller les performances et satisfaction des utilisateurs
- **🏢 Analystes Business** - Générer des insights pour les décisions stratégiques
- **🎓 Étudiants et Académiques** - Collecter des données pour projets de recherche

---

## 📄 Licence

Ce projet est sous licence **MIT** - voir le fichier [LICENSE](../LICENSE) pour les détails.

---

<div align="center">

**🚀 Développé avec ❤️ pour la communauté**

**Si ce projet vous a aidé, pensez à lui donner une ⭐!**

[![GitHub stars](https://img.shields.io/github/stars/dssiqueira/google-play-reviews-scraper?style=social)](../../stargazers)
[![GitHub forks](https://img.shields.io/github/forks/dssiqueira/google-play-reviews-scraper?style=social)](../../network/members)

</div>

### Option 1 : Exécutable (Windows Uniquement)
1. Téléchargez l'exécutable depuis la [page des releases](../../releases)
2. Exécutez `GooglePlayReviewScraper.exe`
3. Terminé ! Pas besoin d'installer Python

### Option 2 : Interface Visuelle (Windows & macOS)
```bash
# 1. Cloner le dépôt
git clone https://github.com/dssiqueira/google-play-reviews-scraper.git
cd google-play-reviews-scraper

# 2. Installer les dépendances
pip install -r requirements.txt

# Windows : Exécutez l'interface graphique
python app_gui.py

# macOS : Exécutez l'interface native
cd src && python3 app_gui_mac.py
```

### Option 3 : Ligne de Commande (Toutes Plateformes)
```bash
# Après avoir cloné et installé les dépendances
python review_scraper.py --url "https://play.google.com/store/apps/details?id=com.whatsapp"
```

**🪟 Utilisateurs Windows** : L'interface s'ouvrira en Portugais. Utilisez le sélecteur de drapeaux dans le coin supérieur droit pour changer de langue !
**🍎 Utilisateurs macOS** : Interface native avec 6 langues, polices SF Pro et intégration Finder !
**🐧 Utilisateurs Linux** : Utilisez l'interface en ligne de commande avec les paramètres montrés ci-dessous.

---

## 💻 **Interface Graphique Moderne**

![Google Play Reviews Scraper Screenshot](../assets/screenshots/google-play-reviews-scraper.png)

### 🎬 **Application en Action**
![Google Play Reviews Scraper Demo](../assets/screenshots/google-play-reviews-scraper.gif)

### ✨ Fonctionnalités de l'Interface :
- 🎨 **Design Material Design** moderne et intuitif
- 🌍 **Multi-langues** avec sélecteur de drapeaux (6 langues)
- 📋 **Collez l'URL** directement depuis le navigateur
- ⚙️ **Configuration simple** (pays, langue, dossier)
- 📊 **Progression en temps réel** avec barre visuelle
- 📁 **Ouverture automatique** des fichiers générés
- 📜 **Défilement fluide** pour les petits écrans
- ℹ️ **Modal "À propos"** avec informations du développeur
- 🎯 **Icône personnalisée** dans la barre des tâches

### 🌍 **Système Multi-langues**
- **🇺🇸 English**
- **🇧🇷 Português**
- **🇪🇸 Español**
- **🇫🇷 Français** (Par défaut)
- **🇩🇪 Deutsch**
- **🇮🇹 Italiano**

**Sélecteur avec vrais drapeaux** : Cliquez sur le drapeau dans le coin supérieur droit pour changer de langue instantanément !

---

## 🛠️ **Interface en Ligne de Commande**

### 🎬 **Démonstration du Terminal**
![Google Play Reviews Scraper Terminal Demo](../assets/screenshots/google-play-reviews-scraper-terminal.gif)

### 🍎🐧 **Pour les Utilisateurs Mac/Linux (Obligatoire)**

Comme l'interface graphique est exclusive à Windows, les utilisateurs Mac et Linux doivent utiliser la ligne de commande :

```bash
git clone https://github.com/dssiqueira/google-play-reviews-scraper.git
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

