import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")  # Dashboard en largeur complète
st.title("Financial Dashboard Example")

# ===============================
# 1️⃣ Top KPIs
# ===============================
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Accounts Receivable", "$6,621,280")
col2.metric("Total Accounts Payable", "$1,630,270")
col3.metric("Equity Ratio", "75.38 %")
col4.metric("Debt Equity", "1.10 %")

# ===============================
# 2️⃣ Gauges style "donut" (Matplotlib)
# ===============================
kpi_cols = st.columns(4)

# Exemple de valeurs
current_ratio = 0.0186
dso = 10
dpo = 28
days_sales = 7

def plot_gauge(value, max_value=31, color='skyblue'):
    fig, ax = plt.subplots(figsize=(2,2))
    ax.pie([value, max_value-value], colors=[color, 'lightgray'],
           startangle=90, counterclock=False, wedgeprops={'width':0.3})
    ax.set(aspect="equal")
    return fig

with kpi_cols[0]:
    st.text("Current Ratio")
    st.pyplot(plot_gauge(current_ratio, 1, 'navy'))

with kpi_cols[1]:
    st.text("DSI (Days Sales Inventory)")
    st.pyplot(plot_gauge(dso, 31, 'orange'))

with kpi_cols[2]:
    st.text("DSO (Days Sales Outstanding)")
    st.pyplot(plot_gauge(days_sales, 31, 'red'))

with kpi_cols[3]:
    st.text("DPO (Days Payable Outstanding)")
    st.pyplot(plot_gauge(dpo, 31, 'green'))

# ===============================
# 3️⃣ Bar chart (Accounts Receivable & Payable)
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
fig_bar.update_layout(barmode='group', height=350)
st.plotly_chart(fig_bar, use_container_width=True)

# ===============================
# 4️⃣ Line chart (Net Working Capital)
# ===============================
st.subheader("Net Working Capital vs Gross Working Capital")
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
net_wc = [100000, 120000, 110000, 150000, 170000, 140000, 180000, 190000, 160000, 140000, 130000, 120000]
gross_wc = [200000, 220000, 210000, 250000, 270000, 240000, 280000, 290000, 260000, 240000, 230000, 220000]

fig_line = go.Figure()
fig_line.add_trace(go.Scatter(x=months, y=net_wc, mode='lines+markers', name='Net Working Capital'))
fig_line.add_trace(go.Scatter(x=months, y=gross_wc, mode='lines+markers', name='Gross Working Capital'))
fig_line.update_layout(height=350)
st.plotly_chart(fig_line, use_container_width=True)

# ===============================
# 5️⃣ Stacked bar chart (Profit & Loss summary)
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
fig_stack.update_layout(barmode='stack', height=350)
st.plotly_chart(fig_stack, use_container_width=True)
