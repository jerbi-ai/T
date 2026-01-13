import streamlit as st
import plotly.graph_objects as go

# Exemple de valeur à afficher
valeur = st.slider("Choisis une valeur", 0, 100, 25)

# Création de la jauge
fig = go.Figure(go.Indicator(
    mode="gauge+number+delta",
    value=valeur,
    domain={'x': [0, 1], 'y': [0, 1]},
    title={'text': "Performance"},
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
