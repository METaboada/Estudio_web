import streamlit as st

def mostrar_admin():
    st.title("⚙️ Administración")
    st.write("Opciones de configuración y control del sistema.")

    if st.button("⬅️ Volver al inicio", key="btn_volver_admin"):
        st.session_state["pagina"] = "Home"
        st.rerun()
