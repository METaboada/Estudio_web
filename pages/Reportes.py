import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---- CONTROL DE AUTENTICACIÓN ----
if "autenticado" not in st.session_state or not st.session_state["autenticado"]:
    st.warning("⚠️ No estás autenticado. Volvé a la página principal.")
    st.stop()

# ---- CONTENIDO DE LA PÁGINA DE REPORTES ----
st.title("📊 Reportes")

st.subheader("Resumen de ventas")

# Ejemplo de dataframe demo
df = pd.DataFrame({
    "Mes": ["Enero", "Febrero", "Marzo", "Abril"],
    "Ventas": [12000, 15000, 13000, 17000]
})

# Mostrar tabla
st.dataframe(df, use_container_width=True)

# Graficar
fig, ax = plt.subplots()
ax.plot(df["Mes"], df["Ventas"], marker='o')
ax.set_title("Ventas mensuales")
ax.set_ylabel("Monto")
st.pyplot(fig)
