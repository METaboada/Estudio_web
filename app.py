import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- CONFIGURACIÓN INICIAL ---
st.set_page_config(page_title="Estudio Web", page_icon="favicon.png", layout="centered")

# --- OCULTAR BARRA LATERAL Y MENÚ SUPERIOR SI NO ESTÁ LOGUEADO ---
if "autenticado" not in st.session_state or not st.session_state["autenticado"]:
    st.markdown("""
        <style>
        [data-testid="stSidebar"] { display: none; }
        header { visibility: hidden; }
        </style>
    """, unsafe_allow_html=True)

# --- INICIALIZAR ESTADO ---
if "autenticado" not in st.session_state:
    st.session_state["autenticado"] = False

# --- LOGIN ---
if not st.session_state["autenticado"]:
    st.title("🔐 Ingreso a la aplicación")
    usuario = st.text_input("Usuario")
    clave = st.text_input("Contraseña", type="password")
    if st.button("Ingresar"):
        # if usuario == st.secrets["auth"]["usuario"] and clave == st.secrets["auth"]["clave"]:
        #     st.session_state["autenticado"] = True
        #     st.rerun()
        # else:
        #     st.error("❌ Usuario o contraseña incorrectos")

        usuarios_validos = st.secrets["auth"]["usuarios"]

        if usuario in usuarios_validos and clave == usuarios_validos[usuario]:
            st.session_state["autenticado"] = True
            st.session_state["usuario"] = usuario  # Guardamos el usuario logueado
            st.rerun()
        else:
            st.error("❌ Usuario o contraseña incorrectos")

    st.stop()

# --- MENÚ INTERNO PERSONALIZADO ---
st.title("🏠 Estudio Web")
menu = st.radio("Navegá por la aplicación", ["Inicio", "Reportes"], horizontal=True)
st.sidebar.write(f"👤 Usuario: {st.session_state['usuario']}")

# --- CONTENIDO SEGÚN SELECCIÓN ---
if menu == "Inicio":
    st.subheader("📌 Página de inicio")
    st.write("Seleccioná una opción del menú superior.")
elif menu == "Reportes":
    st.subheader("📊 Reportes de Ventas")
    df = pd.DataFrame({
        "Mes": ["Enero", "Febrero", "Marzo", "Abril"],
        "Ventas": [12000, 15000, 13000, 17000]
    })
    st.dataframe(df, use_container_width=True)

    fig, ax = plt.subplots()
    ax.plot(df["Mes"], df["Ventas"], marker='o')
    ax.set_title("Ventas mensuales")
    ax.set_ylabel("Monto")
    st.pyplot(fig)
