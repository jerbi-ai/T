import streamlit as st

# Titre de l'application
st.title("🖥️ Chmissi Première App Streamlit")

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
