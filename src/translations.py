#!/usr/bin/env python3
"""
Sistema de traduções para Google Play Reviews Scraper
"""

TRANSLATIONS = {
    'pt': {
        # Janela principal
        'window_title': 'Google Play Reviews Scraper',
        'window_subtitle': 'Colete reviews de apps do Google Play Store',
        
        # Seções
        'url_section': 'URL do App',
        'config_section': 'Configurações',
        'progress_section': 'Progresso',
        'log_section': 'Log',
        
        # Campos
        'url_placeholder': 'Cole a URL do app do Google Play Store...',
        'app_id_label': 'App ID: {}',
        'country_label': 'País:',
        'language_label': 'Idioma:',
        'folder_label': 'Pasta:',
        
        # Botões
        'paste_button': 'Colar',
        'choose_button': 'Escolher',
        'start_button': 'Iniciar Coleta',
        'stop_button': 'Parar',
        'clear_button': 'Limpar',
        'csv_button': 'CSV',
        'json_button': 'JSON',
        'folder_button': 'Pasta',
        'close_button': 'Fechar',
        
        # Status
        'ready_status': 'Pronto para iniciar',
        'starting_status': 'Iniciando coleta...',
        'running_status': 'Executando...',
        'stopping_status': 'Parando...',
        'ready_status_bar': 'Pronto',
        'completed_status': 'Concluído: {} reviews coletadas',
        
        # Log messages
        'scraper_started': 'Scraper iniciado - Cole uma URL para começar',
        'url_pasted': 'URL colada da área de transferência',
        'folder_changed': 'Pasta alterada para: {}',
        'processing_url': 'Processando URL: {}',
        'app_id_extracted': 'App ID extraído: {}',
        'stopping_collection': 'Parando coleta...',
        'log_cleared': 'Log limpo',
        'statistics_title': 'Estatísticas:',
        'total_reviews': 'Total: {} reviews',
        'average_rating': 'Rating médio: {:.2f}',
        'rating_distribution': '{}★: {} ({:.1f}%)',
        
        # Mensagens de erro
        'error_title': 'Erro',
        'warning_title': 'Aviso',
        'error_invalid_url': 'Por favor, insira uma URL válida',
        'error_file_not_found': 'Arquivo não encontrado',
        'error_folder_not_found': 'Não foi possível abrir a pasta',
        'error_clipboard': 'Não foi possível colar da área de transferência',
        'error_invalid_url_status': 'URL inválida',
        'error_app_id_extraction': 'App ID extraído: {}',
        
        # Modal Sobre
        'about_title': 'Sobre - Google Play Reviews Scraper',
        'about_description': '''Ferramenta para extrair e analisar reviews de aplicativos do Google Play Store.

Funcionalidades:
• Extração completa de reviews
• Exportação em CSV e JSON
• Análise de ratings e estatísticas
• Interface intuitiva e fácil de usar''',
        'about_external_tool': '🔗 Ferramenta para análise dos dados:',
        'about_external_link': 'Review Stats Pro - Análise Avançada',
        'about_developed_with': 'Desenvolvido com',
        'about_developed_by': 'por',
        'about_developer': 'DSiqueira',
        
        # Países
        'countries': {
            'br': 'Brasil',
            'us': 'Estados Unidos',
            'uk': 'Reino Unido',
            'ca': 'Canadá',
            'au': 'Austrália',
            'de': 'Alemanha',
            'fr': 'França',
            'es': 'Espanha',
            'it': 'Itália'
        },
        
        # Idiomas
        'languages': {
            'pt': 'Português',
            'en': 'English',
            'es': 'Español',
            'fr': 'Français',
            'de': 'Deutsch',
            'it': 'Italiano'
        }
    },
    
    'en': {
        # Main window
        'window_title': 'Google Play Reviews Scraper',
        'window_subtitle': 'Collect app reviews from Google Play Store',
        
        # Sections
        'url_section': 'App URL',
        'config_section': 'Settings',
        'progress_section': 'Progress',
        'log_section': 'Log',
        
        # Fields
        'url_placeholder': 'Paste the Google Play Store app URL...',
        'app_id_label': 'App ID: {}',
        'country_label': 'Country:',
        'language_label': 'Language:',
        'folder_label': 'Folder:',
        
        # Buttons
        'paste_button': 'Paste',
        'choose_button': 'Choose',
        'start_button': 'Start Collection',
        'stop_button': 'Stop',
        'clear_button': 'Clear',
        'csv_button': 'CSV',
        'json_button': 'JSON',
        'folder_button': 'Folder',
        'close_button': 'Close',
        
        # Status
        'ready_status': 'Ready to start',
        'starting_status': 'Starting collection...',
        'running_status': 'Running...',
        'stopping_status': 'Stopping...',
        'ready_status_bar': 'Ready',
        'completed_status': 'Completed: {} reviews collected',
        
        # Log messages
        'scraper_started': 'Scraper started - Paste a URL to begin',
        'url_pasted': 'URL pasted from clipboard',
        'folder_changed': 'Folder changed to: {}',
        'processing_url': 'Processing URL: {}',
        'app_id_extracted': 'App ID extracted: {}',
        'stopping_collection': 'Stopping collection...',
        'log_cleared': 'Log cleared',
        'statistics_title': 'Statistics:',
        'total_reviews': 'Total: {} reviews',
        'average_rating': 'Average rating: {:.2f}',
        'rating_distribution': '{}★: {} ({:.1f}%)',
        
        # Error messages
        'error_title': 'Error',
        'warning_title': 'Warning',
        'error_invalid_url': 'Please enter a valid URL',
        'error_file_not_found': 'File not found',
        'error_folder_not_found': 'Could not open folder',
        'error_clipboard': 'Could not paste from clipboard',
        'error_invalid_url_status': 'Invalid URL',
        'error_app_id_extraction': 'App ID extracted: {}',
        
        # About modal
        'about_title': 'About - Google Play Reviews Scraper',
        'about_description': '''Tool to extract and analyze app reviews from Google Play Store.

Features:
• Complete review extraction
• CSV and JSON export
• Rating analysis and statistics
• Intuitive and easy-to-use interface''',
        'about_external_tool': '🔗 Tool for data analysis:',
        'about_external_link': 'Review Stats Pro - Advanced Analysis',
        'about_developed_with': 'Developed with',
        'about_developed_by': 'by',
        'about_developer': 'DSiqueira',
        
        # Countries
        'countries': {
            'br': 'Brazil',
            'us': 'United States',
            'uk': 'United Kingdom',
            'ca': 'Canada',
            'au': 'Australia',
            'de': 'Germany',
            'fr': 'France',
            'es': 'Spain',
            'it': 'Italy'
        },
        
        # Languages
        'languages': {
            'pt': 'Português',
            'en': 'English',
            'es': 'Español',
            'fr': 'Français',
            'de': 'Deutsch',
            'it': 'Italiano'
        }
    },
    
    'es': {
        # Ventana principal
        'window_title': 'Google Play Reviews Scraper',
        'window_subtitle': 'Recopila reseñas de apps de Google Play Store',
        
        # Secciones
        'url_section': 'URL de la App',
        'config_section': 'Configuración',
        'progress_section': 'Progreso',
        'log_section': 'Registro',
        
        # Campos
        'url_placeholder': 'Pega la URL de la app de Google Play Store...',
        'app_id_label': 'ID de App: {}',
        'country_label': 'País:',
        'language_label': 'Idioma:',
        'folder_label': 'Carpeta:',
        
        # Botones
        'paste_button': 'Pegar',
        'choose_button': 'Elegir',
        'start_button': 'Iniciar Recopilación',
        'stop_button': 'Parar',
        'clear_button': 'Limpiar',
        'csv_button': 'CSV',
        'json_button': 'JSON',
        'folder_button': 'Carpeta',
        'close_button': 'Cerrar',
        
        # Estado
        'ready_status': 'Listo para comenzar',
        'starting_status': 'Iniciando recopilación...',
        'running_status': 'Ejecutando...',
        'stopping_status': 'Parando...',
        'ready_status_bar': 'Listo',
        'completed_status': 'Completado: {} reseñas recopiladas',
        
        # Mensajes de registro
        'scraper_started': 'Scraper iniciado - Pega una URL para comenzar',
        'url_pasted': 'URL pegada del portapapeles',
        'folder_changed': 'Carpeta cambiada a: {}',
        'processing_url': 'Procesando URL: {}',
        'app_id_extracted': 'ID de App extraído: {}',
        'stopping_collection': 'Parando recopilación...',
        'log_cleared': 'Registro limpiado',
        'statistics_title': 'Estadísticas:',
        'total_reviews': 'Total: {} reseñas',
        'average_rating': 'Calificación promedio: {:.2f}',
        'rating_distribution': '{}★: {} ({:.1f}%)',
        
        # Mensajes de error
        'error_title': 'Error',
        'warning_title': 'Advertencia',
        'error_invalid_url': 'Por favor, ingresa una URL válida',
        'error_file_not_found': 'Archivo no encontrado',
        'error_folder_not_found': 'No se pudo abrir la carpeta',
        'error_clipboard': 'No se pudo pegar del portapapeles',
        'error_invalid_url_status': 'URL inválida',
        'error_app_id_extraction': 'ID de App extraído: {}',
        
        # Modal Acerca de
        'about_title': 'Acerca de - Google Play Reviews Scraper',
        'about_description': '''Herramienta para extraer y analizar reseñas de aplicaciones de Google Play Store.

Características:
• Extracción completa de reseñas
• Exportación en CSV y JSON
• Análisis de calificaciones y estadísticas
• Interfaz intuitiva y fácil de usar''',
        'about_external_tool': '🔗 Herramienta para análisis de datos:',
        'about_external_link': 'Review Stats Pro - Análisis Avanzado',
        'about_developed_with': 'Desarrollado con',
        'about_developed_by': 'por',
        'about_developer': 'DSiqueira',
        
        # Países
        'countries': {
            'br': 'Brasil',
            'us': 'Estados Unidos',
            'uk': 'Reino Unido',
            'ca': 'Canadá',
            'au': 'Australia',
            'de': 'Alemania',
            'fr': 'Francia',
            'es': 'España',
            'it': 'Italia'
        },
        
        # Idiomas
        'languages': {
            'pt': 'Português',
            'en': 'English',
            'es': 'Español',
            'fr': 'Français',
            'de': 'Deutsch',
            'it': 'Italiano'
        }
    },
    
    'fr': {
        # Fenêtre principale
        'window_title': 'Google Play Reviews Scraper',
        'window_subtitle': 'Collectez les avis d\'apps du Google Play Store',
        
        # Sections
        'url_section': 'URL de l\'App',
        'config_section': 'Paramètres',
        'progress_section': 'Progrès',
        'log_section': 'Journal',
        
        # Champs
        'url_placeholder': 'Collez l\'URL de l\'app du Google Play Store...',
        'app_id_label': 'ID App: {}',
        'country_label': 'Pays:',
        'language_label': 'Langue:',
        'folder_label': 'Dossier:',
        
        # Boutons
        'paste_button': 'Coller',
        'choose_button': 'Choisir',
        'start_button': 'Démarrer Collection',
        'stop_button': 'Arrêter',
        'clear_button': 'Effacer',
        'csv_button': 'CSV',
        'json_button': 'JSON',
        'folder_button': 'Dossier',
        'close_button': 'Fermer',
        
        # État
        'ready_status': 'Prêt à commencer',
        'starting_status': 'Démarrage de la collection...',
        'running_status': 'En cours...',
        'stopping_status': 'Arrêt...',
        'ready_status_bar': 'Prêt',
        'completed_status': 'Terminé: {} avis collectés',
        
        # Messages du journal
        'scraper_started': 'Scraper démarré - Collez une URL pour commencer',
        'url_pasted': 'URL collée du presse-papiers',
        'folder_changed': 'Dossier changé vers: {}',
        'processing_url': 'Traitement de l\'URL: {}',
        'app_id_extracted': 'ID App extrait: {}',
        'stopping_collection': 'Arrêt de la collection...',
        'log_cleared': 'Journal effacé',
        'statistics_title': 'Statistiques:',
        'total_reviews': 'Total: {} avis',
        'average_rating': 'Note moyenne: {:.2f}',
        'rating_distribution': '{}★: {} ({:.1f}%)',
        
        # Messages d'erreur
        'error_title': 'Erreur',
        'warning_title': 'Avertissement',
        'error_invalid_url': 'Veuillez saisir une URL valide',
        'error_file_not_found': 'Fichier non trouvé',
        'error_folder_not_found': 'Impossible d\'ouvrir le dossier',
        'error_clipboard': 'Impossible de coller du presse-papiers',
        'error_invalid_url_status': 'URL invalide',
        'error_app_id_extraction': 'ID App extrait: {}',
        
        # Modal À propos
        'about_title': 'À propos - Google Play Reviews Scraper',
        'about_description': '''Outil pour extraire et analyser les avis d\'applications du Google Play Store.

Fonctionnalités:
• Extraction complète des avis
• Export en CSV et JSON
• Analyse des notes et statistiques
• Interface intuitive et facile à utiliser''',
        'about_external_tool': '🔗 Outil pour l\'analyse des données:',
        'about_external_link': 'Review Stats Pro - Analyse Avancée',
        'about_developed_with': 'Développé avec',
        'about_developed_by': 'par',
        'about_developer': 'DSiqueira',
        
        # Pays
        'countries': {
            'br': 'Brésil',
            'us': 'États-Unis',
            'uk': 'Royaume-Uni',
            'ca': 'Canada',
            'au': 'Australie',
            'de': 'Allemagne',
            'fr': 'France',
            'es': 'Espagne',
            'it': 'Italie'
        },
        
        # Langues
        'languages': {
            'pt': 'Português',
            'en': 'English',
            'es': 'Español',
            'fr': 'Français',
            'de': 'Deutsch',
            'it': 'Italiano'
        }
    },
    
    'de': {
        # Hauptfenster
        'window_title': 'Google Play Reviews Scraper',
        'window_subtitle': 'Sammeln Sie App-Bewertungen aus dem Google Play Store',
        
        # Abschnitte
        'url_section': 'App-URL',
        'config_section': 'Einstellungen',
        'progress_section': 'Fortschritt',
        'log_section': 'Protokoll',
        
        # Felder
        'url_placeholder': 'Google Play Store App-URL einfügen...',
        'app_id_label': 'App-ID: {}',
        'country_label': 'Land:',
        'language_label': 'Sprache:',
        'folder_label': 'Ordner:',
        
        # Schaltflächen
        'paste_button': 'Einfügen',
        'choose_button': 'Wählen',
        'start_button': 'Sammlung Starten',
        'stop_button': 'Stoppen',
        'clear_button': 'Löschen',
        'csv_button': 'CSV',
        'json_button': 'JSON',
        'folder_button': 'Ordner',
        'close_button': 'Schließen',
        
        # Status
        'ready_status': 'Bereit zum Starten',
        'starting_status': 'Sammlung wird gestartet...',
        'running_status': 'Läuft...',
        'stopping_status': 'Wird gestoppt...',
        'ready_status_bar': 'Bereit',
        'completed_status': 'Abgeschlossen: {} Bewertungen gesammelt',
        
        # Protokollnachrichten
        'scraper_started': 'Scraper gestartet - URL einfügen zum Beginnen',
        'url_pasted': 'URL aus Zwischenablage eingefügt',
        'folder_changed': 'Ordner geändert zu: {}',
        'processing_url': 'URL wird verarbeitet: {}',
        'app_id_extracted': 'App-ID extrahiert: {}',
        'stopping_collection': 'Sammlung wird gestoppt...',
        'log_cleared': 'Protokoll gelöscht',
        'statistics_title': 'Statistiken:',
        'total_reviews': 'Gesamt: {} Bewertungen',
        'average_rating': 'Durchschnittsbewertung: {:.2f}',
        'rating_distribution': '{}★: {} ({:.1f}%)',
        
        # Fehlermeldungen
        'error_title': 'Fehler',
        'warning_title': 'Warnung',
        'error_invalid_url': 'Bitte geben Sie eine gültige URL ein',
        'error_file_not_found': 'Datei nicht gefunden',
        'error_folder_not_found': 'Ordner konnte nicht geöffnet werden',
        'error_clipboard': 'Konnte nicht aus Zwischenablage einfügen',
        'error_invalid_url_status': 'Ungültige URL',
        'error_app_id_extraction': 'App-ID extrahiert: {}',
        
        # Über-Dialog
        'about_title': 'Über - Google Play Reviews Scraper',
        'about_description': '''Tool zum Extrahieren und Analysieren von App-Bewertungen aus dem Google Play Store.

Funktionen:
• Vollständige Bewertungsextraktion
• Export in CSV und JSON
• Bewertungsanalyse und Statistiken
• Intuitive und benutzerfreundliche Oberfläche''',
        'about_external_tool': '🔗 Tool für Datenanalyse:',
        'about_external_link': 'Review Stats Pro - Erweiterte Analyse',
        'about_developed_with': 'Entwickelt mit',
        'about_developed_by': 'von',
        'about_developer': 'DSiqueira',
        
        # Länder
        'countries': {
            'br': 'Brasilien',
            'us': 'Vereinigte Staaten',
            'uk': 'Vereinigtes Königreich',
            'ca': 'Kanada',
            'au': 'Australien',
            'de': 'Deutschland',
            'fr': 'Frankreich',
            'es': 'Spanien',
            'it': 'Italien'
        },
        
        # Sprachen
        'languages': {
            'pt': 'Português',
            'en': 'English',
            'es': 'Español',
            'fr': 'Français',
            'de': 'Deutsch',
            'it': 'Italiano'
        }
    },
    
    'it': {
        # Finestra principale
        'window_title': 'Google Play Reviews Scraper',
        'window_subtitle': 'Raccogli recensioni di app dal Google Play Store',
        
        # Sezioni
        'url_section': 'URL dell\'App',
        'config_section': 'Impostazioni',
        'progress_section': 'Progresso',
        'log_section': 'Registro',
        
        # Campi
        'url_placeholder': 'Incolla l\'URL dell\'app del Google Play Store...',
        'app_id_label': 'ID App: {}',
        'country_label': 'Paese:',
        'language_label': 'Lingua:',
        'folder_label': 'Cartella:',
        
        # Pulsanti
        'paste_button': 'Incolla',
        'choose_button': 'Scegli',
        'start_button': 'Inizia Raccolta',
        'stop_button': 'Ferma',
        'clear_button': 'Pulisci',
        'csv_button': 'CSV',
        'json_button': 'JSON',
        'folder_button': 'Cartella',
        'close_button': 'Chiudi',
        
        # Stato
        'ready_status': 'Pronto per iniziare',
        'starting_status': 'Avvio raccolta...',
        'running_status': 'In esecuzione...',
        'stopping_status': 'Fermando...',
        'ready_status_bar': 'Pronto',
        'completed_status': 'Completato: {} recensioni raccolte',
        
        # Messaggi del registro
        'scraper_started': 'Scraper avviato - Incolla un URL per iniziare',
        'url_pasted': 'URL incollato dagli appunti',
        'folder_changed': 'Cartella cambiata in: {}',
        'processing_url': 'Elaborazione URL: {}',
        'app_id_extracted': 'ID App estratto: {}',
        'stopping_collection': 'Fermando raccolta...',
        'log_cleared': 'Registro pulito',
        'statistics_title': 'Statistiche:',
        'total_reviews': 'Totale: {} recensioni',
        'average_rating': 'Valutazione media: {:.2f}',
        'rating_distribution': '{}★: {} ({:.1f}%)',
        
        # Messaggi di errore
        'error_title': 'Errore',
        'warning_title': 'Avviso',
        'error_invalid_url': 'Inserisci un URL valido',
        'error_file_not_found': 'File non trovato',
        'error_folder_not_found': 'Impossibile aprire la cartella',
        'error_clipboard': 'Impossibile incollare dagli appunti',
        'error_invalid_url_status': 'URL non valido',
        'error_app_id_extraction': 'ID App estratto: {}',
        
        # Finestra Informazioni
        'about_title': 'Informazioni - Google Play Reviews Scraper',
        'about_description': '''Strumento per estrarre e analizzare recensioni di app dal Google Play Store.

Caratteristiche:
• Estrazione completa delle recensioni
• Esportazione in CSV e JSON
• Analisi delle valutazioni e statistiche
• Interfaccia intuitiva e facile da usare''',
        'about_external_tool': '🔗 Strumento per analisi dati:',
        'about_external_link': 'Review Stats Pro - Analisi Avanzata',
        'about_developed_with': 'Sviluppato con',
        'about_developed_by': 'da',
        'about_developer': 'DSiqueira',
        
        # Paesi
        'countries': {
            'br': 'Brasile',
            'us': 'Stati Uniti',
            'uk': 'Regno Unito',
            'ca': 'Canada',
            'au': 'Australia',
            'de': 'Germania',
            'fr': 'Francia',
            'es': 'Spagna',
            'it': 'Italia'
        },
        
        # Lingue
        'languages': {
            'pt': 'Português',
            'en': 'English',
            'es': 'Español',
            'fr': 'Français',
            'de': 'Deutsch',
            'it': 'Italiano'
        }
    }
}

class Translator:
    def __init__(self, language='pt'):
        self.current_language = language
        self.translations = TRANSLATIONS
    
    def set_language(self, language):
        """Define o idioma atual"""
        if language in self.translations:
            self.current_language = language
            return True
        return False
    
    def get(self, key, *args):
        """Obtém uma tradução"""
        try:
            text = self.translations[self.current_language][key]
            if args:
                return text.format(*args)
            return text
        except KeyError:
            # Fallback para português se a chave não existir
            try:
                text = self.translations['pt'][key]
                if args:
                    return text.format(*args)
                return text
            except KeyError:
                return f"[{key}]"  # Mostra a chave se não encontrar tradução
    
    def get_available_languages(self):
        """Retorna lista de idiomas disponíveis"""
        return list(self.translations.keys())
    
    def get_language_name(self, lang_code):
        """Retorna o nome do idioma"""
        return self.get('languages').get(lang_code, lang_code)
    
    def get_country_name(self, country_code):
        """Retorna o nome do país"""
        return self.get('countries').get(country_code, country_code)

# Instância global do tradutor
translator = Translator()