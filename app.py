# fichier : app.py
import streamlit as st
import cv2

st.title("Live Camera avec Streamlit")

# Accès à la caméra
run = st.checkbox('Activer la caméra')

# Zone où afficher la vidéo
FRAME_WINDOW = st.image([])

# Initialiser la caméra
cap = cv2.VideoCapture(0)  # 0 = webcam par défaut

while run:
    ret, frame = cap.read()
    if not ret:
        st.warning("Impossible d'accéder à la caméra")
        break
    # Convertir BGR (OpenCV) en RGB (Streamlit)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)
    
cap.release()
