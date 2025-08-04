<div align="center">

# 📱 Google Play Reviews Scraper

![Google Play Reviews Scraper](../assets/icons/google-play.png)

**🚀 Herramienta profesional para extraer y analizar reseñas de apps del Google Play Store**

*Extrae miles de reseñas en minutos con una interfaz moderna y hermosa*

---

## 🌍 **Elige tu Idioma / Choose Your Language**

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

**[🎬 Ver Demo](#-demo) • [⚡ Inicio Rápido](#-inicio-rápido) • [📖 Características](#-características) • [🛠️ Instalación](#️-instalación)**

---

</div>

## 🎬 Demo

<div align="center">

### 🖥️ Interfaz Moderna
*Interfaz hermosa e intuitiva con soporte multi-idioma*

![Vista Previa de Interfaz](../assets/screenshots/google-play-reviews-scraper.png)

### ⚡ Aplicación en Acción
*Ve el scraper funcionando con progreso en tiempo real*

![Demo de la Aplicación](../assets/screenshots/google-play-reviews-scraper.gif)

### 📊 Interfaz de Línea de Comandos
*También disponible vía terminal para automatización*

![Demo del Terminal](../assets/screenshots/google-play-reviews-scraper-terminal.gif)

</div>

---

## ⚡ Inicio Rápido

### 🖥️ **Compatibilidad de Plataformas**

| Plataforma | Interfaz Gráfica | Línea de Comandos | Notas |
|:----------:|:----------------:|:-----------------:|:------|
| 🪟 **Windows** | ✅ Soporte Completo | ✅ Soportado | GUI moderna con todas las características |
| 🍎 **macOS** | ✅ Interfaz Nativa | ✅ Soportado | Optimizada para diseño macOS |
| 🐧 **Linux** | ⚠️ GUI Básica | ✅ Soportado | GUI disponible pero CLI recomendado |

### 🎯 **Opción 1: Aplicación GUI (Recomendada)**

#### **🚀 Instalación con Un Comando**
```bash
git clone https://github.com/dssiqueira/google-play-reviews-scraper.git
cd google-play-reviews-scraper
python install.py
```

#### **🔧 Instalación Manual**
```bash
# Windows: python src/app_gui.py
# macOS: python src/app_gui_mac.py  
# Linux: python src/app_gui.py
```

### 🔧 **Opción 2: Línea de Comandos**

```bash
# Extraer reseñas de una sola app
python src/review_scraper.py --url "https://play.google.com/store/apps/details?id=com.whatsapp"

# Procesamiento por lotes de múltiples apps
python src/review_scraper.py --batch lista_apps.txt --output resultados/
```

### 📦 **Opción 3: Módulo Python**

```python
from src.review_scraper import GooglePlayReviewScraper

scraper = GooglePlayReviewScraper()
reviews = scraper.scrape_reviews("com.whatsapp")
print(f"¡Extraídas {len(reviews)} reseñas!")
```

---

## 📈 **Review Stats Pro - Análisis Profesional**

Después de extraer reseñas, analiza tus datos con nuestra plataforma profesional:

**🔗 [Review Stats Pro](https://review-stats-pro.lovable.app/)**

### ✨ **Características:**
- 📊 **Análisis de Sentimiento** - Comprende emociones de usuarios
- 📈 **Detección de Tendencias** - Identifica patrones temporales
- 🔍 **Extracción de Palabras Clave** - Encuentra temas más mencionados
- 📊 **Gráficos Interactivos** - Visualizaciones profesionales

### 💡 **Flujo de trabajo:**
1. Extraer reseñas con esta herramienta
2. Subir JSON a Review Stats Pro
3. Obtener análisis profesionales instantáneos

---

## 📖 Características

<div align="center">

| 🎯 **Características Principales** | 🎨 **Interfaz** | 📊 **Salida** | 🌍 **Multi-Idioma** |
|:---:|:---:|:---:|:---:|
| Extrae **TODAS** las reseñas | GUI moderna con temas | Exportación CSV y JSON | 6 idiomas soportados |
| **Procesamiento por lotes** | Progreso en tiempo real | Análisis detallados | Auto-detección de idioma |
| **Filtrado inteligente** | Arrastrar y soltar URLs | Estadísticas de tiempo | Traducciones personalizadas |
| **Limitación de velocidad** | Cola de múltiples apps | Manejo de errores | Soporte RTL |

</div>

### 🚀 **¿Qué lo hace especial?**

- **🎯 Extracción Completa**: Obtiene TODAS las reseñas disponibles, no solo las recientes
- **⚡ Súper Rápido**: Scraping optimizado con limitación inteligente de velocidad  
- **🎨 Interfaz Hermosa**: GUI moderna con temas claro/oscuro
- **📊 Análisis Ricos**: Estadísticas detalladas y seguimiento de tiempo
- **🔄 Procesamiento por Lotes**: Maneja múltiples apps simultáneamente
- **🌍 Multi-Idioma**: Interfaz disponible en 6 idiomas
- **📱 Detección Inteligente**: Auto-detecta información de la app y maneja errores elegantemente
- **💾 Múltiples Formatos**: Exporta a CSV, JSON con campos personalizables
- **🛡️ Robusto**: Maneja problemas de red, límites de velocidad y casos extremos

---

## 🛠️ Instalación

### 📋 **Requisitos**

- **Python 3.7+** (3.9+ recomendado)
- **Conexión a internet** para scraping
- **2GB RAM** mínimo (4GB+ para grandes datasets)

### 🔧 **Dependencias**

```bash
# Dependencias principales (instaladas automáticamente)
google-play-scraper  # API de Google Play Store
pandas              # Procesamiento de datos
tkinter            # Framework GUI (usualmente pre-instalado)
```

### 📦 **Métodos de Instalación**

#### **Método 1: Git Clone (Recomendado)**
```bash
git clone https://github.com/dssiqueira/google-play-reviews-scraper.git
cd google-play-reviews-scraper
pip install -r requirements.txt
```

#### **Método 2: Descarga Directa**
```bash
# Descargar ZIP desde GitHub
# Extraer a la carpeta deseada
cd google-play-reviews-scraper-main
pip install -r requirements.txt
```

#### **Método 3: Entorno Virtual (Avanzado)**
```bash
python -m venv scraper_env
source scraper_env/bin/activate  # Linux/Mac
# o
scraper_env\Scripts\activate     # Windows

pip install -r requirements.txt
```

### ✅ **Verificar Instalación**

```bash
# Probar el scraper
python src/review_scraper.py --help

# Ejecutar GUI
python src/app_gui.py
```

---

## 📊 Ejemplos de Uso

### 🎯 **Uso de GUI**

1. **Ejecutar la aplicación**
   ```bash
   python src/app_gui.py
   ```

2. **Agregar apps a la cola**
   - Pegar URL de Google Play Store
   - Hacer clic en "Agregar" para encolar
   - Repetir para múltiples apps

3. **Configurar opciones**
   - Elegir país/idioma
   - Establecer directorio de salida
   - Seleccionar formato de exportación

4. **Iniciar extracción**
   - Hacer clic en "Iniciar Scraping"
   - Monitorear progreso en tiempo real
   - Acceder a resultados vía botones

### 🔧 **Uso de Línea de Comandos**

```bash
# Uso básico
python src/review_scraper.py --url "https://play.google.com/store/apps/details?id=com.whatsapp"

# Opciones avanzadas
python src/review_scraper.py \
  --url "https://play.google.com/store/apps/details?id=com.whatsapp" \
  --country "es" \
  --language "es" \
  --output "whatsapp_reviews" \
  --format "both"

# Procesamiento por lotes
python src/review_scraper.py --batch lista_apps.txt --output resultados/
```

### 🐍 **Integración Python**

```python
from src.review_scraper import GooglePlayReviewScraper

# Inicializar scraper
scraper = GooglePlayReviewScraper(country='es', lang='es')

# Extraer reseñas
reviews = scraper.scrape_reviews('com.whatsapp')

# Procesar resultados
print(f"Total de reseñas: {len(reviews)}")
for review in reviews[:5]:  # Mostrar primeras 5
    print(f"⭐ {review['score']}/5 - {review['content'][:100]}...")
```

---

## 📈 Ejemplos de Salida

### 📄 **Salida CSV**
```csv
userName,score,content,thumbsUpCount,reviewCreatedVersion,at,appVersion
Juan Pérez,5,"¡App increíble! Me encantan las nuevas características",42,1.2.3,2024-01-15,1.2.3
María García,4,"Buena pero necesita mejorar la interfaz",15,1.2.2,2024-01-14,1.2.3
...
```

### 📋 **Salida JSON**
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
      "userName": "Juan Pérez",
      "score": 5,
      "content": "¡App increíble! Me encantan las nuevas características",
      "thumbsUpCount": 42,
      "at": "2024-01-15T08:20:00Z"
    }
  ]
}
```

### 📊 **Estadísticas Generadas**
- **Total de reseñas extraídas**
- **Calificación promedio**
- **Distribución de calificaciones (1-5 estrellas)**
- **Tiempo de extracción y velocidad**
- **Reseñas más útiles**
- **Proporción de reseñas recientes vs antiguas**

---

## 📁 Estructura del Proyecto

```
📦 google-play-reviews-scraper/
├── 📂 src/                          # 🐍 Código fuente
│   ├── app_gui.py                   # 🖥️ Aplicación GUI moderna
│   ├── review_scraper.py            # ⚙️ Motor de scraping principal
│   ├── translations.py              # 🌍 Soporte multi-idioma
│   └── time_stats.py                # 📊 Análisis de rendimiento
├── 📂 assets/                       # 🎨 Recursos visuales
│   ├── icons/                       # 🎯 Iconos de la aplicación
│   │   ├── google-play.png          # 📱 Icono principal de la app
│   │   └── google-play.ico          # 🖼️ Icono de Windows
│   ├── flags/                       # 🏳️ Banderas de idiomas (24x24px)
│   │   ├── br.png                   # 🇧🇷 Brasil
│   │   ├── en.png                   # 🇺🇸 Inglés
│   │   └── ...                      # 🌍 Otros idiomas
│   └── screenshots/                 # 📸 Imágenes de demostración
├── 📂 docs/                         # 📖 Documentación
│   ├── README.md                    # 🇺🇸 Docs en inglés
│   ├── README_ES.md                 # 🇪🇸 Docs en español
│   └── TRANSLATIONS.md              # 🌍 Guía de traducción
├── 📂 examples/                     # 📋 Ejemplos de salida
│   ├── sample_reviews.csv           # 📊 Ejemplo CSV
│   ├── sample_reviews.json          # 📄 Ejemplo JSON
│   └── README.md                    # 📝 Guía de ejemplos
├── 📄 requirements.txt              # 📦 Dependencias Python
├── 📄 LICENSE                       # ⚖️ Licencia MIT
└── 📄 README.md                     # 📖 Este archivo
```

---

## 🎯 Casos de Uso

<div align="center">

| 🏢 **Negocios** | 🔬 **Investigación** | 📱 **Desarrollo** | 📊 **Analytics** |
|:---:|:---:|:---:|:---:|
| Análisis de competencia | Estudios de comportamiento | Feedback de características | Tendencias de mercado |
| Investigación de mercado | Investigación académica | Reportes de bugs | Análisis de sentimiento |
| Monitoreo de marca | Investigación UX | Optimización de app store | Métricas de rendimiento |
| Insights de clientes | Datos de encuestas | Pruebas de usuario | Gestión de reputación |

</div>

### 💼 **Perfecto para:**

- **📊 Investigadores de Mercado** - Analizar apps competidoras y tendencias de mercado
- **🎯 Gerentes de Producto** - Recopilar feedback de usuarios para planificación de características  
- **🔍 Investigadores UX** - Entender puntos de dolor y preferencias de usuarios
- **📈 Desarrolladores de Apps** - Monitorear rendimiento y satisfacción de usuarios
- **🏢 Analistas de Negocios** - Generar insights para decisiones estratégicas
- **🎓 Estudiantes y Académicos** - Recopilar datos para proyectos de investigación

---

## 🌍 Soporte Multi-Idioma

<div align="center">

**🇺🇸 English** • **🇧🇷 Português** • **🇪🇸 Español** • **🇫🇷 Français** • **🇩🇪 Deutsch** • **🇮🇹 Italiano**

*La interfaz se adapta automáticamente al idioma de tu sistema*

</div>

---

## 🤝 Contribuyendo

¡Damos la bienvenida a las contribuciones! Aquí te mostramos cómo puedes ayudar:

### 🐛 **Reportar Problemas**
- ¿Encontraste un bug? [Abre un issue](../../issues)
- Incluye pasos para reproducir
- Proporciona información del sistema

### 💡 **Sugerir Características**
- ¿Tienes una idea? [Inicia una discusión](../../discussions)
- Explica el caso de uso
- Proporciona mockups si es posible

### 🔧 **Contribuciones de Código**
```bash
# 1. Hacer fork del repositorio
# 2. Crear una rama de característica
git checkout -b feature/caracteristica-increible

