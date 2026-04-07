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

# 2. Veri Fonksiyonları
CSV_PATH = 'data/venatura_database.csv'

def load_data():
    if os.path.exists(CSV_PATH):
        return pd.read_csv(CSV_PATH)
    return pd.DataFrame(columns=["Product_Name", "Form", "BCS_Class", "SPIP_Coeff", "Status"])

def run_scraper():
    url = "https://venatura.co/urunler/"
    headers = {'User-Agent': 'NutriProof-Academic-Bot/1.0'}
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        products = []
        items = soup.find_all('h2', class_='woocommerce-loop-product__title')
        
        for item in items:
            name = item.get_text().strip()
            # Senin kriterlerine göre basit tahminleme
            bcs = 1 if any(x in name for x in ["Bisglisinat", "Lipozomal", "Şelat"]) else 2
            products.append({
                "Product_Name": name,
                "Form": "Auto-Scraped", 
                "BCS_Class": bcs,
                "SPIP_Coeff": 0.95 if bcs == 1 else 0.70,
                "Status": "Pending Approval"
            })
        new_df = pd.DataFrame(products)
        new_df.to_csv(CSV_PATH, index=False)
        return True
    except Exception as e:
        st.error(f"Error: {e}")
        return False

# 3. Arayüz
df = load_data()

st.sidebar.markdown("<h2 style='color:#FFBF00;'>NUTRIPROOF</h2>", unsafe_allow_html=True)
if st.sidebar.button("🚀 RUN LIVE SCRAPER"):
    with st.sidebar.status("Scanning Venatura..."):
        if run_scraper():
            st.sidebar.success("Scraping Complete!")
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
        # Analiz ve onaylama mantığı buraya gelecek
        st.info(f"Analyzing: {selected_prod}")
    else:
        st.warning("Please run the scraper first from the sidebar!")
