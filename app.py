# lire_CR3.py
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Lecture CR3.xlsx", layout="centered")
st.title("📊 Affichage du fichier CR3.xlsx")

# Lire directement le fichier (s'il est dans le même dossier que ce script)
try:
    df = pd.read_excel("CR3.xlsx")
    st.write("Aperçu du fichier :")
    st.dataframe(df)  # Affiche le tableau dans Streamlit

    # Optionnel : quelques statistiques
    st.subheader("Statistiques rapides")
    st.write(df.describe())  # Moyenne, min, max, etc. pour les colonnes numériques

except FileNotFoundError:
    st.error("Le fichier CR3.xlsx n'a pas été trouvé dans le dossier du script.")
