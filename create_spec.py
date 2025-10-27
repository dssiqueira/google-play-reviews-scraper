"""
Cria arquivo .spec customizado para PyInstaller
Garante que google_play_scraper seja incluído corretamente
"""

import os
import sys

# Encontra o caminho do google_play_scraper
try:
    import google_play_scraper
    gps_path = os.path.dirname(google_play_scraper.__file__)
    print(f"✅ google_play_scraper encontrado em: {gps_path}")
except ImportError:
    print("❌ ERRO: google_play_scraper não está instalado!")
    print("Execute: pip install google-play-scraper")
    sys.exit(1)

# Verifica e prepara assets
assets_list = []
assets_path = os.path.abspath('assets')
if os.path.exists(assets_path):
    for root, dirs, files in os.walk(assets_path):
        for file in files:
            file_path = os.path.join(root, file)
            rel_path = os.path.relpath(root, '.')
            assets_list.append(f"(r'{file_path}', r'{rel_path}')")
    print(f"✅ {len(assets_list)} assets encontrados")
else:
    print(f"⚠️  Pasta assets não encontrada")

# Converte lista de assets para string
assets_str = ",\n    ".join(assets_list)

# Conteúdo do arquivo .spec
spec_content = f"""# -*- mode: python ; coding: utf-8 -*-

import os
import sys
from PyInstaller.utils.hooks import collect_all, collect_submodules

# Coleta TODOS os módulos e dados do google_play_scraper
datas = []
binaries = []
hiddenimports = []

# Força coleta de google_play_scraper
tmp_ret = collect_all('google_play_scraper')
datas += tmp_ret[0]
binaries += tmp_ret[1]
hiddenimports += tmp_ret[2]

# Força coleta de pandas
tmp_ret = collect_all('pandas')
datas += tmp_ret[0]
binaries += tmp_ret[1]
hiddenimports += tmp_ret[2]

# Adiciona assets manualmente
datas += [
    {assets_str}
]

# Adiciona imports adicionais
hiddenimports += [
    'google_play_scraper',
    'google_play_scraper.scraper',
    'google_play_scraper.features',
    'google_play_scraper.features.app',
    'google_play_scraper.features.reviews',
    'google_play_scraper.constants',
    'google_play_scraper.constants.element',
    'google_play_scraper.constants.regex',
    'google_play_scraper.constants.request',
    'google_play_scraper.util',
    'google_play_scraper.util.request',
    'pandas',
    'pandas._libs',
    'pandas._libs.tslibs',
    'tkinter',
    'tkinter.ttk',
]

a = Analysis(
    ['src/app_gui.py'],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={{}},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='GooglePlayReviewsScraper',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # Sem console (GUI)
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='assets/icons/google-play.ico',
)
"""

# Salva o arquivo .spec
spec_file = 'GooglePlayReviewsScraper_custom.spec'
with open(spec_file, 'w', encoding='utf-8') as f:
    f.write(spec_content)

print(f"✅ Arquivo .spec criado: {spec_file}")
print("\nAgora execute:")
print(f"  python -m PyInstaller {spec_file}")
