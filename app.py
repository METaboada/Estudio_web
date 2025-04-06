import streamlit as st
import mysql.connector
import pandas as pd


# --- Configuración inicial ---
st.set_page_config(page_title="Estudio Web",
                   page_icon="favicon.png",  # Usa el archivo local,
                    layout="centered")


# --- Funciones por página ---
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



# def mostrar_clientes():
#     st.title("👥 Clientes")
#     st.write("Esta es la página de inicio.")

#     if st.button("⬅️ Volver al inicio", key="btn_volver_clientes"):
#         st.session_state["pagina"] = "Home"
#         st.rerun()

#     # Boton con un buscador para seleccionar clientes de una tabla de mysql
#     st.write("Buscador de clientes")
#     cliente = st.text_input("Buscar cliente")
#     if cliente:
#         st.write(f"Buscando cliente: {cliente}")

def mostrar_clientes():
    st.title("👥 Clientes")
    st.write("Esta es la página de inicio.")

    if st.button("⬅️ Volver al inicio", key="btn_volver_clientes"):
        st.session_state["pagina"] = "Home"
        st.rerun()

    st.write("Buscador de clientes")
    cliente = st.text_input("Buscar cliente (nombre o CUIT)")

    if cliente:
        try:
            # Conexión usando los secrets de Streamlit Cloud
            conexion = mysql.connector.connect(
                host=st.secrets["mysql"]["host"],
                user=st.secrets["mysql"]["user"],
                password=st.secrets["mysql"]["password"],
                database=st.secrets["mysql"]["database"]
            )

            cursor = conexion.cursor(dictionary=True)

            query = """
                SELECT * FROM clientes 
                WHERE nombre LIKE %s OR cuit LIKE %s
            """
            like_pattern = f"%{cliente}%"
            cursor.execute(query, (like_pattern, like_pattern))
            resultados = cursor.fetchall()

            if resultados:
                df = pd.DataFrame(resultados)
                st.write(f"🔍 Resultados para: **{cliente}**")
                # st.dataframe(df)
                st.dataframe(df, hide_index=True)
            else:
                st.warning("No se encontraron clientes que coincidan con la búsqueda.")

            cursor.close()
            conexion.close()

        except mysql.connector.Error as e:
            st.error(f"❌ Error al conectar con la base de datos: {e}")


def mostrar_admin():

    st.title("⚙️ Administración")
    st.write("Opciones de configuración y control del sistema.")

    if st.button("⬅️ Volver al inicio", key="btn_volver_admin"):
        st.session_state["pagina"] = "Home"
        st.rerun()


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


# --- Main ---
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
