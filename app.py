import streamlit as st
import plotly.graph_objects as go
from PIL import Image

st.title("Dashboard avec Photo et Cercle de Pourcentage")

# Chargement de l'image
image = Image.open("OneTech.jpg")  # Remplace par le nom de ton fichier

# Création de 2 colonnes
col1, col2 = st.columns([3, 1])  # col1 plus large pour le graphique, col2 pour la photo

# 1️⃣ Photo dans la colonne de droite
with col2:
    st.image(image, caption="Photo", use_column_width=True)

# 2️⃣ Contenu principal dans la colonne de gauche
with col1:
    st.subheader("Cercle de pourcentage")
    pourcentage = st.slider("Sélectionnez un pourcentage :", 0, 100, 65)
    
    # Cercle de pourcentage avec Plotly
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
    st.plotly_chart(fig)
