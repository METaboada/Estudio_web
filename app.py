import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- Configuración inicial ---
st.set_page_config(page_title="Estudio Web", layout="centered")

# --- Inicializar autenticación ---
if "autenticado" not in st.session_state:
    st.session_state["autenticado"] = False

# --- Autenticación ---
if not st.session_state["autenticado"]:
    st.title("🔐 Ingreso a la aplicación")
    usuario = st.text_input("Usuario")
    clave = st.text_input("Contraseña", type="password")
    
    usuarios = st.secrets["auth"]["usuarios"]
    if st.button("Ingresar"):
        if usuario in usuarios and clave == usuarios[usuario]:
            st.session_state["autenticado"] = True
            st.session_state["pagina"] = "Home"
            st.experimental_rerun()
        else:
            st.error("❌ Usuario o contraseña incorrectos")
    st.stop()

# --- Inicializar página actual ---
if "pagina" not in st.session_state:
    st.session_state["pagina"] = "Home"

# --- Menú de navegación ---
st.sidebar.title("📚 Menú")
if st.sidebar.button("🏠 Home"):
    st.session_state["pagina"] = "Home"
if st.sidebar.button("📊 Reportes"):
    st.session_state["pagina"] = "Reportes"
if st.sidebar.button("⚙️ Admin"):
    st.session_state["pagina"] = "Admin"
if st.sidebar.button("🔒 Cerrar sesión"):
    st.session_state["autenticado"] = False
    st.experimental_rerun()

# --- Contenido de cada página ---
pagina = st.session_state["pagina"]

if pagina == "Home":
    st.title("🏠 Bienvenido")
    st.write("Esta es la página de inicio.")
    
elif pagina == "Reportes":
    st.title("📊 Reportes")
    df = pd.DataFrame({
        "Mes": ["Enero", "Febrero", "Marzo", "Abril"],
        "Ventas": [12000, 15000, 13000, 17000]
    })
    st.dataframe(df, use_container_width=True)
    
    fig, ax = plt.subplots()
    ax.plot(df["Mes"], df["Ventas"], marker='o')
    ax.set_title("Ventas mensuales")
    st.pyplot(fig)

elif pagina == "Admin":
    st.title("⚙️ Administración")
    st.write("Opciones de configuración y control del sistema.")
