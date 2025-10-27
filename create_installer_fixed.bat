@echo off
echo ========================================
echo Criando Instalador
echo ========================================
echo.

REM Verifica se o executavel existe
if not exist "release\GooglePlayReviewsScraper.exe" (
    echo ❌ Executavel nao encontrado!
    echo.
    echo Execute primeiro: python build_exe.py
    echo.
    pause
    exit /b 1
)

echo ✅ Executavel encontrado
echo.

REM Cria pasta de saida
if not exist "installer" mkdir installer

echo 🔨 Compilando instalador...
echo.

REM Tenta varios caminhos possiveis do Inno Setup
set ISCC_PATH=""

if exist "C:\Program Files (x86)\Inno Setup 6\iscc.exe" (
    set ISCC_PATH="C:\Program Files (x86)\Inno Setup 6\iscc.exe"
)

if exist "C:\Program Files\Inno Setup 6\iscc.exe" (
    set ISCC_PATH="C:\Program Files\Inno Setup 6\iscc.exe"
)

if exist "C:\Program Files (x86)\Inno Setup 5\iscc.exe" (
    set ISCC_PATH="C:\Program Files (x86)\Inno Setup 5\iscc.exe"
)

if %ISCC_PATH%=="" (
    echo ❌ Inno Setup nao encontrado!
    echo.
    echo Por favor, instale o Inno Setup:
    echo https://jrsoftware.org/isdl.php
    echo.
    echo Ou adicione ao PATH:
    echo C:\Program Files (x86)\Inno Setup 6
    echo.
    pause
    exit /b 1
)

echo ✅ Inno Setup encontrado em: %ISCC_PATH%
echo.

REM Compila o instalador
%ISCC_PATH% installer.iss

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ========================================
    echo ✅ INSTALADOR CRIADO COM SUCESSO!
    echo ========================================
    echo.
    echo 📁 Localização: installer\GooglePlayReviewsScraper-Setup-v1.0.0.exe
    echo.
    echo 💡 Distribua este instalador para os usuarios!
    echo    Eles nao precisarao instalar Python ou dependencias.
    echo.
) else (
    echo.
    echo ❌ Erro ao criar instalador
    echo.
)

pause
