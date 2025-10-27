"""
Script para criar executável do Google Play Reviews Scraper
Usa PyInstaller para gerar um .exe standalone no Windows
"""

import os
import sys
import subprocess
import shutil

def check_dependencies():
    """Verifica se as dependências necessárias estão instaladas"""
    print("🔍 Verificando dependências...")
    
    # Lista de dependências críticas
    dependencies = [
        ('google_play_scraper', 'google-play-scraper>=1.2.0'),
        ('pandas', 'pandas>=1.5.0'),
        ('PyInstaller', 'pyinstaller>=5.0.0'),
        ('pefile', 'pefile>=2023.2.7'),
    ]
    
    missing = []
    
    for module_name, pip_name in dependencies:
        try:
            __import__(module_name)
            print(f"✅ {module_name} instalado")
        except ImportError:
            print(f"❌ {module_name} não encontrado")
            missing.append(pip_name)
    
    if missing:
        print(f"\n⚠️  Instalando {len(missing)} dependência(s) faltante(s)...")
        for dep in missing:
            print(f"   Instalando {dep}...")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", dep])
                print(f"   ✅ {dep} instalado com sucesso")
            except subprocess.CalledProcessError as e:
                print(f"   ❌ Erro ao instalar {dep}: {e}")
                print(f"\n⚠️  Por favor, instale manualmente:")
                print(f"   pip install {dep}")
                sys.exit(1)
    
    print("\n✅ Todas as dependências estão instaladas!")

def clean_build_folders():
    """Remove pastas de build anteriores"""
    print("\n🧹 Limpando builds anteriores...")
    
    folders_to_clean = ['build', 'dist', '__pycache__']
    for folder in folders_to_clean:
        if os.path.exists(folder):
            shutil.rmtree(folder)
            print(f"   Removido: {folder}")
    
    # Remove arquivos .spec antigos
    for file in os.listdir('.'):
        if file.endswith('.spec'):
            os.remove(file)
            print(f"   Removido: {file}")

def build_executable():
    """Constrói o executável usando PyInstaller com arquivo .spec customizado"""
    print("\n🔨 Construindo executável...")
    
    # Primeiro, cria o arquivo .spec customizado
    print("📝 Criando arquivo .spec customizado...")
    try:
        subprocess.check_call([sys.executable, 'create_spec.py'])
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao criar .spec: {e}")
        return False
    
    # Agora usa o arquivo .spec para build
    spec_file = 'GooglePlayReviewsScraper_custom.spec'
    
    if not os.path.exists(spec_file):
        print(f"❌ Arquivo {spec_file} não foi criado!")
        return False
    
    print(f"🔨 Usando {spec_file} para build...")
    
    cmd = [
        sys.executable,
        '-m', 'PyInstaller',
        spec_file,
        '--clean',
        '--noconfirm',
    ]
    
    try:
        subprocess.check_call(cmd)
        print("✅ Executável criado com sucesso!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao criar executável: {e}")
        print("\n💡 Dica: Verifique se google_play_scraper está instalado:")
        print("   pip install google-play-scraper")
        return False
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        return False

def create_release_folder():
    """Cria pasta de release com o executável e arquivos necessários"""
    print("\n📦 Criando pasta de release...")
    
    release_folder = 'release'
    if os.path.exists(release_folder):
        shutil.rmtree(release_folder)
    
    os.makedirs(release_folder)
    
    # Copia o executável
    exe_path = 'dist/GooglePlayReviewsScraper.exe'
    if os.path.exists(exe_path):
        shutil.copy(exe_path, release_folder)
        print(f"   ✅ Copiado: GooglePlayReviewsScraper.exe")
    
    # Cria README para o executável
    readme_content = """# Google Play Reviews Scraper - Executável

## 🚀 Como usar

1. **Execute o programa**: Clique duas vezes em `GooglePlayReviewsScraper.exe`

2. **Interface Gráfica**: 
   - Cole a URL do app do Google Play Store
   - Ou adicione o ID do app diretamente
   - Configure país e idioma (opcional)
   - Clique em "Iniciar Coleta"

3. **Resultados**: 
   - Os arquivos CSV e JSON serão salvos na mesma pasta do executável
   - Você pode abrir os resultados diretamente pela interface

## 📋 Requisitos

- Windows 10 ou superior
- Conexão com internet

## ⚠️ Observações

- O executável pode demorar alguns segundos para iniciar na primeira vez
- Alguns antivírus podem alertar sobre o arquivo (falso positivo)
- Se necessário, adicione exceção no antivírus

## 🆘 Suporte

Para mais informações, visite:
https://github.com/dssiqueira/google-play-reviews-scraper

## 📄 Licença

MIT License - Veja LICENSE para mais detalhes
"""
    
    with open(os.path.join(release_folder, 'LEIA-ME.txt'), 'w', encoding='utf-8') as f:
        f.write(readme_content)
    print(f"   ✅ Criado: LEIA-ME.txt")
    
    # Copia LICENSE se existir
    if os.path.exists('LICENSE'):
        shutil.copy('LICENSE', release_folder)
        print(f"   ✅ Copiado: LICENSE")
    
    print(f"\n✅ Pasta de release criada: {os.path.abspath(release_folder)}")

def main():
    """Função principal"""
    print("=" * 60)
    print("🚀 Google Play Reviews Scraper - Build Executável")
    print("=" * 60)
    
    # Verifica se está no diretório correto
    if not os.path.exists('src/app_gui.py'):
        print("❌ Erro: Execute este script na raiz do projeto!")
        sys.exit(1)
    
    # Verifica dependências
    check_dependencies()
    
    # Limpa builds anteriores
    clean_build_folders()
    
    # Constrói o executável
    if build_executable():
        # Cria pasta de release
        create_release_folder()
        
        print("\n" + "=" * 60)
        print("✅ BUILD CONCLUÍDO COM SUCESSO!")
        print("=" * 60)
        print(f"\n📁 Executável disponível em: release/GooglePlayReviewsScraper.exe")
        print("\n💡 Dica: Distribua a pasta 'release' completa para os usuários")
    else:
        print("\n❌ Build falhou. Verifique os erros acima.")
        sys.exit(1)

if __name__ == "__main__":
    main()
