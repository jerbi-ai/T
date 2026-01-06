# fichier : app.py
import streamlit as st
import matplotlib.pyplot as plt

# Titre de l'application
st.title("Exemple de Diagramme avec Streamlit")

# Données pour le diagramme
categories = ['A', 'B', 'C', 'D']
valeurs = [10, 20, 15, 30]

# Création du diagramme
fig, ax = plt.subplots()
ax.bar(categories, valeurs, color='skyblue')
ax.set_xlabel('Catégories')
ax.set_ylabel('Valeurs')
ax.set_title('Diagramme à Barres Exemple')

# Affichage du diagramme dans Streamlit
st.pyplot(fig)
