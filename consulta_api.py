import requests
import pandas as pd

# Definimos la URL de una API pública de datos económicos en Argentina
url = "https://api.argentinadatos.com/v1/cotizaciones/dolares"

try:
    # Hacemos la consulta a la API
    response = requests.get(url)
    
    if response.status_code == 200:
        datos = response.json()
        
        # Convertimos los datos a una tabla con Pandas
        df = pd.DataFrame(datos)
        
        print("¡Datos obtenidos con éxito desde la API!")
        print("\nPrimeras filas de los datos:")
        print(df.head())
        
    else:
        print(f"Error al conectar con la API. Código: {response.status_code}")

except Exception as e:
    print(f"Ocurrió un error: {e}")