from dotenv import load_dotenv
import streamlit as st
import pandas as pd
import os
from insert_data import insert_data 


load_dotenv()


st.title("School Notes App")


def cargar_archivo(archivo):
    try:
        if archivo is not None:
            df = pd.read_excel(archivo, engine='openpyxl')
            return df
    except Exception as e:
        st.error(f"Error al cargar el archivo: {e}")
        return None


uploaded_file1 = st.file_uploader("Elige el primer archivo Excel (Grupo 1)", type=["xlsx"])
uploaded_file2 = st.file_uploader("Elige el segundo archivo Excel (Grupo 2)", type=["xlsx"])


df1 = cargar_archivo(uploaded_file1)
df2 = cargar_archivo(uploaded_file2)

if df1 is not None:
    st.write("Datos del primer archivo:")
    st.write(df1)

if df2 is not None:
    st.write("Datos del segundo archivo:")
    st.write(df2)

if df1 is not None and df2 is not None:
    combined_df = pd.concat([df1, df2], ignore_index=True)
    st.write("Datos combinados:")
    st.write(combined_df)

    if st.button('Guardar Datos Combinados'):
        try:
            os.makedirs('data', exist_ok=True)
            combined_df.to_excel("data/datos_combinados.xlsx", index=False)
            st.success("Datos combinados guardados exitosamente como 'datos_combinados.xlsx'")
            
    
            insert_data(combined_df)
            st.success("Datos insertados en la base de datos exitosamente")
        except Exception as e:
            st.error(f"Error al guardar el archivo o insertar los datos en la base de datos: {e}")

st.write(f"Archivo 1: {uploaded_file1.name if uploaded_file1 else 'No cargado'}")
st.write(f"Archivo 2: {uploaded_file2.name if uploaded_file2 else 'No cargado'}")
