# 🎓 Student Performance Prediction (ML Project)

This project predicts a student’s **final average academic score** using demographic, educational, and preparation-related features.  
It is built using **Machine Learning (Scikit-learn)** and deployed using **Streamlit** for interactive predictions.

---

## 🚀 Live Application
👉 *(Add your Streamlit app link here after deployment)*

---

## 🧠 Problem Statement
Educational performance is influenced by multiple non-academic factors such as:
- Parental education
- Test preparation
- Socio-economic indicators (e.g., lunch type)
- Demographic categories

The goal is to **predict the final average score** (derived from math, reading, and writing scores) **without data leakage**, using only ethically explainable features.

---

## 📂 Project Structure

Student_performance_prediction/
│
├── data/
│   └── StudentsPerformance.csv
│
├── notebooks/
│   ├── Student_Performance_Prediction.ipynb
│   
│
├── student_model.pkl
├── streamlit_app.py
├── requirements.txt
├── README.md
├── .gitignore

---


## 📊 Dataset Description

**Source:** Student Performance Dataset  

### Features Used
| Feature | Description |
|------|-----------|
| gender | Student gender |
| race/ethnicity | Demographic group |
| parental level of education | Highest education of parents |
| lunch | Standard / Free-reduced (socio-economic indicator) |
| test preparation course | Completed or not |

### Target Variable
- **Average Score** = (Math + Reading + Writing) / 3

---

## ⚙️ Machine Learning Pipeline

- **Preprocessing**
  - OneHotEncoding → Gender, Race/Ethnicity, Lunch
  - OrdinalEncoding → Parental Education, Test Preparation
- **Model**
  - Linear Regression (baseline)
- **Pipeline**
  - `ColumnTransformer + Pipeline` (production-safe)

---

## 📈 Model Performance

| Metric | Value |
|------|------|
| R² Score | ~0.21 |
| RMSE | ~12 |
| MAE | ~10 |


---

## 🖥️ Streamlit Web App Features

The web application allows users to:
- Select student demographic details
- Choose parental education and preparation status
- Include lunch type as a socio-economic indicator
- Instantly predict the **final average score**

---

## 🧑‍💻 Technologies Used

- Python
- Pandas, NumPy
- Scikit-learn
- Joblib
- Streamlit

---

## 📦 Installation (Local)

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py


🔒 Ethical Considerations

Academic leakage features were intentionally removed

Lunch and race are included only for analysis, not decision-making

Model is for educational insight, not judgment or discrimination

👨‍🎓 Author

Ayush Chauhan
Machine Learning Enthusiast
B.Tech Undergraduate | NIT Sikkim