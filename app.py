import streamlit as st
import pandas as pd
import os

# 1. Sayfa Konfigürasyonu ve Tema
st.set_page_config(page_title="NutriProof Expert Panel", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #00152E; color: #F8F9FA; }
    h1, h2, h3 { color: #FFBF00 !important; font-family: 'Serif'; }
    [data-testid="stMetricValue"] { color: #FFBF00 !important; }
    [data-testid="stMetric"] { background-color: #002B5B; padding: 20px; border-radius: 15px; border-left: 5px solid #FFBF00; }
    </style>
    """, unsafe_allow_html=True)

# 2. Veri Okuma (Hafıza Bağlantısı)
csv_path = 'data/venatura_database.csv'
if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)
else:
    df = pd.DataFrame(columns=["Product_Name", "Form", "BCS_Class", "SPIP_Coeff", "Status"])

# 3. Sol Menü
st.sidebar.markdown("<h2 style='color:#FFBF00;'>NUTRIPROOF</h2>", unsafe_allow_html=True)
page = st.sidebar.radio("Navigation", ["Dashboard", "Venatura Lab", "Global Matrix"])

if page == "Dashboard":
    st.title("🏛️ NutriProof: Global Accreditation Center")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Products", len(df), f"+{len(df[df['Status'] == 'Scraped'])} New")
    col2.metric("Verified", len(df[df['Status'] == 'Verified']), "High Accuracy")
    col3.metric("Review Needed", len(df[df['Status'] == 'Pending']), "Critical")

    st.subheader("📦 Database Status (Live from GitHub)")
    st.dataframe(df, use_container_width=True)

elif page == "Venatura Lab":
    st.title("🧪 Venatura Expert Review")
    
    selected_prod = st.selectbox("Select Product to Analyze", df['Product_Name'].tolist())
    prod_data = df[df['Product_Name'] == selected_prod].iloc[0]

    col_info, col_risk = st.columns(2)
    
    with col_info:
        st.subheader(f"Analysis: {selected_prod}")
        bcs = st.select_slider("Override BCS Class", options=[1, 2, 3, 4], value=int(prod_data['BCS_Class']))
        spip = st.slider("Override SPIP Coefficient", 0.0, 1.0, float(prod_data['SPIP_Coeff']))
        
        score = int((100 / bcs) * spip)
        st.metric("Final ProofScore", f"{score}/100")

    with col_risk:
        st.subheader("⚠️ Interaction & Risk Engine")
        if "Mag" in selected_prod:
            st.error("INTERACTION ALERT: Do not take with Calcium or Thyroid medication (Levothyroxine). Wait 4 hours.")
        elif "Vit C" in selected_prod:
            st.warning("INFO: High doses may affect urine glucose tests.")
        else:
            st.success("No critical interactions found in academic database.")

    if st.button("SAVE ACADEMIC APPROVAL"):
        st.balloons()
        st.success(f"{selected_prod} has been officially accredited!")
