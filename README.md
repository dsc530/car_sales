# Aplicación Web de Gráficos Estadísticos de Autos

Esta es una aplicación web desarrollada en Python utilizando **Streamlit** y publicada en **Render**. La aplicación permite visualizar dos tipos de gráficos estadísticos interactivos relacionados con un conjunto de datos de autos disponibles para la venta.

## Funcionalidades

La aplicación ofrece las siguientes opciones a través de dos cajas de verificación:

1. **Histograma del Odómetro (Kilómetros recorridos):**
   - Este gráfico muestra la distribución de los kilómetros recorridos por los autos en venta.
   - El eje X representa los kilómetros recorridos (valores del odómetro) y el eje Y muestra la frecuencia de autos en cada rango de kilómetros.
   - El histograma se puede visualizar o ocultar según el estado de la casilla de verificación.

2. **Gráfico de Dispersión (Precio vs Kilómetros recorridos):**
   - Este gráfico compara el precio de cada auto con el valor de su odómetro.
   - En el eje X se muestran los kilómetros recorridos, mientras que en el eje Y se representa el precio de los autos.
   - Al igual que el histograma, este gráfico se puede mostrar u ocultar según la selección en la casilla de verificación.

## Cómo usar la aplicación

1. Abre la aplicación en el navegador a través del enlace ***https://carsales-45bi.onrender.com/***. 
2. Selecciona las opciones de visualización de gráficos marcando o desmarcando las casillas correspondientes:
   - **Histograma**: Muestra u oculta el histograma de kilómetros recorridos.
   - **Gráfico de dispersión**: Muestra u oculta el gráfico de dispersión (Precio vs Kilómetros).
   
## Requisitos

- **Python 3.12.5**
- **Streamlit**
- **Pandas**

## Instalación y Ejecución Local

1. Clona este repositorio:
   git clone https://github.com/dsc530/car_sales.git

