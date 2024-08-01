import streamlit as st
from supabase import create_client, Client

#Configurar Supabase
SUPABASE_URL = "https://dzrqlfnxxtompvovsiso.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImR6cnFsZm54eHRvbXB2b3ZzaXNvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjI0NzMwMTUsImV4cCI6MjAzODA0OTAxNX0.j4JmBL6IKm1obWB29ytLOZq0_cIvZ8iRL3m3KSzZFQc"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_students():
    response = supabase.table('students').select('*').execute()
    return response.data

def count_students():
    response = supabase.table('students').select('*', count='exact').execute()
    return response.count

def add_student(name, age):
    supabase.table('students').insert({"name": name, "age": age}).execute()

st.title("CRUD con Streamlit y Supabase")

menu = ["Ver", "Agregar"]
choice = st.sidebar.selectbox("Menú", menu)

if choice == "Ver":
    st.subheader("Lista de estudiantes")
    students = get_students()
    student_count = count_students()
    st.write(f"Cantidad total de estudiantes: {student_count}")
    for student in students:
        st.write(f"ID: {student['id']}, Nombre: {student['name']}, Edad: {student['age']}")