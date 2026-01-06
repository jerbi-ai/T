import streamlit as st
import plotly.graph_objects as go

st.title("Dashboard avec photo à l'extrême droite")

# Charger l'image depuis fichier ou URL
photo_url = "OneTech.jpg"  # ou une URL

# Affichage de la photo à droite avec HTML/CSS
st.markdown(
    f"""
    <div style="display: flex; justify-content: flex-end;">
        <img src="{photo_url}" width="200">
    </div>
    """,
    unsafe_allow_html=True
)

# Cercle de pourcentage en dessous (ou tu peux ajouter d'autres éléments)
st.subheader("Cercle de pourcentage")
pourcentage = st.slider("Sélectionnez un pourcentage :", 0, 100, 65)

fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=pourcentage,
    number={'suffix': "%", 'font': {'size': 36}},
    gauge={
        'axis': {'range': [0, 100]},
        'bar': {'color': "skyblue", 'thickness': 0.3},
        'bgcolor': "lightgray",
        'steps': [
            {'range': [0, 50], 'color': 'lightcoral'},
            {'range': [50, 75], 'color': 'gold'},
            {'range': [75, 100], 'color': 'lightgreen'}
        ],
    }
))
fig.update_layout(height=400)
st.plotly_chart(fig)
