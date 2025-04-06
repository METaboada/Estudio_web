import streamlit as st

st.set_page_config(
    page_title="Estudio Web",
    page_icon="favicon.png",
    layout="centered"
)

# # ---- INICIALIZAR SESSION_STATE ----
# if "autenticado" not in st.session_state:
#     st.session_state["autenticado"] = False

if "autenticado" not in st.session_state or not st.session_state["autenticado"]:
    # Ocultar barra lateral y menú superior hasta que esté autenticado
    hide_menu = """
        <style>
        [data-testid="stSidebar"] {display: none;}
        header {visibility: hidden;}
        </style>
    """
    st.markdown(hide_menu, unsafe_allow_html=True)




# ---- LOGIN ----
if not st.session_state["autenticado"]:
    st.title("🔐 Ingreso a la aplicación")

    usuario = st.text_input("Usuario")
    clave = st.text_input("Contraseña", type="password")

    if st.button("Ingresar"):
        if usuario == st.secrets["auth"]["usuario"] and clave == st.secrets["auth"]["clave"]:
            st.session_state["autenticado"] = True
            st.success("✅ Bienvenido, acceso concedido")
            st.rerun()  # Esto recarga la app mostrando el contenido protegido
        else:
            st.error("❌ Usuario o contraseña incorrectos")

    st.stop()  # Detiene aquí si no está autenticado

# ---- CONTENIDO PROTEGIDO: DASHBOARD / MENÚ ----
st.title("🏠 Bienvenido al Estudio Web")

st.markdown("Seleccioná una opción del menú de la izquierda o accedé a los reportes desde la sección correspondiente.")

# Podés agregar contenido adicional acá, como accesos rápidos:
st.info("🔗 También podés ir a la página de **Reportes** desde el menú de la izquierda.")
