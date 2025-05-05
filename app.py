import streamlit as st

# Titre de l'application
st.title("🖥️ Monji Première App Streamlit")

# 1. Lire le fichier texte
try:
    with open("mon_fichier.txt", "r", encoding="utf-8") as file:
        contenu_fichier = file.read()
except FileNotFoundError:
    contenu_fichier = "⚠️ Fichier non trouvé (créez un fichier 'mon_fichier.txt' dans le même dossier)"

# 2. Afficher le contenu du fichier dans une boîte dédiée
st.subheader("Contenu du fichier texte :")
st.text_area("", contenu_fichier, height=200)

# Saisie utilisateur
nom = st.text_input("Comment tu t'appelles ?")
age = st.slider("Quel âge as-tu ?", 0, 100)

# Bouton de validation
if st.button("Valider"):
    if nom:
        st.success(f"Salut {nom} ! Tu as {age} ans 🎉")
    else:
        st.warning("⚠️ Oublie pas de rentrer ton nom !")

# Bonus : Case à cocher
if st.checkbox("Afficher un message secret"):
    st.write("🔐 Le code secret est : **1234**")
