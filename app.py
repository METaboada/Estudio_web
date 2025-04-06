
import streamlit as st
from pantallas.home import mostrar_home
from pantallas.clientes import mostrar_clientes
from pantallas.admin import mostrar_admin
from components.sidebar import menu_sidebar

st.set_page_config(page_title="Estudio Web", page_icon="favicon.png", layout="centered")

def main():
    if "autenticado" not in st.session_state:
        st.session_state["autenticado"] = False

    if not st.session_state["autenticado"]:
        st.title("🔐 Ingreso a la aplicación")
        usuario = st.text_input("Usuario")
        clave = st.text_input("Contraseña", type="password")

        usuarios = st.secrets["auth"]["usuarios"]
        if st.button("Ingresar", key="btn_ingresar"):
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

    match st.session_state["pagina"]:
        case "Clientes":
            mostrar_clientes()
        case "Admin":
            mostrar_admin()
        case _:
            mostrar_home()

if __name__ == "__main__":
    main()
