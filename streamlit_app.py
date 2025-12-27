import streamlit as st
import pandas as pd
import joblib

# ---------------- LOAD MODEL ----------------
@st.cache_resource
def load_model():
    return joblib.load("student_model.pkl")

model = load_model()

# ---------------- APP CONFIG ----------------
st.set_page_config(
    page_title="Student Performance Prediction",
    page_icon="🎓",
    layout="centered"
)

# ---------------- TITLE ----------------
st.title("🎓 Student Performance Prediction")
st.write(
    "This application predicts a student's **expected average score** "
    "based on educational and socio-demographic factors using Machine Learning."
)

st.divider()

# ---------------- USER INPUT ----------------
st.subheader("Enter Student Details")

gender = st.selectbox("Gender", ["male", "female"])

race = st.selectbox(
    "Race / Ethnicity",
    ["group A", "group B", "group C", "group D", "group E"]
)

parental_education = st.selectbox(
    "Parental Level of Education",
    [
        "some high school",
        "high school",
        "some college",
        "associate's degree",
        "bachelor's degree",
        "master's degree"
    ]
)

lunch = st.selectbox(
    "Lunch Type",
    ["standard", "free/reduced"]
)

test_prep = st.selectbox(
    "Test Preparation Course",
    ["none", "completed"]
)

# ---------------- PREDICTION ----------------
if st.button("Predict Average Score"):
    input_df = pd.DataFrame({
        "gender": [gender],
        "race/ethnicity": [race],
        "parental level of education": [parental_education],
        "lunch": [lunch],
        "test preparation course": [test_prep]
    })

    prediction = model.predict(input_df)[0]

    st.success(f"📊 Predicted Average Score: **{prediction:.2f}**")

    st.caption(
        "⚠️ This prediction is based on background factors only and "
        "does not define a student's intelligence or potential."
    )

st.divider()

# ---------------- FOOTER ----------------
st.markdown(
    """
    ### 👨‍💻 Developed By  
    **Ayush Chauhan**  
    *Machine Learning Enthusiast*

    **Tech Stack Used**
    - Python  
    - Pandas, NumPy  
    - Scikit-learn  
    - Streamlit  

    *For educational and analytical purposes only.*
    """
)
