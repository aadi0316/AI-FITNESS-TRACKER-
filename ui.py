import streamlit as st
import requests

st.header("🔥 Manual Calorie Prediction")

# The form container
with st.form("manual_calorie_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        u_weight = st.number_input("Weight (kg)", value=70.0)
        u_height = st.number_input("Height (cm)", value=170.0)
        u_age = st.number_input("Age", value=25)
        u_gender = st.selectbox("Gender", ["Male", "Female"])
        
    with col2:
        u_duration = st.number_input("Exercise Duration (min)", value=30)
        u_heart = st.number_input("Average Heart Rate", value=110)
        u_temp = st.number_input("Body Temp (Celsius)", value=37.5)

    # THIS IS THE BUTTON THAT FIXES THE ERROR
    submitted = st.form_submit_button("Calculate Now")

# This part happens AFTER the form is submitted
if submitted:
    gender_encoded = 0 if u_gender == "Male" else 1
    
    payload = {
        "weight": u_weight,
        "height": u_height,
        "age": u_age,
        "gender": gender_encoded,
        "duration": u_duration,
        "heart_rate": u_heart,
        "body_temp": u_temp
    }

    try:
        # Calling your Flask API on port 5000
        response = requests.post("http://127.0.0.1:5000/predict_calories", json=payload)
        
        if response.status_code == 200:
            result = response.json()
            st.success(f"### Estimated Calories Burned: {result['calories_burned']} kcal")
        else:
            st.error(f"Backend error: {response.text}")
            
    except Exception as e:
        st.error(f"Connection failed! Is your Flask server running in the other terminal? Error: {e}")