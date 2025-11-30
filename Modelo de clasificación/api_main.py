from fastapi import FastAPI
from joblib import load
import json
from typing import TypedDict, Literal, Annotated
import pandas as pd
from input_schema import InputPayload

# Caragamos el modelo
with open("clasificador_complicaciones_rf.joblib", "rb") as f:
    model = load(f)

with open("feature_order.json") as f:
    FEATURE_ORDER = json.load(f)

# Inicializamos el servidor
app = FastAPI(title="Servicio de Trasplantes - Predicción de complicaciones")

@app.post("/complicaciones")
async def predict(features: InputPayload):
    try:
        X = pd.DataFrame([features])
        X['Child_Pugh_Letra'] = X['Child_Pugh_Letra'].replace({
            'A' : 1,
            'B' : 2,
            'C' : 3
        })

        for col in FEATURE_ORDER:
            if col not in X.columns:
                X[col] = 0
                print(f'{col} not in original data')

        df = X[FEATURE_ORDER]
        prediction = model.predict(df).tolist()
        return {"prediction": prediction}
    except:
        return