import streamlit as st

def menu_sidebar():
    st.sidebar.title("📚 Menú")
    if st.sidebar.button("🏢 Estudio Taboada", key="sidebar_home"):
        st.session_state["pagina"] = "Home"
    if st.sidebar.button("👥 Clientes", key="sidebar_clientes"):
        st.session_state["pagina"] = "Clientes"
    if st.sidebar.button("⚙️ Admin", key="sidebar_admin"):
        st.session_state["pagina"] = "Admin"
    if st.sidebar.button("🔒 Cerrar sesión", key="sidebar_logout"):
        st.session_state["autenticado"] = False
        st.rerun()
