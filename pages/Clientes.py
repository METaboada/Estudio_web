import streamlit as st

# Control de autenticación
if "autenticado" not in st.session_state or not st.session_state["autenticado"]:
    st.warning("⚠️ No estás autenticado. Volvé a la página principal.")
    st.stop()

st.title("📁 Página de Clientes")
st.write("Contenido visible solo si estás logueado.")
