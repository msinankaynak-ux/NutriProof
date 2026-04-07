import requests
from bs4 import BeautifulSoup

class VenaturaCrawler:
    def __init__(self):
        self.base_url = "https://venatura.co/urunler/"
        self.headers = {'User-Agent': 'NutriProof-Academic-Bot/1.0'}

    def get_all_product_links(self):
        # Tüm ürün linklerini toplar
        response = requests.get(self.base_url, headers=self.headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        links = [a['href'] for a in soup.select('.product-loop-title a')]
        return links

    def parse_product_details(self, url):
        # Ürün içindeki mg, form ve yardımcı maddeleri ayıklar
        # Oxford Mavisi panelde senin önüne düşecek ham veriyi hazırlar
        pass
