import streamlit as st
import pandas as pd

# 1. Sayfa Konfigürasyonu ve Oxford & Gold Teması
st.set_page_config(page_title="NutriProof Expert Panel", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #00152E; color: #F8F9FA; }
    .stButton>button { background-color: #FFBF00; color: #002147; font-weight: bold; border-radius: 5px; }
    h1, h2, h3 { color: #FFBF00 !important; font-family: 'Serif'; }
    [data-testid="stMetricValue"] { color: #FFBF00 !important; }
    [data-testid="stMetric"] { background-color: #002B5B; padding: 20px; border-radius: 15px; border-left: 5px solid #FFBF00; }
    .stSlider [data-baseweb="slider"] { color: #FFBF00; }
    </style>
    """, unsafe_allow_html=True)

# 2. Sol Menü (Sidebar)
st.sidebar.markdown(f"<h2 style='color:#FFBF00;'>NUTRIPROOF</h2>", unsafe_allow_html=True)
page = st.sidebar.radio("Navigation", ["Dashboard", "Venatura Lab", "BCS Matrix"])

# 3. Sayfa İçerikleri
if page == "Dashboard":
    st.title("🏛️ NutriProof: Global Accreditation Center")
    col1, col2, col3 = st.columns(3)
    col1.metric("Scraped Products", "128", "+12 Venatura")
    col2.metric("Verified (Gold)", "45", "92% Accuracy")
    col3.metric("Pending Review", "14", "Action Required")

    st.subheader("Recent Activity")
    st.write("Venatura Magnezyum Bisglisinat verisi sisteme işlendi. Akademik onay bekleniyor.")

elif page == "Venatura Lab":
    st.title("🧪 Venatura Formulation Simulator")
    
    col_img, col_info = st.columns([1, 2])
    
    with col_img:
        st.image("https://venatura.co/wp-content/uploads/2021/04/magnezyum-bisglisinat.png", caption="Venatura Magnezyum Bisglisinat")
    
    with col_info:
        st.subheader("Academic Control Panel")
        # Senin uzmanlık alanın olan sliderlar
        bcs_class = st.select_slider("Select BCS Class", options=[1, 2, 3, 4], value=1)
        spip_coeff = st.slider("Set SPIP Permeability Coefficient", 0.0, 1.0, 0.95)
        
        # ProofScore Hesaplama Mantığı (Basit Simülasyon)
        calculated_score = int((100 / bcs_class) * spip_coeff)
        
        st.metric("Dynamic ProofScore", f"{calculated_score}/100")
        
        if st.button("APPROVE & ACCREDIT"):
            st.success(f"Venatura Magnezyum Bisglisinat was accredited with score {calculated_score}!")

    st.divider()
    st.subheader("📦 Scraped Products From Venatura")
    # Kazınan (Scraped) verileri simüle eden tablo
    venatura_data = {
        "Product Name": ["Mag. Bisglycinate", "Liposomal Vitamin C", "Vitamin D3K2", "Methylcobalamin B12"],
        "Form": ["Chelated", "Liposomal", "Oil Drop", "Sublingual"],
        "Raw Status": ["Pending", "Scraped", "Scraped", "Pending"],
        "Expert Score": [calculated_score, 98, 88, 91]
    }
    df = pd.DataFrame(venatura_data)
    st.table(df)

elif page == "BCS Matrix":
    st.title("📊 Global BCS & SPIP Master Matrix")
    st.write("Bu bölümde tüm etken maddelerin farmasötik katsayılarını Excel gibi yöneteceksiniz.")
    # İleride buraya devasa tabloyu ekleyeceğiz
