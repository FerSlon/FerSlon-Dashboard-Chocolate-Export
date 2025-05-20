import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

BASE_URL = "https://raw.githubusercontent.com/FerSlon/FerSlon-Dashboard-Chocolate-Export/main/"

# URLs de los archivos CSV
clientes_url = BASE_URL + "clientes.csv"
mercados_url = BASE_URL + "mercados.csv"
exportaciones_url = BASE_URL + "exportaciones.csv"
barreras_url = BASE_URL + "barreras.csv"

# Cargar datos
try:
    clientes = pd.read_csv(clientes_url)
    mercados = pd.read_csv(mercados_url)
    exportaciones = pd.read_csv(exportaciones_url)
    barreras = pd.read_csv(barreras_url)
except Exception as e:
    st.error("Error al cargar los archivos CSV. Verificá las URLs y el nombre de tu usuario en GitHub.")
    st.stop()

# Título del Dashboard
st.title("Dashboard Interactivo de Exportaciones de Chocolates")

# Filtro de país
paises = exportaciones["País"].unique()
pais_seleccionado = st.selectbox("Selecciona un país para ver los detalles", paises)

# Mostrar datos de clientes
st.subheader("Clientes")
clientes_filtrados = clientes[clientes["País"] == pais_seleccionado]
st.dataframe(clientes_filtrados)

# Mostrar datos de exportaciones
st.subheader("Exportaciones de Chocolates")
exportaciones_filtradas = exportaciones[exportaciones["País"] == pais_seleccionado]
fig1, ax1 = plt.subplots()
ax1.bar(
    exportaciones_filtradas["País"],
    exportaciones_filtradas["Exportaciones (USD millones)"],
    color="#2E86C1"
)
ax1.set_xlabel("País")
ax1.set_ylabel("Exportaciones (USD millones)")
ax1.set_title(f"Exportaciones de Chocolates en {pais_seleccionado}")
st.pyplot(fig1)

# Mostrar datos de mercados
st.subheader("Segmentos de Mercado")
mercados_filtrados = mercados[mercados["País"] == pais_seleccionado]
st.dataframe(mercados_filtrados)

# Mostrar barreras de entrada
st.subheader("Barreras de Entrada")
barreras_filtradas = barreras[barreras["País"] == pais_seleccionado]
st.dataframe(barreras_filtradas)

# Análisis Comparativo
st.subheader("Análisis Comparativo del Tamaño de Mercado")
fig2, ax2 = plt.subplots(figsize=(8, 5))
ax2.bar(
    mercados["País"],
    mercados["Tamaño del Mercado (USD millones)"],
    color="#F39C12"
)
ax2.set_xlabel("País")
ax2.set_ylabel("Tamaño del Mercado (USD millones)")
ax2.set_title("Comparación de Tamaños de Mercado")
plt.xticks(rotation=45)
st.pyplot(fig2)
