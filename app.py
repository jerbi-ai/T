# fichier : app.py
import streamlit as st
import plotly.graph_objects as go
from PIL import Image

# Titre
st.title("Cercle de Pourcentage avec Image")

# Charger une image
image = Image.open("OneTech.jpg")  # Remplace par le nom de ton fichier
st.image(image, caption="Voici mon image", use_column_width=True)

# Slider pour le pourcentage
pourcentage = st.slider("Sélectionnez un pourcentage :", 0, 100, 65)

# Cercle de pourcentage professionnel avec Plotly
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=pourcentage,
    number={'suffix': "%", 'font': {'size': 36}},
    gauge={
        'axis': {'range': [0, 100]},
        'bar': {'color': "skyblue", 'thickness': 0.3},
        'bgcolor': "lightgray",
        'steps': [
            {'range': [0, 50], 'color': 'lightcoral'},
            {'range': [50, 75], 'color': 'gold'},
            {'range': [75, 100], 'color': 'lightgreen'}
        ],
    }
))
fig.update_layout(height=400)

# Affichage du graphique
st.plotly_chart(fig)
