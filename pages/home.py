import streamlit as st

def mostrar_home():
    st.title("🏢 Estudio Taboada")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("👥 Clientes", key="btn_clientes_home"):
            st.session_state["pagina"] = "Clientes"
            st.rerun()
    with col2:
        if st.button("⚙️ Ir a Admin", key="btn_admin_home"):
            st.session_state["pagina"] = "Admin"
            st.rerun()
