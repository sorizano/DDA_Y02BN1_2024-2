import streamlit as st
from supabase import create_client, Client
import pandas as pd

#Configurar Supabase
url = "https://dzrqlfnxxtompvovsiso.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImR6cnFsZm54eHRvbXB2b3ZzaXNvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjI0NzMwMTUsImV4cCI6MjAzODA0OTAxNX0.j4JmBL6IKm1obWB29ytLOZq0_cIvZ8iRL3m3KSzZFQc"
supabase: Client = create_client(url, key)

st.title("Sistema de facturación")

# Selección de operación
option = st.selectbox(
    '¿Qué operación desea realizar?',
    ('Consultar Clientes', 'Consultar Productos', 'Generar Factura', 'Ver Facturas')
)

if option == 'Consultar Clientes':
    clientes = supabase.table('clientes').select('*').execute()
    df_clientes = pd.DataFrame(clientes.data)
    st.write(df_clientes)

elif option == 'Consultar Productos':
    productos = supabase.table('productos').select('*').execute()
    df_productos = pd.DataFrame(productos.data)
    st.write(df_productos)

elif option == 'Generar Factura':
    #Datos del cliente
    cliente_id = st.number_input("ID del Cliente", min_value=1)
    productos = supabase.table('productos').select('*').execute()
    df_productos = pd.DataFrame(productos.data)

    #Selección de productos y cantidades
    selected_products = st.multiselect("Seleccione productos", df_productos['nombre'])
    product_qty = {}
    for product in selected_products:
        qty = st.numer_input(f"Cantidad de {product}", min_value=1)
        product_qry[product] = qty