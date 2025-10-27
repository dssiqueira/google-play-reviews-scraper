@echo off
echo ========================================
echo Organizando Documentacao
echo ========================================
echo.

REM Cria pasta docs/build se nao existir
if not exist "docs\build" mkdir "docs\build"

REM Move arquivos de build para docs/build
echo Movendo arquivos de build...
move /Y "BUILD.md" "docs\build\" 2>nul
move /Y "COMO-CRIAR-EXECUTAVEL.md" "docs\build\" 2>nul
move /Y "COMO-CRIAR-INSTALADOR.md" "docs\build\" 2>nul
move /Y "GUIA-RAPIDO-INSTALADOR.md" "docs\build\" 2>nul
move /Y "DISTRIBUICAO.md" "docs\build\" 2>nul
move /Y "SOLUCAO-FINAL.md" "docs\build\" 2>nul
move /Y "TROUBLESHOOTING.md" "docs\build\" 2>nul

REM Move arquivos gerais para docs
echo Movendo arquivos gerais...
move /Y "ORGANIZACAO-PROJETO.md" "docs\" 2>nul
move /Y "RESUMO-FINAL.md" "docs\" 2>nul

echo.
echo ========================================
echo ✅ Organizacao Concluida!
echo ========================================
echo.
echo Estrutura:
echo   docs/
echo   ├── build/              (Guias de build)
echo   ├── ORGANIZACAO-PROJETO.md
echo   └── RESUMO-FINAL.md
echo.
echo Raiz mantida limpa com apenas:
echo   - README.md
echo   - LICENSE
echo   - requirements.txt
echo.
pause
