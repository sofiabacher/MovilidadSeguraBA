# 🚦 MovilidadSeguraBA

## Dashboard Inteligente de Movilidad Urbana para la Ciudad de Buenos Aires

MovilidadSeguraBA es una aplicación web interactiva desarrollada en Python y Streamlit que permite visualizar y analizar información de movilidad urbana en la Ciudad de Buenos Aires.

El objetivo del proyecto es transformar datos de tránsito e incidentes urbanos en información visual, clara y accionable mediante mapas interactivos, indicadores clave y análisis de datos.

---

## 🌐 Demo

**Aplicación desplegada:**

https://movilidadseguraba.streamlit.app/

---

## 📌 Objetivos del Proyecto

- Centralizar información relacionada con la movilidad urbana.
- Visualizar eventos e incidentes georreferenciados.
- Analizar niveles de congestión vehicular.
- Monitorear indicadores de tránsito.
- Facilitar la interpretación de datos mediante dashboards interactivos.
- Aplicar técnicas de visualización y análisis de datos utilizando herramientas modernas de Python.

---

## 🛠️ Tecnologías Utilizadas

### Backend y Procesamiento de Datos

- Python
- Pandas
- Requests

### Visualización

- Streamlit
- Plotly

### Geolocalización

- Folium
- Streamlit-Folium

### Configuración y Despliegue

- Python Dotenv
- GitHub
- Streamlit Community Cloud

---

## 🚦 Funcionalidades Principales

### 📊 KPIs de Movilidad

El dashboard presenta indicadores clave:

- Flujo vehicular total
- Velocidad promedio
- Cantidad de zonas críticas
- Nivel de congestión general
- Sensores activos

### 🗺️ Mapa Interactivo de Incidentes

Visualización geográfica mediante Folium:

- Siniestros viales
- Obras
- Eventos urbanos
- Marcadores interactivos
- Agrupación de incidentes
- Heatmap de concentración

### 📈 Análisis de Tránsito

Incluye visualizaciones dinámicas para:

- Flujo vehicular
- Velocidad promedio por barrio
- Distribución de congestión
- Evolución temporal del tránsito
- Sensores con mayor circulación

### 🚨 Sistema de Alertas

Detección automática de:

- Congestión alta
- Zonas críticas
- Situaciones de riesgo vial

### 🧠 Inteligencia Urbana

Generación de insights automáticos sobre:

- Barrios con mayor flujo vehicular
- Sensores críticos
- Estado general de la movilidad

---

## 🎛️ Filtros Interactivos

El usuario puede filtrar información por:

- Barrio
- Nivel de congestión

Los filtros actualizan automáticamente:

- KPIs
- Gráficos
- Mapa
- Heatmap
- Tablas

---

## 🔌 Integración con APIs del GCBA

El proyecto fue diseñado para consumir información proveniente de las APIs oficiales de transporte del Gobierno de la Ciudad de Buenos Aires (GCBA), incluyendo datos relacionados con:

- Flujo vehicular
- Tránsito urbano
- Sensores de circulación
- Incidentes y eventos viales

La arquitectura del sistema ya incluye los módulos necesarios para realizar las consultas a dichas APIs utilizando credenciales oficiales.

### Situación actual

Durante el desarrollo del proyecto se detectó que los endpoints consultados devolvían respuestas vacías (`[]`), por lo que no fue posible obtener datos reales para la visualización.

Para garantizar el funcionamiento del dashboard y continuar con el desarrollo, se implementó una estrategia de simulación mediante datasets mock (datos ficticios realistas).

Actualmente la aplicación utiliza:

- `transito_mock.csv`
- `eventos_mock.csv`

Estos archivos permiten demostrar todas las funcionalidades del sistema sin depender de la disponibilidad de datos reales.

---

## 🔐 Uso de Credenciales de la API

En caso de que las APIs del GCBA comiencen a devolver información real, será necesario solicitar credenciales de acceso completando el formulario disponible en el portal oficial del Gobierno de la Ciudad.

Una vez obtenidas las credenciales, se deberá crear un archivo `.env` en la raíz del proyecto:

```env
CLIENT_ID=TU_CLIENT_ID
CLIENT_SECRET=TU_CLIENT_SECRET
```
Estas credenciales permiten autenticar las consultas realizadas a los servicios del GCBA.

---

## 🚀 Cómo Ejecutar el Proyecto Localmente

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU-USUARIO/MovilidadSeguraBA.git
```
### 2. Ingresar al proyecto

```bash
cd MovilidadSeguraBA
```
### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```
### 4. Configurar credenciales (opcional)
Solo si la API del GCBA devuelve datos reales:

```env
CLIENT_ID=TU_CLIENT_ID
CLIENT_SECRET=TU_CLIENT_SECRET
```
### 5. Ejecutar la aplicación

```bash
streamlit run app.py
```
