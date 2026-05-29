import folium

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
        zoom_start=12
    )

    for incidente in incidentes:
        folium.Marker(   # Muestro cada incidente como un marcador
            location=[
                incidente["lat"], 
                incidente["lon"]
            ],

            popup=f"""
                <b>Tipo:</b> {incidente['tipo']}<br>
                <b>Descripción:</b> {incidente['descripcion']}<br>
                <b>Congestión:</b> {incidente['congestion']}  
            """,

            icon=folium.Icon(
                color=obtener_color(incidente["tipo"])
            )

        ).add_to(mapa)
    
    return mapa