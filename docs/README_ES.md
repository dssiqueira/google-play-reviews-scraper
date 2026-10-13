<div align="center">

<img src="../assets/icons/google-play.png" width="72" alt="">

# Google Play Reviews Scraper

**Recopila reseñas de Google Play Store en CSV, JSON o Excel — desde una app de escritorio o la terminal.**

[🇺🇸 English](../README.md) · [🇧🇷 Português](README_PT.md) · [🇪🇸 Español](README_ES.md) · [🇫🇷 Français](README_FR.md) · [🇩🇪 Deutsch](README_DE.md) · [🇮🇹 Italiano](README_IT.md)

<img src="../assets/screenshots/app-light.png" width="720" alt="La app recopilando reseñas de cuatro apps">

</div>

## Funciones

- **Cola con varias apps** — pega URLs de Play Store o IDs de paquete, incluso muchas a la vez (una por línea).
- **Solo lo que necesitas** — todo, las últimas *N* por app, o solo las reseñas desde una fecha.
- **CSV, JSON y Excel** — el CSV se abre en Excel con los acentos correctos; el JSON incluye los metadatos de la app.
- **Detén cuando quieras** — detener es inmediato y conserva lo ya recopilado.
- **Resistente** — los fallos de red se reintentan en lugar de cortar la recopilación sin avisar.
- **Resumen de valoraciones** — media y distribución de 1 a 5★ al terminar.
- **Modo claro y oscuro**, interfaz en 6 idiomas, recuerda tu configuración.
- **La misma app en Windows, macOS y Linux**, además de CLI y API en Python.

<div align="center">
<img src="../assets/screenshots/app-dark-summary.png" width="600" alt="">
</div>

## Primeros pasos

### Windows — sin Python

Descarga el instalador o el `.exe` desde [Releases](https://github.com/dssiqueira/google-play-reviews-scraper/releases) y ejecútalo.

### Desde el código fuente

```bash
git clone https://github.com/dssiqueira/google-play-reviews-scraper.git
cd google-play-reviews-scraper
pip install -r requirements.txt

python src/app_gui.py         # app de escritorio
python src/review_scraper.py  # modo interactivo en la terminal
```

> **Linux:** Tk suele ser un paquete aparte — `sudo apt install python3-tk` (Debian/Ubuntu).

## Línea de comandos

```bash
# una app, por ID o URL
python src/review_scraper.py com.whatsapp

# varias apps, tienda de EE. UU. en inglés, máx. 1.000 cada una, desde el 1 de enero, en CSV + Excel
python src/review_scraper.py com.whatsapp com.instagram.android \
    --country us --lang en --max 1000 --since 2026-01-01 --format csv,xlsx
```

Todas las opciones, la API de Python y el formato de los datos están en el [README en inglés](../README.md).

## Bueno saber

- **¿Cuántas reseñas puedo obtener?** Las que Google Play entregue para ese país/idioma — normalmente menos que el total de la ficha, que suma todos los idiomas.
- **¿Está permitido?** Lee páginas públicas, como un navegador. Las reseñas incluyen nombres de usuario: trata los datos con responsabilidad (RGPD) y respeta los términos de Google Play.

¿Gráficos y análisis de sentimiento? Sube el JSON a **[Review Stats Pro](https://review-stats-pro.lovable.app/)**.

## Licencia

[MIT](../LICENSE) © Douglas Siqueira
