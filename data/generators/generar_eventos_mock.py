import pandas as pd
import random
from datetime import datetime, timedelta

avenidas = [
    "9 de Julio",
    "Corrientes",
    "Santa Fe",
    "Rivadavia",
    "Cabildo",
    "Libertador",
    "Belgrano",
    "Paseo Colon"
]

barrios = [
    "Palermo",
    "Recoleta",
    "Belgrano",
    "Caballito",
    "Microcentro",
    "Retiro",
    "Puerto Madero"
]

coordenadas = {
    "Palermo": (-34.5875, -58.4300),
    "Recoleta": (-34.5889, -58.3974),
    "Belgrano": (-34.5621, -58.4563),
    "Caballito": (-34.6186, -58.4422),
    "Microcentro": (-34.6037, -58.3816),
    "Retiro": (-34.5917, -58.3747),
    "Puerto Madero": (-34.6118, -58.3636)
}

tipos = [
    "Choque",
    "Corte",
    "Manifestacion",
    "Obra",
    "Semaforo fuera de servicio",
    "Accidente multiple"
]

severidades = ["Baja", "Media", "Alta"]
estados = ["Activo", "Resuelto"]

registros = []

inicio = datetime.now() - timedelta(days=7)

for i in range(500):
    barrio = random.choice(barrios)
    lat, lon = coordenadas[barrio]
    tipo = random.choice(tipos)

    if tipo in ["Accidente multiple", "Choque"]:
        severidad = random.choices(
            severidades,
            weights=[1, 3, 5]
        )[0]
    else:
        severidad = random.choice(severidades)

    registros.append({
        "id_evento": f"EV-{10000+i}",
        "tipo_evento": tipo,
        "severidad": severidad,
        "avenida": random.choice(avenidas),
        "barrio": barrio,
        "descripcion": f"{tipo} reportado en zona de {barrio}",
        "timestamp": inicio + timedelta(minutes=i * 5),
        "estado": random.choice(estados),
        "latitud": lat + random.uniform(-0.005, 0.005),
        "longitud": lon + random.uniform(-0.005, 0.005)
    })

    df = pd.DataFrame(registros)
    print(df.head())

    df.to_csv("../raw/eventos_mock.csv", index=False)
    print("Archivo eventos_mock.csv generado correctamente")
