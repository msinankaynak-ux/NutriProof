import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_venatura_data():
    url = "https://venatura.com.tr/urunler/" # Venatura'nın ana ürün listesi
    headers = {'User-Agent': 'NutriProof-Academic-Bot/1.0'}
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    products = []
    # Ürün isimlerini ve linklerini topluyoruz
    items = soup.find_all('h2', class_='woocommerce-loop-product__title')
    
    for item in items:
        name = item.get_text().strip()
        # Farmakokinetik tahminler (Şimdilik bot otomatik yapıyor, sen onaylayacaksın)
        bcs = 1 if "Bisglisinat" in name or "Lipozomal" in name else 2
        spip = 0.95 if bcs == 1 else 0.70
        
        products.append({
            "Product_Name": name,
            "Form": "Scraped", 
            "BCS_Class": bcs,
            "SPIP_Coeff": spip,
            "Status": "Scraped"
        })
    
    return pd.DataFrame(products)

# Veriyi çek ve CSV dosyasına kaydet
# Bu işlem, Dashboard'daki tabloyu otomatik güncelleyecek
new_data = get_venatura_data()
new_data.to_csv('data/venatura_database.csv', index=False)
print("Venatura verileri başarıyla kazındı ve tabloya işlendi!")
