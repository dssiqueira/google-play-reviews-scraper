@echo off
echo 🚀 Configurando ambiente para build...
echo.

REM Cria ambiente virtual
echo 📦 Criando ambiente virtual...
python -m venv build_env

REM Ativa o ambiente virtual
echo 🔄 Ativando ambiente virtual...
call build_env\Scripts\activate.bat

REM Atualiza pip
echo ⬆️ Atualizando pip...
python -m pip install --upgrade pip

REM Instala dependências
echo 📋 Instalando dependências...
pip install pyinstaller pefile google-play-scraper pandas

REM Cria o executável
echo 🔨 Criando executável...
pyinstaller --onefile --windowed --name=GooglePlayReviewScraper --add-data=img;img --icon=img/google-play.ico app_gui.py

REM Verifica se foi criado
if exist "dist\GooglePlayReviewScraper.exe" (
    echo ✅ Executável criado com sucesso!
    echo 📁 Localização: dist\GooglePlayReviewScraper.exe
    
    echo.
    echo 🧹 Limpando arquivos temporários...
    if exist "build" rmdir /s /q "build"
    if exist "GooglePlayReviewScraper.spec" del "GooglePlayReviewScraper.spec"
    
    echo.
    echo 🎉 CONCLUÍDO!
    echo 💡 Para distribuir, copie o arquivo: dist\GooglePlayReviewScraper.exe
) else (
    echo ❌ Erro ao criar executável!
)

REM Desativa ambiente virtual
deactivate

echo.
echo 💡 Você pode deletar a pasta 'build_env' após o build
pause