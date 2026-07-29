import os
import pickle
import pandas as pd
import streamlit as st

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


model_path = os.path.join(
    BASE_DIR,
    "models",
    "ShippingCostPredication.pkl"
)

encoder_path = os.path.join(
    BASE_DIR,
    "models",
    "encoder.pkl"
)


model = pickle.load(open(model_path, "rb"))
encoder = pickle.load(open(encoder_path, "rb"))

# Page configuration
st.set_page_config(page_title="Shipping Cost Prediction",page_icon="🚢",layout="centered")

st.title("🚢 Shipping Cost Prediction")
st.write("Enter shipment details to predict shipping cost")

css_path = os.path.join(BASE_DIR, "style.css")

with open(css_path, encoding="utf-8") as f:
    css = f.read()

st.markdown(
    f"<style>{css}</style>",
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

# Input fields

    trade_direction = st.selectbox("Trade Direction", ["Export", "Import"])

    cargo_type = st.selectbox("Cargo Type", ["Electronics", "Crude Oil", "Machinery", "Steel Coils", "Rice", "Wheat", "Textiles", "Fuel Oil"])

    incoterms = st.selectbox("Incoterms",["EXW","CFR","DDP","FOB","FAS","CIF"])

    port_loading = st.selectbox("Port of Loading",["Karachi Port","Port Qasim, Karachi","Gwadar Port","Singapore","Rotterdam, Netherlands","Hamburg, Germany"])

with col2:

    port_discharge = st.selectbox("Port of Discharge",["Singapore","Karachi Port","Port Qasim, Karachi","Rotterdam, Netherlands","Hamburg, Germany"])

    vessel_type = st.selectbox("Vessel Type",["Container Ship","Bulk Carrier (Handymax)","General Cargo Ship","VLCC","MR Tanker"])

    cargo_volume = st.number_input("Cargo Volume (MT)",min_value=2016.85,value=299985.15)

    transit_days = st.number_input("Transit Days",min_value=5.0,value=35.0)


# -----------------------------
# Predict Button + Model Cards
# -----------------------------

col_btn, col_acc, col_model, col_features = st.columns([3,1,1,1])


with col_btn:
    predict = st.button("Predict")


with col_acc:
    st.markdown("""
    <div class="mini-card">
        <div class="card-title">74.2%</div>
        <div class="card-subtitle">Model Accuracy</div>
    </div>
    """, unsafe_allow_html=True)


with col_model:
    st.markdown("""
    <div class="mini-card">
        <div class="card-title">GBoostingRegressor</div>
        <div class="card-subtitle">Training Algorithm</div>
    </div>
    """, unsafe_allow_html=True)


with col_features:
    st.markdown("""
    <div class="mini-card">
        <div class="card-title">8</div>
        <div class="card-subtitle">Features</div>
    </div>
    """, unsafe_allow_html=True)

if predict:

    categorical = pd.DataFrame([{
        "Trade_Direction": trade_direction,
        "Cargo_Type": cargo_type,
        "Incoterms": incoterms,
        "Port_of_Loading": port_loading,
        "Port_of_Discharge": port_discharge,
        "Vessel_Type": vessel_type
    }])

    encoded = encoder.transform(categorical).toarray()

    numerical = [
        cargo_volume,
        transit_days
    ]

    features = [numerical + encoded[0].tolist()]

    prediction = model.predict(features)

    st.success(
        f"Estimated Shipping Cost: ${prediction[0]:,.2f}"
    )
