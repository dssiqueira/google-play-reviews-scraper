@echo off
echo ========================================
echo Criando Instalador
echo ========================================
echo.

REM Verifica se Inno Setup esta instalado
where iscc >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo ❌ Inno Setup nao encontrado!
    echo.
    echo Por favor, instale o Inno Setup:
    echo https://jrsoftware.org/isdl.php
    echo.
    echo Apos instalar, adicione ao PATH:
    echo C:\Program Files (x86)\Inno Setup 6
    echo.
    pause
    exit /b 1
)

echo ✅ Inno Setup encontrado
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

REM Compila o instalador
iscc installer.iss

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
