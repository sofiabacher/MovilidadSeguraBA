import requests
import pandas as pd
import streamlit as st

CLIENT_ID = st.secrets["CLIENT_ID"]
CLIENT_SECRET = st.secrets["CLIENT_SECRET"]

TRANSITO_URL = "https://apitransporte.buenosaires.gob.ar/datos/movilidad/transito"

def obtener_mock_transito():
    return pd.read_csv("data/raw/transito_mock.csv")

def obtener_datos_transito():
    params = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }

    try:
        response = requests.get(TRANSITO_URL, params=params)
        
        print("Status:", response.status_code)
    
        if response.status_code == 200:
            data = response.json()
            print(data)

            if len(data) == 0:
                print("API vacía --> usando mock data")
                return obtener_mock_transito()
        
            return pd.DataFrame(data)

        else:
            print(f"Error obteniendo datos: {response.text}")
            return obtener_mock_transito()
    
    except Exception as e:
        print("Error: ", e)
        return obtener_mock_transito()
    
    
