# ✅ Checklist para Commit

## 📦 Arquivos Essenciais (Commitar)

### 📄 Raiz
- ✅ `README.md` - Documentação principal
- ✅ `LICENSE` - Licença MIT
- ✅ `requirements.txt` - Dependências
- ✅ `.gitignore` - Arquivos ignorados
- ✅ `INSTALLER-INFO.txt` - Info do instalador

### 🐍 Código Fonte
- ✅ `src/` - Todo o código Python
  - `app_gui.py`
  - `app_gui_mac.py`
  - `review_scraper.py`
  - `translations.py`
  - `time_stats.py`

### 🎨 Assets
- ✅ `assets/` - Ícones e bandeiras
  - `icons/`
  - `flags/`
  - `screenshots/`

### 📚 Documentação
- ✅ `docs/` - Toda documentação
  - `README.md` (índice)
  - `build/` (guias de build)
  - `README_*.md` (multilíngue)
  - `ORGANIZACAO-PROJETO.md`
  - `RESUMO-FINAL.md`

### 🔨 Scripts de Build
- ✅ `build_exe.py` - Cria executável
- ✅ `create_spec.py` - Gera .spec
- ✅ `build_installer.py` - Cria instalador
- ✅ `installer.iss` - Config Inno Setup

### 🧹 Scripts Auxiliares
- ✅ `clean.bat` - Limpa temporários
- ✅ `organize_docs.bat` - Organiza docs
- ✅ `create_installer.bat` - Cria instalador (legado)
- ✅ `create_installer_fixed.bat` - Cria instalador (fix)
- ✅ `INSTALAR-INNO-SETUP.bat` - Guia Inno Setup

### 📝 Exemplos (Opcional)
- ✅ `examples/` - Exemplos de uso

---

## 🗑️ Arquivos Temporários (NÃO Commitar)

Estes já estão no `.gitignore`:

- ❌ `build/` - Build temporário
- ❌ `dist/` - Executável gerado
- ❌ `release/` - Pasta de release
- ❌ `installer/` - Instalador gerado
- ❌ `*.spec` - Arquivos spec
- ❌ `__pycache__/` - Cache Python
- ❌ `*.csv` - Reviews coletados
- ❌ `*.json` - Reviews coletados

---

## 📊 Resumo

| Categoria | Arquivos | Status |
|-----------|----------|--------|
| Código fonte | ~10 arquivos | ✅ Commitar |
| Assets | ~15 arquivos | ✅ Commitar |
| Documentação | ~15 arquivos | ✅ Commitar |
| Scripts | ~10 arquivos | ✅ Commitar |
| Temporários | Vários | ❌ Ignorados |

---

## 🚀 Comandos Git

```bash
# Ver status
git status

# Adicionar tudo (temporários já ignorados)
git add .

# Commit
git commit -m "feat: adiciona build de executável e instalador

- Adiciona script build_exe.py para criar executável standalone
- Adiciona build_installer.py para criar instalador profissional
- Inclui todos os assets (ícones e bandeiras) no executável
- Organiza documentação em docs/
- Adiciona guias completos de build e distribuição
- Executável funciona sem Python instalado
- Instalador profissional com Inno Setup"

# Push
git push
```

---

## ✨ Estrutura Final (Commitada)

```
google-play-reviews-scraper/
├── 📄 README.md
├── 📄 LICENSE
├── 📄 requirements.txt
├── 📄 .gitignore
│
├── 📁 src/                    ✅ Código fonte
├── 📁 assets/                 ✅ Ícones e bandeiras
├── 📁 docs/                   ✅ Documentação completa
├── 📁 examples/               ✅ Exemplos
│
├── 🔨 build_exe.py            ✅ Build executável
├── 🔨 create_spec.py          ✅ Gera .spec
├── 🔨 build_installer.py      ✅ Build instalador
├── 🔨 installer.iss           ✅ Config Inno Setup
│
└── 🧹 Scripts auxiliares      ✅ Utilitários
```

**Total: ~50 arquivos essenciais**

---

## 💡 Dica

Antes de commitar, execute:

```bash
# Limpa tudo
.\clean.bat

# Verifica o que será commitado
git status

# Se estiver tudo certo, commit!
git add .
git commit -m "sua mensagem"
```

**Pronto para commit!** 🎉
