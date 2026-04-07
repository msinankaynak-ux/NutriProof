import streamlit as st
import pandas as pd
import os

# 1. Sayfa Ayarları
st.set_page_config(page_title="NutriProof Expert Panel", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #00152E; color: #F8F9FA; }
    h1, h2, h3 { color: #FFBF00 !important; font-family: 'Serif'; }
    [data-testid="stMetricValue"] { color: #FFBF00 !important; }
    [data-testid="stMetric"] { background-color: #002B5B; padding: 20px; border-radius: 15px; border-left: 5px solid #FFBF00; }
    .stTextArea textarea { background-color: #002B5B; color: #F8F9FA; border: 1px solid #FFBF00; }
    </style>
    """, unsafe_allow_html=True)

CSV_PATH = 'data/venatura_database.csv'

# Veri Yükleme
def load_data():
    if os.path.exists(CSV_PATH):
        return pd.read_csv(CSV_PATH)
    return pd.DataFrame(columns=["Product_Name", "Form", "BCS_Class", "SPIP_Coeff", "Status"])

df = load_data()

st.sidebar.markdown("<h2 style='color:#FFBF00;'>NUTRIPROOF</h2>", unsafe_allow_html=True)
page = st.sidebar.radio("Navigation", ["Dashboard", "AI Data Entry", "Venatura Lab"])

if page == "Dashboard":
    st.title("🏛️ NutriProof: Global Accreditation Center")
    st.metric("Inventory", len(df), delta="Live Data")
    st.dataframe(df, use_container_width=True)

elif page == "AI Data Entry":
    st.title("🧠 AI-Powered Academic Entry")
    st.write("Venatura sitesinden kopyaladığınız ürün listesini buraya yapıştırın.")
    
    raw_text = st.text_area("Paste Raw Product Data Here:", height=200, placeholder="Örn: Venatura Magnezyum Bisglisinat 60 Tablet...")
    
    if st.button("PROCESS & ADD TO DATABASE"):
        lines = raw_text.split('\n')
        new_entries = []
        for line in lines:
            if len(line.strip()) > 5:
                # Akıllı analiz (BCS ve SPIP Tahminleme)
                name = line.strip()
                bcs = 1 if any(x in name.lower() for x in ["bisglisinat", "lipozomal", "şelat"]) else 2
                new_entries.append({
                    "Product_Name": name,
                    "Form": "AI-Parsed",
                    "BCS_Class": bcs,
                    "SPIP_Coeff": 0.95 if bcs == 1 else 0.75,
                    "Status": "Pending Review"
                })
        
        if new_entries:
            new_df = pd.concat([df, pd.DataFrame(new_entries)], ignore_index=True)
            new_df.drop_duplicates(subset=['Product_Name'], keep='last', inplace=True)
            new_df.to_csv(CSV_PATH, index=False)
            st.success(f"{len(new_entries)} yeni ürün akademik envantere eklendi!")
            st.rerun()

elif page == "Venatura Lab":
    st.title("🧪 Expert Analysis Lab")
    if not df.empty:
        selected_prod = st.selectbox("Select Product", df['Product_Name'].tolist())
        # Burada senin BCS/SPIP sliderların olacak
        st.info(f"Analyzing: {selected_prod}")
    else:
        st.warning("Henüz veri girişi yapılmadı!")
