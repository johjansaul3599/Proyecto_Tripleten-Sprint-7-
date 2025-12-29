import streamlit as st
import pandas as pd
import plotly_express as px

# Leer el archivo CSV en un DataFrame
car_data = pd.read_csv('vehicles_us.csv')

# 2. Crear el encabezado
st.header('Análisis de Datos de Vehículos en EE. UU.')

# 3. Crear el botón para el histograma
build_histogram = st.button('Construir histograma') # crear un botón

if build_histogram: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creando un histograma para la columna odómetro')
    
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
    
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# 4. Crear el botón para el gráfico de dispersión
build_scatter = st.button('Construir gráfico de dispersión') # crear otro botón

if build_scatter: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creando un gráfico de dispersión para la relación precio vs kilometraje')
    
    # crear un gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price")
    
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)