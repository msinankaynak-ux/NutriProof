import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import os

# 1. Sayfa Konfigürasyonu
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

def load_data():
    if os.path.exists(CSV_PATH):
        return pd.read_csv(CSV_PATH)
    return pd.DataFrame(columns=["Product_Name", "Form", "BCS_Class", "SPIP_Coeff", "Status"])

def run_scraper():
    # B PLANI: Daha dayanıklı bağlantı ayarları
    url = "https://venatura.com.tr/urunlerimiz/" # Alternatif adres
    # Gerçek bir tarayıcı gibi davranması için "User-Agent" ekliyoruz
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        # verify=False ekleyerek SSL sertifika hatalarını (HTTPS) geçiyoruz
        response = requests.get(url, headers=headers, timeout=15, verify=False)
        response.raise_for_status() # Hata varsa yakala
        
        soup = BeautifulSoup(response.content, 'html.parser')
        products = []
        
        # com.tr sitesindeki farklı kod yapısına (h3 veya h2) göre tarıyoruz
        items = soup.select('h3') or soup.select('h2')
        
        for item in items:
            name = item.get_text().strip()
            if len(name) > 5: # Çok kısa ve anlamsız isimleri ele
                bcs = 1 if any(x in name.lower() for x in ["bisglisinat", "lipozomal", "şelat"]) else 2
                products.append({
                    "Product_Name": name,
                    "Form": "Auto-Scraped", 
                    "BCS_Class": bcs,
                    "SPIP_Coeff": 0.95 if bcs == 1 else 0.70,
                    "Status": "Pending Approval"
                })
        
        if products:
            new_df = pd.DataFrame(products)
            new_df.to_csv(CSV_PATH, index=False)
            return True
        return False
    except Exception as e:
        st.sidebar.error(f"Bağlantı Hatası: {e}")
        return False

# 3. Arayüz
df = load_data()

st.sidebar.markdown("<h2 style='color:#FFBF00;'>NUTRIPROOF</h2>", unsafe_allow_html=True)
if st.sidebar.button("🚀 RUN LIVE SCRAPER"):
    with st.sidebar.status("Venatura Veritabanına Erişiliyor..."):
        if run_scraper():
            st.sidebar.success("Tarama Başarılı!")
            st.rerun()

page = st.sidebar.radio("Navigation", ["Dashboard", "Venatura Lab", "Global Matrix"])

if page == "Dashboard":
    st.title("🏛️ NutriProof: Global Accreditation Center")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Scraped", len(df))
    col2.metric("Verified", len(df[df['Status'] == 'Verified']))
    col3.metric("Review Needed", len(df[df['Status'] == 'Pending Approval']))

    st.subheader("📦 Academic Database (Live)")
    st.dataframe(df, use_container_width=True)

elif page == "Venatura Lab":
    st.title("🧪 Expert Analysis Lab")
    if not df.empty:
        selected_prod = st.selectbox("Select Product", df['Product_Name'].tolist())
        st.info(f"Analyzing: {selected_prod}")
    else:
        st.warning("Please run the scraper first from the sidebar!")
