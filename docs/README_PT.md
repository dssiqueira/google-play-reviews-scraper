<div align="center">

# 📱 Google Play Reviews Scraper

![Google Play Reviews Scraper](../assets/icons/google-play.png)

**🚀 Ferramenta profissional para extrair e analisar reviews de apps do Google Play Store**

*Extraia milhares de reviews em minutos com uma interface moderna e bonita*

---

## 🌍 **Escolha seu Idioma / Choose Your Language**

[![🇺🇸 English](https://img.shields.io/badge/🇺🇸-English-4285f4?style=for-the-badge&labelColor=white)](../README.md)
[![🇧🇷 Português](https://img.shields.io/badge/🇧🇷-Português-00a86b?style=for-the-badge&labelColor=white)](README_PT.md)
[![🇪🇸 Español](https://img.shields.io/badge/🇪🇸-Español-ea4335?style=for-the-badge&labelColor=white)](README_ES.md)
[![🇫🇷 Français](https://img.shields.io/badge/🇫🇷-Français-4285f4?style=for-the-badge&labelColor=white)](README_FR.md)
[![🇩🇪 Deutsch](https://img.shields.io/badge/🇩🇪-Deutsch-333333?style=for-the-badge&labelColor=white)](README_DE.md)
[![🇮🇹 Italiano](https://img.shields.io/badge/🇮🇹-Italiano-00a86b?style=for-the-badge&labelColor=white)](README_IT.md)

---

[![Python](https://img.shields.io/badge/Python-3.7+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](../LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Cross--Platform-lightgrey?style=for-the-badge)](https://github.com)
[![GUI](https://img.shields.io/badge/Interface-GUI_Moderna-blue?style=for-the-badge)](../src/app_gui.py)

**[🎬 Ver Demo](#-demo) • [⚡ Início Rápido](#-início-rápido) • [📖 Funcionalidades](#-funcionalidades) • [🛠️ Instalação](#️-instalação)**

---

</div>

## 🎬 Demo

<div align="center">

### 🖥️ Interface Moderna
*Interface bonita e intuitiva com suporte a múltiplos idiomas*

![Prévia da Interface](../assets/screenshots/interface-preview.png)

### ⚡ Processamento em Lote
*Processe múltiplos apps simultaneamente com progresso em tempo real*

![Processamento em Lote](../assets/screenshots/batch-processing.gif)

### 📊 Formatos de Saída Ricos
*Exporte para CSV, JSON com análises detalhadas*

![Formatos de Saída](../assets/screenshots/output-formats.png)

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
| 🍎 **macOS** | ✅ **NOVO!** Interface Nativa | ✅ Suportado | ❌ Não disponível |
| 🐧 **Linux** | ❌ Apenas terminal | ✅ Suportado | ❌ Não disponível |

> **✨ NOVO**: macOS agora tem interface visual nativa com 6 idiomas e design nativo!
## ⚡ Início Rápido

### 🎯 **Opção 1: Aplicação GUI (Recomendada)**

```bash
# 1. Clone o repositório
git clone https://github.com/your-username/google-play-reviews-scraper.git
cd google-play-reviews-scraper

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Execute a interface gráfica
python src/app_gui.py
```

### 🔧 **Opção 2: Linha de Comando**

```bash
# Extrair reviews de um único app
python src/review_scraper.py --url "https://play.google.com/store/apps/details?id=com.whatsapp"

# Processamento em lote de múltiplos apps
python src/review_scraper.py --batch lista_apps.txt --output resultados/
```

### 📦 **Opção 3: Módulo Python**

```python
from src.review_scraper import GooglePlayReviewScraper

scraper = GooglePlayReviewScraper()
reviews = scraper.scrape_reviews("com.whatsapp")
print(f"Extraídos {len(reviews)} reviews!")
```

---

## 📖 Funcionalidades

<div align="center">

| 🎯 **Recursos Principais** | 🎨 **Interface** | 📊 **Saída** | 🌍 **Multi-Idioma** |
|:---:|:---:|:---:|:---:|
| Extrai **TODOS** os reviews | GUI moderna com temas | Exportação CSV & JSON | 6 idiomas suportados |
| **Processamento em lote** | Progresso em tempo real | Análises detalhadas | Auto-detecção de idioma |
| **Filtragem inteligente** | Arrastar e soltar URLs | Estatísticas de tempo | Traduções personalizadas |
| **Limitação de taxa** | Fila de múltiplos apps | Tratamento de erros | Suporte RTL |

</div>

### 🚀 **O que torna especial?**

- **🎯 Extração Completa**: Obtém TODOS os reviews disponíveis, não apenas os recentes
- **⚡ Super Rápido**: Scraping otimizado com limitação inteligente de taxa  
- **🎨 Interface Bonita**: GUI moderna com temas claro/escuro
- **📊 Análises Ricas**: Estatísticas detalhadas e rastreamento de tempo
- **🔄 Processamento em Lote**: Lida com múltiplos apps simultaneamente
- **🌍 Multi-Idioma**: Interface disponível em 6 idiomas
- **📱 Detecção Inteligente**: Auto-detecta informações do app e trata erros graciosamente
- **💾 Múltiplos Formatos**: Exporta para CSV, JSON com campos personalizáveis
- **🛡️ Robusto**: Lida com problemas de rede, limites de taxa e casos extremos

---

## �️ IInstalação

### � **RCequisitos**

- **Python 3.7+** (3.9+ recomendado)
- **Conexão com internet** para scraping
- **2GB RAM** mínimo (4GB+ para grandes datasets)

### � **Duependências**

```bash
# Dependências principais (instaladas automaticamente)
google-play-scraper  # API do Google Play Store
pandas              # Processamento de dados
tkinter            # Framework GUI (geralmente pré-instalado)
```

### 📦 **Métodos de Instalação**

#### **Método 1: Git Clone (Recomendado)**
```bash
git clone https://github.com/your-username/google-play-reviews-scraper.git
cd google-play-reviews-scraper
pip install -r requirements.txt
```

#### **Método 2: Download Direto**
```bash
# Baixe o ZIP do GitHub
# Extraia para a pasta desejada
cd google-play-reviews-scraper-main
pip install -r requirements.txt
```

#### **Método 3: Ambiente Virtual (Avançado)**
```bash
python -m venv scraper_env
source scraper_env/bin/activate  # Linux/Mac
# ou
scraper_env\Scripts\activate     # Windows

pip install -r requirements.txt
```

### ✅ **Verificar Instalação**

```bash
# Testar o scraper
python src/review_scraper.py --help

# Executar GUI
python src/app_gui.py
```

---

## 📊 Exemplos de Uso

### 🎯 **Uso da GUI**

1. **Execute a aplicação**
   ```bash
   python src/app_gui.py
   ```

2. **Adicione apps à fila**
   - Cole a URL do Google Play Store
   - Clique em "Adicionar" para enfileirar
   - Repita para múltiplos apps

3. **Configure as opções**
   - Escolha país/idioma
   - Defina diretório de saída
   - Selecione formato de exportação

4. **Inicie a extração**
   - Clique em "Iniciar Scraping"
   - Monitore o progresso em tempo real
   - Acesse resultados via botões

### 🔧 **Uso da Linha de Comando**

```bash
# Uso básico
python src/review_scraper.py --url "https://play.google.com/store/apps/details?id=com.whatsapp"

# Opções avançadas
python src/review_scraper.py \
  --url "https://play.google.com/store/apps/details?id=com.whatsapp" \
  --country "br" \
  --language "pt" \
  --output "whatsapp_reviews" \
  --format "both"

# Processamento em lote
python src/review_scraper.py --batch lista_apps.txt --output resultados/
```

### 🐍 **Integração Python**

```python
from src.review_scraper import GooglePlayReviewScraper

# Inicializar scraper
scraper = GooglePlayReviewScraper(country='br', lang='pt')

# Extrair reviews
reviews = scraper.scrape_reviews('com.whatsapp')

# Processar resultados
print(f"Total de reviews: {len(reviews)}")
for review in reviews[:5]:  # Mostrar primeiros 5
    print(f"⭐ {review['score']}/5 - {review['content'][:100]}...")
```

---

## 📈 Exemplos de Saída

### 📄 **Saída CSV**
```csv
userName,score,content,thumbsUpCount,reviewCreatedVersion,at,appVersion
João Silva,5,"App incrível! Adoro os novos recursos",42,1.2.3,2024-01-15,1.2.3
Maria Santos,4,"Bom mas precisa melhorar a interface",15,1.2.2,2024-01-14,1.2.3
...
```

### 📋 **Saída JSON**
```json
{
  "app_info": {
    "title": "WhatsApp Messenger",
    "appId": "com.whatsapp",
    "score": 4.1,
    "reviews_count": 50000000
  },
  "extraction_info": {
    "total_reviews": 1500,
    "extraction_date": "2024-01-15T10:30:00Z",
    "time_taken": "2m 34s"
  },
  "reviews": [
    {
      "userName": "João Silva",
      "score": 5,
      "content": "App incrível! Adoro os novos recursos",
      "thumbsUpCount": 42,
      "at": "2024-01-15T08:20:00Z"
    }
  ]
}
```

### 📊 **Estatísticas Geradas**
- **Total de reviews extraídos**
- **Avaliação média**
- **Distribuição de notas (1-5 estrelas)**
- **Tempo de extração e velocidade**
- **Reviews mais úteis**
- **Proporção de reviews recentes vs antigos**

---

## 📁 Estrutura do Projeto

```
📦 google-play-reviews-scraper/
├── 📂 src/                          # 🐍 Código fonte
│   ├── app_gui.py                   # 🖥️ Aplicação GUI moderna
│   ├── review_scraper.py            # ⚙️ Motor de scraping principal
│   ├── translations.py              # 🌍 Suporte multi-idioma
│   └── time_stats.py                # 📊 Análises de performance
├── 📂 assets/                       # 🎨 Recursos visuais
│   ├── icons/                       # 🎯 Ícones da aplicação
│   │   ├── google-play.png          # 📱 Ícone principal do app
│   │   └── google-play.ico          # 🖼️ Ícone do Windows
│   ├── flags/                       # 🏳️ Bandeiras de idiomas (24x24px)
│   │   ├── br.png                   # 🇧🇷 Brasil
│   │   ├── en.png                   # 🇺🇸 Inglês
│   │   └── ...                      # 🌍 Outros idiomas
│   └── screenshots/                 # 📸 Imagens de demonstração
├── 📂 docs/                         # 📖 Documentação
│   ├── README.md                    # 🇺🇸 Docs em inglês
│   ├── README_PT.md                 # 🇧🇷 Docs em português
│   └── TRANSLATIONS.md              # 🌍 Guia de tradução
├── 📂 examples/                     # 📋 Exemplos de saída
│   ├── sample_reviews.csv           # 📊 Exemplo CSV
│   ├── sample_reviews.json          # 📄 Exemplo JSON
│   └── README.md                    # 📝 Guia de exemplos
├── 📄 requirements.txt              # 📦 Dependências Python
├── 📄 LICENSE                       # ⚖️ Licença MIT
└── 📄 README.md                     # 📖 Este arquivo
```

### Opção 1: Executável (Apenas Windows)
1. Baixe o executável da [página de releases](../../releases)
2. Execute `GooglePlayReviewScraper.exe`
3. Pronto! Não precisa instalar Python

### Opção 2: Interface Visual (Windows & macOS)
```bash
# Clone o repositório
git clone https://github.com/seu-usuario/google-play-reviews-scraper.git
cd google-play-reviews-scraper

# Instale as dependências
pip install -r requirements.txt

# Windows: Execute a interface gráfica
python app_gui.py

# macOS: Execute a interface nativa
cd src && python3 app_gui_mac.py
```

### Opção 3: Linha de Comando (Todas as Plataformas)
```bash
# Após clonar e instalar dependências
python review_scraper.py --url "https://play.google.com/store/apps/details?id=com.whatsapp"
```

**🪟 Usuários Windows**: A interface abrirá em Português. Use o seletor de bandeiras no canto superior direito para trocar idioma!
**🍎 Usuários macOS**: Interface nativa com 6 idiomas, fontes SF Pro e integração com Finder!
**🐧 Usuários Linux**: Use a interface de linha de comando com os parâmetros mostrados abaixo.

---

## 💻 **Interface Gráfica Moderna**

![Google Play Reviews Scraper Screenshot](../assets/screenshots/google-play-reviews-scraper.png)

### 🎬 **Aplicação em Funcionamento**
![Google Play Reviews Scraper Demo](../assets/screenshots/google-play-reviews-scraper.gif)

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

### 🎬 **Demonstração do Terminal**
![Google Play Reviews Scraper Terminal Demo](../assets/screenshots/google-play-reviews-scraper-terminal.gif)

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

</div>---

## 🎯
 Casos de Uso

<div align="center">

| 🏢 **Negócios** | 🔬 **Pesquisa** | 📱 **Desenvolvimento** | 📊 **Analytics** |
|:---:|:---:|:---:|:---:|
| Análise de concorrência | Estudos de comportamento | Feedback de recursos | Tendências de mercado |
| Pesquisa de mercado | Pesquisa acadêmica | Relatórios de bugs | Análise de sentimento |
| Monitoramento de marca | Pesquisa UX | Otimização de app store | Métricas de performance |
| Insights de clientes | Dados de pesquisa | Testes de usuário | Gestão de reputação |

</div>

### 💼 **Perfeito para:**

- **📊 Pesquisadores de Mercado** - Analisar apps concorrentes e tendências de mercado
- **🎯 Gerentes de Produto** - Coletar feedback de usuários para planejamento de recursos  
- **🔍 Pesquisadores UX** - Entender pontos de dor e preferências dos usuários
- **📈 Desenvolvedores de Apps** - Monitorar performance e satisfação dos usuários
- **🏢 Analistas de Negócios** - Gerar insights para decisões estratégicas
- **🎓 Estudantes e Acadêmicos** - Coletar dados para projetos de pesquisa

---

## 🌍 Suporte Multi-Idioma

<div align="center">

**🇺🇸 English** • **🇧🇷 Português** • **🇪🇸 Español** • **🇫🇷 Français** • **🇩🇪 Deutsch** • **🇮🇹 Italiano**

*A interface se adapta automaticamente ao idioma do seu sistema*

</div>

---

## 🌍 **Documentação Completa em Outros Idiomas**

<div align="center">

**📖 Documentação completa com guias detalhados, exemplos e tutoriais:**

[![🇺🇸 Complete English Documentation](https://img.shields.io/badge/🇺🇸-Complete_Documentation-4285f4?style=for-the-badge)](../README.md)
[![🇪🇸 Documentación Completa en Español](https://img.shields.io/badge/🇪🇸-Documentación_Completa-ea4335?style=for-the-badge)](README_ES.md)
[![🇫🇷 Documentation Complète en Français](https://img.shields.io/badge/🇫🇷-Documentation_Complète-4285f4?style=for-the-badge)](README_FR.md)
[![🇩🇪 Vollständige Dokumentation auf Deutsch](https://img.shields.io/badge/🇩🇪-Vollständige_Dokumentation-333333?style=for-the-badge)](README_DE.md)
[![🇮🇹 Documentazione Completa in Italiano](https://img.shields.io/badge/🇮🇹-Documentazione_Completa-00a86b?style=for-the-badge)](README_IT.md)

*Cada versão de idioma inclui exemplos localizados, contexto cultural e orientações específicas da região*

**📋 [Ver Todos os Idiomas e Guia de Tradução](LANGUAGES.md)**

</div>

---

## 🤝 Contribuindo

Damos as boas-vindas a contribuições! Veja como você pode ajudar:

### 🐛 **Reportar Problemas**
- Encontrou um bug? [Abra uma issue](../../issues)
- Inclua passos para reproduzir
- Forneça informações do sistema

### 💡 **Sugerir Recursos**
- Tem uma ideia? [Inicie uma discussão](../../discussions)
- Explique o caso de uso
- Forneça mockups se possível

### 🔧 **Contribuições de Código**
```bash
# 1. Faça fork do repositório
# 2. Crie uma branch de recurso
git checkout -b feature/recurso-incrivel

# 3. Faça suas alterações
# 4. Teste completamente
python -m pytest tests/

# 5. Envie um pull request
```

### 🌍 **Traduções**
Ajude-nos a suportar mais idiomas! Veja o [guia de traduções](TRANSLATIONS.md).

---

## 📞 Suporte

### 🆘 **Precisa de Ajuda?**

- **📖 Documentação**: Confira nossos [guias detalhados](../docs/)
- **💬 Discussões**: Participe das nossas [discussões da comunidade](../../discussions)
- **🐛 Issues**: Reporte bugs na [seção de issues](../../issues)
- **📧 Email**: Entre em contato conosco em support@example.com

### ❓ **FAQ**

<details>
<summary><strong>🔍 Quantos reviews posso extrair?</strong></summary>

A ferramenta extrai TODOS os reviews disponíveis do Google Play Store. Isso pode variar de centenas a milhões dependendo da popularidade do app.

</details>

<details>
<summary><strong>⚡ Quão rápida é a extração?</strong></summary>

A velocidade varia pelo tamanho do app e condições de rede. Taxas típicas:
- Apps pequenos (< 1K reviews): 30-60 segundos
- Apps médios (1K-10K reviews): 2-5 minutos  
- Apps grandes (10K+ reviews): 5-30 minutos

</details>

<details>
<summary><strong>🌍 Quais países/idiomas são suportados?</strong></summary>

Todos os países e idiomas suportados pelo Google Play Store. A ferramenta lida automaticamente com localização e diferenças regionais.

</details>

<details>
<summary><strong>🛡️ Isso é legal?</strong></summary>

Sim! A ferramenta acessa apenas dados publicamente disponíveis do Google Play Store, similar a visualizar reviews em um navegador web.

</details>

---

## 📄 Licença

Este projeto está licenciado sob a **Licença MIT** - veja o arquivo [LICENSE](../LICENSE) para detalhes.

### 🔓 **O que isso significa:**
- ✅ **Uso comercial** permitido
- ✅ **Modificação** permitida  
- ✅ **Distribuição** permitida
- ✅ **Uso privado** permitido
- ❌ **Nenhuma garantia** fornecida
- ❌ **Nenhuma responsabilidade** assumida

---

## 🏆 Agradecimentos

### 🙏 **Agradecimentos Especiais**

- **[google-play-scraper](https://github.com/JoMingyu/google-play-scraper)** - Funcionalidade principal de scraping
- **[pandas](https://pandas.pydata.org/)** - Processamento e análise de dados
- **[tkinter](https://docs.python.org/3/library/tkinter.html)** - Framework GUI
- **Contribuidores da comunidade** - Relatórios de bugs, solicitações de recursos e traduções

### 🌟 **Inspiração**

Este projeto foi criado para democratizar o acesso a dados de app stores para pesquisadores, desenvolvedores e empresas que precisam de insights mas não têm recursos para ferramentas de analytics caras.

---

<div align="center">

## ⭐ **Histórico de Estrelas**

[![Star History Chart](https://api.star-history.com/svg?repos=your-username/google-play-reviews-scraper&type=Date)](https://star-history.com/#your-username/google-play-reviews-scraper&Date)

---

**🚀 Desenvolvido com ❤️ para a comunidade**

**Se este projeto te ajudou, considere dar uma ⭐!**

*Seu apoio nos motiva a continuar melhorando e adicionando novos recursos*

[![GitHub stars](https://img.shields.io/github/stars/your-username/google-play-reviews-scraper?style=social)](../../stargazers)
[![GitHub forks](https://img.shields.io/github/forks/your-username/google-play-reviews-scraper?style=social)](../../network/members)
[![GitHub watchers](https://img.shields.io/github/watchers/your-username/google-play-reviews-scraper?style=social)](../../watchers)

</div>