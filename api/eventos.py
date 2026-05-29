import requests
import pandas as pd

from api.auth import obtener_token

EVENTOS_URL = "https://api-transporte.buenosaires.gob.ar/eventos"

def obtener_eventos():
    token = obtener_token()

    if not token:
        return pd.DataFrame()
    
    headers = {"Authorization": f"Bearer {token}"}

    try:
        response = requests.get(EVENTOS_URL, headers=headers)
        
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
    
    