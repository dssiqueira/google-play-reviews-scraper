# 📁 Organização do Projeto

## ✅ Arquivos Essenciais (Manter)

### 📄 Documentação Principal
```
README.md                    - Documentação principal do projeto
LICENSE                      - Licença MIT
requirements.txt             - Dependências Python
.gitignore                   - Arquivos ignorados pelo Git
```

### 🐍 Código Fonte
```
src/
├── app_gui.py              - Interface gráfica Windows
├── app_gui_mac.py          - Interface gráfica macOS
├── review_scraper.py       - Motor de scraping
├── translations.py         - Traduções (6 idiomas)
└── time_stats.py           - Estatísticas de tempo
```

### 🎨 Assets
```
assets/
├── icons/
│   ├── google-play.ico     - Ícone do executável
│   └── google-play.png     - Ícone da interface
└── flags/
    ├── br.png              - Bandeiras para seletor
    ├── en.png              - de idiomas
    ├── es.png
    ├── fr.png
    ├── de.png
    └── it.png
```

### 🔨 Scripts de Build
```
build_exe.py                - Cria o executável
create_spec.py              - Gera arquivo .spec customizado
installer.iss               - Configuração do instalador
create_installer.bat        - Script para criar instalador
```

### 📚 Documentação de Build
```
BUILD.md                    - Como criar o executável
COMO-CRIAR-INSTALADOR.md    - Como criar o instalador
GUIA-RAPIDO-INSTALADOR.md   - Guia rápido do instalador
```

### 📖 Documentação Adicional (Opcional)
```
docs/
├── README_PT.md            - README em Português
├── README_ES.md            - README em Espanhol
├── README_FR.md            - README em Francês
├── README_DE.md            - README em Alemão
└── README_IT.md            - README em Italiano
```

### 📝 Exemplos (Opcional)
```
examples/
├── example_usage.py        - Exemplo de uso
└── batch_scraping.py       - Exemplo de batch
```

---

## 🗑️ Arquivos Temporários (Deletar/Ignorar)

### Arquivos de Build
```
build/                      - Pasta temporária do PyInstaller
dist/                       - Pasta temporária do PyInstaller
*.spec                      - Arquivos spec gerados
GooglePlayReviewsScraper_custom.spec
```

### Arquivos de Output (Reviews coletados)
```
*.csv                       - Reviews em CSV
*.json                      - Reviews em JSON
time_stats.json             - Estatísticas
*_reviews.csv
*_reviews.json
```

**Exemplos para deletar:**
```
bet365_apostas_esportivas_reviews.csv
bet365_apostas_esportivas_reviews.json
betano_-_apostasonlinecassino_reviews.csv
betano_-_apostasonlinecassino_reviews.json
estrela_bet_-_apostas_online_reviews.csv
estrela_bet_-_apostas_online_reviews.json
h2bet_-_casa_de_apostas_online_reviews.csv
h2bet_-_casa_de_apostas_online_reviews.json
novibet_-_apostas_cassino_reviews.csv
novibet_-_apostas_cassino_reviews.json
superbet_apostas_esportivas_reviews.csv
superbet_apostas_esportivas_reviews.json
```

### Pasta Release (Distribuição)
```
release/                    - Executável final
└── GooglePlayReviewsScraper.exe
```

**Nota:** Mantenha no Git apenas se quiser distribuir o executável pronto.
Caso contrário, cada desenvolvedor cria o seu próprio.

### Documentação Extra (Consolidar)
```
DISTRIBUICAO.md             - Pode ser mesclado com BUILD.md
SOLUCAO-FINAL.md            - Pode ser mesclado com BUILD.md
TROUBLESHOOTING.md          - Manter separado
COMO-CRIAR-EXECUTAVEL.md    - Pode ser mesclado com BUILD.md
```

### Scripts Auxiliares
```
install.py                  - Instalador de dependências (redundante)
install_dependencies.bat    - Instalador de dependências (redundante)
test_exe.bat                - Script de teste (opcional)
INSTALLER-INFO.txt          - Usado pelo instalador (manter)
```

---

## 🎯 Estrutura Recomendada (Limpa)

```
google-play-reviews-scraper/
├── 📄 README.md
├── 📄 LICENSE
├── 📄 requirements.txt
├── 📄 .gitignore
│
├── 📁 src/
│   ├── app_gui.py
│   ├── app_gui_mac.py
│   ├── review_scraper.py
│   ├── translations.py
│   └── time_stats.py
│
├── 📁 assets/
│   ├── icons/
│   │   ├── google-play.ico
│   │   └── google-play.png
│   └── flags/
│       ├── br.png
│       ├── en.png
│       ├── es.png
│       ├── fr.png
│       ├── de.png
│       └── it.png
│
├── 📁 docs/
│   ├── BUILD.md                    ← Consolidado
│   ├── INSTALLER.md                ← Consolidado
│   ├── TROUBLESHOOTING.md
│   ├── README_PT.md
│   ├── README_ES.md
│   ├── README_FR.md
│   ├── README_DE.md
│   └── README_IT.md
│
├── 📁 scripts/                     ← Nova pasta
│   ├── build_exe.py
│   ├── create_spec.py
│   ├── create_installer.bat
│   └── installer.iss
│
└── 📁 examples/                    ← Opcional
    ├── example_usage.py
    └── batch_scraping.py
```

---

## 🧹 Script de Limpeza

Crie um arquivo `clean.bat`:

```batch
@echo off
echo Limpando arquivos temporarios...

REM Remove builds
rmdir /s /q build 2>nul
rmdir /s /q dist 2>nul
rmdir /s /q release 2>nul
rmdir /s /q installer 2>nul

REM Remove arquivos spec
del /q *.spec 2>nul

REM Remove reviews coletados
del /q *_reviews.csv 2>nul
del /q *_reviews.json 2>nul
del /q time_stats.json 2>nul

REM Remove cache Python
rmdir /s /q __pycache__ 2>nul
rmdir /s /q src\__pycache__ 2>nul

echo Limpeza concluida!
pause
```

---

## 📝 Atualizar .gitignore

Adicione ao `.gitignore`:

```gitignore
# Build outputs
build/
dist/
release/
installer/

# Spec files
*.spec
GooglePlayReviewsScraper_custom.spec

# Review outputs
*_reviews.csv
*_reviews.json
time_stats.json

# Except examples
!examples/*.csv
!examples/*.json
```

---

## ✅ Checklist de Limpeza

- [ ] Deletar arquivos `*_reviews.csv` e `*_reviews.json`
- [ ] Deletar `time_stats.json`
- [ ] Deletar pasta `build/`
- [ ] Deletar pasta `dist/`
- [ ] Deletar `GooglePlayReviewsScraper_custom.spec`
- [ ] Consolidar documentação em `docs/`
- [ ] Mover scripts para `scripts/`
- [ ] Atualizar `.gitignore`
- [ ] Commit das mudanças

---

## 🎯 Resultado Final

**Antes:** ~50 arquivos (incluindo temporários)
**Depois:** ~25 arquivos essenciais

**Benefícios:**
- ✅ Repositório mais limpo
- ✅ Mais fácil de navegar
- ✅ Menos confusão
- ✅ Git mais rápido
- ✅ Mais profissional
