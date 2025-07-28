import tkinter as tk
from tkinter import messagebox, filedialog
import threading
import os
import time
from review_scraper import GooglePlayReviewScraper
from translations import translator

class ReviewScraperApp:
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
        
        # Cores Material Design otimizadas
        self.colors = {
            'primary': '#1976D2',
            'secondary': '#2E7D32',
            'error': '#C62828',
            'warning': '#E65100',
            'info': '#0277BD',
            'surface': '#FFFFFF',
            'background': '#FAFAFA',
            'on_surface': '#212121',
            'on_background': '#424242',
            'disabled': '#757575',
            'divider': '#E0E0E0'
        }
        
        # Configurar estilo
        self.setup_styles()
        
        # Variáveis
        self.url_var = tk.StringVar()
        self.country_var = tk.StringVar(value="br")
        self.lang_var = tk.StringVar(value="pt")
        self.output_dir_var = tk.StringVar(value=os.getcwd())
        
        # Estado
        self.scraper = GooglePlayReviewScraper()  # Inicializa scraper
        self.is_running = False
        self.csv_path = None
        self.json_path = None
        
        self.create_interface()
        
        # Bind eventos
        self.url_var.trace('w', self.on_url_change)

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
        self.create_action_section(self.scrollable_frame)
        self.create_progress_section(self.scrollable_frame)
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
        """Cria o cabeçalho"""
        header = tk.Frame(parent, bg=self.colors['background'])
        header.pack(fill=tk.X, pady=(0, 20))
        
        # Container para título e botão info
        title_container = tk.Frame(header, bg=self.colors['background'])
        title_container.pack(fill=tk.X)
        
        # Título centralizado
        title_frame = tk.Frame(title_container, bg=self.colors['background'])
        title_frame.pack(expand=True)
        
        self.title_label = tk.Label(title_frame, text=translator.get('window_title'),
                font=('Segoe UI', 20, 'bold'), fg=self.colors['on_background'],
                bg=self.colors['background'])
        self.title_label.pack()
        
        # Container para controles do canto superior direito
        controls_frame = tk.Frame(title_container, bg=self.colors['background'])
        controls_frame.pack(side=tk.RIGHT, anchor=tk.NE, padx=(0, 5), pady=(5, 0))
        
        # Seletor de idioma customizado com bandeiras
        self.create_language_selector(controls_frame)
        
        # Botão de informação (menor e mais discreto)
        info_btn = tk.Button(controls_frame, text="ℹ", font=('Segoe UI', 10),
                           bg=self.colors['background'], fg=self.colors['disabled'], 
                           relief='flat', bd=0, width=2, height=1, cursor='hand2', 
                           command=self.show_about)
        info_btn.pack(side=tk.LEFT)
        
        # Hover effect para o botão info (mais sutil)
        def on_enter(e):
            info_btn.config(fg=self.colors['info'], bg=self.colors['divider'])
        def on_leave(e):
            info_btn.config(fg=self.colors['disabled'], bg=self.colors['background'])
        info_btn.bind("<Enter>", on_enter)
        info_btn.bind("<Leave>", on_leave)
        
        self.subtitle_label = tk.Label(header, text=translator.get('window_subtitle'),
                font=('Segoe UI', 12), fg=self.colors['primary'],
                bg=self.colors['background'])
        self.subtitle_label.pack(pady=(5, 0))
        
    def create_url_section(self, parent):
        """Cria a seção de URL"""
        section, self.url_section_title = self.create_card(parent, translator.get('url_section'))
        
        # URL entry
        url_frame = tk.Frame(section, bg=self.colors['surface'])
        url_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.url_entry = tk.Entry(url_frame, textvariable=self.url_var,
                                 font=('Segoe UI', 11), bg=self.colors['surface'],
                                 fg=self.colors['on_surface'], relief='solid', bd=1)
        self.url_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=8, ipadx=10)
        
        self.paste_btn = self.create_button(url_frame, translator.get('paste_button'), self.paste_url, self.colors['info'])
        self.paste_btn.pack(side=tk.RIGHT, padx=(10, 0))
        
        # App ID
        self.app_id_label = tk.Label(section, text="", font=('Segoe UI', 10),
                                   fg=self.colors['primary'], bg=self.colors['surface'])
        self.app_id_label.pack(anchor=tk.W)
        
        self.setup_placeholder()
        
    def create_config_section(self, parent):
        """Cria a seção de configurações"""
        section, self.config_section_title = self.create_card(parent, translator.get('config_section'))
        
        # Linha 1: País e Idioma
        row1 = tk.Frame(section, bg=self.colors['surface'])
        row1.pack(fill=tk.X, pady=(0, 10))
        
        self.country_label = tk.Label(row1, text=translator.get('country_label'), font=('Segoe UI', 10),
                fg=self.colors['on_surface'], bg=self.colors['surface'])
        self.country_label.pack(side=tk.LEFT)
        
        from tkinter import ttk
        ttk.Combobox(row1, textvariable=self.country_var,
                    values=["br", "us", "uk", "ca", "au", "de", "fr", "es", "it"],
                    width=8, state="readonly").pack(side=tk.LEFT, padx=(5, 20))
        
        self.language_label = tk.Label(row1, text=translator.get('language_label'), font=('Segoe UI', 10),
                fg=self.colors['on_surface'], bg=self.colors['surface'])
        self.language_label.pack(side=tk.LEFT)
        
        ttk.Combobox(row1, textvariable=self.lang_var,
                    values=["pt", "en", "es", "fr", "de", "it"],
                    width=8, state="readonly").pack(side=tk.LEFT, padx=(5, 0))
        
        # Linha 2: Pasta
        row2 = tk.Frame(section, bg=self.colors['surface'])
        row2.pack(fill=tk.X)
        
        self.folder_text_label = tk.Label(row2, text=translator.get('folder_label'), font=('Segoe UI', 10),
                fg=self.colors['on_surface'], bg=self.colors['surface'])
        self.folder_text_label.pack(side=tk.LEFT)
        
        self.folder_label = tk.Label(row2, text=self.output_dir_var.get(),
                                   font=('Segoe UI', 9), fg=self.colors['primary'],
                                   bg=self.colors['surface'], cursor='hand2')
        self.folder_label.pack(side=tk.LEFT, padx=(5, 10), fill=tk.X, expand=True)
        self.folder_label.bind("<Button-1>", lambda e: self.open_folder())
        
        self.choose_btn = self.create_button(row2, translator.get('choose_button'), self.choose_folder, self.colors['warning'])
        self.choose_btn.pack(side=tk.RIGHT)
        
    def create_action_section(self, parent):
        """Cria a seção de ações"""
        actions = tk.Frame(parent, bg=self.colors['background'])
        actions.pack(fill=tk.X, pady=15)
        
        buttons = tk.Frame(actions, bg=self.colors['background'])
        buttons.pack()
        
        self.start_btn = self.create_button(buttons, translator.get('start_button'), self.start_scraping, 
                                          self.colors['primary'], primary=True)
        self.start_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        self.stop_btn = self.create_button(buttons, translator.get('stop_button'), self.stop_scraping, 
                                         self.colors['error'], state=tk.DISABLED)
        self.stop_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        self.clear_btn = self.create_button(buttons, translator.get('clear_button'), self.clear_log, self.colors['disabled'])
        self.clear_btn.pack(side=tk.LEFT)
        
    def create_progress_section(self, parent):
        """Cria a seção de progresso"""
        section, self.progress_section_title = self.create_card(parent, translator.get('progress_section'))
        
        # Barra de progresso simples
        self.progress_var = tk.DoubleVar()
        progress_bg = tk.Frame(section, bg=self.colors['divider'], height=6)
        progress_bg.pack(fill=tk.X, pady=(0, 10))
        
        self.progress_canvas = tk.Canvas(progress_bg, height=6, bg=self.colors['divider'], 
                                        highlightthickness=0, bd=0)
        self.progress_canvas.pack(fill=tk.X)
        self.progress_bar_id = self.progress_canvas.create_rectangle(0, 0, 0, 6, 
                                                                    fill=self.colors['primary'], outline="")
        
        # Status
        self.status_label = tk.Label(section, text="Pronto para iniciar",
                                   font=('Segoe UI', 10), fg=self.colors['on_surface'],
                                   bg=self.colors['surface'])
        self.status_label.pack(pady=(0, 10))
        
        # Botões de resultado
        results = tk.Frame(section, bg=self.colors['surface'])
        results.pack()
        
        self.open_csv_btn = self.create_button(results, "CSV", lambda: self.open_file(self.csv_path),
                                             self.colors['secondary'], state=tk.DISABLED)
        self.open_csv_btn.pack(side=tk.LEFT, padx=(0, 5))
        
        self.open_json_btn = self.create_button(results, "JSON", lambda: self.open_file(self.json_path),
                                              self.colors['info'], state=tk.DISABLED)
        self.open_json_btn.pack(side=tk.LEFT, padx=(0, 5))
        
        self.open_folder_btn = self.create_button(results, "Pasta", self.open_folder,
                                                self.colors['warning'], state=tk.DISABLED)
        self.open_folder_btn.pack(side=tk.LEFT)
        
    def create_log_section(self, parent):
        """Cria a seção de log"""
        section, self.log_section_title = self.create_card(parent, translator.get('log_section'), expand=True)
        
        # Text com scrollbar
        log_frame = tk.Frame(section, bg=self.colors['surface'])
        log_frame.pack(fill=tk.BOTH, expand=True)
        
        scrollbar = tk.Scrollbar(log_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.log_text = tk.Text(log_frame, wrap=tk.WORD, font=('Consolas', 9),
                               bg='#F8F9FA', fg=self.colors['on_surface'],
                               relief='flat', bd=0, padx=10, pady=10, height=8,
                               yscrollcommand=scrollbar.set)
        self.log_text.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.log_text.yview)
        
        # Log inicial
        self.log(translator.get('scraper_started'))

    def create_status_bar(self):
        """Cria a barra de status"""
        self.status_var = tk.StringVar(value="Pronto")
        tk.Label(self.root, textvariable=self.status_var, anchor=tk.W,
                font=('Segoe UI', 9), bg=self.colors['surface'],
                fg=self.colors['on_surface'], padx=15, pady=5).pack(side=tk.BOTTOM, fill=tk.X)

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
    
    def create_button(self, parent, text, command, bg, primary=False, state=tk.NORMAL):
        """Cria um botão padronizado com tamanho fixo"""
        # Tamanho fixo para todos os botões
        if primary:
            font = ('Segoe UI', 11, 'bold')
            width, height = 15, 2  # Botão principal maior
        else:
            font = ('Segoe UI', 10, 'normal')
            width, height = 12, 2  # Botões secundários
        
        btn = tk.Button(parent, text=text, command=command, bg=bg, fg='white',
                       font=font, relief='flat', bd=0, cursor='hand2', state=state,
                       width=width, height=height,  # Tamanho fixo
                       activeforeground='white',
                       disabledforeground='white')
        
        # Hover effect mantendo texto branco
        hover_bg = self.darken_color(bg)
        btn.bind("<Enter>", lambda e: btn.config(bg=hover_bg, fg='white') if btn['state'] != tk.DISABLED else None)
        btn.bind("<Leave>", lambda e: btn.config(bg=bg, fg='white') if btn['state'] != tk.DISABLED else None)
        
        return btn
    
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
        """Configura placeholder para URL"""
        placeholder = translator.get('url_placeholder')
        
        def on_focus_in(e):
            if self.url_var.get() == placeholder:
                self.url_var.set("")
                self.url_entry.config(fg=self.colors['on_surface'])
        
        def on_focus_out(e):
            if not self.url_var.get():
                self.url_var.set(placeholder)
                self.url_entry.config(fg=self.colors['disabled'])
        
        self.url_var.set(placeholder)
        self.url_entry.config(fg=self.colors['disabled'])
        self.url_entry.bind('<FocusIn>', on_focus_in)
        self.url_entry.bind('<FocusOut>', on_focus_out)

    def on_url_change(self, *args):
        """Chamado quando URL muda"""
        url = self.url_var.get()
        placeholder_text = "Cole a URL do app do Google Play Store..."
        
        if url and url != placeholder_text:
            try:
                app_id = self.scraper.extract_app_id_from_url(url) if self.scraper else ""
                self.app_id_label.config(text=f"App ID: {app_id}")
                self.status_var.set(f"App ID extraído: {app_id}")
            except:
                self.app_id_label.config(text="")
                self.status_var.set("URL inválida")
        else:
            self.app_id_label.config(text="")
            self.status_var.set("Pronto")

    def update_progress(self, value):
        """Atualiza barra de progresso"""
        self.progress_var.set(value)
        
        # Atualiza barra visual
        canvas_width = self.progress_canvas.winfo_width()
        if canvas_width > 1:
            progress_width = (value / 100) * canvas_width
            self.progress_canvas.coords(self.progress_bar_id, 0, 0, progress_width, 20)
    
    def paste_url(self):
        """Cola URL da área de transferência"""
        try:
            clipboard_content = self.root.clipboard_get()
            self.url_var.set(clipboard_content)
            self.log("URL colada da área de transferência")
        except:
            messagebox.showwarning("Aviso", "Não foi possível colar da área de transferência")
    
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
        """Inicia o scraping"""
        url = self.url_var.get().strip()
        
        if not url:
            messagebox.showerror("Erro", "Por favor, insira uma URL")
            return
        
        if "play.google.com" not in url:
            messagebox.showerror("Erro", "URL deve ser do Google Play Store")
            return
        
        # Atualiza interface
        self.is_running = True
        self.start_btn.config(state=tk.DISABLED, bg=self.colors['disabled'], fg='white')
        self.stop_btn.config(state=tk.NORMAL, bg=self.colors['error'], fg='white')
        self.open_csv_btn.config(state=tk.DISABLED, bg=self.colors['disabled'], fg='white')
        self.open_json_btn.config(state=tk.DISABLED, bg=self.colors['disabled'], fg='white')
        self.open_folder_btn.config(state=tk.DISABLED, bg=self.colors['disabled'], fg='white')
        self.progress_var.set(0)
        self.update_progress(0)
        self.status_label.config(text="Iniciando coleta...")
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
        """Worker thread para scraping"""
        try:
            url = self.url_var.get()
            self.log(f"Processando URL: {url}")
            
            # Extrai app_id
            app_id = self.scraper.extract_app_id_from_url(url)
            self.log(f"App ID extraído: {app_id}")
            
            # Coleta reviews
            self.log("Iniciando coleta de reviews...")
            reviews_data, app_info = self.scraper.extract_all_reviews(app_id)
            
            if reviews_data and self.is_running:
                # Salva arquivos
                output_dir = self.output_dir_var.get()
                
                # Muda para o diretório de saída
                original_dir = os.getcwd()
                os.chdir(output_dir)
                
                try:
                    self.scraper.save_reviews(reviews_data, app_info)
                    
                    # Encontra os arquivos criados
                    app_name = self.scraper.clean_filename(app_info.get('title', 'app'))
                    self.csv_path = os.path.join(output_dir, f"{app_name}_reviews.csv")
                    self.json_path = os.path.join(output_dir, f"{app_name}_reviews.json")
                    
                    # Mostra estatísticas
                    self.show_statistics(reviews_data)
                    
                    # Habilita botões
                    self.root.after(0, self.enable_result_buttons)
                    
                    self.log(f"\nColeta finalizada com sucesso!")
                    self.log(f"Arquivos salvos em: {output_dir}")
                    
                    self.root.after(0, lambda: self.status_label.config(
                        text=f"Concluído: {len(reviews_data)} reviews coletadas"))
                    
                finally:
                    os.chdir(original_dir)
            else:
                self.log("Nenhuma review foi coletada")
                
        except Exception as e:
            self.log(f"Erro: {e}")
            self.root.after(0, lambda: self.status_label.config(text=f"Erro: {str(e)}"))
        
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
        self.start_btn.config(state=tk.NORMAL, bg=self.colors['primary'], fg='white')
        self.stop_btn.config(state=tk.DISABLED, bg=self.colors['disabled'], fg='white')
        self.status_var.set("Pronto")
    
    def enable_result_buttons(self):
        """Habilita botões de resultado"""
        if self.csv_path and os.path.exists(self.csv_path):
            self.open_csv_btn.config(state=tk.NORMAL, bg=self.colors['secondary'], fg='white')
        if self.json_path and os.path.exists(self.json_path):
            self.open_json_btn.config(state=tk.NORMAL, bg=self.colors['info'], fg='white')
        self.open_folder_btn.config(state=tk.NORMAL, bg=self.colors['warning'], fg='white')
    
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
    
    def clear_log(self):
        """Limpa o log"""
        self.log_text.delete(1.0, tk.END)
        self.log("Log limpo")

    def show_about(self):
        """Mostra a janela Sobre"""
        # Calcula posição central antes de criar a janela
        window_width = 500
        window_height = 400
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
                justify=tk.CENTER, wraplength=440).pack(pady=(0, 20))
        
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