import streamlit as st
import requests

st.title("Fake Job Prediction App🔔💻")
st.write("")
st.write("      Enter job details to predict.")
st.write("")
API_URL = "http://localhost:8000/predict"

location=st.text_input("Location", "US,New York, NY")
st.write("")
telecommuting=st.number_input("Telecommuting (0 or 1)", min_value=0, max_value=1, value=0)
st.write("")
has_company_logo=st.number_input("Has Company Logo (0 or 1)", min_value=0, max_value=1, value=1)
st.write("")
has_questions=st.number_input("Has Questions (0 or 1)", min_value=0, max_value=1, value=0)
st.write("")
employment_type=st.selectbox("Employment Type", ["Full-time", "Part-time", "Contract", "Temporary", "Internship", "Other"])
st.write("")
required_experience=st.selectbox("Required Experience", ["No Experience", "1 Year", "2 Years", "3 Years", "4 Years", "5+ Years"])
st.write("")
required_education=st.selectbox("Required Education", ["High School", "Associate Degree", "Bachelor's Degree", "Master's Degree", "Doctorate", "Other"])
st.write("")
industry=st.selectbox("Industry", ["IT", "Finance", "Healthcare", "Education", "Retail", "Other"])
st.write("")
function=st.selectbox("Function", ["Engineering", "Sales", "Marketing", "Operations", "HR", "Other"])   
st.write("")
if st.button("Predict"):
    input_data = {
        "location": location,
        "telecommuting": telecommuting,
        "has_company_logo": has_company_logo,
        "has_questions": has_questions,
        "employment_type": employment_type,
        "required_experience": required_experience,
        "required_education": required_education,
        "industry": industry,
        "function": function
    }
    
    response = requests.post(
            API_URL,
            json=input_data)
    result=response.json()
    if response.status_code == 200:
            st.success(f"Prediction: {'Fake Job' if result['prediction'] == 1 else 'Genuine Job'}")
            st.info(f"Confidence: {result['confidence']:.2f}%")
            st.warning(" Data is imbalanced NLP is needed for better results ..Currentlyyy working on it ")
    else:
            st.error(f"Error: {result['error']}")