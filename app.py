import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import os
import time

# 1. Sayfa Ayarları
st.set_page_config(page_title="NutriProof Expert Panel", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #00152E; color: #F8F9FA; }
    h1, h2, h3 { color: #FFBF00 !important; font-family: 'Serif'; }
    [data-testid="stMetricValue"] { color: #FFBF00 !important; }
    [data-testid="stMetric"] { background-color: #002B5B; padding: 20px; border-radius: 15px; border-left: 5px solid #FFBF00; }
    .stButton>button { background-color: #FFBF00; color: #002147; font-weight: bold; width: 100%; border: none; height: 3em;}
    </style>
    """, unsafe_allow_html=True)

CSV_PATH = 'data/venatura_database.csv'

def run_advanced_scraper():
    # Bu sefer doğrudan ürünler sayfasına değil, ana katalog üzerinden sızıyoruz
    url = "https://venatura.co/urunler/" 
    
    # Sunucuyu kandırmak için en gelişmiş Header seti
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3',
        'Referer': 'https://www.google.com/',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }

    try:
        session = requests.Session()
        # Önce ana sayfaya bir "çerez" (cookie) bırakalım ki yabancı durmayalım
        session.get("https://venatura.co/", headers=headers, timeout=10, verify=False)
        time.sleep(1) # İnsansı bir duraksama
        
        response = session.get(url, headers=headers, timeout=15, verify=False)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        products = []
        
        # Venatura'nın ürün başlıklarını yakalayan seçiciler
        items = soup.find_all(['h2', 'h3'], class_='woocommerce-loop-product__title')
        
        if not items: # Alternatif seçici
            items = soup.select('.product-title') or soup.select('.entry-title')

        for item in items:
            name = item.get_text().strip()
            if len(name) > 3:
                # Akademik ön tahmin mantığı (Senin BCS uzmanlığın için temel)
                is_premium = any(x in name.lower() for x in ["bisglisinat", "lipozomal", "şelat", "piko"])
                bcs = 1 if is_premium else 2
                products.append({
                    "Product_Name": name,
                    "Form": "Auto-Detected", 
                    "BCS_Class": bcs,
                    "SPIP_Coeff": 0.95 if bcs == 1 else 0.75,
                    "Status": "Scraped"
                })
        
        if products:
            new_df = pd.DataFrame(products)
            new_df.to_csv(CSV_PATH, index=False)
            return len(products)
        return 0
    except Exception as e:
        st.sidebar.error(f"Detaylı Hata: {e}")
        return -1

# 3. Arayüz Mantığı
if os.path.exists(CSV_PATH):
    df = pd.read_csv(CSV_PATH)
else:
    df = pd.DataFrame(columns=["Product_Name", "Form", "BCS_Class", "SPIP_Coeff", "Status"])

st.sidebar.markdown("<h2 style='color:#FFBF00;'>NUTRIPROOF</h2>", unsafe_allow_html=True)

if st.sidebar.button("🚀 FORCE LIVE SCRAPE"):
    with st.sidebar.status("Bypassing Server Guards..."):
        count = run_advanced_scraper()
        if count > 0:
            st.sidebar.success(f"Başarılı! {count} Ürün Çekildi.")
            time.sleep(1)
            st.rerun()
        elif count == 0:
            st.sidebar.warning("Bağlantı kuruldu ama ürün bulunamadı.")

page = st.sidebar.radio("Navigation", ["Dashboard", "Venatura Lab"])

if page == "Dashboard":
    st.title("🏛️ NutriProof: Global Accreditation Center")
    st.metric("Live Inventory", len(df), delta=f"{len(df)} Products Detected")
    st.dataframe(df, use_container_width=True)
