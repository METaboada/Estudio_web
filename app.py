import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- Configuración inicial ---
st.set_page_config(page_title="Estudio Web",
                   page_icon="favicon.png",  # Usa el archivo local,
                    layout="centered")


# --- Funciones por página ---
def mostrar_home():
    st.title("🏢 Estudio Taboada")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("📊 Ir a Reportes"):
            st.session_state["pagina"] = "Reportes"
            st.rerun()
    with col2:
        if st.button("⚙️ Ir a Admin"):
            st.session_state["pagina"] = "Admin"
            st.rerun()



def mostrar_clientes():
    st.title("👥 Clientes")
    st.write("Esta es la página de inicio.")

    # Boton con un buscador para seleccionar clientes de una tabla de mysql
    st.write("Buscador de clientes")
    cliente = st.text_input("Buscar cliente")
    if cliente:
        st.write(f"Buscando cliente: {cliente}")



def mostrar_admin():

    st.title("⚙️ Administración")
    st.write("Opciones de configuración y control del sistema.")

    if st.button("⬅️ Volver al inicio"):
        st.session_state["pagina"] = "Home"
        st.rerun()


def menu_sidebar():
    st.sidebar.title("📚 Menú")
    if st.sidebar.button("👥 Clientes"):
        st.session_state["pagina"] = "Clientes"
    if st.sidebar.button("⚙️ Admin"):
        st.session_state["pagina"] = "Admin"
    if st.sidebar.button("🔒 Cerrar sesión"):
        st.session_state["autenticado"] = False
        st.rerun()


# --- Main ---
def main():
    if "autenticado" not in st.session_state:
        st.session_state["autenticado"] = False

    if not st.session_state["autenticado"]:
        st.title("🔐 Ingreso a la aplicación")
        usuario = st.text_input("Usuario")
        clave = st.text_input("Contraseña", type="password")

        usuarios = st.secrets["auth"]["usuarios"]
        if st.button("Ingresar"):
            if usuario in usuarios and clave == usuarios[usuario]:
                st.session_state["autenticado"] = True
                st.session_state["pagina"] = "Home"
                st.rerun()
            else:
                st.error("❌ Usuario o contraseña incorrectos")
        st.stop()

    if "pagina" not in st.session_state:
        st.session_state["pagina"] = "Home"

    menu_sidebar()

    pagina = st.session_state["pagina"]
    if pagina == "Clientes":
        mostrar_clientes()
    if pagina == "Home":
        mostrar_home()
    elif pagina == "Admin":
        mostrar_admin()


# --- Ejecutar ---
if __name__ == "__main__":
    main()
