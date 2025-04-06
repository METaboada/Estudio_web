import streamlit as st
from utils.db import obtener_clientes

def mostrar_clientes():
    st.title("👥 Clientes")

    if st.button("⬅️ Volver al inicio", key="btn_volver_clientes"):
        st.session_state["pagina"] = "Home"
        st.rerun()

    cliente = st.text_input("Buscar cliente (nombre o CUIT)")

    if cliente:
        df = obtener_clientes(cliente)
        if df is not None and not df.empty:
            st.write(f"🔍 Resultados para: **{cliente}**")
            st.dataframe(df, hide_index=True)
        else:
            st.warning("No se encontraron clientes que coincidan con la búsqueda.")
