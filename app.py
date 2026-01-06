# fichier : app.py
import streamlit as st
import plotly.graph_objects as go

st.title("Cercle de Pourcentage Professionnel")

# Choix du pourcentage
pourcentage = st.slider("Sélectionnez un pourcentage :", 0, 100, 65)

# Création du graphique type "gauge"
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=pourcentage,
    number={'suffix': "%", 'font': {'size': 36}},
    gauge={
        'axis': {'range': [0, 100], 'tickwidth': 2, 'tickcolor': "darkblue"},
        'bar': {'color': "skyblue", 'thickness': 0.3},
        'bgcolor': "lightgray",
        'borderwidth': 2,
        'bordercolor': "gray",
        'steps': [
            {'range': [0, 50], 'color': 'lightcoral'},
            {'range': [50, 75], 'color': 'gold'},
            {'range': [75, 100], 'color': 'lightgreen'}
        ],
        'threshold': {
            'line': {'color': "red", 'width': 4},
            'thickness': 0.75,
            'value': pourcentage
        }
    }
))

fig.update_layout(height=400)

# Affichage dans Streamlit
st.plotly_chart(fig)
