from fastapi import FastAPI, Query
from pydantic import BaseModel
import pandas as pd
import joblib
import os
import numpy as np

app = FastAPI()
# loading models and encoder
SVC = joblib.load('./models/SVC_pipeline.pkl')  
gradient_boost = joblib.load('./models/gradient_boost_pipeline.pkl')
encoder = joblib.load('./models/label_encoder.pkl')

class DfFeatures(BaseModel):
    PRG: int
    PL: int
    PR: int
    SK: int
    TS: int
    M11: float
    BD2: float
    Age: int
    Insurance: int
    
@app.get('/')
def status_check(
    title: str = Query('Sepsis Prediction API', title='Project Title', description='Title of the project'),
):
    status_message = {
        'api_name': 'Sepsis Prediction API',
        'description': 'This API predicts the likelihood of sepsis based on patient data.',
        'status': 'API is online and functioning correctly.',
        'models_loaded': {
            'svc_model': 'loaded',
            'gradient_boost_model': 'loaded',
            'label_encoder': 'loaded'
        }
    }
    return status_message

@app.post('/predict_sepsis')
def predict_sepsis(data: DfFeatures, model: str = Query('SVC', enum=['SVC', 'gradient_boost'])):
    df = pd.DataFrame([data.model_dump()])

    # Select the model based on the query parameter
    if model == 'SVC':
        prediction = SVC.predict(df)
        probability = SVC.predict_proba(df)
    elif model == 'gradient_boost':
        prediction = gradient_boost.predict(df)
        probability = gradient_boost.predict_proba(df)
    
    prediction = int(prediction[0])
    prediction = encoder.inverse_transform([prediction])[0]
    probability = probability[0]

    return {
        'model_used': model,
        'prediction': prediction,
        'probability': f'The probability of the prediction is {probability[0]:.2f}'
    }