@echo off
echo ========================================
echo Instalando Dependencias
echo ========================================
echo.

echo Instalando google-play-scraper...
pip install google-play-scraper>=1.2.0

echo.
echo Instalando pandas...
pip install pandas>=1.5.0

echo.
echo Instalando pyinstaller...
pip install pyinstaller>=5.0.0

echo.
echo Instalando pefile...
pip install pefile>=2023.2.7

echo.
echo ========================================
echo Instalacao concluida!
echo ========================================
echo.
echo Agora execute: python build_exe.py
echo.
pause
