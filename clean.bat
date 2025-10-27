@echo off
echo ========================================
echo Limpando Arquivos Temporarios
echo ========================================
echo.

echo Removendo builds...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist release rmdir /s /q release
if exist installer rmdir /s /q installer

echo Removendo arquivos spec...
if exist GooglePlayReviewsScraper_custom.spec del /q GooglePlayReviewsScraper_custom.spec

echo Removendo reviews coletados...
del /q *_reviews.csv 2>nul
del /q *_reviews.json 2>nul
del /q time_stats.json 2>nul

echo Removendo cache Python...
if exist __pycache__ rmdir /s /q __pycache__
if exist src\__pycache__ rmdir /s /q src\__pycache__

echo.
echo ========================================
echo ✅ Limpeza Concluida!
echo ========================================
echo.
echo Arquivos essenciais mantidos:
echo - Codigo fonte (src/)
echo - Assets (assets/)
echo - Documentacao (*.md)
echo - Scripts de build (build_exe.py, etc)
echo.
pause
