import requests
import pandas as pd
import os

from dotenv import load_dotenv
load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

EVENTOS_URL = "https://api-transporte.buenosaires.gob.ar/eventos"

def obtener_eventos():
    params = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }

    try:
        response = requests.get(EVENTOS_URL, params=params)
        
        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame(data)
            return df

        else:
            print(f"Error obteniendo eventos: {response.text}")
            return pd.DataFrame()
    
    except Exception as e:
        print("Error: ", e)
        return pd.DataFrame()
    
    