kboximport pandas as pd
import plotly.express as px
import streamlit as st

st.header("Vehicle graphics and analysis")

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
car_data["manufacturer"] = car_data['model'].str.split(" ").str[0]
type_brand_button = st.checkbox("Construir comparativa de marca con tipo de vehiculo")
hist_button = st.checkbox('Construir histograma') # crear un botón
scatt_checkbox = st.checkbox("Construir grafico de dispersion")
      
if type_brand_button:
    st.write("Construir comparativa de marca con tipo de vehiculo")

    fig_manufacturer_type = fig = px.histogram(car_data, x="manufacturer", color="type", title="Vehicle type and brand")

    st.plotly_chart(fig_manufacturer_type,use_container_width=True)

if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig_model_condition = px.histogram(car_data, x="model_year", color="condition", title="Vehicle Model vs. Condition")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_model_condition, use_container_width=True)

if scatt_checkbox: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creacion de un diagrama de dispersion del precio comparado con el millaje')

    # crear un histograma
    fig_price_mileage = px.scatter(car_data, x="odometer", y="price", color="condition", log_y=True, title="Vehicle Price vs. Mileage")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_price_mileage, use_container_width=True)
