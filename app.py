import streamlit as st
import matplotlib.pyplot as plt

# --- CSS pour l'image en arrière-plan ---
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("OneTech.jpg");
        background-size: cover;
        background-position: center;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# --- Titre ---
st.title("Suivi des accidents")

# --- Données ---
nombre_accidents = 35

# --- Affichage de la note ---
st.markdown(f"📊 **Le nombre d'accidents ce mois est {nombre_accidents}**")

# --- Graphique ---
mois = ["Ce mois"]
valeurs = [nombre_accidents]

plt.bar(mois, valeurs, color='red')
plt.ylabel("Nombre d'accidents")
plt.title("Accidents ce mois")
st.pyplot(plt)
