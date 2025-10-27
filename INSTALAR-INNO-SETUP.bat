@echo off
echo ========================================
echo Guia de Instalacao do Inno Setup
echo ========================================
echo.
echo Para criar o instalador, voce precisa do Inno Setup.
echo.
echo 1. Abra o navegador
echo 2. Va para: https://jrsoftware.org/isdl.php
echo 3. Baixe "Inno Setup 6.x.x"
echo 4. Execute o instalador
echo 5. Clique em Next -> Next -> Install
echo 6. Aguarde a instalacao (2 minutos)
echo 7. Clique em Finish
echo.
echo Depois de instalar, execute:
echo   create_installer.bat
echo.
echo ========================================
echo.
echo Deseja abrir o site agora? (S/N)
set /p resposta=
if /i "%resposta%"=="S" start https://jrsoftware.org/isdl.php
echo.
pause
