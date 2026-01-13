import streamlit as st
import plotly.graph_objects as go

# Valeur fixe
valeur = 90  # ici on fixe la valeur à 75

# Création de la jauge
fig = go.Figure(go.Indicator(
    mode="gauge+number+delta",
    value=valeur,
    domain={'x': [0, 1], 'y': [0, 1]},
    title={'text': "Nombre de jours"},
    gauge={
        'axis': {'range': [0, 100]},
        'bar': {'color': "blue"},
        'steps': [
            {'range': [0, 50], 'color': "lightgray"},
            {'range': [50, 100], 'color': "gray"}],
        'threshold': {
            'line': {'color': "red", 'width': 4},
            'thickness': 0.75,
            'value': valeur}}))

st.plotly_chart(fig, use_container_width=True)
