import streamlit as st
import pandas as pd
import plotly_express as px

car_data=pd.read_csv('vehicles_us.csv')

st.header('Datos de Autos Disponibles Para Venta')

st.subheader('Por favor escoja como desea observar los datos:')

hist_chart=st.checkbox('Histograma')
scat_chart=st.checkbox('Gráfico de dispersión')


if hist_chart:
    
    st.write('Creación de un histograma para los datos de anuncio de coches')
    fig=px.histogram(car_data,x='odometer',title='Cantidad de Kms Recorridos Por Auto',labels = {'odometer': 'Kms Recorridos'})
    st.plotly_chart(fig, use_container_width=True,)
    

if scat_chart:
    st.write('Creacion de un gráfico de dispersión para los datos de anuncio de coches')
    fig=px.scatter(car_data, x="odometer", y="price", title='Precio de Acuerdo a los Kms Recorridos',labels = {'odometer': 'Kms Recorridos', 'price':'Precio Vehículo/USD'})
    st.plotly_chart(fig, use_container_width=True,)
