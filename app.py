import streamlit as st

st.set_page_config(
    page_title="Estudio Web",
    page_icon="favicon.png",
    layout="centered"  # ⬅️ esta es la opción por defecto
)

# ---- LOGIN ----
if "autenticado" not in st.session_state:
    st.session_state["autenticado"] = False

if not st.session_state["autenticado"]:
    st.title("🔐 Ingreso a la aplicación")

    usuario = st.text_input("Usuario")
    clave = st.text_input("Contraseña", type="password")

    if st.button("Ingresar"):
        if usuario == st.secrets["auth"]["usuario"] and clave == st.secrets["auth"]["clave"]:
            st.session_state["autenticado"] = True
            st.success("✅ Bienvenido, acceso concedido")
            
        else:
            st.error("❌ Usuario o contraseña incorrectos")

    st.stop()  # No se muestra nada más si no está autenticado


