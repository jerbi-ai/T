# safeyear2026.py

import streamlit as st
import pandas as pd
import datetime

# ======================
# Initialisation
# ======================
st.set_page_config(page_title="SafeYear 2026", layout="wide")

# TITRE COLORÉ EN HAUT
st.markdown(
    """
    <h1 style='text-align: center;'>
        <span style='color: blue;'>TTE</span> 
        <span style='color: orange;'>INTERNATIONAL</span>
    </h1>
    """,
    unsafe_allow_html=True
)

# Sous-titre
st.subheader("📅 SafeYear 2026 - Suivi des accidents")

# ======================
# Création du calendrier
# ======================
@st.cache_data
def create_calendar():
    start_date = datetime.date(2026, 1, 1)
    end_date = datetime.date(2026, 12, 31)
    dates = pd.date_range(start=start_date, end=end_date)
    df = pd.DataFrame(dates, columns=["Date"])
    df["Accident"] = False
    return df

df = create_calendar()

# ======================
# Limiter jusqu'à hier
# ======================
yesterday = datetime.date.today() - datetime.timedelta(days=1)
df = df[df["Date"] <= pd.Timestamp(yesterday)]

# ======================
# Ajout accident (Sidebar)
# ======================
st.sidebar.header("📌 Enregistrer un accident")

date_accident = st.sidebar.date_input(
    "Date de l'accident",
    value=yesterday,
    max_value=yesterday  # on ne peut pas sélectionner demain ou aujourd'hui
)

description = st.sidebar.text_input("Description (optionnelle)")

if st.sidebar.button("Ajouter accident"):
    df.loc[df["Date"] == pd.Timestamp(date_accident), "Accident"] = True
    st.sidebar.success(f"Accident ajouté pour {date_accident}")

# ======================
# Calcul des jours sans accident
# ======================
def calculate_lta_days(df):
    count = 0
    consecutive = []

    for accident in df["Accident"]:
        if not accident:
            count += 1
        else:
            count = 0
        consecutive.append(count)

    df["JoursSansAccident"] = consecutive
    return df

df = calculate_lta_days(df)

# ======================
# 📊 STATISTIQUES GLOBALES (EN HAUT)
# ======================
st.subheader("📊 Statistiques globales (du 1er janvier jusqu'à hier)")

total_days_without_accident = df["JoursSansAccident"].iloc[-1]
total_accidents = df["Accident"].sum()

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Jours sans accident depuis le 1er janvier",
        total_days_without_accident
    )

with col2:
    st.metric(
        "Total d'accidents enregistrés",
        total_accidents
    )

st.divider()

# ======================
# Affichage du calendrier
# ======================
st.subheader("📅 Calendrier (du 1er janvier jusqu'à hier)")

months = df["Date"].dt.month.unique()

for month in months:
    month_name = (
        df[df["Date"].dt.month == month]["Date"]
        .dt.strftime("%B %Y")
        .iloc[0]
    )

    st.markdown(f"### {month_name}")

    month_df = df[df["Date"].dt.month == month]

    display_df = pd.DataFrame({
        "Jour": month_df["Date"].dt.day,
        "Accident": month_df["Accident"].apply(
            lambda x: "🔴" if x else "🟢"
        ),
        "Jours consécutifs sans accident": month_df["JoursSansAccident"]
    })

    st.table(display_df)
