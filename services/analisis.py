import pandas as pd

def crear_dataframe_transito():
    datos = {
        "hora": [
            "08:00",
            "09:00",
            "10:00",
            "11:00",
            "12:00",
            "13:00",
            "14:00"
        ],
         "flujo": [
            3200,
            5400,
            6100,
            4500,
            3900,
            7100,
            6800
        ],
        "velocidad": [
            52,
            40,
            28,
            35,
            45,
            22,
            25
        ],
        "zona": [
            "Centro",
            "Centro",
            "Norte",
            "Sur",
            "Oeste",
            "Centro",
            "Norte"
        ]
    }

    return pd.DataFrame(datos)

def calcular_metricas(df):
    flujo_total = df["flujo"].sum()
    velocidad_promedio = round(df["velocidad"].mean(), 2)
    zonas_criticas = len(df[df["velocidad"] < 30])

    if velocidad_promedio < 30:   # Cuanta más lenta la circulación --> +congestión
        congestion = "Alta"
    elif velocidad_promedio < 45:
        congestion = "Media"
    else:
        congestion = "Baja"
    
    return {
        "flujo_total": flujo_total,
        "velocidad_promedio": velocidad_promedio,
        "zonas_criticas": zonas_criticas,
        "congestion": congestion
    }