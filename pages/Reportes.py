import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---- CONTROL DE AUTENTICACIÓN ----
if "autenticado" not in st.session_state or not st.session_state["autenticado"]:
    st.warning("⚠️ No estás autenticado. Volvé a la página principal.")
    st.stop()

# ---- TÍTULO Y ENCABEZADO ----
st.title("📊 Reportes")
st.markdown("En esta sección podés visualizar el resumen de ventas mensuales.")

# ---- DATAFRAME DEMO ----
st.subheader("📅 Ventas por Mes")

df = pd.DataFrame({
    "Mes": ["Enero", "Febrero", "Marzo", "Abril"],
    "Ventas": [12000, 15000, 13000, 17000]
})

st.dataframe(df, use_container_width=True)

# ---- GRÁFICO LINEAL ----
st.subheader("📈 Evolución de Ventas")

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(df["Mes"], df["Ventas"], marker='o', color='royalblue', linestyle='-')
ax.set_title("Ventas Mensuales", fontsize=14)
ax.set_ylabel("Monto en $", fontsize=12)
ax.set_xlabel("Mes", fontsize=12)
ax.grid(True, linestyle="--", alpha=0.5)

st.pyplot(fig)
