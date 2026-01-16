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
        <span style='color: blue;'>ONE</span><span style='color: orange;'>TECH</span>
    </h1>
    """,
    unsafe_allow_html=True
)

# Sous-titre
st.subheader("🚨 Suivi des accidents")

# ======================
# Dernier accident connu (OFFICIEL)
# ======================
last_accident_date = datetime.date(2026, 1, 14)
last_accident_desc = (
    "L’accident s’est produit lors d’une opération de manutention. L’agent de bord de ligne procédait au transport d’une bobine à l’aide d’un chariot. Celui-ci est devenu instable, provoquant la chute de la bobine sur le genou gauche de l’opérateur."
    
)

# ======================
# Dates utiles
# ======================
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)

# ======================
# Création du calendrier 2026
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
# Déclaration de l'accident du 14 janvier 2026
# ======================
df.loc[df["Date"] == pd.Timestamp("2026-01-14"), "Accident"] = True

# ======================
# Limiter l'affichage jusqu'à hier
# ======================
df = df[df["Date"] <= pd.Timestamp(yesterday)]

# ======================
# Ajout accident manuel (Sidebar)
# ======================
st.sidebar.header("📌 Enregistrer un accident")

date_accident = st.sidebar.date_input(
    "Date de l'accident",
    value=yesterday,
    min_value=datetime.date(2026, 1, 1),
    max_value=yesterday
)

if st.sidebar.button("Ajouter accident"):
    df.loc[df["Date"] == pd.Timestamp(date_accident), "Accident"] = True
    st.sidebar.success(f"Accident ajouté pour {date_accident}")

# ======================
# Calcul des jours consécutifs sans accident
# ======================
def calculate_lta_days(df):
    count = 0
    values = []
    for accident in df["Accident"]:
        if accident:
            count = 0
        else:
            count += 1
        values.append(count)
    df["JoursSansAccident"] = values
    return df

df = calculate_lta_days(df)

# ======================
# Calcul : jours depuis le dernier accident
# ======================
days_since_last_accident = (yesterday - last_accident_date).days

# ======================
# Affichage Dernier accident
# ======================
st.markdown(
    f"""
    <div style='text-align: center; margin-bottom: 20px;'>
        <h3>Dernier accident ({last_accident_date.strftime('%d/%m/%Y')})</h3>
        <h2>{days_since_last_accident} jours sans accident</h2>
        <p style='font-size:18px; color: lightcoral; font-weight:bold;'>
            {last_accident_desc}
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# ======================
# 📊 STATISTIQUES GLOBALES
# ======================
st.subheader("📊 Statistiques globales (du 1er janvier jusqu'à hier)")

total_days_without_accident = df["JoursSansAccident"].iloc[-1]
total_accidents = df["Accident"].sum()

col1, col2 = st.columns(2)

with col1:
    st.metric("Jours sans accident depuis le 1er janvier", total_days_without_accident)

with col2:
    st.metric("Total d'accidents enregistrés", total_accidents)

# ======================
# Rappel compteur officiel
# ======================
st.markdown(
    f"""
    <div style='text-align: center; margin-top: 10px;'>
        <p style='font-size:18px; font-weight:bold;'>
            Nombre de jours sans accident depuis le dernier accident : {days_since_last_accident}
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# ======================
# 📅 Calendrier
# ======================
st.subheader("📅 Calendrier (du 1er janvier jusqu'à hier)")

months = df["Date"].dt.month.unique()

for month in months:
    month_name = df[df["Date"].dt.month == month]["Date"].dt.strftime("%B %Y").iloc[0]
    st.markdown(f"### {month_name}")

    month_df = df[df["Date"].dt.month == month]

    display_df = pd.DataFrame({
        "Jour": month_df["Date"].dt.day,
        "Accident": month_df["Accident"].map(lambda x: "🔴" if x else "🟢"),
        "Jours consécutifs sans accident": month_df["JoursSansAccident"]
    })

    st.table(display_df)
