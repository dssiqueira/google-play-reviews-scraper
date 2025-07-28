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

![Google Play Reviews Scraper](img/google-play.png)

**Outil professionnel pour extraire et analyser les avis d'applications du Google Play Store**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)](https://windows.microsoft.com)

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
| 🍎 **macOS** | ❌ Terminal uniquement | ✅ Supporté | ❌ Non disponible |
| 🐧 **Linux** | ❌ Terminal uniquement | ✅ Supporté | ❌ Non disponible |

> **Note** : L'interface graphique est disponible uniquement pour Windows. Les utilisateurs Mac et Linux doivent utiliser la version en ligne de commande.

### Option 1 : Exécutable (Windows Uniquement)
1. Téléchargez l'exécutable depuis la [page des releases](../../releases)
2. Exécutez `GooglePlayReviewScraper.exe`
3. Terminé ! Pas besoin d'installer Python

### Option 2 : Code Source (Toutes Plateformes)
```bash
# Clonez le dépôt
git clone https://github.com/votre-utilisateur/google-play-reviews-scraper.git
cd google-play-reviews-scraper

# Installez les dépendances
pip install -r requirements.txt

# Windows : Exécutez l'interface graphique
python app_gui.py

# Mac/Linux : Utilisez la ligne de commande
python review_scraper.py --url "https://play.google.com/store/apps/details?id=com.whatsapp"
```

**Utilisateurs Windows** : L'interface s'ouvrira en Portugais. Utilisez le sélecteur de drapeaux dans le coin supérieur droit pour changer de langue !
**Utilisateurs Mac/Linux** : Utilisez l'interface en ligne de commande avec les paramètres montrés ci-dessous.

---

## 💻 **Interface Graphique Moderne**

![Interface](https://via.placeholder.com/800x500/1976D2/FFFFFF?text=Interface+Multi-langues)

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

### 🍎🐧 **Pour les Utilisateurs Mac/Linux (Obligatoire)**

Comme l'interface graphique est exclusive à Windows, les utilisateurs Mac et Linux doivent utiliser la ligne de commande :

```bash
# Usage de base
python review_scraper.py --url "https://play.google.com/store/apps/details?id=com.whatsapp"

# Avec des paramètres personnalisés
python review_scraper.py \
  --app-id "com.whatsapp" \
  --country "fr" \
  --lang "fr" \
  --output "whatsapp_reviews"

# Obtenir de l'aide
python review_scraper.py --help
```

### 🪟 **Pour les Utilisateurs Windows (Optionnel)**

Les utilisateurs Windows peuvent aussi utiliser la ligne de commande pour l'automatisation :

```bash
# Exemple de base
python review_scraper.py --url "https://play.google.com/store/apps/details?id=com.whatsapp"

# Avec des paramètres personnalisés
python review_scraper.py \
  --app-id "com.whatsapp" \
  --country "us" \
  --lang "en" \
  --output "whatsapp_usa_reviews"

# Aide complète
python review_scraper.py --help
```

### **Paramètres Disponibles :**
```
--url, -u          URL complète de l'app
--app-id, -a       ID de l'app (ex: com.whatsapp)
--country, -c      Code du pays (défaut: fr)
--lang, -l         Code de la langue (défaut: fr)
--output, -o       Nom des fichiers de sortie
--help, -h         Affiche cette aide
```

---

## 📖 **Comment Utiliser**

### 1️⃣ **Trouvez l'Application**
Allez sur Google Play Store et trouvez l'application désirée. Exemple :
```
https://play.google.com/store/apps/details?id=com.whatsapp
```

### 2️⃣ **Collez l'URL**
- Ouvrez Google Play Reviews Scraper
- Collez l'URL complète dans le champ
- L'ID de l'application sera extrait automatiquement

### 3️⃣ **Configurez (Optionnel)**
- **Pays** : `fr` (France), `us` (États-Unis), `br` (Brésil)...
- **Langue** : `fr` (Français), `en` (Anglais), `pt` (Portugais)...
- **Dossier** : Choisissez où sauvegarder les fichiers

### 4️⃣ **Exécutez**
Cliquez sur "Démarrer Collection" et attendez. Le processus est automatique !

---

## 🌍 **Langues Supportées dans l'Interface**

L'application supporte **6 langues** avec traduction complète de l'interface :

| Drapeau | Code | Langue | Statut |
|---------|------|--------|--------|
| 🇺🇸 | `en` | **English** | ✅ Complet |
| 🇧🇷 | `pt` | **Português** | ✅ Complet |
| 🇪🇸 | `es` | **Español** | ✅ Complet |
| 🇫🇷 | `fr` | **Français** | ✅ Par défaut |
| 🇩🇪 | `de` | **Deutsch** | ✅ Complet |
| 🇮🇹 | `it` | **Italiano** | ✅ Complet |

**Comment utiliser** : Cliquez sur le drapeau dans le coin supérieur droit de l'interface pour changer de langue instantanément !

### 🎯 **Ce qui est traduit :**
- ✅ Tous les boutons et étiquettes
- ✅ Titres des sections
- ✅ Messages de statut et journal
- ✅ Modal "À propos" complet
- ✅ Placeholders et tooltips
- ✅ Messages d'erreur

---

## 🚀 **Nouveautés de la Version Actuelle**

### ✨ **Fonctionnalités Implémentées**
- 🌍 **Système multi-langues complet** (6 langues)
- 🎨 **Interface Material Design** moderne et responsive
- 🏳️ **Sélecteur de drapeaux** avec images PNG réelles (24x24px)
- 📜 **Défilement fluide** pour écrans de toute taille
- 🎯 **Icône personnalisée** Google Play dans la barre des tâches
- ℹ️ **Modal "À propos"** avec informations du projet
- 🔄 **Traduction instantanée** de toute l'interface
- 📊 **Barres de progression** visuelles et informatives

---

<div align="center">

**Développé avec ❤️ par [DSiqueira](https://dsiqueira.com)**

⭐ **Si ce projet vous a été utile, laissez une étoile !** ⭐

</div>