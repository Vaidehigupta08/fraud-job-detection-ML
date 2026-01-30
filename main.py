from fastapi import FastAPI 
from pydantic import BaseModel
import pickle
import pandas as pd

model=pickle.load(open('xgb_model.pkl','rb'))
encoder=pickle.load(open('ordinal_encoder.pkl','rb'))
app=FastAPI(title="Job Fraud Detection API")

class jobinput(BaseModel):
    location: str
    telecommuting: int
    has_company_logo: int
    has_questions: int
    employment_type: str
    required_experience: str
    required_education: str
    industry: str
    function: str

categorical_cols = [
    "location",
    "employment_type",
    "required_experience",
    "required_education",
    "industry",
    "function"
]
@app.post("/predict")
def predict(data: jobinput):
    try:
        df = pd.DataFrame([data.dict()])

        # encode categorical columns
        df[categorical_cols] = encoder.transform(df[categorical_cols])

        # ensure same column order
        feature_order = [
            "location",
            "telecommuting",
            "has_company_logo",
            "has_questions",
            "employment_type",
            "required_experience",
            "required_education",
            "industry",
            "function",
        ]
        df = df[feature_order]

        # convert to numpy
        X = df.to_numpy()

        # prediction
        pred = int(model.predict(X)[0])  
                     # ✅ cast to int
        prob = float(model.predict_proba(X)[0][1])    # ✅ cast to float
         

        threshold = 0.3

        pred = 1 if prob >= threshold else 0

        if pred == 1:
         confidence = prob * 100
        else:
         confidence = (1 - prob) * 100

        return {
            "prediction": "Fraudulent" if pred == 1 else "Genuine",
            "confidence": round(confidence, 2)
        }

    except Exception as e:
        return {
            "error": "Prediction failed",
            "message": str(e)
        }


@app.get('/')
def index():    
    return {"message": "Welcome to Job Fraud Detection API"}        
