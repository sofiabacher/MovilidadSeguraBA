import streamlit as st 
import plotly.express as px
from streamlit_folium import st_folium

from services.mapa import crear_mapa
from services.analisis import (crear_dataframe_transito, calcular_metricas)

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

print(df_transito.columns)

# -------- Sidebar ---------------------

st.sidebar.title("Filtros")

zonas = st.sidebar.multiselect(
    "Seleccionar zonas",
    df_transito["zona"].unique(),
    default=df_transito["zona"].unique()
)

df_filtrado = df_transito[
    df_transito["zona"].isin(zonas)
]

# ----------- Métricas --------------

metricas = calcular_metricas(df_filtrado)
col1, col2, col3, col4 = st.columns(4)

col1.metric("Flujo total", f"{metricas['flujo_total']}")
col2.metric("Velocidad promedio", f"{metricas['velocidad_promedio']} km/h")
col3.metric("Flujo vehicular", metricas["zonas_criticas"])
col4.metric("Nivel de congestión", metricas["congestion"])

# ------------ Alertas ------------

if metricas["congestion"] == "Alta":
    st.error("⚠ Congestión crítica detectada")
elif metricas["congestion"] == "Media":
    st.warning("⚠ Congestión moderada")
else:
    st.success("✅ Flujo vehicular normal")

# ------------ Incidentes DEMO ------------

incidentes = [
    {
        "tipo": "Siniestro",
        "descripcion": "Choque múltiple",
        "lat": -34.6037,
        "lon": -58.3816,
        "congestion": "Alta"
    },
    {
        "tipo": "Obra",
        "descripcion": "Corte parcial",
        "lat": -34.6150,
        "lon": -58.4333,
        "congestion": "Media"
    },
    {
        "tipo": "Evento",
        "descripcion": "Manifestación",
        "lat": -34.5950,
        "lon": -58.4100,
        "congestion": "Alta"
    }
]

# ------------ Mapa ------------

st.markdown("---")
st.subheader("🗺️ Mapa de incidentes")

mapa = crear_mapa(incidentes)
st_folium(mapa, width=1400, height=500)

# ------------ Gráficos ------------

st.markdown("---")
st.write("📈 Flujo vehicular por hora")

fig_flujo = px.line(
    df_filtrado,
    x="hora",
    y="flujo",
    markers=True
)

st.plotly_chart(fig_flujo, use_container_width=True)

# ------------ Velocidad ------------

st.subheader("🚗 Velocidad promedio por zona")

fig_velocidad = px.bar(
    df_filtrado,
    x="zona",
    y="velocidad",
    color="zona"
)

st.plotly_chart(fig_velocidad, use_container_width=True)


# ------------ Tabla ------------

st.markdown("---")
st.subheader("📋 Datos de tránsito")
st.dataframe(df_filtrado, use_container_width=True)