import streamlit as st
import time
from datetime import datetime

st.set_page_config(layout="wide")

# Style CSS personnalisé
st.markdown("""
<style>
.file-display {
    background-color: #f0f2f6;
    border-radius: 10px;
    padding: 15px;
    font-family: monospace;
}
</style>
""", unsafe_allow_html=True)

# Lecture auto-rafraîchie
def auto_refreshing_reader(file_path, refresh_interval=2):
    last_update = st.empty()
    content_display = st.empty()
    
    while True:
        try:
            with open(file_path) as f:
                content = f.read()
            
            # Affichage avec style
            last_update.markdown(f"Dernière mise à jour : {datetime.now().strftime('%H:%M:%S')}")
            content_display.markdown(f'<div class="file-display">{content}</div>', 
                                   unsafe_allow_html=True)
        
        except FileNotFoundError:
            content_display.error("Fichier non trouvé")
        
        time.sleep(refresh_interval)

# Lancement
auto_refreshing_reader("mon_fichier.txt")
