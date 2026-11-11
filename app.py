import streamlit as st
import requests
import pandas as pd

st.title("SugarAnalytics - Monitoreo de Precios y API")

st.subheader("Evolución del Precio Promedio del Azúcar (Argentina)")
st.image("evolucion_precio_azucar.png", caption="Evolución del Precio Promedio (Mayo - Septiembre 2026)", use_container_width=True)

st.divider()

st.subheader("Conexión en Tiempo Real con API de Cotizaciones")
st.write("Haz clic en el botón para consultar los datos actualizados desde la API pública.")

if st.button("Consultar API de Cotizaciones"):
    url = "https://api.argentinadatos.com/v1/cotizaciones/dolares"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            datos = response.json()
            df = pd.DataFrame(datos)
            
            st.success("¡Datos obtenidos con éxito desde la API!")
            st.write("Primeras filas de los datos obtenidos:")
            st.dataframe(df.head())
        else:
            st.error(f"Error al conectar con la API. Código: {response.status_code}")
            
    except Exception as e:
        st.error(f"Ocurrió un error de conexión: {e}")