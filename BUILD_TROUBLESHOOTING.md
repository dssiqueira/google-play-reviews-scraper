# 🔧 Guia de Solução de Problemas - Build

## ❌ Problema: `ModuleNotFoundError: No module named 'pefile'`

### 🎯 **Solução Rápida:**

1. **Instale as dependências manualmente:**
   ```bash
   pip install --user pyinstaller pefile
   ```

2. **Se ainda não funcionar, tente:**
   ```bash
   python -m pip install --upgrade pip
   pip install --user --upgrade pyinstaller pefile setuptools
   ```

3. **Use o script batch (mais confiável no Windows):**
   ```bash
   build.bat
   ```

---

## 🐍 **Problema com Python Store (Microsoft Store)**

Se você instalou o Python pela Microsoft Store, pode haver conflitos. 

### **Soluções:**

1. **Desinstale o Python da Microsoft Store**
2. **Instale o Python oficial:** https://python.org/downloads
3. **Ou use um ambiente virtual:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   python build_simple.py
   ```

---

## 🔄 **Método Manual (Sempre Funciona)**

Se os scripts automáticos não funcionarem:

```bash
# 1. Instale as dependências
pip install pyinstaller pefile

# 2. Execute o PyInstaller diretamente
pyinstaller --onefile --windowed --name="GooglePlayReviewScraper" --add-data="img;img" --icon="img/google-play.ico" app_gui.py

# 3. O executável estará em: dist/GooglePlayReviewScraper.exe
```

---

## 📁 **Estrutura Necessária**

Certifique-se de que você tem:
```
projeto/
├── app_gui.py              ✅ Arquivo principal
├── review_scraper.py       ✅ Módulo de scraping
├── translations.py         ✅ Traduções
├── requirements.txt        ✅ Dependências
└── img/
    └── google-play.ico     ✅ Ícone (obrigatório)
```

---

## 🚀 **Scripts Disponíveis**

1. **`build_simple.py`** - Script Python completo
2. **`build_alternative.py`** - Versão simplificada
3. **`build.bat`** - Script batch para Windows
4. **Comando manual** - Sempre funciona

---

## 💡 **Dicas Extras**

- **Execute como administrador** se houver problemas de permissão
- **Feche antivírus** temporariamente (pode bloquear o PyInstaller)
- **Use pasta sem espaços** no nome
- **Verifique se tem espaço em disco** (executável pode ter 50-100MB)

---

## 🆘 **Se nada funcionar**

1. Crie um **ambiente virtual limpo**
2. Use **Python 3.9-3.11** (mais estável com PyInstaller)
3. Instale **apenas as dependências necessárias**
4. Execute o **comando manual** acima

---

**💬 Precisa de mais ajuda?** Abra uma issue no GitHub!