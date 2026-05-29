import pandas as pd

def calcular_metricas(df):
    flujo_total = df["vehiculos"].sum()

    velocidad_promedio = round(
        df["velocidad_promedio"].mean(), 
        2
    )

    zonas_criticas = len(
        df[df["nivel_congestion"] == "Alta"]
    )

    sensores_activos = df["id_sensor"].nunique()

    if velocidad_promedio < 20:   # Cuanta más lenta la circulación --> +congestión
        congestion = "Alta"
    elif velocidad_promedio < 40:
        congestion = "Media"
    else:
        congestion = "Baja"
    
    return {
        "flujo_total": flujo_total,
        "velocidad_promedio": velocidad_promedio,
        "zonas_criticas": zonas_criticas,
        "sensores_activos": sensores_activos,
        "congestion": congestion
    }

def top_barrios_congestion(df):
    return (
        df.groupby("barrio")["vehiculos"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
        .reset_index()
    )

def sensores_criticos(df):
    return(
        df.groupby("id_sensor")["vehiculos"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

def evolucion_trafico(df):
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    evolucion = (
        df.groupby(df["timestamp"].dt.hour)['vehiculos']
        .mean()
        .reset_index()
    )

    evolucion.columns = ["hora", "vehiculos"]
    
    return evolucion

