<div align="center">

# ðŸ“± Google Play Reviews Scraper

![Google Play Reviews Scraper](../assets/icons/google-play.png)

**ðŸš€ Ferramenta profissional para extrair e analisar reviews de apps do Google Play Store**

*Extraia milhares de reviews em minutos com uma interface moderna e bonita*

---

## ðŸŒ **Escolha seu Idioma / Choose Your Language**

[![ðŸ‡ºðŸ‡¸ English](https://img.shields.io/badge/ðŸ‡ºðŸ‡¸-English-4285f4?style=for-the-badge&labelColor=white)](../README.md)
[![ðŸ‡§ðŸ‡· PortuguÃªs](https://img.shields.io/badge/ðŸ‡§ðŸ‡·-PortuguÃªs-00a86b?style=for-the-badge&labelColor=white)](README_PT.md)
[![ðŸ‡ªðŸ‡¸ EspaÃ±ol](https://img.shields.io/badge/ðŸ‡ªðŸ‡¸-EspaÃ±ol-ea4335?style=for-the-badge&labelColor=white)](README_ES.md)
[![ðŸ‡«ðŸ‡· FranÃ§ais](https://img.shields.io/badge/ðŸ‡«ðŸ‡·-FranÃ§ais-4285f4?style=for-the-badge&labelColor=white)](README_FR.md)
[![ðŸ‡©ðŸ‡ª Deutsch](https://img.shields.io/badge/ðŸ‡©ðŸ‡ª-Deutsch-333333?style=for-the-badge&labelColor=white)](README_DE.md)
[![ðŸ‡®ðŸ‡¹ Italiano](https://img.shields.io/badge/ðŸ‡®ðŸ‡¹-Italiano-00a86b?style=for-the-badge&labelColor=white)](README_IT.md)

---

[![Python](https://img.shields.io/badge/Python-3.7+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](../LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Cross--Platform-lightgrey?style=for-the-badge)](https://github.com)
[![GUI](https://img.shields.io/badge/Interface-GUI_Moderna-blue?style=for-the-badge)](../src/app_gui.py)

**[ðŸŽ¬ Ver Demo](#-demo) â€¢ [âš¡ InÃ­cio RÃ¡pido](#-inÃ­cio-rÃ¡pido) â€¢ [ðŸ“– Funcionalidades](#-funcionalidades) â€¢ [ðŸ› ï¸ InstalaÃ§Ã£o](#ï¸-instalaÃ§Ã£o)**

---

</div>

## ðŸŽ¬ Demo

<div align="center">

### ðŸ–¥ï¸ Interface Moderna
*Interface bonita e intuitiva com suporte a mÃºltiplos idiomas*

![PrÃ©via da Interface](../assets/screenshots/google-play-reviews-scraper.png)

### âš¡ AplicaÃ§Ã£o em AÃ§Ã£o
*Veja o scraper funcionando com progresso em tempo real*

![Demo da AplicaÃ§Ã£o](../assets/screenshots/google-play-reviews-scraper.gif)

### ðŸ“Š Interface de Linha de Comando
*TambÃ©m disponÃ­vel via terminal para automaÃ§Ã£o*

![Demo do Terminal](../assets/screenshots/google-play-reviews-scraper-terminal.gif)

</div>

---

## âš¡ InÃ­cio RÃ¡pido

### ðŸ–¥ï¸ **Compatibilidade de Plataformas**

| Plataforma | Interface GrÃ¡fica | Linha de Comando | ObservaÃ§Ãµes |
|:----------:|:-----------------:|:----------------:|:------------|
| ðŸªŸ **Windows** | âœ… Suporte Completo | âœ… Suportado | GUI moderna com todos os recursos |
| ðŸŽ **macOS** | âœ… Interface Nativa | âœ… Suportado | Otimizada para design macOS |
| ðŸ§ **Linux** | âš ï¸ GUI BÃ¡sica | âœ… Suportado | GUI disponÃ­vel mas CLI recomendado |

### ðŸŽ¯ **OpÃ§Ã£o 1: AplicaÃ§Ã£o GUI (Recomendada)**

#### **ðŸªŸ UsuÃ¡rios Windows**
```bash
# 1. Clone o repositÃ³rio
git clone https://github.com/dssiqueira/google-play-reviews-scraper.git
cd google-play-reviews-scraper

# 2. Instale as dependÃªncias
pip install -r requirements.txt

# 3. Execute a GUI do Windows
python src/app_gui.py
```

#### **ðŸŽ UsuÃ¡rios macOS**
```bash
# 1. Clone o repositÃ³rio
git clone https://github.com/dssiqueira/google-play-reviews-scraper.git
cd google-play-reviews-scraper

# 2. Instale as dependÃªncias
pip install -r requirements.txt

# 3. Execute a interface nativa do macOS
python src/app_gui_mac.py
```

**âœ¨ Recursos do macOS:**
- ðŸŽ¨ **Design nativo do macOS** com fontes SF Pro
- ðŸ–±ï¸ **Suporte ao trackpad** e scroll nativo
- ðŸ“ **IntegraÃ§Ã£o com Finder** para fÃ¡cil acesso aos arquivos
- ðŸŒ **6 idiomas** com detecÃ§Ã£o automÃ¡tica de localizaÃ§Ã£o

#### **ðŸ§ UsuÃ¡rios Linux**
```bash
# 1. Clone o repositÃ³rio
git clone https://github.com/dssiqueira/google-play-reviews-scraper.git
cd google-play-reviews-scraper

# 2. Instale as dependÃªncias (incluindo tkinter)
sudo apt-get install python3-tk  # Ubuntu/Debian
# ou
sudo yum install tkinter          # CentOS/RHEL

pip install -r requirements.txt

# 3. Execute a GUI (bÃ¡sica) ou use CLI
python src/app_gui.py
```

### ðŸ”§ **OpÃ§Ã£o 2: Linha de Comando**

```bash
# Extrair reviews de um Ãºnico app
python src/review_scraper.py --url "https://play.google.com/store/apps/details?id=com.whatsapp"

# Processamento em lote de mÃºltiplos apps
python src/review_scraper.py --batch lista_apps.txt --output resultados/
```

### ðŸ“¦ **OpÃ§Ã£o 3: MÃ³dulo Python**

```python
from src.review_scraper import GooglePlayReviewScraper

scraper = GooglePlayReviewScraper()
reviews = scraper.scrape_reviews("com.whatsapp")
print(f"ExtraÃ­dos {len(reviews)} reviews!")
```

---

## ðŸŽ¨ VersÃµes da Interface

### **ðŸªŸ VersÃ£o Windows (`app_gui.py`)**
- **Interface inspirada no Material Design**
- **Seletor multi-idioma** com Ã­cones de bandeiras
- **Suporte a arrastar e soltar** URLs
- **Progresso em tempo real** com estatÃ­sticas detalhadas
- **Gerenciamento de fila** para processamento em lote
- **Abertura automÃ¡tica** dos resultados

### **ðŸŽ VersÃ£o macOS (`app_gui_mac.py`)**
- **Design nativo do macOS** seguindo Apple HIG
- **IntegraÃ§Ã£o com fonte SF Pro**
- **Suporte a gestos do trackpad**
- **IntegraÃ§Ã£o com Finder** para operaÃ§Ãµes de arquivo
- **DiÃ¡logos e notificaÃ§Ãµes** no estilo macOS
- **DetecÃ§Ã£o automÃ¡tica** do modo escuro/claro

### **ðŸ§ VersÃ£o Linux (`app_gui.py`)**
- **Compatibilidade multiplataforma**
- **Interface bÃ¡sica mas funcional**
- **Fallback para linha de comando** recomendado
- **Uso leve** de recursos

---

## ðŸ“ˆ Plataforma de AnÃ¡lise AvanÃ§ada

### ðŸš€ **Review Stats Pro - Analise Seus Dados**

ApÃ³s extrair reviews com esta ferramenta, leve sua anÃ¡lise para o prÃ³ximo nÃ­vel com nossa **plataforma de anÃ¡lise profissional**:

**ðŸ”— [Review Stats Pro](https://review-stats-pro.lovable.app/)**

<div align="center">

[![Review Stats Pro](https://img.shields.io/badge/ðŸš€-Review_Stats_Pro-4285f4?style=for-the-badge&labelColor=white)](https://review-stats-pro.lovable.app/)

*Plataforma profissional de anÃ¡lise de reviews - FaÃ§a upload do seu JSON e obtenha insights instantÃ¢neos*

</div>

### âœ¨ **O que o Review Stats Pro oferece:**

| ðŸ“Š **AnÃ¡lises** | ðŸŽ¯ **Insights** | ðŸ“ˆ **VisualizaÃ§Ãµes** | ðŸ” **Recursos AvanÃ§ados** |
|:---:|:---:|:---:|:---:|
| AnÃ¡lise de Sentimento | DetecÃ§Ã£o de TendÃªncias | GrÃ¡ficos Interativos | ExtraÃ§Ã£o de Palavras-chave |
| DistribuiÃ§Ã£o de Notas | Comportamento do UsuÃ¡rio | SÃ©ries Temporais | ComparaÃ§Ã£o de Concorrentes |
| Taxa de Resposta | Pontos de Dor | Mapas de Calor | Exportar RelatÃ³rios |
| MÃ©tricas de Crescimento | SolicitaÃ§Ãµes de Recursos | Nuvens de Palavras | IntegraÃ§Ã£o API |

### ðŸŽ¯ **Como usar em conjunto:**

1. **ðŸ“± Extrair reviews** com esta ferramenta scraper
2. **ðŸ“¤ Fazer upload do arquivo JSON** para Review Stats Pro
3. **ðŸ“Š Obter anÃ¡lises instantÃ¢neas** e insights
4. **ðŸ“ˆ Tomar decisÃµes baseadas em dados**

```bash
# 1. Extrair reviews (esta ferramenta)
python src/app_gui.py

# 2. Fazer upload do arquivo JSON gerado para:
# https://review-stats-pro.lovable.app/

# 3. Obter anÃ¡lises profissionais instantaneamente!
```

### ðŸ’¡ **Fluxo de trabalho perfeito:**
- **Esta ferramenta**: Coleta TODOS os reviews eficientemente
- **Review Stats Pro**: Analisa e visualiza os dados profissionalmente

---

## ðŸ“– Funcionalidades

<div align="center">

| ðŸŽ¯ **Recursos Principais** | ðŸŽ¨ **Interface** | ðŸ“Š **SaÃ­da** | ðŸŒ **Multi-Idioma** |
|:---:|:---:|:---:|:---:|
| Extrai **TODOS** os reviews | GUI moderna com temas | ExportaÃ§Ã£o CSV & JSON | 6 idiomas suportados |
| **Processamento em lote** | Progresso em tempo real | AnÃ¡lises detalhadas | Auto-detecÃ§Ã£o de idioma |
| **Filtragem inteligente** | Arrastar e soltar URLs | EstatÃ­sticas de tempo | TraduÃ§Ãµes personalizadas |
| **LimitaÃ§Ã£o de taxa** | Fila de mÃºltiplos apps | Tratamento de erros | Suporte RTL |

</div>

### ðŸš€ **O que torna especial?**

- **ðŸŽ¯ ExtraÃ§Ã£o Completa**: ObtÃ©m TODOS os reviews disponÃ­veis, nÃ£o apenas os recentes
- **âš¡ Super RÃ¡pido**: Scraping otimizado com limitaÃ§Ã£o inteligente de taxa  
- **ðŸŽ¨ Interface Bonita**: GUI moderna com temas claro/escuro
- **ðŸ“Š AnÃ¡lises Ricas**: EstatÃ­sticas detalhadas e rastreamento de tempo
- **ðŸ”„ Processamento em Lote**: Lida com mÃºltiplos apps simultaneamente
- **ðŸŒ Multi-Idioma**: Interface disponÃ­vel em 6 idiomas
- **ðŸ“± DetecÃ§Ã£o Inteligente**: Auto-detecta informaÃ§Ãµes do app e trata erros graciosamente
- **ðŸ’¾ MÃºltiplos Formatos**: Exporta para CSV, JSON com campos personalizÃ¡veis
- **ðŸ›¡ï¸ Robusto**: Lida com problemas de rede, limites de taxa e casos extremos

---
---

## 📊 Exemplos de Saída

### 📄 **Formato CSV**
```csv
review_id,user_name,content,score,thumbs_up_count,at,reply_content,reply_at,app_version
gp:AOqpTOH123...,João Silva,"Ótimo app!",5,12,2024-01-15 10:30:00,"Obrigado!",2024-01-16 09:15:00,2.1.5
```

### 📋 **Formato JSON**
```json
{
  "collection_info": {
    "collected_at": "2024-01-15T10:30:00Z",
    "total_reviews": 1500,
    "country": "br",
    "language": "pt"
  },
  "app_info": {
    "appId": "com.whatsapp",
    "title": "WhatsApp Messenger",
    "developer": "WhatsApp LLC",
    "score": 4.1,
    "reviews": 50000000
  },
  "reviews": [
    {
      "review_id": "gp:AOqpTOH123...",
      "user_name": "João Silva",
      "content": "Ótimo app!",
      "score": 5,
      "thumbs_up_count": 12,
      "at": "2024-01-15T10:30:00Z"
    }
  ]
}
```

---

## ⚠️ Solução de Problemas

### **Problemas Comuns**

#### **🐍 Problemas de Versão do Python**
```bash
# Verificar versão do Python
python --version

# Se usando Python 3.7 ou anterior, atualize para 3.9+
# Windows: Baixe de python.org
# macOS: brew install python@3.9
# Linux: sudo apt install python3.9
```

#### **📦 Problemas de Instalação**
```bash
# Limpar cache do pip
pip cache purge

# Instalar com saída detalhada
pip install -r requirements.txt -v

# Usar ambiente virtual (recomendado)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

#### **🌐 Problemas de Rede/Scraping**
- **Limitação de taxa**: A ferramenta lida automaticamente com limites de taxa
- **Nenhum review encontrado**: Verifique se a URL do app está correta
- **Erros de conexão**: Verifique a conexão com internet e tente novamente

#### **🖥️ Problemas com GUI**

**Windows:**
```bash
# Testar se tkinter está disponível
python -c "import tkinter; print('Tkinter OK')"

# Se GUI não abrir, tente:
python src/app_gui.py
```

**macOS:**
```bash
# Use a versão nativa do macOS
python src/app_gui_mac.py

# Se problemas persistirem, verifique instalação do Python:
python3 --version
which python3
```

**Linux:**
```bash
# Instalar tkinter se ausente
sudo apt-get install python3-tk  # Ubuntu/Debian
sudo yum install tkinter          # CentOS/RHEL
sudo pacman -S tk                 # Arch Linux

# Testar GUI
python src/app_gui.py
```

---

## 🎯 Casos de Uso

### 💼 **Perfeito para:**

- **📊 Pesquisadores de Mercado** - Analisar apps concorrentes e tendências de mercado
- **🎯 Product Managers** - Coletar feedback de usuários para planejamento de funcionalidades  
- **🔍 Pesquisadores UX** - Entender pontos de dor e preferências dos usuários
- **📈 Desenvolvedores de Apps** - Monitorar performance e satisfação dos usuários
- **🏢 Analistas de Negócios** - Gerar insights para decisões estratégicas
- **🎓 Estudantes e Acadêmicos** - Coletar dados para projetos de pesquisa

### 🔗 **Fluxo de Trabalho Recomendado:**

1. **Extrair** reviews usando esta ferramenta
2. **Fazer upload** do JSON para [Review Stats Pro](https://review-stats-pro.lovable.app/)
3. **Analisar** com gráficos e insights profissionais
4. **Tomar** decisões baseadas em dados

---

## 🛠️ Ferramentas Complementares

### 📊 **Review Stats Pro**
**Plataforma de análise profissional para seus dados extraídos**

[![Review Stats Pro](https://img.shields.io/badge/🚀-Acessar_Review_Stats_Pro-4285f4?style=for-the-badge)](https://review-stats-pro.lovable.app/)

**Recursos:**
- 🎯 **Análise de Sentimento** - Entenda as emoções dos usuários
- 📈 **Detecção de Tendências** - Identifique padrões ao longo do tempo  
- 🔍 **Extração de Palavras-chave** - Encontre tópicos mais mencionados
- 📊 **Gráficos Interativos** - Visualizações bonitas
- 📤 **Exportar Relatórios** - Relatórios profissionais em PDF/Excel
- 🔄 **Atualizações em Tempo Real** - Dashboard com atualizações ao vivo

**Como usar:**
1. Extrair reviews com este scraper
2. Fazer upload do arquivo JSON para Review Stats Pro
3. Obter análises profissionais instantâneas

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Veja como você pode ajudar:

### 🐛 **Reportar Problemas**
- Encontrou um bug? [Abra uma issue](https://github.com/dssiqueira/google-play-reviews-scraper/issues)
- Inclua passos para reproduzir
- Forneça informações do sistema (OS, versão do Python)

### 💡 **Sugerir Funcionalidades**
- Tem uma ideia? [Inicie uma discussão](https://github.com/dssiqueira/google-play-reviews-scraper/discussions)
- Explique o caso de uso
- Forneça mockups se possível

### 🔧 **Contribuições de Código**
```bash
# 1. Faça fork do repositório
# 2. Crie uma branch de funcionalidade
git checkout -b feature/funcionalidade-incrivel

# 3. Faça suas alterações
# 4. Teste completamente
# 5. Envie um pull request
```

---

## 📞 Suporte

### 🆘 **Precisa de Ajuda?**
- **📖 Documentação**: Confira nossos guias detalhados acima
- **💬 Discussões**: Participe das [discussões da comunidade](https://github.com/dssiqueira/google-play-reviews-scraper/discussions)
- **🐛 Issues**: Reporte bugs na [seção de issues](https://github.com/dssiqueira/google-play-reviews-scraper/issues)

### ❓ **FAQ**

<details>
<summary><strong>🔍 Quantos reviews posso extrair?</strong></summary>

A ferramenta extrai TODOS os reviews disponíveis do Google Play Store. Isso pode variar de centenas a milhões dependendo da popularidade do app.
</details>

<details>
<summary><strong>⚡ Qual a velocidade da extração?</strong></summary>

A velocidade varia pelo tamanho do app e condições da rede:
- Apps pequenos (< 1K reviews): 30-60 segundos
- Apps médios (1K-10K reviews): 2-5 minutos  
- Apps grandes (10K+ reviews): 5-30 minutos
</details>

<details>
<summary><strong>🌍 Quais países/idiomas são suportados?</strong></summary>

Todos os países e idiomas suportados pelo Google Play Store. A ferramenta lida automaticamente com localização e diferenças regionais.
</details>

<details>
<summary><strong>📊 Como posso analisar os dados extraídos?</strong></summary>

Recomendamos usar [Review Stats Pro](https://review-stats-pro.lovable.app/) - uma plataforma de análise profissional projetada especificamente para dados de reviews. Simplesmente faça upload do seu arquivo JSON e obtenha insights instantâneos com análise de sentimento, tendências e gráficos interativos.
</details>

<details>
<summary><strong>🛡️ Isso é legal?</strong></summary>

Sim! A ferramenta acessa apenas dados publicamente disponíveis do Google Play Store, similar a visualizar reviews em um navegador web.
</details>

---

## 📄 Licença

Este projeto está licenciado sob a **Licença MIT** - veja o arquivo [LICENSE](../LICENSE) para detalhes.

---

<div align="center">

**🚀 Desenvolvido com ❤️ para a comunidade**

**Se este projeto te ajudou, considere dar uma ⭐!**

[![GitHub stars](https://img.shields.io/github/stars/dssiqueira/google-play-reviews-scraper?style=social)](../../stargazers)
[![GitHub forks](https://img.shields.io/github/forks/dssiqueira/google-play-reviews-scraper?style=social)](../../network/members)

</div>