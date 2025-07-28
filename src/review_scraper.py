from google_play_scraper import app, reviews, Sort
import pandas as pd
import json
import time
import argparse
import re
from urllib.parse import parse_qs, urlparse

class GooglePlayReviewScraper:
    """Scraper otimizado para coletar reviews do Google Play Store"""
    
    def __init__(self, country='br', lang='pt'):
        self.country = country
        self.lang = lang
    
    def extract_app_id_from_url(self, url):
        """Extrai o app_id de uma URL do Google Play Store"""
        # Método mais eficiente usando parse_qs diretamente
        try:
            parsed_url = urlparse(url)
            query_params = parse_qs(parsed_url.query)
            
            if 'id' in query_params:
                return query_params['id'][0]
            
            # Fallback para regex se parse_qs falhar
            match = re.search(r'id=([^&]+)', url)
            if match:
                return match.group(1)
            
            raise ValueError("App ID não encontrado na URL")
            
        except Exception as e:
            raise ValueError(f"Erro ao processar URL: {e}")
    
    def validate_app_id(self, app_id):
        """Valida se o app_id está no formato correto"""
        return bool(re.match(r'^[a-zA-Z][a-zA-Z0-9_]*(\.[a-zA-Z][a-zA-Z0-9_]*)+$', app_id))
    
    def extract_all_reviews(self, app_id):
        """Extrai TODOS os reviews de um app do Google Play Store"""
        
        print(f"Coletando informações do app: {app_id}")
        
        # Informações básicas do app
        try:
            app_info = app(app_id, lang=self.lang, country=self.country)
            print(f"App: {app_info.get('title', 'N/A')}")
            print(f"Total de reviews: {app_info.get('reviews', 0)}")
        except Exception as e:
            print(f"Erro ao obter informações: {e}")
            app_info = {'appId': app_id, 'title': 'App desconhecido', 'error': str(e)}
        
        print("Iniciando coleta de reviews...")
        
        all_reviews = []
        continuation_token = None
        batch_count = 0
        
        while True:
            try:
                batch_count += 1
                print(f"Batch {batch_count}...")
                
                result, continuation_token = reviews(
                    app_id,
                    lang=self.lang,
                    country=self.country,
                    sort=Sort.NEWEST,
                    count=200,
                    continuation_token=continuation_token
                )
                
                if not result:
                    break
                
                # Processa reviews de forma mais eficiente
                batch_reviews = [
                    {
                        'review_id': r.get('reviewId', ''),
                        'user_name': r.get('userName', 'N/A'),
                        'content': r.get('content', 'N/A'),
                        'score': r.get('score', 0),
                        'thumbs_up_count': r.get('thumbsUpCount', 0),
                        'at': r.get('at', ''),
                        'reply_content': r.get('replyContent', ''),
                        'reply_at': r.get('repliedAt', ''),
                        'app_version': r.get('appVersion', '')
                    }
                    for r in result
                ]
                
                all_reviews.extend(batch_reviews)
                print(f"Total: {len(all_reviews)} reviews")
                
                if not continuation_token:
                    break
                
                time.sleep(0.3)  # Pausa reduzida
                
            except Exception as e:
                print(f"Erro no batch {batch_count}: {e}")
                break
        
        print(f"Coleta finalizada! Total: {len(all_reviews)} reviews")
        return all_reviews, app_info

    def save_reviews(self, reviews_data, app_info, filename_prefix=None):
        """Salva os reviews em CSV e JSON"""
        if not reviews_data:
            print("Nenhuma review para salvar")
            return
        
        # Determina nome do arquivo
        if filename_prefix is None and app_info and app_info.get('title'):
            filename_prefix = f"{self.clean_filename(app_info['title'])}_reviews"
        elif filename_prefix is None:
            filename_prefix = "google_play_reviews"
        
        # Salva CSV
        pd.DataFrame(reviews_data).to_csv(f'{filename_prefix}.csv', index=False, encoding='utf-8')
        
        # Salva JSON
        json_data = {
            'collection_info': {
                'collected_at': time.strftime('%Y-%m-%d %H:%M:%S'),
                'total_reviews': len(reviews_data),
                'country': self.country,
                'language': self.lang
            },
            'app_info': app_info or {},
            'reviews': reviews_data
        }
        
        with open(f'{filename_prefix}.json', 'w', encoding='utf-8') as f:
            json.dump(json_data, f, ensure_ascii=False, indent=2, default=str)
        
        print(f"Arquivos salvos: {filename_prefix}.csv e {filename_prefix}.json")
    
    def clean_filename(self, filename):
        """Limpa o nome do arquivo removendo caracteres inválidos"""
        # Remove caracteres inválidos e normaliza
        cleaned = re.sub(r'[<>:"/\\|?*]', '', filename)
        cleaned = re.sub(r'\s+', '_', cleaned)
        cleaned = re.sub(r'[^\w\-_.]', '', cleaned)
        cleaned = re.sub(r'_+', '_', cleaned).strip('._')
        
        return (cleaned[:40] if len(cleaned) > 40 else cleaned).lower() or "app"
    
    def show_statistics(self, reviews_data):
        """Mostra estatísticas dos reviews"""
        if not reviews_data:
            return
            
        print(f"\nEstatísticas:")
        print(f"Total: {len(reviews_data)} reviews")
        
        scores = [r['score'] for r in reviews_data if r['score']]
        if scores:
            print(f"Rating médio: {sum(scores)/len(scores):.2f}")
            for rating in range(1, 6):
                count = scores.count(rating)
                print(f"  {rating}★: {count} ({count/len(scores)*100:.1f}%)")
    
    def show_sample_reviews(self, reviews_data, count=3):
        """Mostra algumas reviews de exemplo"""
        print(f"\nPrimeiras {count} reviews:")
        
        for i, review in enumerate(reviews_data[:count], 1):
            print(f"\n{i}. {review['user_name']} ({review['score']}★)")
            print(f"   {review['content'][:80]}...")
            if review['reply_content']:
                print(f"   Resposta: {review['reply_content'][:60]}...")

