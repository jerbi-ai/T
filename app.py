import streamlit as st

# Titre de l'application
st.title("nombre de reclamations")

# Données (ici on met un exemple)
nombre_accidents = 3

# Affichage de la note
st.markdown(f"📊 **Le nombre d'accidents ce mois est {nombre_accidents}**")

# Optionnel : ajouter un graphique simple
import matplotlib.pyplot as plt

# Exemple de graphique pour visualiser
mois = ["Ce mois"]
valeurs = [nombre_accidents]

plt.bar(mois, valeurs, color='red')
plt.ylabel("Nombre d'accidents")
plt.title("Accidents ce mois")
st.pyplot(plt)
