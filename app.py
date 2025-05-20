import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# URLs de los archivos CSV en tu repositorio de GitHub (reemplaza TU_USUARIO con tu nombre de usuario real)
clientes_url = "https://raw.githubusercontent.com/TU_USUARIO/Dashboard-Chocolate-Export/main/clientes.csv"
mercados_url = "https://raw.githubusercontent.com/TU_USUARIO/Dashboard-Chocolate-Export/main/mercados.csv"
exportaciones_url = "https://raw.githubusercontent.com/TU_USUARIO/Dashboard-Chocolate-Export/main/exportaciones.csv"
barreras_url = "https://raw.githubusercontent.com/TU_USUARIO/Dashboard-Chocolate-Export/main/barreras.csv"

# Cargar los datos
clientes = pd.read_csv(clientes_url)
mercados = pd.read_csv(mercados_url)
exportaciones = pd.read_csv(exportaciones_url)
barreras = pd.read_csv(barreras_url)

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
    color='#2E86C1'
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
