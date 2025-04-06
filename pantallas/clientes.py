# import streamlit as st
# from utils.db import obtener_clientes

# def mostrar_clientes():
#     st.title("👥 Clientes")

#     if st.button("⬅️ Volver al inicio", key="btn_volver_clientes"):
#         st.session_state["pagina"] = "Home"
#         st.rerun()

#     cliente = st.text_input("Buscar cliente (nombre o CUIT)")

#     if cliente:
#         df = obtener_clientes(cliente)
#         if df is not None and not df.empty:
#             st.write(f"🔍 Resultados para: **{cliente}**")
#             st.dataframe(df, hide_index=True)
#         else:
#             st.warning("No se encontraron clientes que coincidan con la búsqueda.")

import streamlit as st
from utils.db import obtener_clientes
from clases.cliente import Cliente



def mostrar_clientes():
    st.title("📁 Gestión de Clientes")

    if st.button("⬅️ Volver al inicio", key="btn_volver_admin"):
        st.session_state["pagina"] = "Home"
        st.rerun()

    filtro = st.text_input("🔍 Buscar cliente por nombre o CUIT")
    if not filtro:
        st.info("Ingresá un filtro para comenzar")
        return

    df_clientes = obtener_clientes(filtro)

    if df_clientes is None or df_clientes.empty:
        st.warning("No se encontraron clientes con ese filtro.")
        return

    lista_clientes = []
    for _, row in df_clientes.iterrows():
        cliente = Cliente(
            id_cliente=row["id_cliente"],
            nombre=row["nombre"],
            cuit=row["cuit"],
            clave_fiscal=row.get("clave_fiscal"),
            clave_ciudad=row.get("clave_ciudad"),
            clave_arba=row.get("clave_arba"),
            clave_sec=row.get("clave_sec"),
            clave_faecys=row.get("clave_faecys"),
            clave_inacap=row.get("clave_inacap"),
            clave_osecac=row.get("clave_osecac"),
            clave_rubrica_digital_caba=row.get("clave_rubrica_digital_caba"),
            clave_estudio_one_web=row.get("clave_estudio_one_web"),
            registro_de_empleadores=row.get("registro_de_empleadores"),
            otros_datos=row.get("otros_datos"),
            domicilio=row.get("domicilio"),
            carpeta=row.get("carpeta"),
            ptovta=row.get("ptovta"),
            nombase=row.get("nombase"),
            ruta_base=row.get("ruta_base"),
            rutabackup=row.get("rutabackup")
        )
        lista_clientes.append(cliente)

    for cliente in lista_clientes:
        with st.expander(f"🧾 {cliente.nombre} ({cliente.cuit})"):
            st.markdown(cliente.mostrar_resumen())

