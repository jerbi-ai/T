import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ===============================
# CONFIG PAGE
# ===============================
st.set_page_config(layout="wide")

# ===============================
# CSS : BACKGROUND ORANGE + STYLE
# ===============================
st.markdown("""
<style>
.stApp {
    background-color: #F28C28;
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
st.markdown("<h1 style='font-size:26px;'>📊TEST</h1>", unsafe_allow_html=True)

# ===============================
# KPIs
# ===============================
k1, k2, k3, k4 = st.columns(4)
k1.metric("Accounts Receivable", "$300,621,280")
k2.metric("Accounts Payable", "$1,630,270")
k3.metric("Equity Ratio", "75.38 %")
k4.metric("Debt Equity", "1.10 %")

# ===============================
# DONUTS / GAUGES (CORRIGÉS)
# ===============================
def donut(value, max_value, title, color):
    fig, ax = plt.subplots(figsize=(2,2))

    ax.pie(
        [value, max_value - value],
        colors=[color, (1, 1, 1, 0.3)],  # RGBA VALIDE
        startangle=90,
        counterclock=False,
        wedgeprops={"width": 0.3}
    )

    ax.set(aspect="equal")
    ax.set_title(title, fontsize=10, color="white")

    fig.patch.set_alpha(0)
    ax.set_facecolor("none")

    return fig

d1, d2, d3, d4 = st.columns(4)

with d1:
    st.pyplot(donut(0.7, 1, "Current Ratio", "#003f5c"))
with d2:
    st.pyplot(donut(10, 31, "DSI", "#bc5090"))
with d3:
    st.pyplot(donut(7, 31, "DSO", "#ff6361"))
with d4:
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
# LINE CHART
# ===============================
st.markdown("### Working Capital")

months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
net_wc = np.random.randint(100000, 200000, 12)
gross_wc = np.random.randint(200000, 300000, 12)

fig_line = go.Figure()
fig_line.add_trace(go.Scatter(x=months, y=net_wc, name="Net WC", mode="lines+markers"))
fig_line.add_trace(go.Scatter(x=months, y=gross_wc, name="Gross WC", mode="lines+markers"))

fig_line.update_layout(
    height=300,
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    font=dict(color="white", size=12),
    legend=dict(font=dict(color="white"))
)

st.plotly_chart(fig_line, use_container_width=True)

# ===============================
# STACKED BAR
# ===============================
st.markdown("### Profit & Loss")

df_pl = pd.DataFrame({
    "Month": months,
    "Revenue": np.random.randint(500000, 900000, 12),
    "Cost": np.random.randint(200000, 500000, 12),
    "Expense": np.random.randint(100000, 200000, 12)
})

fig_pl = go.Figure()
fig_pl.add_bar(x=df_pl["Month"], y=df_pl["Revenue"], name="Revenue")
fig_pl.add_bar(x=df_pl["Month"], y=df_pl["Cost"], name="Cost")
fig_pl.add_bar(x=df_pl["Month"], y=df_pl["Expense"], name="Expense")

fig_pl.update_layout(
    barmode="stack",
    height=300,
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    font=dict(color="white", size=12),
    legend=dict(font=dict(color="white"))
)

st.plotly_chart(fig_pl, use_container_width=True)
