import streamlit as st
import joblib
import numpy as np
import base64

# Load model
model = joblib.load("house_price_model.pkl")

# Optional: Set a background image
def set_bg_from_local(image_file):
    with open(image_file, "rb") as file:
        encoded_string = base64.b64encode(file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded_string}");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Optional background
#set_bg_from_local("background.jpg")  # Replace with your image filename

# Page title
st.markdown(
    """
    <h1 style='text-align: center; font-size: 48px; color: #f0f0f0;'>🏡 House Price Predictor</h1>
    <p style='text-align: center; font-size: 22px; color: #e0e0e0;'>Estimate housing prices with just a few inputs</p>
    <hr style='border: 1px solid #aaa;'/>
    """,
    unsafe_allow_html=True
)

# Input section heading
st.markdown(
    "<h3 style='color:#ffffff; font-size: 26px; margin-top: 40px;'>Enter House Features:</h3>",
    unsafe_allow_html=True
)

# Input layout with 3 columns (spacer in center)
col1, col_space, col2 = st.columns([1.8, 0.4, 1.8])

with col1:
    overall_qual = st.slider("Overall Quality (1=Poor, 10=Excellent)", 1, 10, 5, key="overall_qual")
    gr_liv_area = st.slider("Above Ground Living Area (sq ft)", 500, 4000, 1500, step=100, key="gr_liv_area")
    garage_cars = st.slider("Number of Garage Cars", 0, 4, 2, key="garage_cars")

with col2:
    total_bsmt_sf = st.slider("Total Basement Area (sq ft)", 0, 2000, 800, step=100, key="total_bsmt_sf")
    first_flr_sf = st.slider("First Floor Area (sq ft)", 500, 2500, 1000, step=100, key="first_flr_sf")
    full_bath = st.slider("Number of Full Bathrooms", 0, 4, 2, key="full_bath")

# Style for button
st.markdown("""
    <style>
    div.stButton > button {
        background-color: #00aaff;
        color: white;
        font-size: 22px;
        padding: 0.6em 2em;
        border-radius: 12px;
        margin-top: 30px;
    }
    </style>
    """, unsafe_allow_html=True)

# Predict button
if st.button("Estimate Price"):
    input_data = np.array([[overall_qual, gr_liv_area, garage_cars, total_bsmt_sf, first_flr_sf, full_bath]])
    prediction = model.predict(input_data)[0]

    # Result box
    st.markdown(
        f"""
        <div style='padding: 1.5em; background-color: #1e3c4c; border-radius: 12px; text-align: center; margin-top: 2em;'>
            <h2 style='color: #00ffcc; font-size: 32px;'>💰 Estimated House Price: ${prediction:,.0f}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )
