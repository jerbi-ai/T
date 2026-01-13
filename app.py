# realtime_clock_tunisia.py
import streamlit as st
import datetime
import time
import pytz  # pour gérer le fuseau horaire

st.set_page_config(page_title="Horloge Tunisie", layout="centered")
st.title("🕒 Heure en Temps Réel - Tunisie")

# Conteneur vide pour l'heure
clock_placeholder = st.empty()

# Fuseau horaire Tunisie
tunis_tz = pytz.timezone("Africa/Tunis")

while True:
    now = datetime.datetime.now(tunis_tz)
