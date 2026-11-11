import streamlit as st
import requests
import pandas as pd

st.title("SugarAnalytics - Análisis de Precios y Inflación")

st.subheader("Evolución del Precio Promedio del Azúcar (Argentina)")
st.image("evolucion_precio_azucar.png", caption="Evolución del Precio Promedio (Mayo - Septiembre 2026)", use_container_width=True)

st.divider()

st.subheader("Simulación: Impacto de la Inflación Externa en el Precio del Azúcar")
st.write("Haz clic en el botón para consultar la base de datos externa de inflación y calcular la proyección:")

if st.button("Calcular Proyección por Inflación"):
    # URL de la API pública de inflación oficial de Argentina
    url = "https://api.argentinadatos.com/v1/finanzas/indices/inflacion"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            datos = response.json()
            df = pd.DataFrame(datos)
            
            # Filtramos los últimos meses para que coincida con el período de tu análisis
            df_reciente = df.tail(6).copy()
            
            # Supongamos un precio base inicial del kilo de azúcar de referencia
            precio_inicial = 1200.0
            
            # Simulamos el cálculo acumulado del precio según la inflación mensual (%) de la API
            precios_calculados = []
            precio_actual = precio_inicial
            
            for index, row in df_reciente.iterrows():
                inflacion_mensual = row['valor'] # El valor viene en porcentaje (ej: 4.2)
                precio_actual = precio_actual * (1 + inflacion_mensual / 100)
                precios_calculados.append(round(precio_actual, 2))
                
            df_reciente['Precio_Teorico_Azucar'] = precios_calculados
            
            st.success("¡Cálculo realizado con éxito utilizando la base de datos externa!")
            st.write("Tabla comparativa de inflación y su impacto proyectado en el precio:")
            st.dataframe(df_reciente[['fecha', 'valor', 'Precio_Teorico_Azucar']])
            
            st.info("💡 **Conclusión para tu proyecto:** Este cálculo demuestra cómo la API externa alimenta un modelo matemático para proyectar el valor del azúcar en base a la macroeconomía del país.")
            
        else:
            st.error(f"Error al conectar con la API. Código: {response.status_code}")
            
    except Exception as e:
        st.error(f"Ocurrió un error de conexión: {e}")