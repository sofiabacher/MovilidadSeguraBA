import pandas as pd
import random
from datetime import datetime, timedelta

avenidas = [
    "9 de Julio",
    "Corrientes",
    "Santa Fe",
    "Rivadavia",
    "Cabildo",
    "Belgrano",
    "Paseo Colon",
    "Libertador",
    "Juan B. Justo",
    "Callao",
    "25 de Mayo"
]

barrios = [
    "Palermo",
    "Recoleta",
    "Belgrano",
    "Caballito",
    "Microcentro",
    "Almagro",
    "Flores",
    "Retiro",
    "Constitucion",
    "Puerto Madero",
    "Gral. San Martín"
]

niveles = ["Bajo", "Medio", "Alto"]

coordenadas = {
    "Palermo": (-34.5875, -58.4300),
    "Recoleta": (-34.5889, -58.3974),
    "Belgrano": (-34.5621, -58.4563),
    "Caballito": (-34.6186, -58.4422),
    "Microcentro": (-34.6037, -58.3816),
    "Almagro": (-34.6100, -58.4200),
    "Flores": (-34.6300, -58.4600),
    "Retiro": (-34.5917, -58.3747),
    "Constitucion": (-34.6270, -58.3816),
    "Puerto Madero": (-34.6118, -58.3636),
    "Gral. San Martín": (34.3438, 58.3216)
}

registros = []

inicio = datetime.now() - timedelta(days=7)

for i in range(5000):
    barrio = random.choice(barrios)
    lat, lon = coordenadas[barrio]

    vehiculos = random.randint(50, 1500)
    velocidad = round(random.uniform(10, 70), 2)

    if vehiculos < 400:
        congestion = "Bajo"
    elif vehiculos < 900:
        congestion = "Medio"
    else:
        congestion = "Alto"
    
    registros.append({
        "id_sensor": random.randint(1000, 9999),
        "avenida": random.choice(avenidas),
        "barrio": barrio,
        "timestamp": inicio + timedelta(minutes=i * 2),
        "vehiculos": vehiculos,
        "velocidad_promedio": velocidad,
        "nivel_congestion": congestion,
        "latitud": lat + random.uniform(-0.005, 0.005),
        "longitud": lon + random.uniform(-0.005, 0.005)
    })

df = pd.DataFrame(registros)
print(df.head())

df.to_csv("../raw/transito_mock.csv", index=False)
print("Archivo transito_mock.csv generado correctamente")
