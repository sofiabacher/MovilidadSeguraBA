import requests
import os

from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
SECRET = os.getenv("CLIENT_SECRET")

LOGIN_URL = "https://api-transporte.buenosaires.gob.ar/v1/auth/login"

def obtener_token():
    payload = {
        "client_id": CLIENT_ID,
        "client_secret": SECRET,
    }

    try:
        response = requests.post(LOGIN_URL, json=payload)
        
        if response.status_code == 200:
            data = response.json()
            return data.get("accessToken")

        else:
            print(f"Error autenticando: {response.text}")
            return None
    
    except Exception as e:
        print("Error de conexión:", e)
        return None
