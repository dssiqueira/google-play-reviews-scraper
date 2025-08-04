"""Graphical user interface for the Google Play Reviews Scraper (Mac Version)."""

import tkinter as tk
from tkinter import messagebox, filedialog, font
import threading
import os
import time
import platform
import subprocess
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
        
        # Configurar ícone da aplicação (adaptado para Mac)
        self.setup_icon()
        
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

    def center_window(self, window, width=None, height=None):
        """Centraliza uma janela definindo opcionalmente o tamanho."""
        window.update_idletasks()
        w = width or window.winfo_width()
        h = height or window.winfo_height()
        x = (window.winfo_screenwidth() // 2) - (w // 2)
        y = (window.winfo_screenheight() // 2) - (h // 2)
        geom = f"{w}x{h}+{x}+{y}" if width and height else f"+{x}+{y}"
        window.geometry(geom)

    def create_language_selector(self, parent):
        """Cria seletor de idioma customizado com bandeiras PNG"""
        # Carrega as imagens das bandeiras
        self.load_flag_images()
        
        # Frame para o seletor (lado a lado com outros controles)
        lang_frame = tk.Frame(parent, bg=self.colors['background'])
        lang_frame.pack(side=tk.LEFT, padx=(0, 10))
        
        # Botão atual com bandeira usando Canvas para melhor suporte no Mac
        current_flag = self.get_flag_code(translator.current_language)
        
        # Container para o botão do seletor
        selector_container = tk.Frame(lang_frame, bg=self.colors['background'])
        selector_container.pack()
        
        # Canvas para o botão do seletor (largura aumentada para não cortar bandeira)
        self.lang_selector_canvas = tk.Canvas(selector_container, width=100, height=30,
                                            highlightthickness=0, bd=0, bg=self.colors['background'])
        self.lang_selector_canvas.pack()
        
        # Desenha o botão do seletor (fundo branco por padrão)
        def draw_selector_button(bg_color='#ffffff', border_color=self.colors['border']):
            self.lang_selector_canvas.delete("selector_bg")
            # Fundo do botão (largura aumentada)
            self.lang_selector_canvas.create_rectangle(1, 1, 99, 29, 
                                                     fill=bg_color, outline=border_color, 
                                                     tags="selector_bg")
        
        draw_selector_button()
        
        # Adiciona bandeira e texto
        flag_img = self.flag_images.get(current_flag)
        if flag_img:
            self.lang_flag_id = self.lang_selector_canvas.create_image(8, 15, image=flag_img, tags="selector_content")
        
        font_family = "SF Pro Text" if platform.system() == "Darwin" else "Helvetica"
        self.lang_text_id = self.lang_selector_canvas.create_text(60, 15, 
                                                                 text=translator.current_language.upper(),
                                                                 fill=self.colors['on_background'], 
                                                                 font=(font_family, 9, 'bold'),
                                                                 tags="selector_content")
        
        # Eventos do seletor
        def on_selector_enter(event):
            draw_selector_button('#f5f5f5', self.colors['primary'])  # Cinza claro no hover
            self.lang_selector_canvas.tag_raise("selector_content")
        
        def on_selector_leave(event):
            draw_selector_button()  # Volta ao branco
            self.lang_selector_canvas.tag_raise("selector_content")
        
        def on_selector_click(event):
            draw_selector_button('#e0e0e0', self.colors['primary'])  # Cinza mais escuro no click
            self.lang_selector_canvas.tag_raise("selector_content")
            self.lang_selector_canvas.after(100, lambda: draw_selector_button('#f5f5f5', self.colors['primary']))
            self.lang_selector_canvas.after(150, lambda: self.lang_selector_canvas.tag_raise("selector_content"))
            self.toggle_language_menu()
        
        self.lang_selector_canvas.bind("<Enter>", on_selector_enter)
        self.lang_selector_canvas.bind("<Leave>", on_selector_leave)
        self.lang_selector_canvas.bind("<Button-1>", on_selector_click)
        self.lang_selector_canvas.bind("<Motion>", lambda e: self.lang_selector_canvas.config(cursor="hand2"))
        
        # Salva referência para atualizações
        self.current_lang_display = selector_container  # Para compatibilidade com código existente
        
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
                          font=self.get_font(9),
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
                # Caminho relativo considerando que pode estar em src/
                flag_path = os.path.join("..", "assets", "flags", filename)
                if not os.path.exists(flag_path):
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
                # Se clicou no botão do seletor (Canvas), container ou no menu, não fecha
                if (widget == self.current_lang_display or 
                    widget == self.lang_selector_canvas or
                    widget == self.lang_menu or 
                    widget in self.lang_menu.winfo_children()):
                    return
            
            self.lang_menu.place_forget()
            self.lang_menu_visible = False

    def select_language(self, lang_code):
        """Seleciona um idioma"""
        if translator.set_language(lang_code):
            # Atualiza o botão Canvas com a nova bandeira
            flag_code = self.get_flag_code(lang_code)
            if hasattr(self, 'flag_images') and flag_code in self.flag_images:
                # Atualiza bandeira no Canvas
                if hasattr(self, 'lang_flag_id'):
                    self.lang_selector_canvas.itemconfig(self.lang_flag_id, image=self.flag_images[flag_code])
                
                # Atualiza texto no Canvas
                if hasattr(self, 'lang_text_id'):
                    self.lang_selector_canvas.itemconfig(self.lang_text_id, text=lang_code.upper())
            
            self.hide_language_menu()
            self.update_ui_texts()



    def update_ui_texts(self):
        """Atualiza todos os textos da interface"""
        # Título da janela
        self.root.title(translator.get('window_title'))
        
        # Atualiza seletor de idioma Canvas
        if hasattr(self, 'lang_selector_canvas') and hasattr(self, 'flag_images'):
            flag_code = self.get_flag_code(translator.current_language)
            if flag_code in self.flag_images:
                # Atualiza bandeira no Canvas
                if hasattr(self, 'lang_flag_id'):
                    self.lang_selector_canvas.itemconfig(self.lang_flag_id, image=self.flag_images[flag_code])
                
                # Atualiza texto no Canvas
                if hasattr(self, 'lang_text_id'):
                    self.lang_selector_canvas.itemconfig(self.lang_text_id, text=translator.current_language.upper())
        
        # Cabeçalho
        if hasattr(self, 'title_label'):
            self.title_label.config(text=translator.get('window_title'))
        if hasattr(self, 'subtitle_label'):
            self.subtitle_label.config(text=translator.get('window_subtitle'))
        
        # Títulos das seções
        if hasattr(self, 'url_section_title'):
            self.url_section_title.config(text=translator.get('add_apps_title'))
        if hasattr(self, 'config_section_title'):
            self.config_section_title.config(text=translator.get('config_section'))
        if hasattr(self, 'progress_section_title'):
            self.progress_section_title.config(text=translator.get('progress_section'))
        if hasattr(self, 'log_section_title'):
            self.log_section_title.config(text=translator.get('log_activities_title'))
        if hasattr(self, 'queue_title'):
            self.queue_title.config(text=translator.get('queue_title'))
        
        # Labels das seções
        if hasattr(self, 'country_label'):
            self.country_label.config(text=translator.get('country_label'))
        if hasattr(self, 'language_label'):
            self.language_label.config(text=translator.get('language_label'))
        if hasattr(self, 'folder_label_text'):
            self.folder_label_text.config(text=translator.get('folder_destination_label'))
        
        # Status e botões
        if hasattr(self, 'urls_status_label'):
            if not self.urls_list:
                self.urls_status_label.config(text=translator.get('no_apps_added'))
            else:
                count = len(self.urls_list)
                if count == 1:
                    self.urls_status_label.config(text=translator.get('apps_in_queue_single'))
                else:
                    self.urls_status_label.config(text=translator.get('apps_in_queue_multiple').format(count))
        
        if hasattr(self, 'status_label'):
            self.status_label.config(text=translator.get('ready_to_start'))
        
        if hasattr(self, 'toggle_log_btn'):
            if hasattr(self, 'log_visible') and self.log_visible:
                self.toggle_log_btn.config(text=translator.get('hide_log'))
            else:
                self.toggle_log_btn.config(text=translator.get('show_log'))
        
        # Botões Canvas (não podem ser atualizados diretamente)
        # Recriar botões Canvas com novas traduções
        self.recreate_canvas_buttons()
        
        # Placeholder da URL
        self.setup_placeholder()
        
        # Atualizar lista de apps se existir
        if hasattr(self, 'urls_list'):
            self.update_urls_list()
    
    def recreate_canvas_buttons(self):
        """Atualiza textos dos botões Canvas com novas traduções"""
        try:
            # Atualizar botão principal primeiro (tem método próprio)
            if hasattr(self, 'main_button_canvas') and hasattr(self, 'main_button_text_id'):
                try:
                    # Determinar o texto correto baseado no estado
                    if hasattr(self, 'scraping_active') and self.scraping_active:
                        main_text = translator.get('processing')
                    else:
                        main_text = translator.get('start_button')
                    
                    self.main_button_canvas.itemconfig(self.main_button_text_id, text=main_text)
                    self.main_button_text = main_text
                except tk.TclError:
                    pass
            
            # Lista de botões Canvas que precisam ser atualizados
            canvas_buttons = [
                ('paste_btn_container', 'paste_button'),
                ('add_btn_container', 'add_button'), 
                ('clear_btn_container', 'clear_all_button'),
                ('choose_btn_container', 'choose_button'),
                ('csv_btn_container', 'csv_button'),
                ('json_btn_container', 'json_button'),
                ('folder_btn_container', 'folder_button')
            ]
            
            # Atualizar cada botão Canvas se existir
            for container_attr, text_key in canvas_buttons:
                if hasattr(self, container_attr):
                    container = getattr(self, container_attr)
                    if container and hasattr(container, 'winfo_exists'):
                        try:
                            if container.winfo_exists():
                                # Encontrar o Canvas dentro do container
                                for child in container.winfo_children():
                                    if isinstance(child, tk.Canvas):
                                        # Encontrar todos os itens de texto no Canvas
                                        try:
                                            items = child.find_all()
                                            for item in items:
                                                if child.type(item) == 'text':
                                                    # Atualizar o texto com a nova tradução
                                                    new_text = translator.get(text_key)
                                                    child.itemconfig(item, text=new_text)
                                                    break
                                        except tk.TclError:
                                            # Canvas pode ter sido destruído
                                            continue
                                        break
                        except tk.TclError:
                            # Container pode ter sido destruído
                            continue
        except Exception as e:
            # Em caso de erro, apenas continua sem quebrar a interface
            print(f"Erro ao atualizar botões Canvas: {e}")
    
    def setup_styles(self):
        """Configura estilos básicos"""
        # Configuração mínima necessária
        self.root.configure(bg=self.colors['background'])

    def setup_icon(self):
        """Configura o ícone da aplicação (adaptado para Mac)"""
        try:
            # Caminho inteligente para o ícone
            if os.path.exists("assets"):
                png_path = os.path.join("assets", "icons", "google-play.png")
            else:
                png_path = os.path.join("..", "assets", "icons", "google-play.png")
                
            if os.path.exists(png_path):
                try:
                    from PIL import Image, ImageTk
                    icon_image = Image.open(png_path)
                    # Redimensionar para múltiplos tamanhos para melhor compatibilidade
                    icon_image = icon_image.resize((64, 64), Image.Resampling.LANCZOS)
                    self.icon_photo = ImageTk.PhotoImage(icon_image)
                    
                    # Definir ícone da janela
                    self.root.iconphoto(True, self.icon_photo)
                    
                    # Solução específica para macOS - definir título da aplicação
                    if platform.system() == "Darwin":
                        self.root.title("Google Play Reviews Scraper")
                        # Forçar atualização do dock
                        self.root.update_idletasks()
                        # Chamar método auxiliar para forçar ícone no dock
                        self.root.after(500, self.force_dock_icon_update)
                        
                except ImportError:
                    # Fallback se PIL não estiver disponível
                    try:
                        self.icon_photo = tk.PhotoImage(file=png_path)
                        self.root.iconphoto(True, self.icon_photo)
                    except:
                        print("Não foi possível carregar o ícone")
            else:
                print(f"Ícone não encontrado em: {png_path}")
        except Exception as e:
            print(f"Erro ao carregar ícone: {e}")

    def force_dock_icon_update(self):
        """Força a atualização do ícone no dock do macOS"""
        if platform.system() == "Darwin":
            try:
                # Forçar foco na janela para atualizar o dock
                self.root.lift()
                self.root.attributes('-topmost', True)
                self.root.after(100, lambda: self.root.attributes('-topmost', False))
                
                # Atualizar o título da janela para forçar refresh
                original_title = self.root.title()
                self.root.title("Google Play Reviews Scraper")
                self.root.update()
                
                # Tentar usar AppleScript para definir ícone
                try:
                    import subprocess
                    # Script para definir ícone da aplicação
                    script = '''
                    tell application "System Events"
                        set frontApp to name of first application process whose frontmost is true
                        if frontApp contains "Python" then
                            set visible of application process frontApp to true
                        end if
                    end tell
                    '''
                    subprocess.run(['osascript', '-e', script], capture_output=True, timeout=2)
                except:
                    pass
                    
            except Exception as e:
                print(f"Erro ao forçar atualização do dock: {e}")
    
    # Métodos específicos do Windows removidos para versão Mac
    
    def get_font(self, size=10, weight='normal'):
        """Retorna a fonte apropriada para a plataforma"""
        if platform.system() == "Darwin":  # macOS
            if weight == 'bold':
                return ("SF Pro Text", size, 'bold')
            elif weight == 'normal':
                return ("SF Pro Text", size)
            else:
                return ("SF Pro Text", size, weight)
        else:  # Outras plataformas
            if weight == 'bold':
                return ("Helvetica", size, 'bold')
            elif weight == 'normal':
                return ("Helvetica", size)
            else:
                return ("Helvetica", size, weight)

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
        """Configura scroll com roda do mouse (adaptado para Mac)"""
        def _on_mousewheel(event):
            # No Mac, o delta pode ser diferente
            if platform.system() == "Darwin":
                self.canvas.yview_scroll(int(-1 * event.delta), "units")
            else:
                self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        def bind_to_mousewheel(event):
            self.canvas.bind_all("<MouseWheel>", _on_mousewheel)
            # Adiciona suporte para trackpad no Mac
            if platform.system() == "Darwin":
                self.canvas.bind_all("<Button-4>", lambda e: self.canvas.yview_scroll(-1, "units"))
                self.canvas.bind_all("<Button-5>", lambda e: self.canvas.yview_scroll(1, "units"))
        
        def unbind_from_mousewheel(event):
            self.canvas.unbind_all("<MouseWheel>")
            if platform.system() == "Darwin":
                self.canvas.unbind_all("<Button-4>")
                self.canvas.unbind_all("<Button-5>")
        
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
                font=self.get_font(24, 'bold'), fg=self.colors['on_background'],
                bg=self.colors['background'])
        self.title_label.pack(anchor=tk.W)
        
        # Subtítulo
        self.subtitle_label = tk.Label(text_container, text="Coleta reviews de apps do Google Play Store",
                font=self.get_font(12), fg=self.colors['disabled'],
                bg=self.colors['background'])
        self.subtitle_label.pack(anchor=tk.W, pady=(2, 0))
        
        # Container para controles do canto superior direito
        controls_frame = tk.Frame(header_container, bg=self.colors['background'])
        controls_frame.pack(side=tk.RIGHT, anchor=tk.NE, padx=(10, 0))
        
        # Seletor de idiomas (lado esquerdo dos controles)
        self.create_language_selector(controls_frame)
        
        # Botão de configurações (ícone de engrenagem)
        font_family = "SF Pro Display" if platform.system() == "Darwin" else "Helvetica"
        settings_btn = tk.Button(controls_frame, text="⚙", font=(font_family, 16),
                               bg=self.colors['surface'], fg=self.colors['disabled'], 
                               relief='flat', bd=0, width=3, height=1, cursor='hand2',
                               command=self.show_about)
        settings_btn.pack(side=tk.LEFT)
        
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
        font_family = "SF Pro Display" if platform.system() == "Darwin" else "Helvetica"
        self.url_section_title = tk.Label(section, text=translator.get('add_apps_title'),
                                         font=(font_family, 16, 'bold'), 
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
        
        font_family = "SF Pro Text" if platform.system() == "Darwin" else "Helvetica"
        self.url_entry = tk.Entry(entry_inner, font=(font_family, 12),
                                 bg=self.colors['surface'], fg=self.colors['on_surface'],
                                 relief='flat', bd=0, insertbackground=self.colors['primary'])
        self.url_entry.pack(fill=tk.X, padx=15, pady=10)
        
        # Container para botões
        buttons_container = tk.Frame(input_container, bg=self.colors['surface'])
        buttons_container.pack(side=tk.RIGHT, padx=(10, 0))
        
        # Botão Colar arredondado com cor contrastante
        self.paste_btn_container = self.create_rounded_button(buttons_container, translator.get('paste_button'), 
                                                        self.paste_url, self.colors['btn_pink'], 
                                                        width=70, height=35)
        self.paste_btn_container.pack(side=tk.LEFT, padx=(0, 8))
        
        # Botão Adicionar arredondado com cor contrastante
        self.add_btn_container = self.create_rounded_button(buttons_container, translator.get('add_button'), 
                                                      self.add_url, self.colors['btn_blue'], 
                                                      width=90, height=35)
        self.add_btn_container.pack(side=tk.LEFT)
        
        # Seção Apps na fila
        queue_section = tk.Frame(section, bg=self.colors['surface'])
        queue_section.pack(fill=tk.X, pady=(15, 0))
        
        # Título Apps na fila
        self.queue_title = tk.Label(queue_section, text=translator.get('queue_title'),
                              font=self.get_font(14, 'bold'),
                              fg=self.colors['on_surface'],
                              bg=self.colors['surface'])
        self.queue_title.pack(anchor=tk.W, pady=(0, 10))
        
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
        self.clear_btn_container = self.create_rounded_button(queue_section, translator.get('clear_all_button'), 
                                                        self.clear_all_urls, self.colors['btn_red'], 
                                                        width=120, height=32)
        self.clear_btn_container.pack(anchor=tk.W, pady=(5, 0))
        
        # Status da lista
        self.urls_status_label = tk.Label(queue_section, text=translator.get('no_apps_added'),
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
        self.config_section_title = tk.Label(section, text=translator.get('config_section'),
                                            font=self.get_font(16, 'bold'),
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
                                     font=self.get_font(12, 'bold'),
                                     fg=self.colors['on_surface'],
                                     bg=self.colors['surface'])
        self.country_label.pack(anchor=tk.W)
        
        from tkinter import ttk
        # Estilo customizado para combobox
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Custom.TCombobox',
                       fieldbackground='#ffffff',
                       background='#ffffff',
                       foreground=self.colors['on_surface'],
                       borderwidth=1,
                       relief='solid')
        
        country_combo = ttk.Combobox(country_container, textvariable=self.country_var,
                                   values=["br", "us", "uk", "ca", "au", "de", "fr", "es", "it"],
                                   width=8, state="readonly", style='Custom.TCombobox')
        country_combo.pack(pady=(5, 0))
        
        # Idioma
        lang_container = tk.Frame(config_row, bg=self.colors['surface'])
        lang_container.pack(side=tk.LEFT)
        
        self.language_label = tk.Label(lang_container, text="Idioma:",
                                      font=self.get_font(12, 'bold'),
                                      fg=self.colors['on_surface'],
                                      bg=self.colors['surface'])
        self.language_label.pack(anchor=tk.W)
        
        lang_combo = ttk.Combobox(lang_container, textvariable=self.lang_var,
                                values=["pt", "en", "es", "fr", "de", "it"],
                                width=8, state="readonly", style='Custom.TCombobox')
        lang_combo.pack(pady=(5, 0))
        
        # Pasta de destino
        folder_container = tk.Frame(section, bg=self.colors['surface'])
        folder_container.pack(fill=tk.X)
        
        # Label da pasta
        self.folder_label_text = tk.Label(folder_container, text=translator.get('folder_destination_label'),
                                    font=self.get_font(12, 'bold'),
                                    fg=self.colors['on_surface'],
                                    bg=self.colors['surface'])
        self.folder_label_text.pack(anchor=tk.W, pady=(0, 5))
        
        # Container para caminho e botão
        folder_row = tk.Frame(folder_container, bg=self.colors['surface'])
        folder_row.pack(fill=tk.X)
        
        # Caminho da pasta (clicável)
        self.folder_label = tk.Label(folder_row, text=self.output_dir_var.get(),
                                   font=self.get_font(10), fg=self.colors['info'],
                                   bg=self.colors['surface'], cursor='hand2',
                                   anchor='w', justify='left')
        self.folder_label.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.folder_label.bind("<Button-1>", lambda e: self.open_folder())
        
        # Botão Escolher arredondado com cor contrastante
        self.choose_btn_container = self.create_rounded_button(folder_row, translator.get('choose_button'), 
                                                         self.choose_folder, self.colors['btn_cyan'], 
                                                         width=100, height=32)
        self.choose_btn_container.pack(side=tk.RIGHT)
        
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
        self.progress_section_title = tk.Label(section, text=translator.get('progress_section'),
                                             font=self.get_font(16, 'bold'),
                                             fg=self.colors['on_surface'],
                                             bg=self.colors['surface'])
        self.progress_section_title.pack(anchor=tk.W, pady=(0, 15))
        
        # Status atual
        self.status_label = tk.Label(section, text=translator.get('ready_to_start'),
                                   font=self.get_font(12),
                                   fg=self.colors['disabled'],
                                   bg=self.colors['surface'])
        self.status_label.pack(anchor=tk.W, pady=(0, 10))
        
        # Container para botões de resultado
        self.result_buttons_frame = tk.Frame(section, bg=self.colors['surface'])
        self.result_buttons_frame.pack(fill=tk.X, pady=(10, 0))
        
        # Botões de resultado arredondados com cores contrastantes
        self.csv_btn_container = self.create_rounded_button(self.result_buttons_frame, translator.get('csv_button'), 
                                                           self.open_csv_files, self.colors['btn_green'], 
                                                           width=80, height=35)
        self.csv_btn_container.pack(side=tk.LEFT, padx=(0, 10))
        
        self.json_btn_container = self.create_rounded_button(self.result_buttons_frame, translator.get('json_button'), 
                                                            self.open_json_files, self.colors['btn_blue'], 
                                                            width=80, height=35)
        self.json_btn_container.pack(side=tk.LEFT, padx=(0, 10))
        
        self.folder_btn_container = self.create_rounded_button(self.result_buttons_frame, translator.get('folder_button'), 
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
        
        self.log_section_title = tk.Label(header, text=translator.get('log_activities_title'),
                                         font=('Segoe UI', 16, 'bold'),
                                         fg=self.colors['on_surface'],
                                         bg=self.colors['surface'])
        self.log_section_title.pack(side=tk.LEFT)
        
        # Botão para mostrar/ocultar log
        self.toggle_log_btn = tk.Button(header, text=translator.get('show_log'),
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
            self.toggle_log_btn.config(text=translator.get('show_log'))
            self.log_visible = False
        else:
            # Mostrar log
            self.log_card.pack(fill=tk.X, pady=(0, 20), padx=20)
            self.log_container.pack(fill=tk.BOTH, expand=True, pady=(10, 0))
            self.toggle_log_btn.config(text=translator.get('hide_log'))
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
        """Cria um botão estilizado usando Canvas para melhor suporte de cores no Mac"""
        # Container principal
        btn_container = tk.Frame(parent, bg=self.colors['background'])
        btn_container.configure(width=width, height=height)
        btn_container.pack_propagate(False)
        
        # Canvas para desenhar o botão com cores
        canvas = tk.Canvas(btn_container, width=width, height=height, 
                          highlightthickness=0, bd=0, bg=self.colors['background'])
        canvas.pack(fill=tk.BOTH, expand=True)
        
        # Desenha retângulo arredondado
        def draw_button(color):
            canvas.delete("button_bg")
            # Simula bordas arredondadas com retângulo
            canvas.create_rectangle(2, 2, width-2, height-2, 
                                  fill=color, outline=color, tags="button_bg")
        
        # Desenha botão inicial
        draw_button(bg_color)
        
        # Adiciona texto
        font_family = "SF Pro Text" if platform.system() == "Darwin" else "Helvetica"
        text_id = canvas.create_text(width//2, height//2, text=text, 
                                   fill=text_color, font=(font_family, font_size, 'bold'),
                                   tags="button_text")
        
        # Funções de hover
        hover_color = self.lighten_color(bg_color)
        
        def on_enter(event):
            draw_button(hover_color)
            canvas.tag_raise("button_text")
        
        def on_leave(event):
            draw_button(bg_color)
            canvas.tag_raise("button_text")
        
        def on_click(event):
            # Efeito visual de clique
            draw_button(self.darken_color(bg_color))
            canvas.tag_raise("button_text")
            canvas.after(100, lambda: draw_button(hover_color))
            canvas.after(150, lambda: canvas.tag_raise("button_text"))
            # Executa comando
            if command:
                command()
        
        # Bind eventos
        canvas.bind("<Enter>", on_enter)
        canvas.bind("<Leave>", on_leave)
        canvas.bind("<Button-1>", on_click)
        canvas.bind("<Motion>", lambda e: canvas.config(cursor="hand2"))
        
        return btn_container
        
    def darken_color(self, color):
        """Escurece uma cor para efeito de clique"""
        # Remove o # se presente
        color = color.lstrip('#')
        
        # Converte hex para RGB
        rgb = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
        
        # Escurece cada componente
        darkened = tuple(max(0, int(c * 0.8)) for c in rgb)
        
        # Converte de volta para hex
        return f"#{darkened[0]:02x}{darkened[1]:02x}{darkened[2]:02x}"
    
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
        """Cria o botão principal usando Canvas para melhor suporte de cores no Mac"""
        # Container principal
        btn_container = tk.Frame(parent, bg=self.colors['background'])
        btn_container.configure(height=60)
        btn_container.pack_propagate(False)
        
        # Canvas para desenhar o botão principal
        canvas = tk.Canvas(btn_container, height=60, 
                          highlightthickness=0, bd=0, bg=self.colors['background'])
        canvas.pack(fill=tk.BOTH, expand=True, padx=4, pady=4)
        
        # Cor principal do botão
        main_color = self.colors['success']  # Verde para "iniciar"
        
        # Função para desenhar o botão
        def draw_main_button(color):
            canvas.delete("main_button_bg")
            # Desenha retângulo com bordas arredondadas simuladas
            canvas_width = canvas.winfo_width()
            if canvas_width <= 1:  # Se ainda não foi renderizado
                canvas_width = 400  # Largura padrão
            
            # Retângulo principal
            canvas.create_rectangle(4, 4, canvas_width-4, 56, 
                                  fill=color, outline=color, tags="main_button_bg")
            
            # Simula bordas arredondadas com pequenos retângulos nos cantos
            corner_color = self.lighten_color(color)
            canvas.create_rectangle(4, 4, 8, 8, fill=corner_color, outline=corner_color, tags="main_button_bg")
            canvas.create_rectangle(canvas_width-8, 4, canvas_width-4, 8, fill=corner_color, outline=corner_color, tags="main_button_bg")
            canvas.create_rectangle(4, 52, 8, 56, fill=corner_color, outline=corner_color, tags="main_button_bg")
            canvas.create_rectangle(canvas_width-8, 52, canvas_width-4, 56, fill=corner_color, outline=corner_color, tags="main_button_bg")
        
        # Desenha botão inicial
        canvas.after(10, lambda: draw_main_button(main_color))
        
        # Adiciona texto
        font_family = "SF Pro Display" if platform.system() == "Darwin" else "Helvetica"
        text_id = canvas.create_text(200, 30, text=text, 
                                   fill='white', font=(font_family, 16, 'bold'),
                                   tags="main_button_text")
        
        # Funções de interação
        hover_color = self.lighten_color(main_color)
        click_color = self.darken_color(main_color)
        
        def on_enter(event):
            draw_main_button(hover_color)
            canvas.tag_raise("main_button_text")
        
        def on_leave(event):
            draw_main_button(main_color)
            canvas.tag_raise("main_button_text")
        
        def on_click(event):
            # Efeito visual de clique
            draw_main_button(click_color)
            canvas.tag_raise("main_button_text")
            canvas.after(100, lambda: draw_main_button(hover_color))
            canvas.after(150, lambda: canvas.tag_raise("main_button_text"))
            # Executa comando
            if command:
                command()
        
        def on_configure(event):
            # Redesenha quando o canvas muda de tamanho
            draw_main_button(main_color)
            canvas.tag_raise("main_button_text")
            # Reposiciona o texto no centro
            canvas.coords(text_id, event.width//2, 30)
        
        # Bind eventos
        canvas.bind("<Enter>", on_enter)
        canvas.bind("<Leave>", on_leave)
        canvas.bind("<Button-1>", on_click)
        canvas.bind("<Configure>", on_configure)
        canvas.bind("<Motion>", lambda e: canvas.config(cursor="hand2"))
        
        # Salva referências para poder alterar o texto depois
        self.main_button_canvas = canvas
        self.main_button_text_id = text_id
        self.main_button_text = text
        self.main_button_color = main_color
        
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
        placeholder = translator.get('url_placeholder')
        
        def on_focus_in(e):
            if self.url_entry.get() == placeholder:
                self.url_entry.delete(0, tk.END)
                self.url_entry.config(fg=self.colors['on_surface'])
        
        def on_focus_out(e):
            if not self.url_entry.get():
                self.url_entry.insert(0, placeholder)
                self.url_entry.config(fg=self.colors['disabled'])
        
        # Limpar conteúdo anterior antes de inserir novo placeholder
        current_content = self.url_entry.get()
        # Verifica se o conteúdo atual é um placeholder (contém "Cole a URL" ou "Paste the URL")
        is_placeholder = (not current_content or 
                         "Cole a URL" in current_content or 
                         "Paste the URL" in current_content or
                         "Pega la URL" in current_content or
                         "Collez l'URL" in current_content or
                         "Fügen Sie die URL" in current_content or
                         "Incolla l'URL" in current_content)
        
        if is_placeholder:
            self.url_entry.delete(0, tk.END)
            self.url_entry.insert(0, placeholder)
            self.url_entry.config(fg=self.colors['disabled'])
        
        # Remover binds anteriores para evitar duplicação
        self.url_entry.unbind('<FocusIn>')
        self.url_entry.unbind('<FocusOut>')
        self.url_entry.unbind('<Return>')
        
        # Adicionar novos binds
        self.url_entry.bind('<FocusIn>', on_focus_in)
        self.url_entry.bind('<FocusOut>', on_focus_out)
        
        # Bind Enter para adicionar URL
        self.url_entry.bind('<Return>', lambda e: self.add_url())

    def paste_url(self):
        """Cola URL da área de transferência"""
        try:
            clipboard_content = self.root.clipboard_get()
            placeholder = translator.get('url_placeholder')
            
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
        placeholder = translator.get('url_placeholder')
        
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
            empty_label = tk.Label(self.list_scrollable_frame, text=translator.get('no_apps_yet'),
                                  font=('Segoe UI', 11), fg=self.colors['disabled'],
                                  bg=self.colors['input_bg'])
            empty_label.pack(pady=30)
            # Atualiza status
            self.urls_status_label.config(text=translator.get('no_apps_added'), fg=self.colors['disabled'])
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
                self.urls_status_label.config(text=translator.get('apps_in_queue_single'), fg=self.colors['primary'])
            else:
                self.urls_status_label.config(text=translator.get('apps_in_queue_multiple').format(count), fg=self.colors['primary'])
        
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
        """Abre a pasta de saída (adaptado para Mac)"""
        folder = self.output_dir_var.get()
        if os.path.exists(folder):
            try:
                if platform.system() == "Darwin":  # macOS
                    subprocess.run(['open', folder])
                else:  # Windows ou outros
                    try:
                        os.startfile(folder)
                    except AttributeError:
                        subprocess.run(['xdg-open', folder])
            except Exception as e:
                messagebox.showerror("Erro", "Não foi possível abrir a pasta")
        else:
            messagebox.showerror("Erro", "Pasta não encontrada")
    
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
        """Atualiza o texto do botão principal (Canvas)"""
        if hasattr(self, 'main_button_canvas') and hasattr(self, 'main_button_text_id'):
            self.main_button_canvas.itemconfig(self.main_button_text_id, text=text)
            self.main_button_text = text
            
            # Atualiza cor baseada no texto
            if "Processando" in text or "Coletando" in text:
                new_color = self.colors['warning']  # Laranja para processando
            elif "Parar" in text:
                new_color = self.colors['error']    # Vermelho para parar
            else:
                new_color = self.colors['success']  # Verde para iniciar
                
            self.main_button_color = new_color
    
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
        """Abre um arquivo com o aplicativo padrão (adaptado para Mac)"""
        if filepath and os.path.exists(filepath):
            try:
                if platform.system() == "Darwin":  # macOS
                    subprocess.run(['open', filepath])
                else:  # Windows ou outros
                    try:
                        os.startfile(filepath)
                    except AttributeError:
                        subprocess.run(['xdg-open', filepath])
            except Exception as e:
                messagebox.showerror("Erro", "Não foi possível abrir o arquivo")
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
        # Cria a janela já na posição correta
        about_window = tk.Toplevel(self.root)
        about_window.title(translator.get('about_title'))
        self.center_window(about_window, 650, 570)  # Máximo para alemão
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

        # Cria a janela modal
        modal = tk.Toplevel(self.root)
        modal.title(translator.get('time_saved_title'))
        self.center_window(modal, window_width, window_height)
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
        
        tk.Label(title_frame, text="🎉", font=self.get_font(24),
                bg=self.colors['background']).pack(side=tk.LEFT, padx=(0, 10))
        
        tk.Label(title_frame, text=translator.get('time_saved_title'), font=self.get_font(18, 'bold'),
                fg=self.colors['primary'], bg=self.colors['background']).pack(side=tk.LEFT)
        
        # Mensagem principal mais concisa
        message_text = f"{translator.get('collection_completed')}\n{translator.get('reviews_processed').format(reviews_count)}"
        
        tk.Label(main_frame, text=message_text, font=self.get_font(12),
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
        
        tk.Label(reviews_col, text=f"📈 {translator.get('reviews_label')}", font=self.get_font(10, 'bold'),
                fg=self.colors['primary'], bg=self.colors['surface']).pack()
        
        tk.Label(reviews_col, text=f"{reviews_count:,}", font=self.get_font(18, 'bold'),
                fg=self.colors['info'], bg=self.colors['surface']).pack()
        
        # Coluna 2: Tempo economizado
        time_col = tk.Frame(highlight_content, bg=self.colors['surface'])
        time_col.pack(side=tk.RIGHT, fill=tk.X, expand=True)
        
        tk.Label(time_col, text=f"⏱️ {translator.get('time_saved_label')}", font=self.get_font(10, 'bold'),
                fg=self.colors['primary'], bg=self.colors['surface']).pack()
        
        tk.Label(time_col, text=time_saved_formatted, font=self.get_font(18, 'bold'),
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
        
        # Botão fechar usando Canvas
        close_btn_container = self.create_rounded_button(main_frame, 
                                                       translator.get('close_button'), 
                                                       modal.destroy, 
                                                       self.colors['primary'], 
                                                       width=120, height=40, font_size=11)
        close_btn_container.pack(pady=(10, 0))
        
        # Permite fechar com Enter e Escape
        modal.bind('<Return>', lambda e: modal.destroy())
        modal.bind('<Escape>', lambda e: modal.destroy())
        modal.focus_set()
    
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
    app.center_window(root)
    
    root.mainloop()

if __name__ == "__main__":
    main()
