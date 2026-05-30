import requests
import pandas as pd
import streamlit as st

CLIENT_ID = st.secrets["CLIENT_ID"]
CLIENT_SECRET = st.secrets["CLIENT_SECRET"]

EVENTOS_URL = "https://api-transporte.buenosaires.gob.ar/eventos"

def obtener_mock_eventos():
    return pd.read_csv("data/raw/eventos_mock.csv")

def obtener_eventos():
    params = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }

    try:
        response = requests.get(EVENTOS_URL, params=params)
        
        print("Status:", response.status_code)

        if response.status_code == 200:
            data = response.json()

            if len(data) == 0:
                print("API vacía --> usando mock data")
                return obtener_mock_eventos()

            return pd.DataFrame(data)

        else:
            print(f"Error obteniendo eventos: {response.text}")
            return obtener_mock_eventos()
    
    except Exception as e:
        print("Error: ", e)
        return obtener_mock_eventos()
    
    
