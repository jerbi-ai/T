
import streamlit as st
import base64

st.set_page_config(layout="wide", page_title="Photo Plein Écran")

# --- Fonction pour convertir une image en base64 ---
def image_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# --- UI ---
st.title("Photo Plein Écran (Background)")
st.write("Charge une image pour l'afficher sur toute la fenêtre.")

uploaded_file = st.file_uploader("Choisir une image (JPG/PNG)", type=["jpg", "jpeg", "png"])

# --- CSS de fond plein écran ---
if uploaded_file:
    # Sauvegarder le fichier uploadé pour lecture
    with open("temp_image", "wb") as f:
        f.write(uploaded_file.getbuffer())

    b64_img = image_to_base64("temp_image")

    page_bg_css = f"""
    <style>
    /* Supprime les marges/paddings par défaut */
    .stApp {{
        margin: 0;
        padding: 0;
        height: 100vh;
        background-image: url("data:image/png;base64,{b64_img}");
        background-size: cover;       /* couvre toute la fenêtre, coupe si besoin */
        background-position: center;  /* centre l'image */
        background-repeat: no-repeat;
    }}

    /* Optionnel : cacher l’en-tête et le footer Streamlit pour un vrai plein écran */
    header, footer {{
        visibility: hidden;
        height: 0;
    }}
    </style>
    """

    st.markdown(page_bg_css, unsafe_allow_html=True)

    # Optionnel : afficher un overlay de texte
    st.markdown(
        """
        <div style="
            position: fixed;
            bottom: 20px;
            left: 20px;
            color: white;
            font-size: 18px;
            text-shadow: 0 2px 4px rgba(0,0,0,0.6);
        ">
            Image en arrière-plan (plein écran)
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.info("Importe une image pour l’afficher en fond de page.")
