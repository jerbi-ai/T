import streamlit as st

st.title("Live Camera Streamlit")

# Affiche un flux de la caméra dans le navigateur
img = st.camera_input("Prenez une photo ou activez la caméra")

if img:
    st.image(img)
