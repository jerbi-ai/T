# fichier : app.py
import streamlit as st
import matplotlib.pyplot as plt

# Titre de l'application
st.title("Diagramme Circulaire de Pourcentage")

# Saisie du pourcentage par l'utilisateur
pourcentage = st.slider("Choisissez un pourcentage :", 0, 100, 50)

# Données pour le diagramme
valeurs = [pourcentage, 100 - pourcentage]
labels = [f"{pourcentage}%", ""]

# Création du diagramme circulaire
fig, ax = plt.subplots()
ax.pie(valeurs, labels=labels, colors=['skyblue', 'lightgray'], startangle=90, counterclock=False, wedgeprops={'width':0.3})
ax.set(aspect="equal")  # Cercle parfait

# Affichage dans Streamlit
st.pyplot(fig)
