import folium
from folium.plugins import (MarkerCluster, HeatMap)

def obtener_color(tipo):
    colores = {
        "Siniestro": "red",
        "Obra": "orange",
        "Evento": "blue"
    }

    return colores.get(tipo, "gray")

def crear_mapa(incidentes):
    mapa = folium.Map(   # Centro de CABA
        location=[-34.6037, -58.3816],
        zoom_start=12,
        tiles="CartoDB positron"  # Usamos el mapa de la empresa CartoDB llamado Positron
    )

    marker_cluster = MarkerCluster().add_to(mapa)
    heat_data = []

    for incidente in incidentes:
        lat = incidente["latitud"]
        lon = incidente["longitud"]
        
        heat_data.append([lat, lon])
        
        folium.Marker(   # Muestro cada incidente como un marcador
            location=[lat, lon],

            popup=f"""
                <b>Tipo:</b> {incidente['tipo_evento']}<br>
                <b>Descripción:</b> {incidente['descripcion']}<br>
                <b>Severidad:</b> {incidente['severidad']}<br> 
                <b>Estado:</b> {incidente['estado']}
            """,

            icon=folium.Icon(
                color=obtener_color(incidente["tipo_evento"]),
                icon="info-sign"
            )

        ).add_to(marker_cluster)

    HeatMap(
        heat_data,
        radius=25,
        blur=15,
        max_zoom=13
    ).add_to(mapa)
    
    folium.LayerControl().add_to(mapa)

    return mapa