import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# ===============================
# CONFIGURATION PAGE
# ===============================
st.set_page_config(layout="wide")
st.markdown("""
    <style>
    /* Réduire les titres et textes */
    .css-18e3th9 {padding-top: 0rem;}
    h1 {font-size: 28px;}
    h2 {font-size: 22px;}
    h3 {font-size: 18px;}
    p, span {font-size: 14px;}
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1>Financial Dashboard</h1>', unsafe_allow_html=True)

# ===============================
# PHOTO EN HAUT À DROITE
# ===============================
col_logo1, col_logo2 = st.columns([6,1])
with col_logo2:
    image = Image.open("photo.jpg")  # Remplace par ton fichier
    st.image(image, use_column_width=True)

# ===============================
# KPIs PRINCIPAUX
# ===============================
kpi_cols = st.columns(4)
kpi_cols[0].metric("Total Accounts Receivable", "$6,621,280")
kpi_cols[1].metric("Total Accounts Payable", "$1,630,270")
kpi_cols[2].metric("Equity Ratio", "75.38 %")
kpi_cols[3].metric("Debt Equity", "1.10 %")

# ===============================
# GAUGES DONUTS (Matplotlib)
# ===============================
def plot_gauge(value, max_value=31, color='skyblue', title=""):
    fig, ax = plt.subplots(figsize=(2,2))
    ax.pie([value, max_value-value], colors=[color, 'lightgray'],
           startangle=90, counterclock=False, wedgeprops={'width':0.3})
    ax.set(aspect="equal")
    plt.title(title, fontsize=10)
    return fig

gauge_cols = st.columns(4)
with gauge_cols[0]:
    st.pyplot(plot_gauge(0.0186, 1, 'navy', "Current Ratio"))
with gauge_cols[1]:
    st.pyplot(plot_gauge(10, 31, 'orange', "DSI"))
with gauge_cols[2]:
    st.pyplot(plot_gauge(7, 31, 'red', "DSO"))
with gauge_cols[3]:
    st.pyplot(plot_gauge(28, 31, 'green', "DPO"))

# ===============================
# BAR CHART (Accounts Receivable & Payable)
# ===============================
st.subheader("Accounts Receivable and Payable Aging")
df_bar = pd.DataFrame({
    "Age": ["Current", "1-30", "31-60", "61-90", "91+"],
    "Accounts Receivable": [2100000, 1700000, 900000, 600000, 200000],
    "Accounts Payable": [1200000, 250000, 100000, 80000, 20000]
})
fig_bar = go.Figure()
fig_bar.add_trace(go.Bar(x=df_bar["Age"], y=df_bar["Accounts Receivable"], name="Accounts Receivable"))
fig_bar.add_trace(go.Bar(x=df_bar["Age"], y=df_bar["Accounts Payable"], name="Accounts Payable"))
fig_bar.update_layout(barmode='group', height=300, font=dict(size=12))
st.plotly_chart(fig_bar, use_container_width=True)

# ===============================
# LINE CHART (Net vs Gross Working Capital)
# ===============================
st.subheader("Net Working Capital vs Gross Working Capital")
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
net_wc = [100000, 120000, 110000, 150000, 170000, 140000, 180000, 190000, 160000, 140000, 130000, 120000]
gross_wc = [200000, 220000, 210000, 250000, 270000, 240000, 280000, 290000, 260000, 240000, 230000, 220000]

fig_line = go.Figure()
fig_line.add_trace(go.Scatter(x=months, y=net_wc, mode='lines+markers', name='Net Working Capital'))
fig_line.add_trace(go.Scatter(x=months, y=gross_wc, mode='lines+markers', name='Gross Working Capital'))
fig_line.update_layout(height=300, font=dict(size=12))
st.plotly_chart(fig_line, use_container_width=True)

# ===============================
# STACKED BAR CHART (Profit & Loss)
# ===============================
st.subheader("Profit and Loss Summary")
profit_data = pd.DataFrame({
    "Month": months,
    "Revenue": np.random.randint(500000, 1000000, 12),
    "Cost": np.random.randint(200000, 500000, 12),
    "Expense": np.random.randint(100000, 200000, 12)
})
fig_stack = go.Figure()
fig_stack.add_trace(go.Bar(x=profit_data["Month"], y=profit_data["Revenue"], name="Revenue"))
fig_stack.add_trace(go.Bar(x=profit_data["Month"], y=profit_data["Cost"], name="Cost"))
fig_stack.add_trace(go.Bar(x=profit_data["Month"], y=profit_data["Expense"], name="Expense"))
fig_stack.update_layout(barmode='stack', height=300, font=dict(size=12))
st.plotly_chart(fig_stack, use_container_width=True)
