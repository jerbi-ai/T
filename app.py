import streamlit as st
import datetime
from pytz import timezone
from streamlit_autorefresh import st_autorefresh

st.set_page_config(page_title="Horloge Tunisie", layout="centered")
st.title("🕒 Heure en Temps Réel - Tunisie")

# Rafraîchissement automatique toutes les 1000 ms
st_autorefresh(interval=1000, key="clock")

tunis_tz = timezone("Africa/Tunis")
now = datetime.datetime.now(tunis_tz)
current_time = now.strftime("%H:%M:%S")
current_date = now.strftime("%A %d %B %Y")

st.markdown(f"### {current_date}\n## {current_time}")
