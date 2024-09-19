import streamlit as st
import pandas as pd
import plotly_express as px

car_data=pd.read_csv('vehicles_us.csv')

st.header('Histograma de Datos')
hist_button=st.button('Construir histograma')
scat_button=st.button('Construir dispersión')

if hist_button:
    
    st.write('Creación de un histograma para los datos de anuncio de coches')
    fig=px.histogram(car_data,x='odometer')
    st.plotly_chart(fig, use_container_width=True)

if scat_button:
    st.write('Creacion de un gráfico de dispersión para los datos de anuncio de coches')
    fig=px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)