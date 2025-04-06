import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="📊 Reportes", layout="centered")

st.title("📊 Reportes de Ventas")

df = pd.DataFrame({
    "Mes": ["Enero", "Febrero", "Marzo", "Abril"],
    "Ventas": [12000, 15000, 13000, 17000]
})

st.dataframe(df, use_container_width=True)

fig, ax = plt.subplots()
ax.plot(df["Mes"], df["Ventas"], marker='o')
ax.set_title("Ventas mensuales")
ax.set_ylabel("Monto")
st.pyplot(fig)
