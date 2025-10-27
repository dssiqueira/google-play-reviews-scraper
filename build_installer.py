"""
Script Python para criar o instalador usando Inno Setup
"""

import os
import sys
import subprocess

def find_inno_setup():
    """Encontra o executável do Inno Setup"""
    possible_paths = [
        r"C:\Program Files (x86)\Inno Setup 6\iscc.exe",
        r"C:\Program Files\Inno Setup 6\iscc.exe",
        r"C:\Program Files (x86)\Inno Setup 5\iscc.exe",
        r"C:\Program Files\Inno Setup 5\iscc.exe",
    ]
    
    for path in possible_paths:
        if os.path.exists(path):
            return path
    
    return None

def main():
    print("=" * 60)
    print("🚀 Criando Instalador - Google Play Reviews Scraper")
    print("=" * 60)
    print()
    
    # Verifica se o executável existe
    if not os.path.exists("release/GooglePlayReviewsScraper.exe"):
        print("❌ Executável não encontrado!")
        print()
        print("Execute primeiro: python build_exe.py")
        print()
        sys.exit(1)
    
    print("✅ Executável encontrado")
    print()
    
    # Encontra o Inno Setup
    print("🔍 Procurando Inno Setup...")
    iscc_path = find_inno_setup()
    
    if not iscc_path:
        print("❌ Inno Setup não encontrado!")
        print()
        print("Por favor, instale o Inno Setup:")
        print("https://jrsoftware.org/isdl.php")
        print()
        sys.exit(1)
    
    print(f"✅ Inno Setup encontrado: {iscc_path}")
    print()
    
    # Cria pasta de saída
    if not os.path.exists("installer"):
        os.makedirs("installer")
    
    # Compila o instalador
    print("🔨 Compilando instalador...")
    print()
    
    try:
        result = subprocess.run(
            [iscc_path, "installer.iss"],
            capture_output=True,
            text=True,
            check=True
        )
        
        print(result.stdout)
        
        print()
        print("=" * 60)
        print("✅ INSTALADOR CRIADO COM SUCESSO!")
        print("=" * 60)
        print()
        print("📁 Localização: installer/GooglePlayReviewsScraper-Setup-v1.0.0.exe")
        print()
        print("💡 Distribua este instalador para os usuários!")
        print("   Eles não precisarão instalar Python ou dependências.")
        print()
        
    except subprocess.CalledProcessError as e:
        print("❌ Erro ao compilar instalador:")
        print(e.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
