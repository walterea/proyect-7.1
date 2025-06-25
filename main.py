import pandas as pd
import plotly.express as px
import streamlit as st

st.title("Análisis Exploratorio de Datos - Vehículos en EE. UU.")

@st.cache_data
def load_data():
    df = pd.read_csv("vehicles_us.csv")
    return df

df = load_data()

st.header("Vista previa de los datos")
st.write(df.head())

st.header("Información general")
st.write(df.info())

st.header("Estadísticas descriptivas")
st.write(df.describe())

# Limpieza básica
st.header("Valores nulos")
st.write(df.isnull().sum())

# Histograma de precios
st.header("Distribución de precios")
fig_price = px.histogram(df, x="price", nbins=50, title="Distribución de precios de vehículos")
st.plotly_chart(fig_price)

# Histograma de año del vehículo
st.header("Distribución del año de los vehículos")
fig_year = px.histogram(df, x="model_year", nbins=30, title="Año del vehículo")
st.plotly_chart(fig_year)

# Precio promedio por tipo de vehículo
st.header("Precio promedio por tipo de vehículo")
if 'type' in df.columns:
    fig_type = px.box(df, x="type", y="price", title="Precio por tipo de vehículo")
    st.plotly_chart(fig_type)

# Dispersión precio vs odómetro
st.header("Precio vs. Odómetro")
if 'odometer' in df.columns:
    fig_scatter = px.scatter(df, x="odometer", y="price", title="Precio vs Kilometraje")
    st.plotly_chart(fig_scatter)

# Filtro por tipo
st.header("Filtrado por tipo de vehículo")
if 'type' in df.columns:
    vehicle_types = df['type'].dropna().unique()
    selected_type = st.selectbox("Selecciona un tipo de vehículo:", vehicle_types)
    filtered = df[df['type'] == selected_type]
    st.write(filtered[['price', 'model_year', 'odometer', 'condition']].describe())