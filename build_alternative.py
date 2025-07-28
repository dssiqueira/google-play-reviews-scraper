#!/usr/bin/env python3
"""
Script alternativo para criar executável - Método mais simples
"""
import os
import sys
import subprocess

def main():
    print("🚀 Build Alternativo - Google Play Reviews Scraper")
    print("=" * 50)
    
    # Verifica se os arquivos existem
    if not os.path.exists("app_gui.py"):
        print("❌ app_gui.py não encontrado!")
        return
    
    print("📋 Instruções para criar o executável:")
    print()
    print("1️⃣ Primeiro, instale as dependências:")
    print("   pip install --user pyinstaller pefile")
    print()
    print("2️⃣ Depois execute este comando:")
    print('   pyinstaller --onefile --windowed --name="GooglePlayReviewScraper" --add-data="img;img" --icon="img/google-play.ico" app_gui.py')
    print()
    print("3️⃣ O executável será criado em: dist/GooglePlayReviewScraper.exe")
    print()
    
    # Pergunta se quer tentar automaticamente
    try:
        choice = input("🤔 Quer que eu tente executar automaticamente? (s/n): ").lower()
        if choice in ['s', 'sim', 'y', 'yes']:
            print("\n📦 Instalando dependências...")
            subprocess.run([sys.executable, "-m", "pip", "install", "--user", "pyinstaller", "pefile"])
            
            print("\n🔨 Criando executável...")
            cmd = [
                "pyinstaller", 
                "--onefile", 
                "--windowed", 
                "--name=GooglePlayReviewScraper",
                "--add-data=img;img",
                "--icon=img/google-play.ico",
                "app_gui.py"
            ]
            
            subprocess.run(cmd)
            
            if os.path.exists("dist/GooglePlayReviewScraper.exe"):
                print("✅ Executável criado com sucesso!")
            else:
                print("❌ Algo deu errado. Tente o método manual acima.")
    
    except KeyboardInterrupt:
        print("\n👋 Cancelado pelo usuário")

if __name__ == "__main__":
    main()
    input("\nPressione Enter para sair...")