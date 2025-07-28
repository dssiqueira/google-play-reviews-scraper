# 📱 Google Play Reviews Scraper

<div align="center">

**🌍 Language / Idioma / Langue / Sprache / Lingua**

[![🇺🇸 English](https://img.shields.io/badge/🇺🇸-English-blue?style=for-the-badge)](README.md)
[![🇧🇷 Português](https://img.shields.io/badge/🇧🇷-Português-green?style=for-the-badge)](README_PT.md)
[![🇪🇸 Español](https://img.shields.io/badge/🇪🇸-Español-red?style=for-the-badge)](README_ES.md)
[![🇫🇷 Français](https://img.shields.io/badge/🇫🇷-Français-blue?style=for-the-badge)](README_FR.md)
[![🇩🇪 Deutsch](https://img.shields.io/badge/🇩🇪-Deutsch-black?style=for-the-badge)](README_DE.md)
[![🇮🇹 Italiano](https://img.shields.io/badge/🇮🇹-Italiano-green?style=for-the-badge)](README_IT.md)

---

![Google Play Reviews Scraper](img/google-play.png)

**Ferramenta profissional para extrair e analisar reviews de apps do Google Play Store**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)](https://windows.microsoft.com)

</div>

---

## 🎯 **O que faz?**

Extrai **TODOS** os reviews disponíveis de qualquer app do Google Play Store de forma rápida, organizada e confiável. Ideal para:

- 📊 **Análise de mercado** e concorrência
- 🔍 **Pesquisa de UX** e feedback de usuários  
- 📈 **Monitoramento** de reputação de apps
- 🎯 **Insights** para desenvolvimento de produtos
- 📋 **Relatórios** e apresentações

---

## 🚀 **Instalação Rápida**

### 🖥️ **Compatibilidade de Plataformas**

| Plataforma | Interface Gráfica | Linha de Comando | Executável |
|------------|-------------------|------------------|------------|
| 🪟 **Windows** | ✅ Suporte completo | ✅ Suportado | ✅ Disponível |
| 🍎 **macOS** | ❌ Apenas terminal | ✅ Suportado | ❌ Não disponível |
| 🐧 **Linux** | ❌ Apenas terminal | ✅ Suportado | ❌ Não disponível |

> **Nota**: A interface gráfica está disponível apenas para Windows. Usuários Mac e Linux devem usar a versão de linha de comando.

### Opção 1: Executável (Apenas Windows)
1. Baixe o executável da [página de releases](../../releases)
2. Execute `GooglePlayReviewScraper.exe`
3. Pronto! Não precisa instalar Python

### Opção 2: Código Fonte (Todas as Plataformas)
```bash
# Clone o repositório
git clone https://github.com/seu-usuario/google-play-reviews-scraper.git
cd google-play-reviews-scraper

# Instale as dependências
pip install -r requirements.txt

# Windows: Execute a interface gráfica
python app_gui.py

# Mac/Linux: Use a linha de comando
python review_scraper.py --url "https://play.google.com/store/apps/details?id=com.whatsapp"
```

**Usuários Windows**: A interface abrirá em Português. Use o seletor de bandeiras no canto superior direito para trocar idioma!
**Usuários Mac/Linux**: Use a interface de linha de comando com os parâmetros mostrados abaixo.

---

## 💻 **Interface Gráfica Moderna**

![Interface](https://via.placeholder.com/800x500/1976D2/FFFFFF?text=Interface+Multi-idioma)

### ✨ Funcionalidades da Interface:
- 🎨 **Design Material Design** moderno e intuitivo
- 🌍 **Multi-idiomas** com seletor de bandeiras (6 idiomas)
- 📋 **Cole a URL** diretamente do navegador
- ⚙️ **Configurações simples** (país, idioma, pasta)
- 📊 **Progresso em tempo real** com barra visual
- 📁 **Abertura automática** dos arquivos gerados
- 📜 **Scroll suave** para telas pequenas
- ℹ️ **Modal "Sobre"** com informações do desenvolvedor
- 🎯 **Ícone personalizado** na barra de tarefas

### 🌍 **Sistema Multi-idiomas**
- **🇧🇷 Português** (Padrão)
- **🇺🇸 English**
- **🇪🇸 Español** 
- **🇫🇷 Français**
- **🇩🇪 Deutsch**
- **🇮🇹 Italiano**

**Seletor com bandeiras reais**: Clique na bandeira no canto superior direito para trocar idioma instantaneamente!

---

## 📖 **Como Usar**

### 1️⃣ **Encontre o App**
Vá até o Google Play Store e encontre o app desejado. Exemplo:
```
https://play.google.com/store/apps/details?id=com.whatsapp
```

### 2️⃣ **Cole a URL**
- Abra o Google Play Reviews Scraper
- Cole a URL completa no campo
- O App ID será extraído automaticamente

### 3️⃣ **Configure (Opcional)**
- **País**: `br` (Brasil), `us` (EUA), `uk` (Reino Unido)...
- **Idioma**: `pt` (Português), `en` (Inglês), `es` (Espanhol)...
- **Pasta**: Escolha onde salvar os arquivos

### 4️⃣ **Execute**
Clique em "Iniciar Coleta" e aguarde. O processo é automático!

---

## 🛠️ **Interface de Linha de Comando**

### 🍎🐧 **Para Usuários Mac/Linux (Obrigatório)**

Como a interface gráfica é exclusiva do Windows, usuários Mac e Linux devem usar a linha de comando:

```bash
# Uso básico
python review_scraper.py --url "https://play.google.com/store/apps/details?id=com.whatsapp"

# Com configurações personalizadas
python review_scraper.py \
  --app-id "com.whatsapp" \
  --country "br" \
  --lang "pt" \
  --output "whatsapp_reviews"

# Obter ajuda
python review_scraper.py --help
```

### 🪟 **Para Usuários Windows (Opcional)**

Usuários Windows também podem usar a linha de comando para automação:

```bash
# Exemplo básico
python review_scraper.py --url "https://play.google.com/store/apps/details?id=com.whatsapp"

# Com configurações personalizadas
python review_scraper.py \
  --app-id "com.whatsapp" \
  --country "us" \
  --lang "en" \
  --output "whatsapp_usa_reviews"

# Ajuda completa
python review_scraper.py --help
```

### **Parâmetros Disponíveis:**
```
--url, -u          URL completa do app
--app-id, -a       ID do app (ex: com.whatsapp)
--country, -c      Código do país (padrão: br)
--lang, -l         Código do idioma (padrão: pt)
--output, -o       Nome dos arquivos de saída
--help, -h         Mostra esta ajuda
```

---

## 🌍 **Idiomas Suportados na Interface**

A aplicação suporta **6 idiomas** com tradução completa da interface:

| Bandeira | Código | Idioma | Status |
|----------|--------|--------|--------|
| 🇧🇷 | `pt` | **Português** | ✅ Padrão |
| 🇺🇸 | `en` | **English** | ✅ Completo |
| 🇪🇸 | `es` | **Español** | ✅ Completo |
| 🇫🇷 | `fr` | **Français** | ✅ Completo |
| 🇩🇪 | `de` | **Deutsch** | ✅ Completo |
| 🇮🇹 | `it` | **Italiano** | ✅ Completo |

**Como usar**: Clique na bandeira no canto superior direito da interface para trocar idioma instantaneamente!

### 🎯 **O que é traduzido:**
- ✅ Todos os botões e labels
- ✅ Títulos das seções
- ✅ Mensagens de status e log
- ✅ Modal "Sobre" completo
- ✅ Placeholders e tooltips
- ✅ Mensagens de erro

---

## 🚀 **Novidades da Versão Atual**

### ✨ **Recursos Implementados**
- 🌍 **Sistema multi-idiomas completo** (6 idiomas)
- 🎨 **Interface Material Design** moderna e responsiva
- 🏳️ **Seletor de bandeiras** com imagens PNG reais (24x24px)
- 📜 **Scroll suave** para telas de qualquer tamanho
- 🎯 **Ícone personalizado** do Google Play na barra de tarefas
- ℹ️ **Modal "Sobre"** com informações do projeto
- 🔄 **Tradução instantânea** de toda a interface
- 📊 **Barras de progresso** visuais e informativas

---

<div align="center">

**Desenvolvido com ❤️ por [DSiqueira](https://dsiqueira.com)**

⭐ **Se este projeto foi útil, deixe uma estrela!** ⭐

</div>