# safeyear2026.py
import streamlit as st
import pandas as pd
import datetime

# ======================
# Initialisation
# ======================
st.set_page_config(page_title="SafeYear 2026", layout="wide")

st.title("📅 SafeYear 2026 - Suivi des accidents")

# Charger ou créer le dataframe des jours
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
# Section ajout accident
# ======================
st.sidebar.header("📌 Enregistrer un accident")
date_accident = st.sidebar.date_input("Date de l'accident", value=datetime.date(2026, 1, 1))
description = st.sidebar.text_input("Description (optionnelle)")

if st.sidebar.button("Ajouter accident"):
    df.loc[df["Date"] == pd.Timestamp(date_accident), "Accident"] = True
    st.sidebar.success(f"Accident ajouté pour {date_accident}")

# ======================
# Calcul des jours sans accident
# ======================
def calculate_lta_days(df):
    count = 0
    max_count = 0
    consecutive = []
    for accident in df["Accident"]:
        if not accident:
            count += 1
            consecutive.append(count)
        else:
            count = 0
            consecutive.append(count)
    df["JoursSansAccident"] = consecutive
    return df

df = calculate_lta_days(df)

# ======================
# Affichage du calendrier
# ======================
st.subheader("Calendrier 2026")
months = df["Date"].dt.month.unique()

for month in months:
    st.markdown(f"### {df[df['Date'].dt.month==month]['Date'].dt.strftime('%B %Y').iloc[0]}")
    month_df = df[df["Date"].dt.month==month]
    # Affichage en tableau
    display_df = pd.DataFrame({
        "Jour": month_df["Date"].dt.day,
        "Accident": month_df["Accident"].apply(lambda x: "🔴" if x else "🟢"),
        "Jours consécutifs sans accident": month_df["JoursSansAccident"]
    })
    st.table(display_df)

# ======================
# Statistiques globales
# ======================
st.subheader("📊 Statistiques globales")
total_days_without_accident = df["JoursSansAccident"].max()
st.metric("Plus longue série de jours sans accident", total_days_without_accident)
st.metric("Total d'accidents enregistrés", df["Accident"].sum())




