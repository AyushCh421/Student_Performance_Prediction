import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import OneHotEncoder

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Student Average Score Prediction")

st.subheader("Enter Student Details:")

# User input
gender = st.selectbox("Gender", ['male', 'female'])
race = st.selectbox("Race/Ethnicity", ['group A', 'group B', 'group C', 'group D', 'group E'])
# The 'lunch' column was dropped during preprocessing, so it's not needed for prediction input
# lunch = st.selectbox("Lunch", ['standard', 'free/reduced'])
parental_education = st.selectbox(
    "Parental Level of Education",
    ['some high school', 'high school', 'some college', "associate's degree", "bachelor's degree", "master's degree"]
)
test_prep = st.selectbox("Test Preparation Course", ['none', 'completed'])
math_score = st.number_input("Math Score", min_value=0, max_value=100, value=50)

# Create a DataFrame from user inputs with the correct column names and order
# The pipeline will handle the encoding and scaling
X_input = pd.DataFrame({
    'gender': [gender],
    'race/ethnicity': [race],
    'parental level of education': [parental_education],
    'test preparation course': [test_prep],
    'math score': [math_score]
})


# Predict using the loaded pipeline
prediction = model.predict(X_input)

st.success(f"Predicted Average Score: {prediction[0]:.2f}")
