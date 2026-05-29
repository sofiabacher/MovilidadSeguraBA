import requests
import pandas as pd
import os

from dotenv import load_dotenv
load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

TRANSITO_URL = "https://api-transporte.buenosaires.gob.ar/transito"

def obtener_datos_transito():
    params = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }

    try:
        response = requests.get(TRANSITO_URL, params=params)
        print(response.status_code)
        
        if response.status_code == 200:
            print("REPRESENTACIÓN DEL TEXTO RECIBIDO:")
            print(response.text[:500])
            
            data = response.json()
            return pd.DataFrame(data)

        else:
            print(f"Error obteniendo datos: {response.text}")
            return pd.DataFrame()
    
    except Exception as e:
        print("Error: ", e)
        return pd.DataFrame()
    
    