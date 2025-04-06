import streamlit as st
import mysql.connector
import pandas as pd

def obtener_clientes(filtro):
    try:
        conexion = mysql.connector.connect(
            host=st.secrets["mysql"]["host"],
            user=st.secrets["mysql"]["user"],
            password=st.secrets["mysql"]["password"],
            database=st.secrets["mysql"]["database"]
        )
        cursor = conexion.cursor(dictionary=True)
        like_pattern = f"%{filtro}%"
        query = "SELECT * FROM clientes WHERE nombre LIKE %s OR cuit LIKE %s"
        cursor.execute(query, (like_pattern, like_pattern))
        resultados = cursor.fetchall()
        cursor.close()
        conexion.close()
        return pd.DataFrame(resultados)
    except mysql.connector.Error as e:
        st.error(f"❌ Error al conectar con la base de datos: {e}")
        return None