# 3. Hacer tus cambios
# 4. Probar completamente
python -m pytest tests/

# 5. Enviar un pull request
```

### 🌍 **Traducciones**
¡Ayúdanos a soportar más idiomas! Ve la [guía de traducciones](TRANSLATIONS.md).

---

## 📞 Soporte

### 🆘 **¿Necesitas Ayuda?**

- **📖 Documentación**: Revisa nuestras [guías detalladas](../docs/)
- **💬 Discusiones**: Únete a nuestras [discusiones de la comunidad](../../discussions)
- **🐛 Issues**: Reporta bugs en la [sección de issues](../../issues)
- **📧 Email**: Contáctanos en support@example.com

### ❓ **FAQ**

<details>
<summary><strong>🔍 ¿Cuántas reseñas puedo extraer?</strong></summary>

La herramienta extrae TODAS las reseñas disponibles del Google Play Store. Esto puede variar desde cientos hasta millones dependiendo de la popularidad de la app.

</details>

<details>
<summary><strong>⚡ ¿Qué tan rápida es la extracción?</strong></summary>

La velocidad varía según el tamaño de la app y las condiciones de red. Tasas típicas:
- Apps pequeñas (< 1K reseñas): 30-60 segundos
- Apps medianas (1K-10K reseñas): 2-5 minutos  
- Apps grandes (10K+ reseñas): 5-30 minutos

</details>

<details>
<summary><strong>🌍 ¿Qué países/idiomas están soportados?</strong></summary>

Todos los países e idiomas soportados por Google Play Store. La herramienta maneja automáticamente la localización y diferencias regionales.

</details>

<details>
<summary><strong>🛡️ ¿Es esto legal?</strong></summary>

¡Sí! La herramienta solo accede a datos públicamente disponibles del Google Play Store, similar a ver reseñas en un navegador web.

</details>

---

## 📄 Licencia

Este proyecto está licenciado bajo la **Licencia MIT** - ve el archivo [LICENSE](../LICENSE) para detalles.

### 🔓 **Lo que esto significa:**
- ✅ **Uso comercial** permitido
- ✅ **Modificación** permitida  
- ✅ **Distribución** permitida
- ✅ **Uso privado** permitido
- ❌ **Sin garantía** proporcionada
- ❌ **Sin responsabilidad** asumida

---

## 🏆 Reconocimientos

### 🙏 **Agradecimientos Especiales**

- **[google-play-scraper](https://github.com/JoMingyu/google-play-scraper)** - Funcionalidad principal de scraping
- **[pandas](https://pandas.pydata.org/)** - Procesamiento y análisis de datos
- **[tkinter](https://docs.python.org/3/library/tkinter.html)** - Framework GUI
- **Contribuidores de la comunidad** - Reportes de bugs, solicitudes de características y traducciones

### 🌟 **Inspiración**

Este proyecto fue creado para democratizar el acceso a datos de app stores para investigadores, desarrolladores y empresas que necesitan insights pero carecen de recursos para herramientas de analytics costosas.

---

<div align="center">

## ⭐ **Historial de Estrellas**

[![Star History Chart](https://api.star-history.com/svg?repos=dssiqueira/google-play-reviews-scraper&type=Date)](https://star-history.com/#dssiqueira/google-play-reviews-scraper&Date)

---

**🚀 Desarrollado con ❤️ para la comunidad**

**¡Si este proyecto te ayudó, considera darle una ⭐!**

*Tu apoyo nos motiva a seguir mejorando y agregando nuevas características*

[![GitHub stars](https://img.shields.io/github/stars/dssiqueira/google-play-reviews-scraper?style=social)](../../stargazers)
[![GitHub forks](https://img.shields.io/github/forks/dssiqueira/google-play-reviews-scraper?style=social)](../../network/members)
[![GitHub watchers](https://img.shields.io/github/watchers/dssiqueira/google-play-reviews-scraper?style=social)](../../watchers)

</div>
