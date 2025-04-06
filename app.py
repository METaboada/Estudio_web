# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt

# # --- Configuración inicial ---
# st.set_page_config(page_title="Estudio Web", layout="centered")

# # --- Inicializar autenticación ---
# if "autenticado" not in st.session_state:
#     st.session_state["autenticado"] = False

# # --- Autenticación ---
# if not st.session_state["autenticado"]:
#     st.title("🔐 Ingreso a la aplicación")
#     usuario = st.text_input("Usuario")
#     clave = st.text_input("Contraseña", type="password")
    
#     usuarios = st.secrets["auth"]["usuarios"]
#     if st.button("Ingresar"):
#         if usuario in usuarios and clave == usuarios[usuario]:
#             st.session_state["autenticado"] = True
#             st.session_state["pagina"] = "Home"
#             st.rerun()
#         else:
#             st.error("❌ Usuario o contraseña incorrectos")
#     st.stop()

# # --- Inicializar página actual ---
# if "pagina" not in st.session_state:
#     st.session_state["pagina"] = "Home"

# # --- Menú de navegación (sidebar) ---
# st.sidebar.title("📚 Menú")
# if st.sidebar.button("🏠 Home"):
#     st.session_state["pagina"] = "Home"
# if st.sidebar.button("📊 Reportes"):
#     st.session_state["pagina"] = "Reportes"
# if st.sidebar.button("⚙️ Admin"):
#     st.session_state["pagina"] = "Admin"
# if st.sidebar.button("🔒 Cerrar sesión"):
#     st.session_state["autenticado"] = False
#     st.rerun()

# # --- Contenido de cada página ---
# pagina = st.session_state["pagina"]

# if pagina == "Home":
#     st.title("🏠 Bienvenido")
#     st.write("Esta es la página de inicio.")

#     # --- Botones de navegación desde la página principal ---
#     col1, col2 = st.columns(2)
#     with col1:
#         if st.button("Ir a Reportes"):
#             st.session_state["pagina"] = "Reportes"
#             st.rerun()
#     with col2:
#         if st.button("Ir a Admin"):
#             st.session_state["pagina"] = "Admin"
#             st.rerun()

# elif pagina == "Reportes":
#     st.title("📊 Reportes")
#     df = pd.DataFrame({
#         "Mes": ["Enero", "Febrero", "Marzo", "Abril"],
#         "Ventas": [12000, 15000, 13000, 17000]
#     })
#     st.dataframe(df, use_container_width=True)
    
#     fig, ax = plt.subplots()
#     ax.plot(df["Mes"], df["Ventas"], marker='o')
#     ax.set_title("Ventas mensuales")
#     st.pyplot(fig)

#     # --- Botón para volver a Home ---
#     if st.button("⬅️ Volver al inicio"):
#         st.session_state["pagina"] = "Home"
#         st.rerun()

# elif pagina == "Admin":
#     st.title("⚙️ Administración")
#     st.write("Opciones de configuración y control del sistema.")

#     # --- Botón para volver a Home ---
#     if st.button("⬅️ Volver al inicio"):
#         st.session_state["pagina"] = "Home"
#         st.rerun()


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- Configuración inicial ---
st.set_page_config(page_title="Estudio Web",
                   page_icon="favicon.png",  # Usa el archivo local,
                    layout="centered")


# --- Funciones por página ---
def mostrar_home():
    st.title("🏠 Bienvenido")
    st.write("Esta es la página de inicio.")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("📊 Ir a Reportes"):
            st.session_state["pagina"] = "Reportes"
            st.rerun()
    with col2:
        if st.button("⚙️ Ir a Admin"):
            st.session_state["pagina"] = "Admin"
            st.rerun()


def mostrar_reportes():
    st.title("📊 Reportes")

    if st.button("⬅️ Volver al inicio"):
        st.session_state["pagina"] = "Home"
        st.rerun()

    df = pd.DataFrame({
        "Mes": ["Enero", "Febrero", "Marzo", "Abril"],
        "Ventas": [12000, 15000, 13000, 17000]
    })
    st.dataframe(df, use_container_width=True)

    fig, ax = plt.subplots()
    ax.plot(df["Mes"], df["Ventas"], marker='o')
    ax.set_title("Ventas mensuales")
    st.pyplot(fig)




def mostrar_admin():

    st.title("⚙️ Administración")
    st.write("Opciones de configuración y control del sistema.")

    if st.button("⬅️ Volver al inicio"):
        st.session_state["pagina"] = "Home"
        st.rerun()


def menu_sidebar():
    st.sidebar.title("📚 Menú")
    if st.sidebar.button("🏠 Home"):
        st.session_state["pagina"] = "Home"
    if st.sidebar.button("📊 Reportes"):
        st.session_state["pagina"] = "Reportes"
    if st.sidebar.button("⚙️ Admin"):
        st.session_state["pagina"] = "Admin"
    if st.sidebar.button("🔒 Cerrar sesión"):
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
        if st.button("Ingresar"):
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
    if pagina == "Home":
        mostrar_home()
    elif pagina == "Reportes":
        mostrar_reportes()
    elif pagina == "Admin":
        mostrar_admin()


# --- Ejecutar ---
if __name__ == "__main__":
    main()
