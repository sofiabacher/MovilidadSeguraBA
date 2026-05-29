import pandas as pd

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
