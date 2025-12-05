# app.py

import streamlit as st
import pickle
import numpy as np
from PIL import Image

# Load Model
model = pickle.load(open("model.pkl", "rb"))

# Prediction Function
def predict(house_age, distance_to_nearest_metro, land_area_sqft, number_of_rooms, no_of_nearby_stores):
    data_list = [distance_to_nearest_metro, house_age, land_area_sqft, number_of_rooms, no_of_nearby_stores]
    array = np.array(data_list, np.float64)
    prediction = model.predict([array])
    return prediction

# Streamlit App UI
def main():
    st.title("HOUSE PRICE PREDICTION SYSTEM")

    # Header
    html_temp = """
    <div style="background-color:black;padding:10px;">
    <h2 style="color:white;text-align:center;">House Price Prediction</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    # House Image
    img = Image.open("beautiful-exterior-home-pictures-new-home-design-images-modern-best-house-design-images-best-house-images-images-latest-168696855.webp")
    st.image(img, width=350, caption="House Worth Prediction")

    # User Inputs
    house_age = st.number_input("House Age (years)", min_value=0, max_value=200, value=10)
    distance_to_nearest_metro = st.number_input("Distance to Nearest Metro (km)", min_value=0.0, value=2.5)
    land_area_sqft = st.number_input("Land Area (sqft)", min_value=200, max_value=20000, value=1500)
    number_of_rooms = st.number_input("Number of Rooms", min_value=1, max_value=30, value=3)
    no_of_nearby_stores = st.number_input("Nearby Stores Count", min_value=0, max_value=100, value=10)

    # Prediction Button
    if st.button("Predict Price"):
        result = predict(house_age, distance_to_nearest_metro, land_area_sqft, number_of_rooms, no_of_nearby_stores)
        st.success(f"Predicted House Price: {result[0]:.2f} lakhs")

# Run App
if __name__ == "__main__":
    main()