def main():
    """Função principal"""
    
    # Configuração de argumentos de linha de comando
    parser = argparse.ArgumentParser(
        description='Scraper para coletar reviews do Google Play Store',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos de uso:

1. Com URL:
   python review_scraper.py --url "https://play.google.com/store/apps/details?id=com.kaizengaming.betano.brazil"

2. Com app_id:
   python review_scraper.py --app-id "com.kaizengaming.betano.brazil"

3. Especificando país e idioma:
   python review_scraper.py --url "https://play.google.com/store/apps/details?id=com.whatsapp" --country "us" --lang "en"

4. Especificando nome do arquivo:
   python review_scraper.py --url "https://play.google.com/store/apps/details?id=com.whatsapp" --output "whatsapp_reviews"
        """
    )
    
    # Grupo mutuamente exclusivo para URL ou app_id
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument('--url', '-u', 
                           help='URL do app no Google Play Store')
    input_group.add_argument('--app-id', '-a', 
                           help='ID do app (ex: com.example.app)')
    
    # Argumentos opcionais
    parser.add_argument('--country', '-c', default='br',
                       help='Código do país (padrão: br)')
    parser.add_argument('--lang', '-l', default='pt',
                       help='Código do idioma (padrão: pt)')
    parser.add_argument('--output', '-o', default='google_play_reviews',
                       help='Nome base dos arquivos de saída (padrão: google_play_reviews)')
    
    args = parser.parse_args()
    
    try:
        # Inicializa o scraper
        scraper = GooglePlayReviewScraper(country=args.country, lang=args.lang)
        
        # Determina o app_id
        if args.url:
            print(f"Processando URL: {args.url}")
            app_id = scraper.extract_app_id_from_url(args.url)
        else:
            app_id = args.app_id
            print(f"Usando app_id: {app_id}")
        
        # Valida o app_id
        if not scraper.validate_app_id(app_id):
            print(f"⚠️  Aviso: O app_id '{app_id}' pode não estar no formato correto")
        
        # Extrai todos os reviews
        reviews_data, app_info = scraper.extract_all_reviews(app_id)
        
        if reviews_data:
            # Salva os dados (usa nome do app se output não foi especificado)
            output_name = args.output if args.output != 'google_play_reviews' else None
            scraper.save_reviews(reviews_data, app_info, output_name)
            
            # Mostra estatísticas
            scraper.show_statistics(reviews_data)
            
            # Mostra exemplos
            scraper.show_sample_reviews(reviews_data)
            
        else:
            print("❌ Nenhuma review foi coletada")
            
    except Exception as e:
        print(f"❌ Erro durante a execução: {e}")

def interactive_mode():
    """Modo interativo para facilitar o uso"""
    print("🚀 Google Play Store Review Scraper")
    print("=" * 40)
    
    # Solicita URL ou app_id
    print("\nEscolha uma opção:")
    print("1. Inserir URL do Google Play Store")
    print("2. Inserir app_id diretamente")
    
    choice = input("\nOpção (1 ou 2): ").strip()
    
    scraper = GooglePlayReviewScraper()
    
    try:
        if choice == "1":
            url = input("\nCole a URL do app: ").strip()
            if not url:
                print("❌ URL não pode estar vazia")
                return
            app_id = scraper.extract_app_id_from_url(url)
        elif choice == "2":
            app_id = input("\nDigite o app_id: ").strip()
            if not app_id:
                print("❌ App_id não pode estar vazio")
                return
        else:
            print("❌ Opção inválida")
            return
        
        # Configurações opcionais
        country = input("\nPaís (padrão: br): ").strip() or 'br'
        lang = input("Idioma (padrão: pt): ").strip() or 'pt'
        output = input("Nome do arquivo (padrão: google_play_reviews): ").strip() or 'google_play_reviews'
        
        # Recria scraper com configurações
        scraper = GooglePlayReviewScraper(country=country, lang=lang)
        
        print(f"\n🔍 Iniciando coleta para: {app_id}")
        
        # Extrai reviews
        reviews_data, app_info = scraper.extract_all_reviews(app_id)
        
        if reviews_data:
            # Usa nome do app se output padrão foi mantido
            output_name = output if output != 'google_play_reviews' else None
            scraper.save_reviews(reviews_data, app_info, output_name)
            scraper.show_statistics(reviews_data)
            scraper.show_sample_reviews(reviews_data)
        else:
            print("❌ Nenhuma review foi coletada")
            
    except Exception as e:
        print(f"❌ Erro: {e}")

if __name__ == "__main__":
    import sys
    
    # Se não há argumentos, executa modo interativo
    if len(sys.argv) == 1:
        interactive_mode()
    else:
        main()