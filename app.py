import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ===============================
# CONFIGURATION PAGE
# ===============================
st.set_page_config(layout="wide")

# ===============================
# CSS : BACKGROUND ORANGE + POLICES
# ===============================
st.markdown("""
<style>
.stApp {
    background-color: #F28C28; /* ORANGE PRO */
}

h1, h2, h3, h4, h5, h6, p, span, label {
    color: white !important;
    font-size: 14px;
}

[data-testid="metric-container"] {
    background-color: rgba(255,255,255,0.15);
    padding: 10px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# ===============================
# TITRE
# ===============================
st.markdown("<h1 style='font-size:26px;'>📊 Financial Dashboard</h1>", unsafe_allow_html=True)

# ===============================
# KPIs
# ===============================
kpi1, kpi2, kpi3, kpi4 = st.columns(4)

kpi1.metric("Accounts Receivable", "$6,621,280")
kpi2.metric("Accounts Payable", "$1,630,270")
kpi3.metric("Equity Ratio", "75.38 %")
kpi4.metric("Debt Equity", "1.10 %")

# ===============================
# GAUGES (DONUTS)
# ===============================
def donut(value, max_value, title, color):
    fig, ax = plt.subplots(figsize=(2,2))
    ax.pie(
        [value, max_value - value],
        colors=[color, "rgba(255,255,255,0.3)"],
        startangle=90,
        counterclock=False,
        wedgeprops={"width":0.3}
    )
    ax.set(aspect="equal")
    ax.set_title(title, fontsize=10, color="white")
    fig.patch.set_alpha(0)
    return fig

g1, g2, g3, g4 = st.columns(4)

with g1:
    st.pyplot(donut(0.7, 1, "Current Ratio", "#003f5c"))
with g2:
    st.pyplot(donut(10, 31, "DSI", "#bc5090"))
with g3:
    st.pyplot(donut(7, 31, "DSO", "#ff6361"))
with g4:
    st.pyplot(donut(28, 31, "DPO", "#58508d"))

# ===============================
# BAR CHART
# ===============================
st.markdown("### Accounts Aging")

df_bar = pd.DataFrame({
    "Age": ["Current", "1-30", "31-60", "61-90", "91+"],
    "Receivable": [2100000, 1700000, 900000, 600000, 200000],
    "Payable": [1200000, 250000, 100000, 80000, 20000]
})

fig_bar = go.Figure()
fig_bar.add_bar(x=df_bar["Age"], y=df_bar["Receivable"], name="Receivable")
fig_bar.add_bar(x=df_bar["Age"], y=df_bar["Payable"], name="Payable")

fig_bar.update_layout(
    barmode="group",
    height=300,
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    font=dict(color="white", size=12),
    legend=dict(font=dict(color="white"))
)

st.plotly_chart(fig_bar, use_container_width=True)

# ===============================
# LINE CH
