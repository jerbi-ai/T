# realtime_clock.py
import streamlit as st
import datetime
import time

st.set_page_config(page_title="Horloge en Temps Réel", layout="centered")
st.title("🕒 Horloge en Temps Réel")

# Créer un conteneur vide qui sera mis à jour
clock_placeholder = st.empty()

# Boucle infinie pour mettre à jour l'heure
while True:
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")  # Format Heure:Minute:Seconde
    current_date = now.strftime("%A %d %B %Y")  # Format Jour Date Mois Année
    clock_placeholder.markdown(f"### {current_date}\n## {current_time}")
    time.sleep(1)
