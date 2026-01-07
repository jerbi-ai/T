import streamlit as st
from PIL import Image

# Charger l'image
image = Image.open("OneTech.jpg")

# Titre de l'application
st.title("Affichage d'une image")

# Afficher l'image
st.image(image, caption="Image OneTech", use_container_width=True)
