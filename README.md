# Análisis Técnico: Evolución de Precios del Azúcar en Argentina (Mayo - Septiembre 2026)

## 📌 Descripción del Proyecto
Este repositorio contiene un análisis técnico comparativo de la evolución de los precios promedio del azúcar en el mercado argentino durante el período comprendido entre **mayo y septiembre de 2026**. El objetivo principal es contrastar y contrastar las series de precios oficiales con los registros de importación para evaluar tendencias y variaciones porcentuales.

---

## 📊 Visualización de Datos
El siguiente gráfico generado mediante **Python (Matplotlib)** resume la trayectoria alcista del precio promedio mensual expresado en Pesos Argentinos (ARS):

![Evolución del Precio del Azúcar](evolucion_precio_azucar.png)

* **Período analizado:** Mayo 2026 – Septiembre 2026.
* **Tendencia observada:** Crecimiento sostenido desde los $1,520.00 ARS iniciales hasta los $1,598.00 ARS al cierre de septiembre.

---

## 🛠️ Stack Tecnológico y Herramientas
* **Microsoft Excel:** Limpieza inicial, estructuración del dataset principal y validación cruzada de registros.
* **Python (Matplotlib):** Procesamiento de series temporales y generación de gráficos de alta resolución (`dpi=300`) para documentación técnica.
* **Control de versiones:** Git & GitHub.

---

## 📂 Estructura del Repositorio
```text
├── grafico_azucar.py             # Script de Python para generar la visualización
├── evolucion_precio_azucar.png   # Gráfico exportado en alta resolución
└── README.md                     # Documentación oficial del proyecto
"Además de analizar los datasets históricos del INDEC, sumamos una etapa de automatización conectándonos a una API pública mediante un script en Python. Esto nos permite extraer datos directamente desde la web en formato JSON y estructurarlos de manera dinámica utilizando Pandas, cumpliendo con los requerimientos técnicos de integración de sistemas."
