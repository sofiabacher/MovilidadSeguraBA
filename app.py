import streamlit as st 
import plotly.express as px

from streamlit_folium import st_folium

from services.mapa import crear_mapa
from services.analisis import (calcular_metricas, top_barrios_congestion, sensores_criticos, evolucion_trafico)

from api.transito import obtener_datos_transito
from api.eventos import obtener_eventos

# ------- Configuración -------------------

st.set_page_config(
    page_title="MovilidadSeguraBA",
    page_icon="🚦",
    layout="wide"
)

st.title("🚦 MovilidadSeguraBA")
st.subheader("Dashboard Inteligente de Movilidad Urbana")

# -------- Datos del tránsito ---------------------

@st.cache_data(ttl=300)  # Cachea durante 5'. Evita lentitud, bloquar API, muchas requests
def cargar_datos():
    transito = obtener_datos_transito()
    eventos = obtener_eventos()
    return transito, eventos

df_transito, df_eventos = cargar_datos()

if df_transito.empty:
    st.error("No se pudieron cargar datos de tránsito")
    st.stop()

# -------- Sidebar ---------------------

st.sidebar.title("📍 Filtros")

st.sidebar.subheader("Barrios")
barrios_disponibles = sorted(df_transito["barrio"].unique())
barrios = []

for barrio in barrios_disponibles:
    seleccionado = st.sidebar.checkbox(barrio, value=True)
    if seleccionado:
        barrios.append(barrio)

st.sidebar.subheader("Nivel de congestión")
niveles = []

for nivel in sorted(df_transito["nivel_congestion"].unique()):
    seleccionado = st.sidebar.checkbox(nivel, value=True)
    if seleccionado:
        niveles.append(nivel)

df_filtrado = df_transito[
    (df_transito["barrio"].isin(barrios)) &
    (df_transito["nivel_congestion"].isin(niveles))
]

df_eventos_filtrado = df_eventos[
    df_eventos["barrio"].isin(barrios)
]

# ----------- Métricas --------------

metricas = calcular_metricas(df_filtrado)
col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Flujo total", metricas['flujo_total'])
col2.metric("Velocidad promedio", f"{metricas['velocidad_promedio']} km/h")
col3.metric("Flujo vehicular", metricas["zonas_criticas"])
col4.metric("Nivel de congestión", metricas["congestion"])
col5.metric("Sensores activos", metricas["sensores_activos"])

# ------------ Alertas ------------

if metricas["congestion"] == "Alta":
    st.error("⚠ Congestión crítica detectada")
elif metricas["congestion"] == "Media":
    st.warning("⚠ Congestión moderada")
else:
    st.success("✅ Flujo vehicular normal")

# ------------ Mapa ------------

st.markdown("---")
st.subheader("🗺️ Mapa de incidentes")

incidentes = df_eventos_filtrado.to_dict(orient="records")

mapa = crear_mapa(incidentes)
st_folium(mapa, use_container_width=True, height=500)

# ------------ Gráficos ------------

st.markdown("---")
st.write("📈 Flujo vehicular por hora")

fig_flujo = px.line(
    df_filtrado,
    x="timestamp",
    y="vehiculos",
    color="barrio",
    markers=True
)

st.plotly_chart(fig_flujo, use_container_width="strech")

# ------------------------

st.subheader("🚗 Velocidad promedio por zona")

fig_velocidad = px.bar(
    df_filtrado,
    x="barrio",
    y="velocidad_promedio",
    color="nivel_congestion"
)

st.plotly_chart(fig_velocidad, use_container_width="stretch")

# ------------------------

st.subheader("🚨 Distribución de congestión")

fig_congestion = px.histogram(
    df_filtrado,
    x="nivel_congestion",
    color="nivel_congestion"
)

st.plotly_chart(fig_congestion, use_container_width="stretch")

# ------------------------

st.subheader("🏙️ Barrios con mayor flujo vehicular")

top_barrios = top_barrios_congestion(df_filtrado)

fig_barrios = px.bar(
    top_barrios,
    x="barrio",
    y="vehiculos",
    color="vehiculos"
)

st.plotly_chart(fig_barrios, width="stretch")

# ------------------------

st.subheader("📡 Sensores con mayor tráfico")

sensores = sensores_criticos(df_filtrado)

fig_sensores = px.bar(
    sensores,
    x="id_sensor",
    y="vehiculos",
    color="vehiculos"
)

st.plotly_chart(fig_sensores, width="stretch")

# ------------------------

st.subheader("⏱️ Evolución horaria del tráfico")

evolucion = evolucion_trafico(df_filtrado)

fig_evolucion = px.line(
    evolucion,
    x="hora",
    y="vehiculos",
    markers=True
)

st.plotly_chart(fig_evolucion, width="stretch")

# ------------ Insights ------------

st.markdown("---")
st.subheader("🧠 Insights automáticos")

barrio_critico = top_barrios.iloc[0]

st.info(
    f"""
    El barrio con mayor flujo vehicular es
    {barrio_critico['barrio']}
    con un totalde
    {barrio_critico['vehiculos']} vehículos registrados
    """
)

if metricas["congestion"] == "Alta":
    st.error("""Se detectó una situación crítica de congestión urbana""")

# ------------ Tabla ------------

st.markdown("---")
st.subheader("📋 Datos de tránsito")
st.dataframe(df_filtrado, use_container_width="stretch")
