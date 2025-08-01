"""Graphical user interface for the Google Play Reviews Scraper."""

import tkinter as tk
from tkinter import messagebox, filedialog
import threading
import os
import time
from review_scraper import GooglePlayReviewScraper
from translations import translator
from time_stats import time_stats

class ReviewScraperApp:
    """Main application window that manages the scraping workflow."""
    def __init__(self, root):
        self.root = root
        self.root.title("Google Play Reviews Scraper")
        self.root.geometry("800x700")
        self.root.resizable(True, True)
        self.root.minsize(700, 600)
        
        # Configurar ícone da aplicação
        self.setup_icon()
        
        # Força o ícone na barra de tarefas do Windows
        self.setup_taskbar_icon()
        
        # Tema claro com cores contrastantes e vibrantes
        self.colors = {
            # Cores principais mais vibrantes e contrastantes
            'primary': '#4F46E5',        # Azul índigo mais intenso
            'secondary': '#7C3AED',      # Roxo violeta mais vibrante
            'accent': '#EC4899',         # Rosa magenta vibrante
            'error': '#DC2626',          # Vermelho mais intenso
            'warning': '#D97706',        # Laranja mais contrastante
            'info': '#0891B2',           # Ciano mais escuro
            'success': '#059669',        # Verde mais intenso
            
            # Cores específicas para botões contrastantes
            'btn_blue': '#2563EB',       # Azul royal vibrante
            'btn_purple': '#9333EA',     # Roxo vibrante
            'btn_pink': '#DB2777',       # Rosa pink intenso
            'btn_red': '#DC2626',        # Vermelho intenso
            'btn_orange': '#EA580C',     # Laranja vibrante
            'btn_cyan': '#0891B2',       # Ciano intenso
            'btn_green': '#16A34A',      # Verde vibrante
            'btn_indigo': '#4338CA',     # Índigo profundo
            
            # Cores de interface
            'background': '#F8FAFC',     # Slate 50 (fundo principal)
            'surface': '#FFFFFF',        # Branco (cards)
            'surface_light': '#F1F5F9',  # Slate 100 (hover suave)
            'surface_dark': '#E2E8F0',   # Slate 200 (bordas)
            'on_surface': '#1E293B',     # Slate 800 (texto escuro)
            'on_background': '#334155',  # Slate 700 (texto médio)
            'disabled': '#94A3B8',       # Slate 400 (desabilitado)
            'divider': '#E2E8F0',        # Slate 200 (divisores)
            'input_bg': '#F8FAFC',       # Slate 50 (inputs)
            'input_border': '#D1D5DB',   # Gray 300 (bordas inputs)
            'hover': '#F1F5F9',          # Slate 100 (hover)
            'border': '#E5E7EB',         # Gray 200 (bordas suaves)
            'shadow': '#0000001A'        # Sombra sutil (10% opacidade)
        }
        
        # Configurar estilo
        self.setup_styles()
        
        # Variáveis
        self.country_var = tk.StringVar(value="br")
        self.lang_var = tk.StringVar(value="pt")
        self.output_dir_var = tk.StringVar(value=os.getcwd())
        
        # Estado
        self.scraper = GooglePlayReviewScraper()  # Inicializa scraper
        self.is_running = False
        self.csv_path = None
        self.json_path = None
        
        self.create_interface()
        
        # Bind eventos (removido - agora usa on_urls_change)

    def create_language_selector(self, parent):
        """Cria seletor de idioma customizado com bandeiras PNG"""
        # Carrega as imagens das bandeiras
        self.load_flag_images()
        
        # Frame para o seletor
        lang_frame = tk.Frame(parent, bg=self.colors['background'])
        lang_frame.pack(side=tk.LEFT, padx=(0, 5))
        
        # Botão atual com bandeira (usando get_flag_code para mapear corretamente)
        current_flag = self.get_flag_code(translator.current_language)
        self.current_lang_display = tk.Button(lang_frame,
                                            image=self.flag_images.get(current_flag),
                                            text=f" {translator.current_language.upper()}",
                                            compound=tk.LEFT,
                                            font=('Segoe UI', 9, 'bold'),
                                            bg=self.colors['background'],
                                            fg=self.colors['on_background'],
                                            relief='solid',
                                            bd=1,
                                            padx=8,
                                            pady=4,
                                            cursor='hand2',
                                            command=self.toggle_language_menu)
        self.current_lang_display.pack()
        
        # Menu dropdown (inicialmente oculto)
        self.lang_menu = tk.Frame(self.root, bg=self.colors['surface'], relief='solid', bd=1)
        self.lang_menu_visible = False
        
        # Opções de idioma com bandeiras
        languages = [
            ('pt', 'Português'),
            ('en', 'English'),
            ('es', 'Español'),
            ('fr', 'Français'),
            ('de', 'Deutsch'),
            ('it', 'Italiano')
        ]
        
        for code, display in languages:
            flag_code = self.get_flag_code(code)
            flag_img = self.flag_images.get(flag_code)
            
            btn = tk.Button(self.lang_menu,
                          image=flag_img,
                          text=f"  {display}",
                          compound=tk.LEFT,
                          font=('Segoe UI', 9),
                          bg=self.colors['surface'],
                          fg=self.colors['on_surface'],
                          relief='flat',
                          bd=0,
                          anchor='w',
                          padx=10,
                          pady=6,
                          cursor='hand2',
                          command=lambda c=code: self.select_language(c))
            btn.pack(fill=tk.X)
            
            # Hover effect
            def on_enter(e, button=btn):
                button.config(bg=self.colors['divider'])
            def on_leave(e, button=btn):
                button.config(bg=self.colors['surface'])
            btn.bind('<Enter>', on_enter)
            btn.bind('<Leave>', on_leave)
        
        # Bind para fechar menu ao clicar fora
        self.root.bind('<Button-1>', self.hide_language_menu)

    def load_flag_images(self):
        """Carrega as imagens das bandeiras (24x24px)"""
        self.flag_images = {}
        
        # Mapeamento de idiomas para arquivos de bandeira
        flag_files = {
            'pt': 'br.png',    # Português -> Brasil
            'en': 'en.png',    # English -> Inglaterra/EUA
            'es': 'es.png',    # Español -> Espanha
            'fr': 'fr.png',    # Français -> França
            'de': 'al.png',    # Deutsch -> Alemanha (usando al.png)
            'it': 'it.png',    # Italiano -> Itália
            'br': 'br.png',    # Brasil
            'al': 'al.png'     # Alemanha
        }
        
        for code, filename in flag_files.items():
            try:
                flag_path = os.path.join("assets", "flags", filename)
                if os.path.exists(flag_path):
                    # Carrega a imagem sem redimensionar (já está 24x24px)
                    flag_img = tk.PhotoImage(file=flag_path)
                    self.flag_images[code] = flag_img
                else:
                    print(f"Bandeira não encontrada: {flag_path}")
            except Exception as e:
                print(f"Erro ao carregar bandeira {filename}: {e}")
        
        # Se não conseguiu carregar nenhuma imagem, cria placeholders
        if not self.flag_images:
            print("Nenhuma bandeira carregada, usando placeholders")
            for code in ['pt', 'en', 'es', 'fr', 'de', 'it', 'br', 'al']:
                # Cria uma imagem placeholder 24x24
                placeholder = tk.PhotoImage(width=24, height=24)
                placeholder.put("#CCCCCC", to=(0, 0, 24, 24))
                self.flag_images[code] = placeholder

    def get_flag_code(self, lang_code):
        """Retorna o código da bandeira para o idioma"""
        flag_mapping = {
            'pt': 'br',    # Português -> Brasil
            'en': 'en',    # English -> Inglaterra
            'es': 'es',    # Español -> Espanha
            'fr': 'fr',    # Français -> França
            'de': 'al',    # Deutsch -> Alemanha
            'it': 'it'     # Italiano -> Itália
        }
        return flag_mapping.get(lang_code, 'br')

    def toggle_language_menu(self):
        """Mostra/oculta o menu de idiomas"""
        if self.lang_menu_visible:
            self.hide_language_menu()
        else:
            self.show_language_menu()

    def show_language_menu(self):
        """Mostra o menu de idiomas"""
        # Atualiza a posição antes de mostrar
        self.root.update_idletasks()
        
        # Posiciona o menu abaixo do seletor (coordenadas relativas à janela principal)
        button_x = self.current_lang_display.winfo_x()
        button_y = self.current_lang_display.winfo_y()
        button_height = self.current_lang_display.winfo_height()
        
        # Encontra o frame pai para calcular posição correta
        parent = self.current_lang_display.master
        while parent != self.root:
            button_x += parent.winfo_x()
            button_y += parent.winfo_y()
            parent = parent.master
        
        # Posiciona o menu
        menu_x = button_x
        menu_y = button_y + button_height + 2
        
        self.lang_menu.place(x=menu_x, y=menu_y)
        self.lang_menu_visible = True

    def hide_language_menu(self, event=None):
        """Oculta o menu de idiomas"""
        if hasattr(self, 'lang_menu') and self.lang_menu_visible:
            # Verifica se o clique foi dentro do menu ou botão
            if event:
                widget = event.widget
                # Se clicou no botão do seletor ou no menu, não fecha
                if (widget == self.current_lang_display or 
                    widget == self.lang_menu or 
                    widget in self.lang_menu.winfo_children()):
                    return
            
            self.lang_menu.place_forget()
            self.lang_menu_visible = False

    def select_language(self, lang_code):
        """Seleciona um idioma"""
        if translator.set_language(lang_code):
            # Atualiza o botão com a nova bandeira
            flag_code = self.get_flag_code(lang_code)
            if hasattr(self, 'flag_images') and flag_code in self.flag_images:
                self.current_lang_display.config(
                    image=self.flag_images[flag_code],
                    text=lang_code.upper()
                )
            self.hide_language_menu()
            self.update_ui_texts()



    def update_ui_texts(self):
        """Atualiza todos os textos da interface"""
        # Título da janela
        self.root.title(translator.get('window_title'))
        
        # Atualiza seletor de idioma customizado
        if hasattr(self, 'current_lang_display') and hasattr(self, 'flag_images'):
            flag_code = self.get_flag_code(translator.current_language)
            if flag_code in self.flag_images:
                self.current_lang_display.config(
                    image=self.flag_images[flag_code],
                    text=f" {translator.current_language.upper()}"
                )
        
        # Cabeçalho
        if hasattr(self, 'title_label'):
            self.title_label.config(text=translator.get('window_title'))
        if hasattr(self, 'subtitle_label'):
            self.subtitle_label.config(text=translator.get('window_subtitle'))
        
        # Títulos das seções
        if hasattr(self, 'url_section_title'):
            self.url_section_title.config(text=translator.get('url_section'))
        if hasattr(self, 'config_section_title'):
            self.config_section_title.config(text=translator.get('config_section'))
        if hasattr(self, 'progress_section_title'):
            self.progress_section_title.config(text=translator.get('progress_section'))
        if hasattr(self, 'log_section_title'):
            self.log_section_title.config(text=translator.get('log_section'))
        
        # Labels das seções
        if hasattr(self, 'country_label'):
            self.country_label.config(text=translator.get('country_label'))
        if hasattr(self, 'language_label'):
            self.language_label.config(text=translator.get('language_label'))
        if hasattr(self, 'folder_text_label'):
            self.folder_text_label.config(text=translator.get('folder_label'))
        
        # Botões
        if hasattr(self, 'paste_btn'):
            self.paste_btn.config(text=translator.get('paste_button'))
        if hasattr(self, 'choose_btn'):
            self.choose_btn.config(text=translator.get('choose_button'))
        if hasattr(self, 'start_btn'):
            self.start_btn.config(text=translator.get('start_button'))
        if hasattr(self, 'stop_btn'):
            self.stop_btn.config(text=translator.get('stop_button'))
        if hasattr(self, 'clear_btn'):
            self.clear_btn.config(text=translator.get('clear_button'))
        
        # Placeholder da URL
        self.setup_placeholder()
        
        # Status
        if hasattr(self, 'status_label'):
            self.status_label.config(text=translator.get('ready_status'))
        
        if hasattr(self, 'status_var'):
            self.status_var.set(translator.get('ready_status_bar'))
        
        # Log inicial
        if hasattr(self, 'log_text'):
            self.log_text.delete(1.0, tk.END)
            self.log(translator.get('scraper_started'))
    
    def setup_styles(self):
        """Configura estilos básicos"""
        # Configuração mínima necessária
        self.root.configure(bg=self.colors['background'])

    def setup_icon(self):
        """Configura o ícone da aplicação"""
        try:
            # Primeiro tenta usar o arquivo .ico (melhor para Windows)
            ico_path = os.path.join("assets", "icons", "google-play.ico")
            if os.path.exists(ico_path):
                self.root.iconbitmap(ico_path)
                return
            
            # Fallback para PNG se .ico não existir
            png_path = os.path.join("assets", "icons", "google-play.png")
            if os.path.exists(png_path):
                try:
                    from PIL import Image, ImageTk
                    icon_image = Image.open(png_path)
                    icon_image = icon_image.resize((32, 32), Image.Resampling.LANCZOS)
                    self.icon_photo = ImageTk.PhotoImage(icon_image)
                    self.root.iconphoto(True, self.icon_photo)
                except ImportError:
                    self.icon_photo = tk.PhotoImage(file=png_path)
                    self.root.iconphoto(True, self.icon_photo)
        except Exception as e:
            print(f"Erro ao carregar ícone: {e}")

    def setup_taskbar_icon(self):
        """Configura o ícone na barra de tarefas do Windows"""
        # Agenda para executar após a janela estar totalmente carregada
        self.root.after(100, self._apply_taskbar_icon)
    
    def _apply_taskbar_icon(self):
        """Aplica o ícone na barra de tarefas (executado após delay)"""
        try:
            import ctypes
            import sys
            
            # Define o App User Model ID para que o Windows trate como aplicação separada
            try:
                ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("GooglePlayReviewScraper.1.0")
            except:
                pass
            
            # Aguarda a janela estar visível
            self.root.update()
            
            # Obtém o handle da janela
            hwnd = self.root.winfo_id()
            
            # Carrega o ícone do arquivo .ico
            ico_path = os.path.join("assets", "icons", "google-play.ico")
            if os.path.exists(ico_path):
                ico_path = os.path.abspath(ico_path)
                
                # Constantes do Windows
                IMAGE_ICON = 1
                LR_LOADFROMFILE = 0x00000010
                LR_DEFAULTSIZE = 0x00000040
                WM_SETICON = 0x0080
                ICON_SMALL = 0
                ICON_BIG = 1
                
                # Carrega o ícone pequeno (16x16)
                hicon_small = ctypes.windll.user32.LoadImageW(
                    None, ico_path, IMAGE_ICON, 16, 16, LR_LOADFROMFILE
                )
                
                # Carrega o ícone grande (32x32)
                hicon_large = ctypes.windll.user32.LoadImageW(
                    None, ico_path, IMAGE_ICON, 32, 32, LR_LOADFROMFILE
                )
                
                # Define os ícones na janela
                if hicon_small:
                    ctypes.windll.user32.SendMessageW(hwnd, WM_SETICON, ICON_SMALL, hicon_small)
                if hicon_large:
                    ctypes.windll.user32.SendMessageW(hwnd, WM_SETICON, ICON_BIG, hicon_large)
                
                # Força atualização da barra de tarefas
                try:
                    # Força refresh da janela
                    ctypes.windll.user32.RedrawWindow(hwnd, None, None, 0x0001 | 0x0004)
                    
                    # Agenda uma segunda tentativa se necessário
                    self.root.after(500, self._force_icon_update)
                except:
                    pass
                    
        except Exception as e:
            print(f"Erro ao configurar ícone da barra de tarefas: {e}")
    
    def _force_icon_update(self):
        """Força uma segunda atualização do ícone"""
        try:
            import ctypes
            hwnd = self.root.winfo_id()
            
            # Segunda tentativa de aplicar o ícone
            ico_path = os.path.join("assets", "icons", "google-play.ico")
            if os.path.exists(ico_path):
                ico_path = os.path.abspath(ico_path)
                
                hicon = ctypes.windll.user32.LoadImageW(
                    None, ico_path, 1, 32, 32, 0x00000010
                )
                
                if hicon:
                    ctypes.windll.user32.SendMessageW(hwnd, 0x0080, 1, hicon)
                    
        except Exception:
            pass

    def create_interface(self):
        """Cria a interface principal"""
        self.setup_styles()
        
        # Container principal com scrollbar
        self.create_scrollable_frame()
        
        # Componentes
        self.create_header(self.scrollable_frame)
        self.create_url_section(self.scrollable_frame)
        self.create_config_section(self.scrollable_frame)
        self.create_progress_section(self.scrollable_frame)
        self.create_main_action_button(self.scrollable_frame)
        self.create_log_section(self.scrollable_frame)
        self.create_status_bar()

    def create_scrollable_frame(self):
        """Cria um frame com barra de rolagem"""
        # Container principal
        main_container = tk.Frame(self.root, bg=self.colors['background'])
        main_container.pack(fill=tk.BOTH, expand=True)
        
        # Canvas para scroll
        self.canvas = tk.Canvas(main_container, bg=self.colors['background'], 
                               highlightthickness=0, bd=0)
        
        # Scrollbar vertical (estilizada)
        scrollbar = tk.Scrollbar(main_container, orient="vertical", command=self.canvas.yview,
                               bg=self.colors['background'], troughcolor=self.colors['divider'],
                               activebackground=self.colors['primary'])
        
        # Frame scrollável dentro do canvas
        self.scrollable_frame = tk.Frame(self.canvas, bg=self.colors['background'])
        
        # Configura o scroll
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        # Cria janela no canvas
        self.canvas_window = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        
        # Configura o canvas
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        # Pack dos elementos
        self.canvas.pack(side="left", fill="both", expand=True, padx=20, pady=20)
        scrollbar.pack(side="right", fill="y")
        
        # Bind para redimensionamento
        self.canvas.bind('<Configure>', self.on_canvas_configure)
        
        # Bind para scroll com mouse wheel
        self.bind_mousewheel()

    def on_canvas_configure(self, event):
        """Ajusta o tamanho do frame interno quando o canvas é redimensionado"""
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_window, width=canvas_width)

    def bind_mousewheel(self):
        """Configura scroll com roda do mouse"""
        def _on_mousewheel(event):
            self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        def bind_to_mousewheel(event):
            self.canvas.bind_all("<MouseWheel>", _on_mousewheel)
        
        def unbind_from_mousewheel(event):
            self.canvas.unbind_all("<MouseWheel>")
        
        # Bind quando mouse entra na janela
        self.root.bind('<Enter>', bind_to_mousewheel)
        self.root.bind('<Leave>', unbind_from_mousewheel)
        
        # Suporte para scroll com teclado
        def on_key_press(event):
            if event.keysym == 'Up':
                self.canvas.yview_scroll(-1, "units")
            elif event.keysym == 'Down':
                self.canvas.yview_scroll(1, "units")
            elif event.keysym == 'Page_Up':
                self.canvas.yview_scroll(-1, "pages")
            elif event.keysym == 'Page_Down':
                self.canvas.yview_scroll(1, "pages")
            elif event.keysym == 'Home':
                self.canvas.yview_moveto(0)
            elif event.keysym == 'End':
                self.canvas.yview_moveto(1)
        
        self.root.bind('<Key>', on_key_press)
        self.root.focus_set()

    def create_header(self, parent):
        """Cria o cabeçalho moderno com ícone do Google Play"""
        header = tk.Frame(parent, bg=self.colors['background'])
        header.pack(fill=tk.X, pady=(0, 30))
        
        # Container principal do header
        header_container = tk.Frame(header, bg=self.colors['background'])
        header_container.pack(fill=tk.X)
        
        # Container para ícone e título (lado esquerdo)
        title_container = tk.Frame(header_container, bg=self.colors['background'])
        title_container.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        # Ícone do Google Play (se disponível)
        try:
            icon_path = os.path.join("assets", "icons", "google-play.png")
            if os.path.exists(icon_path):
                icon_img = tk.PhotoImage(file=icon_path)
                # Redimensiona para 48x48
                icon_img = icon_img.subsample(2, 2)  # Ajuste conforme necessário
                icon_label = tk.Label(title_container, image=icon_img, bg=self.colors['background'])
                icon_label.image = icon_img  # Mantém referência
                icon_label.pack(side=tk.LEFT, padx=(0, 15))
        except:
            pass
        
        # Container para textos do título
        text_container = tk.Frame(title_container, bg=self.colors['background'])
        text_container.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        # Título principal
        self.title_label = tk.Label(text_container, text="Google Play Reviews Scraper",
                font=('Segoe UI', 24, 'bold'), fg=self.colors['on_background'],
                bg=self.colors['background'])
        self.title_label.pack(anchor=tk.W)
        
        # Subtítulo
        self.subtitle_label = tk.Label(text_container, text="Coleta reviews de apps do Google Play Store",
                font=('Segoe UI', 12), fg=self.colors['disabled'],
                bg=self.colors['background'])
        self.subtitle_label.pack(anchor=tk.W, pady=(2, 0))
        
        # Container para controles do canto superior direito
        controls_frame = tk.Frame(header_container, bg=self.colors['background'])
        controls_frame.pack(side=tk.RIGHT, anchor=tk.NE, padx=(10, 0))
        
        # Botão de configurações (ícone de engrenagem)
        settings_btn = tk.Button(controls_frame, text="⚙", font=('Segoe UI', 16),
                               bg=self.colors['surface'], fg=self.colors['disabled'], 
                               relief='flat', bd=0, width=3, height=1, cursor='hand2',
                               command=self.show_about)
        settings_btn.pack()
        
        # Hover effect para o botão de configurações
        def on_enter(e):
            settings_btn.config(fg=self.colors['on_surface'], bg=self.colors['surface_light'])
        def on_leave(e):
            settings_btn.config(fg=self.colors['disabled'], bg=self.colors['surface'])
        settings_btn.bind("<Enter>", on_enter)
        settings_btn.bind("<Leave>", on_leave)
        
    def create_url_section(self, parent):
        """Cria a seção de URLs com design moderno"""
        # Card principal com sombra simulada
        shadow_frame = tk.Frame(parent, bg=self.colors['border'], relief='flat', bd=0)
        shadow_frame.pack(fill=tk.X, pady=(0, 20), padx=20)
        
        card = tk.Frame(shadow_frame, bg=self.colors['surface'], relief='flat', bd=0)
        card.pack(fill=tk.X, padx=1, pady=1)
        
        # Padding interno
        section = tk.Frame(card, bg=self.colors['surface'])
        section.pack(fill=tk.X, padx=20, pady=20)
        
        # Título da seção
        self.url_section_title = tk.Label(section, text="Adicionar Apps",
                                         font=('Segoe UI', 16, 'bold'), 
                                         fg=self.colors['on_surface'],
                                         bg=self.colors['surface'])
        self.url_section_title.pack(anchor=tk.W, pady=(0, 15))
        
        # Campo de entrada com design moderno
        input_container = tk.Frame(section, bg=self.colors['surface'])
        input_container.pack(fill=tk.X, pady=(0, 15))
        
        # Entry com bordas arredondadas e tema claro
        entry_frame = tk.Frame(input_container, bg=self.colors['input_border'], relief='flat', bd=0)
        entry_frame.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        
        entry_inner = tk.Frame(entry_frame, bg=self.colors['surface'], relief='flat', bd=0)
        entry_inner.pack(fill=tk.X, padx=1, pady=1)
        
        self.url_entry = tk.Entry(entry_inner, font=('Segoe UI', 12),
                                 bg=self.colors['surface'], fg=self.colors['on_surface'],
                                 relief='flat', bd=0, insertbackground=self.colors['primary'])
        self.url_entry.pack(fill=tk.X, padx=15, pady=10)
        
        # Container para botões
        buttons_container = tk.Frame(input_container, bg=self.colors['surface'])
        buttons_container.pack(side=tk.RIGHT, padx=(10, 0))
        
        # Botão Colar arredondado com cor contrastante
        paste_btn_container = self.create_rounded_button(buttons_container, "Colar", 
                                                        self.paste_url, self.colors['btn_pink'], 
                                                        width=70, height=35)
        paste_btn_container.pack(side=tk.LEFT, padx=(0, 8))
        
        # Botão Adicionar arredondado com cor contrastante
        add_btn_container = self.create_rounded_button(buttons_container, "Adicionar", 
                                                      self.add_url, self.colors['btn_blue'], 
                                                      width=90, height=35)
        add_btn_container.pack(side=tk.LEFT)
        
        # Seção Apps na fila
        queue_section = tk.Frame(section, bg=self.colors['surface'])
        queue_section.pack(fill=tk.X, pady=(15, 0))
        
        # Título Apps na fila
        queue_title = tk.Label(queue_section, text="Apps na fila",
                              font=('Segoe UI', 14, 'bold'),
                              fg=self.colors['on_surface'],
                              bg=self.colors['surface'])
        queue_title.pack(anchor=tk.W, pady=(0, 10))
        
        # Container da lista com bordas arredondadas para tema claro
        list_outer = tk.Frame(queue_section, bg=self.colors['input_border'], relief='flat', bd=0)
        list_outer.pack(fill=tk.X, pady=(0, 15))
        
        list_container = tk.Frame(list_outer, bg=self.colors['input_bg'], 
                                 relief='flat', bd=0, height=120)
        list_container.pack(fill=tk.X, padx=1, pady=1)
        list_container.pack_propagate(False)
        
        # Canvas para scroll
        self.list_canvas = tk.Canvas(list_container, bg=self.colors['background'],
                                    highlightthickness=0, bd=0)
        self.list_scrollbar = tk.Scrollbar(list_container, orient="vertical", 
                                          command=self.list_canvas.yview,
                                          bg=self.colors['surface'])
        self.list_canvas.configure(yscrollcommand=self.list_scrollbar.set)
        
        # Frame scrollável
        self.list_scrollable_frame = tk.Frame(self.list_canvas, bg=self.colors['background'])
        self.list_canvas.create_window((0, 0), window=self.list_scrollable_frame, anchor="nw")
        
        self.list_canvas.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        self.list_scrollbar.pack(side="right", fill="y")
        
        # Bind para scroll
        self.list_scrollable_frame.bind("<Configure>", 
                                       lambda e: self.list_canvas.configure(scrollregion=self.list_canvas.bbox("all")))
        
        # Botão Limpar Todos arredondado com cor contrastante
        clear_btn_container = self.create_rounded_button(queue_section, "Limpar Todos", 
                                                        self.clear_all_urls, self.colors['btn_red'], 
                                                        width=120, height=32)
        clear_btn_container.pack(anchor=tk.W, pady=(5, 0))
        
        # Status da lista
        self.urls_status_label = tk.Label(queue_section, text="Nenhum app adicionado",
                                         font=('Segoe UI', 10), fg=self.colors['disabled'],
                                         bg=self.colors['surface'])
        self.urls_status_label.pack(anchor=tk.W, pady=(8, 0))
        
        # Lista para armazenar URLs
        self.urls_list = []
        
        self.setup_placeholder()
        
    def create_config_section(self, parent):
        """Cria a seção de configurações com design moderno"""
        # Card principal com sombra simulada
        shadow_frame = tk.Frame(parent, bg=self.colors['border'], relief='flat', bd=0)
        shadow_frame.pack(fill=tk.X, pady=(0, 20), padx=20)
        
        card = tk.Frame(shadow_frame, bg=self.colors['surface'], relief='flat', bd=0)
        card.pack(fill=tk.X, padx=1, pady=1)
        
        # Padding interno
        section = tk.Frame(card, bg=self.colors['surface'])
        section.pack(fill=tk.X, padx=20, pady=20)
        
        # Título da seção
        self.config_section_title = tk.Label(section, text="Configurações",
                                            font=('Segoe UI', 16, 'bold'),
                                            fg=self.colors['on_surface'],
                                            bg=self.colors['surface'])
        self.config_section_title.pack(anchor=tk.W, pady=(0, 15))
        
        # Container para País e Idioma
        config_row = tk.Frame(section, bg=self.colors['surface'])
        config_row.pack(fill=tk.X, pady=(0, 15))
        
        # País
        country_container = tk.Frame(config_row, bg=self.colors['surface'])
        country_container.pack(side=tk.LEFT, padx=(0, 30))
        
        self.country_label = tk.Label(country_container, text="País:",
                                     font=('Segoe UI', 12, 'bold'),
                                     fg=self.colors['on_surface'],
                                     bg=self.colors['surface'])
        self.country_label.pack(anchor=tk.W)
        
        from tkinter import ttk
        # Estilo customizado para combobox
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Custom.TCombobox',
                       fieldbackground=self.colors['input_bg'],
                       background=self.colors['input_bg'],
                       foreground=self.colors['on_surface'],
                       borderwidth=0,
                       relief='flat')
        
        country_combo = ttk.Combobox(country_container, textvariable=self.country_var,
                                   values=["br", "us", "uk", "ca", "au", "de", "fr", "es", "it"],
                                   width=6, state="readonly", style='Custom.TCombobox')
        country_combo.pack(pady=(5, 0))
        
        # Idioma
        lang_container = tk.Frame(config_row, bg=self.colors['surface'])
        lang_container.pack(side=tk.LEFT)
        
        self.language_label = tk.Label(lang_container, text="Idioma:",
                                      font=('Segoe UI', 12, 'bold'),
                                      fg=self.colors['on_surface'],
                                      bg=self.colors['surface'])
        self.language_label.pack(anchor=tk.W)
        
        lang_combo = ttk.Combobox(lang_container, textvariable=self.lang_var,
                                values=["pt", "en", "es", "fr", "de", "it"],
                                width=6, state="readonly", style='Custom.TCombobox')
        lang_combo.pack(pady=(5, 0))
        
        # Pasta de destino
        folder_container = tk.Frame(section, bg=self.colors['surface'])
        folder_container.pack(fill=tk.X)
        
        # Label da pasta
        folder_label_text = tk.Label(folder_container, text="Pasta de destino:",
                                    font=('Segoe UI', 12, 'bold'),
                                    fg=self.colors['on_surface'],
                                    bg=self.colors['surface'])
        folder_label_text.pack(anchor=tk.W, pady=(0, 5))
        
        # Container para caminho e botão
        folder_row = tk.Frame(folder_container, bg=self.colors['surface'])
        folder_row.pack(fill=tk.X)
        
        # Caminho da pasta (clicável)
        self.folder_label = tk.Label(folder_row, text=self.output_dir_var.get(),
                                   font=('Segoe UI', 10), fg=self.colors['info'],
                                   bg=self.colors['surface'], cursor='hand2',
                                   anchor='w', justify='left')
        self.folder_label.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.folder_label.bind("<Button-1>", lambda e: self.open_folder())
        
        # Botão Escolher arredondado com cor contrastante
        choose_btn_container = self.create_rounded_button(folder_row, "Escolher", 
                                                         self.choose_folder, self.colors['btn_cyan'], 
                                                         width=100, height=32)
        choose_btn_container.pack(side=tk.RIGHT)
        
    def create_progress_section(self, parent):
        """Cria a seção de progresso com design moderno"""
        # Card principal com sombra simulada
        shadow_frame = tk.Frame(parent, bg=self.colors['border'], relief='flat', bd=0)
        shadow_frame.pack(fill=tk.X, pady=(0, 20), padx=20)
        
        card = tk.Frame(shadow_frame, bg=self.colors['surface'], relief='flat', bd=0)
        card.pack(fill=tk.X, padx=1, pady=1)
        
        # Padding interno
        section = tk.Frame(card, bg=self.colors['surface'])
        section.pack(fill=tk.X, padx=20, pady=20)
        
        # Título da seção
        self.progress_section_title = tk.Label(section, text="Progresso",
                                             font=('Segoe UI', 16, 'bold'),
                                             fg=self.colors['on_surface'],
                                             bg=self.colors['surface'])
        self.progress_section_title.pack(anchor=tk.W, pady=(0, 15))
        
        # Status atual
        self.status_label = tk.Label(section, text="Pronto para iniciar",
                                   font=('Segoe UI', 12),
                                   fg=self.colors['disabled'],
                                   bg=self.colors['surface'])
        self.status_label.pack(anchor=tk.W, pady=(0, 10))
        
        # Container para botões de resultado
        self.result_buttons_frame = tk.Frame(section, bg=self.colors['surface'])
        self.result_buttons_frame.pack(fill=tk.X, pady=(10, 0))
        
        # Botões de resultado arredondados com cores contrastantes
        self.csv_btn_container = self.create_rounded_button(self.result_buttons_frame, "CSV", 
                                                           self.open_csv_files, self.colors['btn_green'], 
                                                           width=80, height=35)
        self.csv_btn_container.pack(side=tk.LEFT, padx=(0, 10))
        
        self.json_btn_container = self.create_rounded_button(self.result_buttons_frame, "JSON", 
                                                            self.open_json_files, self.colors['btn_blue'], 
                                                            width=80, height=35)
        self.json_btn_container.pack(side=tk.LEFT, padx=(0, 10))
        
        self.folder_btn_container = self.create_rounded_button(self.result_buttons_frame, "Pasta", 
                                                              self.open_folder, self.colors['btn_orange'], 
                                                              width=80, height=35)
        self.folder_btn_container.pack(side=tk.LEFT)
        
        # Barra de progresso simples (mantida para compatibilidade)
        self.progress_var = tk.DoubleVar()
        progress_bg = tk.Frame(section, bg=self.colors['divider'], height=6)
        progress_bg.pack(fill=tk.X, pady=(15, 0))
        
        self.progress_canvas = tk.Canvas(progress_bg, height=6, bg=self.colors['divider'], 
                                        highlightthickness=0, bd=0)
        self.progress_canvas.pack(fill=tk.X)
        self.progress_bar_id = self.progress_canvas.create_rectangle(0, 0, 0, 6, 
                                                                    fill=self.colors['primary'], outline="")
    
    def create_main_action_button(self, parent):
        """Cria o botão principal grande com gradiente"""
        # Container para o botão principal
        button_container = tk.Frame(parent, bg=self.colors['background'])
        button_container.pack(fill=tk.X, pady=30, padx=20)
        
        # Botão principal grande arredondado com gradiente
        self.main_start_btn_container = self.create_main_gradient_button(button_container, 
                                                                        "Pronto para iniciar", 
                                                                        self.start_scraping)
        self.main_start_btn_container.pack(fill=tk.X, pady=(0, 10))

        
    def create_log_section(self, parent):
        """Cria a seção de log com design moderno (oculta por padrão)"""
        # Card principal (inicialmente oculto)
        self.log_card = tk.Frame(parent, bg=self.colors['surface'], relief='flat', bd=0)
        
        # Padding interno
        section = tk.Frame(self.log_card, bg=self.colors['surface'])
        section.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Cabeçalho com título e botão de toggle
        header = tk.Frame(section, bg=self.colors['surface'])
        header.pack(fill=tk.X, pady=(0, 10))
        
        self.log_section_title = tk.Label(header, text="Log de Atividades",
                                         font=('Segoe UI', 16, 'bold'),
                                         fg=self.colors['on_surface'],
                                         bg=self.colors['surface'])
        self.log_section_title.pack(side=tk.LEFT)
        
        # Botão para mostrar/ocultar log
        self.toggle_log_btn = tk.Button(header, text="▼ Mostrar",
                                       font=('Segoe UI', 10),
                                       bg=self.colors['surface'], fg=self.colors['disabled'],
                                       relief='flat', bd=0, cursor='hand2',
                                       command=self.toggle_log_visibility)
        self.toggle_log_btn.pack(side=tk.RIGHT)
        
        # Container do log (inicialmente oculto)
        self.log_container = tk.Frame(section, bg=self.colors['surface'])
        
        # Text com scrollbar
        log_frame = tk.Frame(self.log_container, bg=self.colors['surface'])
        log_frame.pack(fill=tk.BOTH, expand=True)
        
        scrollbar = tk.Scrollbar(log_frame, bg=self.colors['surface'])
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.log_text = tk.Text(log_frame, wrap=tk.WORD, font=('Consolas', 10),
                               bg=self.colors['background'], fg=self.colors['on_background'],
                               relief='flat', bd=0, padx=15, pady=15, height=8,
                               yscrollcommand=scrollbar.set, insertbackground=self.colors['on_background'])
        self.log_text.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.log_text.yview)
        
        # Estado inicial: log oculto
        self.log_visible = False
        
        # Log inicial
        self.log("Sistema iniciado - Pronto para coletar reviews!")
    
    def toggle_log_visibility(self):
        """Mostra/oculta a seção de log"""
        if self.log_visible:
            # Ocultar log
            self.log_container.pack_forget()
            self.log_card.pack_forget()
            self.toggle_log_btn.config(text="▼ Mostrar Log")
            self.log_visible = False
        else:
            # Mostrar log
            self.log_card.pack(fill=tk.X, pady=(0, 20), padx=20)
            self.log_container.pack(fill=tk.BOTH, expand=True, pady=(10, 0))
            self.toggle_log_btn.config(text="▲ Ocultar Log")
            self.log_visible = True

    def create_status_bar(self):
        """Cria a barra de status moderna"""
        status_frame = tk.Frame(self.root, bg=self.colors['surface'], height=30)
        status_frame.pack(side=tk.BOTTOM, fill=tk.X)
        status_frame.pack_propagate(False)
        
        self.status_var = tk.StringVar(value="Pronto para iniciar")
        status_label = tk.Label(status_frame, textvariable=self.status_var, anchor=tk.W,
                               font=('Segoe UI', 10), bg=self.colors['surface'],
                               fg=self.colors['disabled'], padx=20, pady=8)
        status_label.pack(side=tk.LEFT, fill=tk.X, expand=True)

    def create_card(self, parent, title, expand=False):
        """Cria um card simples"""
        container = tk.Frame(parent, bg=self.colors['background'])
        if expand:
            container.pack(fill=tk.BOTH, expand=True, pady=(0, 15))
        else:
            container.pack(fill=tk.X, pady=(0, 15))
        
        title_label = tk.Label(container, text=title, font=('Segoe UI', 11, 'bold'),
                fg=self.colors['on_background'], bg=self.colors['background'])
        title_label.pack(anchor=tk.W, pady=(0, 8))
        
        card = tk.Frame(container, bg=self.colors['surface'], relief='solid', bd=1)
        if expand:
            card.pack(fill=tk.BOTH, expand=True)
        else:
            card.pack(fill=tk.X)
        
        inner = tk.Frame(card, bg=self.colors['surface'])
        if expand:
            inner.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        else:
            inner.pack(fill=tk.X, padx=15, pady=15)
        
        return inner, title_label
    
    def create_rounded_button(self, parent, text, command, bg_color, width=120, height=35, font_size=11, text_color='white'):
        """Cria um botão estilizado com aparência arredondada usando frames aninhados"""
        # Container principal com padding para simular bordas arredondadas
        btn_outer = tk.Frame(parent, bg=self.colors['border'], relief='flat', bd=0)
        
        # Frame interno com a cor do botão
        btn_inner = tk.Frame(btn_outer, bg=bg_color, relief='flat', bd=0)
        btn_inner.pack(padx=1, pady=1, fill=tk.BOTH, expand=True)
        
        # Botão real dentro do frame interno
        btn = tk.Button(btn_inner, text=text, command=command,
                       bg=bg_color, fg=text_color,
                       font=('Segoe UI', font_size, 'bold'),
                       relief='flat', bd=0, cursor='hand2',
                       activebackground=self.lighten_color(bg_color),
                       activeforeground=text_color)
        
        # Calcula padding baseado no tamanho desejado
        pad_x = max(1, (width - len(text) * font_size) // 4)
        pad_y = max(1, (height - font_size) // 4)
        
        btn.pack(padx=pad_x, pady=pad_y, fill=tk.BOTH, expand=True)
        
        # Hover effects mais suaves
        hover_color = self.lighten_color(bg_color)
        
        def on_enter(event):
            btn.config(bg=hover_color)
            btn_inner.config(bg=hover_color)
        
        def on_leave(event):
            btn.config(bg=bg_color)
            btn_inner.config(bg=bg_color)
        
        # Bind eventos para hover
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        btn_inner.bind("<Enter>", on_enter)
        btn_inner.bind("<Leave>", on_leave)
        
        # Configura tamanho mínimo
        btn_outer.config(width=width, height=height)
        btn_outer.pack_propagate(False)
        
        return btn_outer
    
    def lighten_color(self, color):
        """Clareia uma cor para hover effect no tema claro"""
        color_map = {
            # Cores principais
            self.colors['primary']: '#6366F1',      # Azul mais claro
            self.colors['secondary']: '#8B5CF6',    # Roxo mais claro
            self.colors['accent']: '#F472B6',       # Rosa mais claro
            self.colors['error']: '#EF4444',        # Vermelho mais claro
            self.colors['warning']: '#F59E0B',      # Laranja mais claro
            self.colors['info']: '#06B6D4',         # Ciano mais claro
            self.colors['success']: '#10B981',      # Verde mais claro
            
            # Cores específicas dos botões
            self.colors['btn_blue']: '#3B82F6',     # Azul hover
            self.colors['btn_purple']: '#A855F7',   # Roxo hover
            self.colors['btn_pink']: '#EC4899',     # Rosa hover
            self.colors['btn_red']: '#EF4444',      # Vermelho hover
            self.colors['btn_orange']: '#F97316',   # Laranja hover
            self.colors['btn_cyan']: '#06B6D4',     # Ciano hover
            self.colors['btn_green']: '#22C55E',    # Verde hover
            self.colors['btn_indigo']: '#6366F1',   # Índigo hover
        }
        return color_map.get(color, color)
    
    def create_main_gradient_button(self, parent, text, command):
        """Cria o botão principal com gradiente simulado usando frames"""
        # Container principal
        btn_container = tk.Frame(parent, bg=parent['bg'])
        
        # Frame externo para sombra
        shadow_frame = tk.Frame(btn_container, bg=self.colors['border'], relief='flat', bd=0)
        shadow_frame.pack(fill=tk.X, padx=2, pady=2)
        
        # Frame do gradiente (simula com cor intermediária)
        gradient_color = self.colors['btn_indigo']  # Cor principal
        gradient_frame = tk.Frame(shadow_frame, bg=gradient_color, relief='flat', bd=0)
        gradient_frame.pack(fill=tk.X, padx=1, pady=1)
        
        # Botão principal
        main_btn = tk.Button(gradient_frame, text=text, command=command,
                           bg=gradient_color, fg='white',
                           font=('Segoe UI', 16, 'bold'),
                           relief='flat', bd=0, cursor='hand2',
                           activebackground=self.colors['btn_purple'],
                           activeforeground='white')
        main_btn.pack(fill=tk.X, padx=8, pady=12)
        
        # Hover effects
        def on_enter(event):
            hover_color = self.colors['btn_purple']
            main_btn.config(bg=hover_color)
            gradient_frame.config(bg=hover_color)
        
        def on_leave(event):
            main_btn.config(bg=gradient_color)
            gradient_frame.config(bg=gradient_color)
        
        # Bind eventos
        main_btn.bind("<Enter>", on_enter)
        main_btn.bind("<Leave>", on_leave)
        gradient_frame.bind("<Enter>", on_enter)
        gradient_frame.bind("<Leave>", on_leave)
        
        # Salva referência para poder alterar o texto depois
        self.main_button = main_btn
        self.main_button_text = text
        
        return btn_container
    
    def create_button(self, parent, text, command, bg, primary=False, state=tk.NORMAL):
        """Cria um botão padronizado com bordas arredondadas"""
        # Usa o novo método de botão arredondado
        if primary:
            return self.create_rounded_button(parent, text, command, bg, width=150, height=40, font_size=12)
        else:
            return self.create_rounded_button(parent, text, command, bg, width=100, height=32, font_size=10)
    
    def darken_color(self, color):
        """Escurece uma cor para hover effect"""
        color_map = {
            self.colors['primary']: '#1565C0',      # Azul mais escuro
            self.colors['secondary']: '#1B5E20',    # Verde mais escuro
            self.colors['error']: '#B71C1C',        # Vermelho mais escuro
            self.colors['warning']: '#BF360C',      # Laranja mais escuro
            self.colors['info']: '#01579B',         # Azul claro mais escuro
            self.colors['disabled']: '#616161'      # Cinza mais escuro
        }
        return color_map.get(color, color)

    def setup_placeholder(self):
        """Configura placeholder para URL única"""
        placeholder = "Cole a URL do app do Google Play Store..."
        
        def on_focus_in(e):
            if self.url_entry.get() == placeholder:
                self.url_entry.delete(0, tk.END)
                self.url_entry.config(fg=self.colors['on_surface'])
        
        def on_focus_out(e):
            if not self.url_entry.get():
                self.url_entry.insert(0, placeholder)
                self.url_entry.config(fg=self.colors['disabled'])
        
        self.url_entry.insert(0, placeholder)
        self.url_entry.config(fg=self.colors['disabled'])
        self.url_entry.bind('<FocusIn>', on_focus_in)
        self.url_entry.bind('<FocusOut>', on_focus_out)
        
        # Bind Enter para adicionar URL
        self.url_entry.bind('<Return>', lambda e: self.add_url())

    def paste_url(self):
        """Cola URL da área de transferência"""
        try:
            clipboard_content = self.root.clipboard_get()
            placeholder = "Cole a URL do app do Google Play Store..."
            
            if self.url_entry.get() == placeholder:
                self.url_entry.delete(0, tk.END)
                self.url_entry.config(fg=self.colors['on_surface'])
            
            self.url_entry.delete(0, tk.END)
            self.url_entry.insert(0, clipboard_content.strip())
            self.url_entry.config(fg=self.colors['on_surface'])
            self.log(translator.get('url_pasted'))
        except tk.TclError:
            messagebox.showerror(translator.get('error_title'), translator.get('error_clipboard'))
    
    def add_url(self):
        """Adiciona URL à lista"""
        url = self.url_entry.get().strip()
        placeholder = "Cole a URL do app do Google Play Store..."
        
        if not url or url == placeholder:
            messagebox.showwarning("Aviso", "Por favor, insira uma URL")
            return
        
        if 'play.google.com/store/apps/details' not in url:
            messagebox.showerror("Erro", "URL deve ser do Google Play Store")
            return
        
        try:
            # Extrai app_id
            app_id = self.scraper.extract_app_id_from_url(url)
            
            # Verifica se já existe
            for existing in self.urls_list:
                if existing['app_id'] == app_id:
                    messagebox.showwarning("Aviso", f"App {app_id} já está na lista")
                    return
            
            # Adiciona à lista
            self.urls_list.append({'url': url, 'app_id': app_id})
            
            # Limpa campo de entrada
            self.url_entry.delete(0, tk.END)
            self.setup_placeholder()
            
            # Atualiza lista visual
            self.update_urls_list()
            self.log(f"App adicionado: {app_id}")
            
        except Exception as e:
            messagebox.showerror("Erro", f"URL inválida: {str(e)}")
    
    def remove_url(self, app_id):
        """Remove URL da lista"""
        self.urls_list = [item for item in self.urls_list if item['app_id'] != app_id]
        self.update_urls_list()
        self.log(f"App removido: {app_id}")
    
    def clear_all_urls(self):
        """Limpa toda a lista"""
        if not self.urls_list:
            return
        
        if messagebox.askyesno("Confirmar", "Deseja remover todos os apps da lista?"):
            self.urls_list = []
            self.update_urls_list()
            self.log("Lista de apps limpa")
    
    def update_urls_list(self):
        """Atualiza a lista visual de URLs"""
        # Limpa lista atual
        for widget in self.list_scrollable_frame.winfo_children():
            widget.destroy()
        
        if not self.urls_list:
            # Mostra mensagem vazia para tema claro
            empty_label = tk.Label(self.list_scrollable_frame, text="Nenhum app adicionado ainda",
                                  font=('Segoe UI', 11), fg=self.colors['disabled'],
                                  bg=self.colors['input_bg'])
            empty_label.pack(pady=30)
            # Atualiza status
            self.urls_status_label.config(text="Nenhum app adicionado", fg=self.colors['disabled'])
        else:
            # Mostra lista de apps com design claro
            for i, url_data in enumerate(self.urls_list):
                app_id = url_data['app_id']
                
                # Frame do item com bordas suaves
                item_outer = tk.Frame(self.list_scrollable_frame, bg=self.colors['border'])
                item_outer.pack(fill=tk.X, padx=8, pady=3)
                
                item_frame = tk.Frame(item_outer, bg=self.colors['surface'])
                item_frame.pack(fill=tk.X, padx=1, pady=1)
                
                # Número e App ID
                info_label = tk.Label(item_frame, text=f"✓ {i+1}. {app_id}",
                                     font=('Segoe UI', 10), fg=self.colors['on_surface'],
                                     bg=self.colors['surface'])
                info_label.pack(side=tk.LEFT, padx=12, pady=8)
                
                # Botão remover arredondado com cor contrastante
                remove_btn_container = self.create_rounded_button(item_frame, "✕", 
                                                                lambda aid=app_id: self.remove_url(aid), 
                                                                self.colors['btn_red'], 
                                                                width=25, height=25, font_size=10)
                remove_btn_container.pack(side=tk.RIGHT, padx=8, pady=4)
            
            # Atualiza status
            count = len(self.urls_list)
            if count == 1:
                self.urls_status_label.config(text="1 app na fila", fg=self.colors['primary'])
            else:
                self.urls_status_label.config(text=f"{count} apps na fila", fg=self.colors['primary'])
        
        # Atualiza scroll region
        self.list_scrollable_frame.update_idletasks()
        self.list_canvas.configure(scrollregion=self.list_canvas.bbox("all"))

    def update_progress(self, value):
        """Atualiza barra de progresso"""
        self.progress_var.set(value)
        
        # Atualiza barra visual
        canvas_width = self.progress_canvas.winfo_width()
        if canvas_width > 1:
            progress_width = (value / 100) * canvas_width
            self.progress_canvas.coords(self.progress_bar_id, 0, 0, progress_width, 20)
    

    
    def choose_folder(self):
        """Escolhe pasta de destino"""
        folder = filedialog.askdirectory(initialdir=self.output_dir_var.get())
        if folder:
            self.output_dir_var.set(folder)
            self.folder_label.config(text=folder)
            self.log(f"Pasta alterada para: {folder}")
    
    def open_folder(self):
        """Abre a pasta de saída"""
        folder = self.output_dir_var.get()
        if os.path.exists(folder):
            try:
                os.startfile(folder)
            except AttributeError:
                import subprocess
                if os.name == 'posix':
                    subprocess.call(['open', folder])
                else:
                    subprocess.call(['xdg-open', folder])
    
    def start_scraping(self):
        """Inicia o scraping (suporta múltiplas URLs)"""
        # Verifica se há URLs na lista
        if not self.urls_list:
            messagebox.showerror("Erro", "Por favor, adicione pelo menos um app à lista")
            return
        
        # Atualiza interface
        self.is_running = True
        self.update_main_button_text("Processando...")
        self.disable_result_buttons()
        self.progress_var.set(0)
        self.update_progress(0)
        
        if len(self.urls_list) == 1:
            self.status_label.config(text="Iniciando coleta...")
        else:
            self.status_label.config(text=f"Iniciando coleta em lote ({len(self.urls_list)} apps)...")
        
        self.status_var.set("Executando...")
        
        # Limpa log
        self.log_text.delete(1.0, tk.END)
        
        # Cria scraper
        self.scraper = GooglePlayReviewScraper(
            country=self.country_var.get(),
            lang=self.lang_var.get()
        )
        
        # Inicia thread
        thread = threading.Thread(target=self.scraping_worker, daemon=True)
        thread.start()
    
    def scraping_worker(self):
        """Worker thread para scraping em lote"""
        total_reviews = 0
        processed_apps = 0
        
        try:
            total_apps = len(self.urls_list)
            output_dir = self.output_dir_var.get()
            
            for i, url_data in enumerate(self.urls_list, 1):
                if not self.is_running:
                    break
                
                url = url_data['url']
                app_id = url_data['app_id']
                
                # Atualiza status
                self.root.after(0, lambda i=i, total=total_apps, app=app_id: self.status_label.config(
                    text=f"App {i}/{total}: {app}"
                ))
                
                self.log(f"[{i}/{total_apps}] Processando: {app_id}")
                
                try:
                    # Extrai reviews
                    reviews_data, app_info = self.scraper.extract_all_reviews(app_id)
                    
                    if reviews_data:
                        # Muda para diretório de saída
                        original_dir = os.getcwd()
                        os.chdir(output_dir)
                        
                        try:
                            self.scraper.save_reviews(reviews_data, app_info)
                            total_reviews += len(reviews_data)
                            processed_apps += 1
                            
                            self.log(f"✅ {len(reviews_data)} reviews coletadas")
                        finally:
                            os.chdir(original_dir)
                    else:
                        self.log("⚠️ Nenhuma review encontrada")
                
                except Exception as e:
                    self.log(f"❌ Erro: {e}")
                
                # Atualiza progresso
                progress = (i / total_apps) * 100
                self.root.after(0, lambda p=progress: self.update_progress(p))
            
            # Finaliza processamento
            if self.is_running and total_reviews > 0:
                # Habilita botões de resultado
                self.root.after(0, self.enable_result_buttons)
                
                # Mostra modal de tempo economizado
                self.root.after(500, lambda: self.show_time_saved_modal(total_reviews))
                
                # Atualiza status final
                if processed_apps == 1:
                    final_status = f"Concluído: {total_reviews} reviews coletadas"
                else:
                    final_status = f"Concluído: {total_reviews} reviews de {processed_apps} apps"
                
                self.root.after(0, lambda: self.status_label.config(text=final_status))
                self.log(f"🎉 {final_status}")
            
        except Exception as e:
            self.log(f"❌ Erro geral: {e}")
        finally:
            self.root.after(0, self.reset_ui)
    
    def stop_scraping(self):
        """Para o scraping"""
        self.is_running = False
        self.log("Parando coleta...")
        self.status_label.config(text="Parando...")
    
    def reset_ui(self):
        """Reseta a interface"""
        self.is_running = False
        self.update_main_button_text("Pronto para iniciar")
        self.status_var.set("Pronto para iniciar")
    
    def enable_result_buttons(self):
        """Habilita botões de resultado"""
        # Como os botões são canvas, eles já estão sempre habilitados
        # Apenas mostra o frame se estiver oculto
        if hasattr(self, 'result_buttons_frame'):
            self.result_buttons_frame.pack(fill=tk.X, pady=(10, 0))
    
    def disable_result_buttons(self):
        """Desabilita botões de resultado"""
        # Para botões canvas, podemos ocultar temporariamente
        pass  # Os botões canvas não precisam ser desabilitados
    
    def update_main_button_text(self, text):
        """Atualiza o texto do botão principal"""
        if hasattr(self, 'main_button'):
            self.main_button.config(text=text)
    
    def show_statistics(self, reviews_data):
        """Mostra estatísticas"""
        if not reviews_data:
            return
        
        self.log(f"\nEstatísticas:")
        self.log(f"Total de reviews: {len(reviews_data)}")
        
        scores = [r['score'] for r in reviews_data if r['score']]
        if scores:
            avg_score = sum(scores) / len(scores)
            self.log(f"Rating médio: {avg_score:.2f}")
            
            for rating in range(1, 6):
                count = scores.count(rating)
                percentage = (count/len(scores))*100
                self.log(f"  {rating} estrelas: {count} ({percentage:.1f}%)")
    
    def open_file(self, filepath):
        """Abre um arquivo"""
        if filepath and os.path.exists(filepath):
            try:
                os.startfile(filepath)
            except AttributeError:
                import subprocess
                if os.name == 'posix':
                    subprocess.call(['open', filepath])
                else:
                    subprocess.call(['xdg-open', filepath])
        else:
            messagebox.showerror("Erro", "Arquivo não encontrado")
    
    def open_csv_files(self):
        """Abre pasta com arquivos CSV"""
        output_dir = self.output_dir_var.get()
        try:
            # Procura por arquivos CSV na pasta de saída
            csv_files = [f for f in os.listdir(output_dir) if f.endswith('.csv')]
            if csv_files:
                # Abre o primeiro arquivo CSV encontrado
                self.open_file(os.path.join(output_dir, csv_files[-1]))  # Último criado
            else:
                messagebox.showinfo("Info", "Nenhum arquivo CSV encontrado")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao abrir arquivo CSV: {e}")
    
    def open_json_files(self):
        """Abre pasta com arquivos JSON"""
        output_dir = self.output_dir_var.get()
        try:
            # Procura por arquivos JSON na pasta de saída
            json_files = [f for f in os.listdir(output_dir) if f.endswith('.json')]
            if json_files:
                # Abre o primeiro arquivo JSON encontrado
                self.open_file(os.path.join(output_dir, json_files[-1]))  # Último criado
            else:
                messagebox.showinfo("Info", "Nenhum arquivo JSON encontrado")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao abrir arquivo JSON: {e}")
    
    def clear_log(self):
        """Limpa o log"""
        self.log_text.delete(1.0, tk.END)
        self.log("Log limpo")

    def show_about(self):
        """Mostra a janela Sobre"""
        # Calcula posição central antes de criar a janela
        window_width = 650  # Máximo para alemão
        window_height = 570  # Reduzido após remover primeiro uso
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        
        # Cria a janela já na posição correta
        about_window = tk.Toplevel(self.root)
        about_window.title(translator.get('about_title'))
        about_window.geometry(f"{window_width}x{window_height}+{x}+{y}")
        about_window.resizable(False, False)
        about_window.configure(bg=self.colors['background'])
        
        # Configura propriedades da janela
        about_window.transient(self.root)
        about_window.grab_set()
        
        # Configura o ícone da janela
        try:
            ico_path = os.path.join("assets", "icons", "google-play.ico")
            if os.path.exists(ico_path):
                about_window.iconbitmap(ico_path)
        except:
            pass
        
        # Container principal
        main_frame = tk.Frame(about_window, bg=self.colors['background'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
        
        # Título centralizado
        tk.Label(main_frame, text=translator.get('window_title'),
                font=('Segoe UI', 16, 'bold'), fg=self.colors['on_background'],
                bg=self.colors['background']).pack(pady=(0, 15))
        
        # Descrição do projeto centralizada
        tk.Label(main_frame, text=translator.get('about_description'), font=('Segoe UI', 10),
                fg=self.colors['on_background'], bg=self.colors['background'],
                justify=tk.CENTER, wraplength=590).pack(pady=(0, 20))
        
        # Ferramenta externa centralizada
        tk.Label(main_frame, text=translator.get('about_external_tool'),
                font=('Segoe UI', 11, 'bold'), fg=self.colors['primary'],
                bg=self.colors['background']).pack(pady=(0, 5))
        
        # Link da ferramenta externa centralizado
        link_frame = tk.Frame(main_frame, bg=self.colors['background'])
        link_frame.pack(pady=(0, 20))
        
        external_link = tk.Label(link_frame, text=translator.get('about_external_link'),
                               font=('Segoe UI', 10, 'underline'), fg=self.colors['info'],
                               bg=self.colors['background'], cursor='hand2')
        external_link.pack()
        external_link.bind("<Button-1>", lambda e: self.open_url("https://review-stats-pro.lovable.app/"))
        
        # Seção de estatísticas de tempo economizado
        stats_summary = time_stats.get_stats_summary()
        
        # Separador antes das estatísticas
        separator1 = tk.Frame(main_frame, height=1, bg=self.colors['divider'])
        separator1.pack(fill=tk.X, pady=(20, 15))
        
        # Título das estatísticas
        tk.Label(main_frame, text=f"📊 {translator.get('usage_statistics')}",
                font=('Segoe UI', 12, 'bold'), fg=self.colors['primary'],
                bg=self.colors['background']).pack(pady=(0, 10))
        
        if stats_summary['total_reviews'] > 0:
            # Card com estatísticas
            stats_frame = tk.Frame(main_frame, bg=self.colors['surface'], relief='solid', bd=1)
            stats_frame.pack(fill=tk.X, pady=(0, 15))
            
            # Estatísticas principais
            stats_content = tk.Frame(stats_frame, bg=self.colors['surface'])
            stats_content.pack(fill=tk.X, padx=20, pady=(20, 25))
            
            # Destaques principais em duas colunas
            highlights_frame = tk.Frame(stats_content, bg=self.colors['surface'])
            highlights_frame.pack(fill=tk.X, pady=(0, 15))
            
            # Coluna 1: Total de Reviews
            reviews_highlight = tk.Frame(highlights_frame, bg=self.colors['surface'])
            reviews_highlight.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
            
            tk.Label(reviews_highlight, text=f"📈 {translator.get('reviews_collected')}",
                    font=('Segoe UI', 10, 'bold'), fg=self.colors['primary'],
                    bg=self.colors['surface']).pack()
            
            tk.Label(reviews_highlight, text=f"{stats_summary['total_reviews']:,}",
                    font=('Segoe UI', 16, 'bold'), fg=self.colors['info'],
                    bg=self.colors['surface']).pack()
            
            # Coluna 2: Tempo Economizado
            time_highlight = tk.Frame(highlights_frame, bg=self.colors['surface'])
            time_highlight.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=(10, 0))
            
            tk.Label(time_highlight, text=f"⏱️ {translator.get('total_time_saved')}",
                    font=('Segoe UI', 10, 'bold'), fg=self.colors['primary'],
                    bg=self.colors['surface']).pack()
            
            tk.Label(time_highlight, text=stats_summary['total_time_saved_formatted'],
                    font=('Segoe UI', 16, 'bold'), fg=self.colors['secondary'],
                    bg=self.colors['surface']).pack()
            
            # Separador sutil
            separator_stats = tk.Frame(stats_content, height=1, bg=self.colors['divider'])
            separator_stats.pack(fill=tk.X, pady=(5, 10))
            
            # Outras estatísticas - layout especial para alemão
            other_stats = tk.Frame(stats_content, bg=self.colors['surface'])
            other_stats.pack(fill=tk.X, pady=(5, 0))
            
            # Layout específico para alemão
            if translator.current_language == 'de':
                # Para alemão: layout mais compacto e limpo
                stats_compact = tk.Frame(other_stats, bg=self.colors['surface'])
                stats_compact.pack(fill=tk.X, pady=(0, 5))
                
                # Apenas Sessions
                sessions_text = f"🔄 {translator.get('usage_sessions')}: {stats_summary['total_sessions']:,}"
                tk.Label(stats_compact, text=sessions_text,
                        font=('Segoe UI', 9), fg=self.colors['on_surface'],
                        bg=self.colors['surface'], anchor='w').pack(fill=tk.X)
            else:
                # Para outros idiomas: layout limpo
                # Apenas sessões de uso
                sessions_frame = tk.Frame(other_stats, bg=self.colors['surface'])
                sessions_frame.pack(fill=tk.X)
                
                sessions_text = f"🔄 {translator.get('usage_sessions')}: {stats_summary['total_sessions']:,}"
                tk.Label(sessions_frame, text=sessions_text,
                        font=('Segoe UI', 9), fg=self.colors['on_surface'],
                        bg=self.colors['surface'], anchor='w', wraplength=580).pack(fill=tk.X)
        else:
            # Mensagem quando não há estatísticas
            no_stats_frame = tk.Frame(main_frame, bg=self.colors['surface'], relief='solid', bd=1)
            no_stats_frame.pack(fill=tk.X, pady=(0, 15))
            
            tk.Label(no_stats_frame, text=translator.get('no_stats_message'),
                    font=('Segoe UI', 10), fg=self.colors['on_surface'],
                    bg=self.colors['surface'], justify=tk.CENTER).pack(pady=20)
        
        # Separador
        separator = tk.Frame(main_frame, height=1, bg=self.colors['divider'])
        separator.pack(fill=tk.X, pady=20)
        
        # Desenvolvido por (centralizado)
        dev_frame = tk.Frame(main_frame, bg=self.colors['background'])
        dev_frame.pack()
        
        tk.Label(dev_frame, text=translator.get('about_developed_with'), font=('Segoe UI', 10),
                fg=self.colors['on_background'], bg=self.colors['background']).pack(side=tk.LEFT)
        
        tk.Label(dev_frame, text="♥", font=('Segoe UI', 12), fg='#E91E63',
                bg=self.colors['background']).pack(side=tk.LEFT, padx=(5, 5))
        
        tk.Label(dev_frame, text=translator.get('about_developed_by'), font=('Segoe UI', 10),
                fg=self.colors['on_background'], bg=self.colors['background']).pack(side=tk.LEFT)
        
        # Link do desenvolvedor
        dev_link = tk.Label(dev_frame, text=translator.get('about_developer'), font=('Segoe UI', 10, 'bold', 'underline'),
                          fg=self.colors['primary'], bg=self.colors['background'], cursor='hand2')
        dev_link.pack(side=tk.LEFT, padx=(5, 0))
        dev_link.bind("<Button-1>", lambda e: self.open_url("https://dsiqueira.com/"))
        
        # Botão Fechar
        close_btn = tk.Button(main_frame, text=translator.get('close_button'), command=about_window.destroy,
                            bg=self.colors['primary'], fg='white', font=('Segoe UI', 10, 'bold'),
                            relief='flat', bd=0, cursor='hand2', width=10, height=2)
        close_btn.pack(pady=(30, 0))
        
        # Hover effect para o botão fechar
        def on_enter(e):
            close_btn.config(bg=self.darken_color(self.colors['primary']))
        def on_leave(e):
            close_btn.config(bg=self.colors['primary'])
        close_btn.bind("<Enter>", on_enter)
        close_btn.bind("<Leave>", on_leave)

    def open_url(self, url):
        """Abre URL no navegador padrão"""
        import webbrowser
        webbrowser.open(url)
    
    def show_time_saved_modal(self, reviews_count):
        """Mostra modal com tempo economizado"""
        if reviews_count <= 0:
            return
        
        # Salva a sessão e obtém tempo economizado
        time_saved_seconds = time_stats.add_session(reviews_count)
        
        # Obtém estatísticas totais
        stats_summary = time_stats.get_stats_summary()
        
        time_saved_formatted = time_stats.format_time(time_saved_seconds)
        manual_time_formatted = time_stats.format_time(reviews_count * 30)  # Mesmo valor, mas para contexto
        
        # Calcula posição central
        window_width = 500
        window_height = 350
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        
        # Cria a janela modal
        modal = tk.Toplevel(self.root)
        modal.title(translator.get('time_saved_title'))
        modal.geometry(f"{window_width}x{window_height}+{x}+{y}")
        modal.resizable(False, False)
        modal.configure(bg=self.colors['background'])
        
        # Configura propriedades da janela
        modal.transient(self.root)
        modal.grab_set()
        
        # Configura o ícone da janela
        try:
            ico_path = os.path.join("assets", "icons", "google-play.ico")
            if os.path.exists(ico_path):
                modal.iconbitmap(ico_path)
        except:
            pass
        
        # Container principal
        main_frame = tk.Frame(modal, bg=self.colors['background'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
        
        # Ícone e título
        title_frame = tk.Frame(main_frame, bg=self.colors['background'])
        title_frame.pack(pady=(0, 20))
        
        tk.Label(title_frame, text="🎉", font=('Segoe UI', 24),
                bg=self.colors['background']).pack(side=tk.LEFT, padx=(0, 10))
        
        tk.Label(title_frame, text=translator.get('time_saved_title'), font=('Segoe UI', 18, 'bold'),
                fg=self.colors['primary'], bg=self.colors['background']).pack(side=tk.LEFT)
        
        # Mensagem principal mais concisa
        message_text = f"{translator.get('collection_completed')}\n{translator.get('reviews_processed').format(reviews_count)}"
        
        tk.Label(main_frame, text=message_text, font=('Segoe UI', 12),
                fg=self.colors['on_background'], bg=self.colors['background'],
                wraplength=440, justify=tk.CENTER).pack(pady=(0, 20))
        
        # Card com destaque - layout em duas colunas
        highlight_frame = tk.Frame(main_frame, bg=self.colors['surface'], relief='solid', bd=1)
        highlight_frame.pack(fill=tk.X, pady=(0, 20))
        
        highlight_content = tk.Frame(highlight_frame, bg=self.colors['surface'])
        highlight_content.pack(fill=tk.X, padx=20, pady=15)
        
        # Coluna 1: Reviews processadas
        reviews_col = tk.Frame(highlight_content, bg=self.colors['surface'])
        reviews_col.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        tk.Label(reviews_col, text=f"📈 {translator.get('reviews_label')}", font=('Segoe UI', 10, 'bold'),
                fg=self.colors['primary'], bg=self.colors['surface']).pack()
        
        tk.Label(reviews_col, text=f"{reviews_count:,}", font=('Segoe UI', 18, 'bold'),
                fg=self.colors['info'], bg=self.colors['surface']).pack()
        
        # Coluna 2: Tempo economizado
        time_col = tk.Frame(highlight_content, bg=self.colors['surface'])
        time_col.pack(side=tk.RIGHT, fill=tk.X, expand=True)
        
        tk.Label(time_col, text=f"⏱️ {translator.get('time_saved_label')}", font=('Segoe UI', 10, 'bold'),
                fg=self.colors['primary'], bg=self.colors['surface']).pack()
        
        tk.Label(time_col, text=time_saved_formatted, font=('Segoe UI', 18, 'bold'),
                fg=self.colors['secondary'], bg=self.colors['surface']).pack()
        
        # Explicação sutil
        explanation = tk.Label(highlight_frame, text=translator.get('manual_comparison'),
                              font=('Segoe UI', 8), fg=self.colors['disabled'],
                              bg=self.colors['surface'])
        explanation.pack(pady=(0, 10))
        
        # Estatísticas totais (mais compactas)
        if stats_summary['total_sessions'] > 1:  # Só mostra se não é a primeira sessão
            total_frame = tk.Frame(main_frame, bg=self.colors['background'])
            total_frame.pack(fill=tk.X, pady=(0, 15))
            
            tk.Label(total_frame, text=f"📊 {translator.get('accumulated_totals')}", font=('Segoe UI', 10, 'bold'),
                    fg=self.colors['primary'], bg=self.colors['background']).pack(pady=(0, 5))
            
            total_text = translator.get('total_summary').format(
                f"{stats_summary['total_reviews']:,}",
                stats_summary['total_time_saved_formatted'],
                f"{stats_summary['total_sessions']:,}"
            )
            
            tk.Label(total_frame, text=total_text, font=('Segoe UI', 9),
                    fg=self.colors['on_surface'], bg=self.colors['background'],
                    justify=tk.CENTER).pack()
        
        # Botão fechar
        close_btn = tk.Button(main_frame, text=translator.get('close_button'), command=modal.destroy,
                            bg=self.colors['primary'], fg='white', font=('Segoe UI', 11, 'bold'),
                            relief='flat', bd=0, cursor='hand2', width=12, height=2)
        close_btn.pack(pady=(10, 0))
        
        # Hover effect para o botão
        def on_enter(e):
            close_btn.config(bg=self.darken_color(self.colors['primary']))
        def on_leave(e):
            close_btn.config(bg=self.colors['primary'])
        close_btn.bind("<Enter>", on_enter)
        close_btn.bind("<Leave>", on_leave)
        
        # Foco no botão para permitir fechar com Enter
        close_btn.focus_set()
        modal.bind('<Return>', lambda e: modal.destroy())
        modal.bind('<Escape>', lambda e: modal.destroy())
    
    def log(self, message):
        """Adiciona mensagem ao log"""
        timestamp = time.strftime("%H:%M:%S")
        self.log_text.insert(tk.END, f"[{timestamp}] {message}\n")
        self.log_text.see(tk.END)
        self.root.update_idletasks()

def main():
    """Função principal"""
    root = tk.Tk()
    app = ReviewScraperApp(root)
    
    # Centraliza janela
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
    y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
    root.geometry(f"+{x}+{y}")
    
    root.mainloop()

if __name__ == "__main__":
    main()