import matplotlib.pyplot as plt

# 1. Definir los datos de Períodos y Precios
periodos = ['May 2026', 'Jun 2026', 'Jul 2026', 'Ago 2026', 'Sep 2026']
precios = [1520.00, 1550.00, 1570.00, 1585.00, 1598.00]

# 2. Configurar el tamaño equilibrado de la figura
plt.figure(figsize=(8, 4.5), dpi=100)

# 3. Graficar la línea con marcadores
plt.plot(periodos, precios, marker='o', color='#1f77b4', linewidth=2, markersize=7, label='Precio Promedio (ARS)')

# 4. Añadir etiquetas con los valores exactos encima de cada punto
for i, txt in enumerate(precios):
    plt.annotate(f"${txt:,.2f}", (periodos[i], precios[i]), textcoords="offset points", xytext=(0,8), ha='center', fontsize=8, fontweight='bold')

# 5. Títulos y etiquetas de los ejes
plt.title('Evolución del Precio Promedio del Azúcar (Argentina - Mayo a Septiembre 2026)', fontsize=10, fontweight='bold', pad=12)
plt.xlabel('Período', fontsize=9, fontweight='bold')
plt.ylabel('Precio (ARS)', fontsize=9, fontweight='bold')

# 6. Cuadrícula de fondo sutil y límites
plt.grid(True, linestyle='--', alpha=0.5)
plt.ylim(1500, 1620)

# 7. Ajuste automático y guardado de la imagen para GitHub
plt.tight_layout()
plt.savefig('evolucion_precio_azucar.png', dpi=300)

# Mostrar el gráfico en pantalla
plt.show()