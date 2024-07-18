import streamlit as st

#Título de la aplicación
st.title("Ingreso de Datos y Estructuras Condicionales")

#Ingreso de la edad
edad = st.number_input("Ingrese su edad", min_value=0, max_value=120, step=1)