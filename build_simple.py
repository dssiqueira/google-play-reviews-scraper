#!/usr/bin/env python3
"""
Script simples para criar executável do Google Play Reviews Scraper
"""
import os
import sys
import subprocess
import shutil

def install_dependencies():
    """Instala dependências necessárias"""
    print("📦 Verificando dependências...")
    
    # Lista de dependências necessárias
    dependencies = [
        "pyinstaller>=6.0.0",
        "pefile>=2023.2.7"
    ]
    
    for dep in dependencies:
        try:
            # Tenta importar o módulo
            module_name = dep.split(">=")[0].replace("-", "_")
            if module_name == "pyinstaller":
                import PyInstaller
            elif module_name == "pefile":
                import pefile
            print(f"✅ {dep.split('>=')[0]} já instalado")
        except ImportError:
            print(f"📦 Instalando {dep}...")
            try:
                subprocess.run([
                    sys.executable, "-m", "pip", "install", 
                    "--user", "--upgrade", dep
                ], check=True, capture_output=True, text=True)
                print(f"✅ {dep.split('>=')[0]} instalado com sucesso")
            except subprocess.CalledProcessError as e:
                print(f"❌ Erro ao instalar {dep}: {e}")
                print("💡 Tente executar manualmente:")
                print(f"   pip install --user {dep}")
                return False
    return True

def main():
    print("🚀 Criando executável do Google Play Reviews Scraper...")
    
    # Verifica arquivos necessários
    if not os.path.exists("app_gui.py"):
        print("❌ app_gui.py não encontrado!")
        return False
    
    if not os.path.exists("img/google-play.ico"):
        print("❌ img/google-play.ico não encontrado!")
        print("💡 Certifique-se de que a pasta 'img' existe com o arquivo 'google-play.ico'")
        return False
    
    # Instala dependências
    if not install_dependencies():
        return False
    
    # Limpa builds anteriores
    print("🧹 Limpando builds anteriores...")
    for folder in ["build", "dist", "__pycache__"]:
        if os.path.exists(folder):
            shutil.rmtree(folder)
    
    for file in ["GooglePlayReviewScraper.spec"]:
        if os.path.exists(file):
            os.remove(file)
    
    # Cria executável
    print("🔨 Criando executável...")
    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--onefile",
        "--windowed",
        "--name=GooglePlayReviewScraper",
        "--add-data=img;img",
        "--icon=img/google-play.ico",
        "--clean",
        "--noconfirm",
        "app_gui.py"
    ]
    
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        
        # Verifica se foi criado
        exe_path = "dist/GooglePlayReviewScraper.exe"
        if os.path.exists(exe_path):
            size = os.path.getsize(exe_path) / (1024 * 1024)
            print(f"✅ Executável criado: {exe_path}")
            print(f"📏 Tamanho: {size:.1f} MB")
            
            # Limpa arquivos temporários
            print("🧹 Limpando arquivos temporários...")
            if os.path.exists("build"):
                shutil.rmtree("build")
            for spec_file in ["GooglePlayReviewScraper.spec"]:
                if os.path.exists(spec_file):
                    os.remove(spec_file)
            
            print("\\n🎉 CONCLUÍDO!")
            print("📁 Para distribuir, copie o arquivo: dist/GooglePlayReviewScraper.exe")
            print("💡 O usuário não precisa ter Python instalado!")
            return True
        else:
            print("❌ Executável não foi criado")
            return False
            
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao criar executável:")
        print(f"Código de saída: {e.returncode}")
        if e.stdout:
            print("Saída:", e.stdout)
        if e.stderr:
            print("Erro:", e.stderr)
        
        print("\\n💡 Possíveis soluções:")
        print("1. Reinstale o Python em uma pasta sem espaços")
        print("2. Execute como administrador")
        print("3. Use um ambiente virtual (venv)")
        print("4. Instale manualmente: pip install --user pyinstaller pefile")
        
        return False

if __name__ == "__main__":
    success = main()
    input("\\nPressione Enter para sair...")
    sys.exit(0 if success else 1)