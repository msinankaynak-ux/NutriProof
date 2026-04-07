import streamlit as st
import pandas as pd

# 1. Oxford & Gold Teması Ayarları
st.set_page_config(page_title="NutriProof Expert Panel", layout="wide")

# Özel CSS ile Oxford Mavisi ve Gold Amber dokunuşu
st.markdown("""
    <style>
    .main { background-color: #00152E; color: #F8F9FA; }
    .stButton>button { background-color: #FFBF00; color: #002147; font-weight: bold; }
    h1, h2, h3 { color: #FFBF00 !important; font-family: 'Serif'; }
    .stMetric { background-color: #002B5B; padding: 15px; border-radius: 10px; border-left: 5px solid #FFBF00; }
    </style>
    """, unsafe_allow_view_allowed=True)

# 2. Sidebar (Sol Menü)
st.sidebar.image("https://via.placeholder.com/150?text=NutriProof", width=100)
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Dashboard", "Venatura Analysis", "BCS Matrix"])

# 3. Ana Panel
if page == "Dashboard":
    st.title("🏛️ NutriProof: Global Accreditation Center")
    col1, col2, col3 = st.columns(3)
    col1.metric("Scraped Products", "128", "+12 this week")
    col2.metric("Verified (Gold)", "45", "92%")
    col3.metric("Pending Review", "14", "-2")

    st.subheader("Recent Activity: Venatura Magnezyum Bisglisinat")
    st.write("Current ProofScore: **94** (Class 1 Confirmed)")

elif page == "Venatura Analysis":
    st.title("🧪 Venatura Formulation Lab")
    # Burada senin o meşhur Magnezyum verisini analiz edeceğiz
    st.info("Venatura Magnezyum Bisglisinat verisi başarıyla kazındı. Onay bekleniyor.")
    
    bcs_val = st.selectbox("Select BCS Class for Magnesium Bisglycinate", [1, 2, 3, 4])
    st.write(f"When BCS is Class {bcs_val}, Total Bioavailability is optimized.")
