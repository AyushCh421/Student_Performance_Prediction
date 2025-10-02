import streamlit as st
import pandas as pd
import pickle

st.title("Student Performance Prediction")

# Load the trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# User inputs
gender = st.selectbox("Gender", ["male", "female"])
race = st.selectbox("Race/Ethnicity", ["group A","group B","group C","group D","group E"])
education = st.selectbox("Parental Education", ["some high school","high school","some college","associate's degree","bachelor's degree","master's degree"])
prep = st.selectbox("Test Preparation", ["none", "completed"])

# Make prediction
input_df = pd.DataFrame([[gender, race, education, prep]],
                        columns=['gender','race/ethnicity','parental level of education','test preparation course'])
prediction = model.predict(input_df)
st.write(f"Predicted Average Score: {prediction[0]:.2f}")
     
