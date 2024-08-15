import streamlit as st
from supabase import create_client, Client
from fpdf import FPDF
from datetime import datetime


# Configurar Supabase
SUPABASE_URL = "https://dzrqlfnxxtompvovsiso.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImR6cnFsZm54eHRvbXB2b3ZzaXNvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjI0NzMwMTUsImV4cCI6MjAzODA0OTAxNX0.j4JmBL6IKm1obWB29ytLOZq0_cIvZ8iRL3m3KSzZFQc"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def get_students():
    response = supabase.table('students').select('*').execute()
    return response.data

def count_students():
    response = supabase.table('students').select('*', count='exact').execute()
    return response.count

def generate_pdf(students, student_count):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Reporte de Estudiantes", ln=True, align='C')

    #Obtener la fecha y hora actual
    current_datetime = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    pdf.set_font("Arial", size=10)
    pdf.cell(200,10, txt=f"Generado el: {current_datetime}", ln=True, align='R')

    pdf.set_font("Arial", size=10)
    pdf.cell(200, 10, txt=f"Cantidad total de estudiantes: {student_count}", ln=True, align='L')

    pdf.ln(10)  # Salto de línea

    for student in students:
        pdf.cell(200, 10, txt=f"ID: {student['id']}, Nombre: {student['name']}, Edad: {student['age']}", ln=True, align='L')

    # Guardar el PDF
    pdf.output("reporte_estudiantes.pdf")

def download_pdf():
    with open("reporte_estudiantes.pdf", "rb") as f:
        st.download_button('Descargar reporte en PDF', f, file_name="reporte_estudiantes.pdf")


# Streamlit APP
st.title("Streamlit y Supabase")

menu = ["Ver", "Agregar", "Actualizar", "Eliminar", "Generar Reporte"]
choice = st.sidebar.selectbox("Menú", menu)

if choice == "Ver":
    st.subheader("Lista de estudiantes")
    students = get_students()
    student_count = count_students()
    st.write(f"Cantidad total de estudiantes: {student_count}")
    for student in students:
        st.write(f"ID: {student['id']}, Nombre: {student['name']}, Edad: {student['age']}")

elif choice == "Generar Reporte":
    st.subheader("Generar Reporte en PDF")
    students = get_students()
    student_count = count_students()
    generate_pdf(students, student_count)
    st.success("Reporte generado exitosamente")
    download_pdf()
