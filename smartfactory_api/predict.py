import joblib
import pandas as pd

model = joblib.load("modele_rf_smartfactory.pkl")
scaler = joblib.load("scaler.pkl")

def faire_prediction(donnees):
    df = pd.DataFrame([donnees])
    df_scaled = scaler.transform(df)
    prediction = model.predict(df_scaled)
    return prediction[0]
