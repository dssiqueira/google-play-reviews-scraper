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

## 🎯 **Que fait-il ?**

Extrait **TOUS** les avis disponibles de n'importe quelle application du Google Play Store de manière rapide, organisée et fiable. Idéal pour :

- 📊 **Analyse de marché** et recherche concurrentielle
- 🔍 **Recherche UX** et analyse des commentaires utilisateurs  
- 📈 **Surveillance** de la réputation des applications
- 🎯 **Insights** pour le développement de produits
- 📋 **Rapports** et présentations

---

## 🚀 **Installation Rapide**

### 🖥️ **Compatibilité des Plateformes**

| Plateforme | Interface Graphique | Ligne de Commande | Exécutable |
|------------|---------------------|-------------------|------------|
| 🪟 **Windows** | ✅ Support complet | ✅ Supporté | ✅ Disponible |
| 🍎 **macOS** | ✅ **NOUVEAU!** Interface Native | ✅ Supporté | ❌ Non disponible |
| 🐧 **Linux** | ❌ Terminal uniquement | ✅ Supporté | ❌ Non disponible |

> **✨ NOUVEAU**: macOS a maintenant une interface visuelle native avec 6 langues et un design natif!

### Option 1 : Exécutable (Windows Uniquement)
1. Téléchargez l'exécutable depuis la [page des releases](../../releases)
2. Exécutez `GooglePlayReviewScraper.exe`
3. Terminé ! Pas besoin d'installer Python

### Option 2 : Interface Visuelle (Windows & macOS)
```bash
# 1. Cloner le dépôt
git clone https://github.com/your-username/google-play-reviews-scraper.git
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