@echo off
echo 🚀 Criando executável do Google Play Reviews Scraper...
echo.

REM Verifica se o Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python não encontrado! Instale o Python primeiro.
    pause
    exit /b 1
)

REM Verifica se os arquivos necessários existem
if not exist "app_gui.py" (
    echo ❌ app_gui.py não encontrado!
    pause
    exit /b 1
)

if not exist "img\google-play.ico" (
    echo ❌ img\google-play.ico não encontrado!
    pause
    exit /b 1
)

echo 📦 Instalando dependências necessárias...
python -m pip install --user pyinstaller pefile

echo.
echo 🧹 Limpando builds anteriores...
if exist "build" rmdir /s /q "build"
if exist "dist" rmdir /s /q "dist"
if exist "GooglePlayReviewScraper.spec" del "GooglePlayReviewScraper.spec"

echo.
echo 🔨 Criando executável...
python -m PyInstaller --onefile --windowed --name=GooglePlayReviewScraper --add-data=img;img --icon=img/google-play.ico app_gui.py

echo.
if exist "dist\GooglePlayReviewScraper.exe" (
    echo ✅ Executável criado com sucesso!
    echo 📁 Localização: dist\GooglePlayReviewScraper.exe
    
    REM Mostra o tamanho do arquivo
    for %%A in ("dist\GooglePlayReviewScraper.exe") do (
        set /a size=%%~zA/1024/1024
        echo 📏 Tamanho: !size! MB
    )
    
    echo.
    echo 🧹 Limpando arquivos temporários...
    if exist "build" rmdir /s /q "build"
    if exist "GooglePlayReviewScraper.spec" del "GooglePlayReviewScraper.spec"
    
    echo.
    echo 🎉 CONCLUÍDO!
    echo 💡 Para distribuir, copie o arquivo: dist\GooglePlayReviewScraper.exe
    echo 💡 O usuário não precisa ter Python instalado!
) else (
    echo ❌ Erro ao criar executável!
    echo 💡 Verifique se todas as dependências estão instaladas
)

echo.
pause