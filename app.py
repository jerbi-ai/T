import streamlit as st
import pandas as pd
import time
from datetime import datetime

# Configuration de la page
st.set_page_config(layout="wide")
st.title("📋 Tableau de Lecture de Fichier Texte")

# Style CSS personnalisé
st.markdown("""
<style>
table {
    width: 100%;
    border-collapse: collapse;
}
th, td {
    border: 1px solid #dddddd;
    text-align: left;
    padding: 8px;
}
tr:nth-child(even) {
    background-color: #f2f2f2;
}
.file-info {
    color: #666;
    font-size: 0.9em;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

def read_file_to_table(file_path):
    """Lit un fichier texte et retourne un DataFrame avec chaque ligne dans une cellule"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]
        
        # Création du DataFrame
        df = pd.DataFrame({
            "Ligne": range(1, len(lines)+1,
            "Contenu": lines
        })
        return df, len(lines)
    
    except FileNotFoundError:
        return None, 0

# Interface utilisateur
file_path = "mon_fichier.txt"
refresh_interval = st.slider("Intervalle de rafraîchissement (secondes)", 1, 10, 2)

placeholder = st.empty()

while True:
    # Lecture du fichier
    df, line_count = read_file_to_table(file_path)
    
    with placeholder.container():
        # Affichage des métadonnées
        st.markdown(f"""
        <div class="file-info">
            Dernière mise à jour: {datetime.now().strftime('%H:%M:%S')} | 
            Fichier: {file_path} | 
            Lignes: {line_count}
        </div>
        """, unsafe_allow_html=True)
        
        # Affichage du tableau
        if df is not None:
            st.table(df)
        else:
            st.error(f"Fichier {file_path} non trouvé")
    
    time.sleep(refresh_interval)
