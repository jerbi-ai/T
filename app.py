# safeyear2026.py
import streamlit as st
import pandas as pd
import datetime
import os

# ======================
# Configuration Streamlit
# ======================
st.set_page_config(page_title="SafeYear 2026", layout="wide")
st.title("📅 SafeYear 2026 - Suivi des accidents")

# ======================
# Fichier Excel
# ======================
FILE_NAME = "accidents_2026.xlsx"

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
# Sauvegarde accident dans Excel
# ======================
def save_accident_to_excel(date_accident, description):
    mois = date_accident.strftime("%B").lower()
    jour = date_accident.day

    new_row = {
        "Mois": mois,
        "Jour": jour,
        "Description": description
    }

    if os.path.exists(FILE_NAME):
        df_excel = pd.read_excel(FILE_NAME)
        df_excel = pd.concat(
            [df_excel, pd.DataFrame([new_row])],
            ignore_index=True
        )
    else:
        df_excel = pd.DataFrame([new_row])

    df_excel.to_excel(FILE_NAME, index=False)

# ======================
# Sidebar - Ajout accident
# ======================
st.sidebar.header("📌 Enregistrer un accident")

date_accident = st.sidebar.date_input(
    "Date de l'accident",
    value=datetime.date(2026, 1, 1)
)

description = st.sidebar.text_input(
    "Description (optionnelle)",
    placeholder="ex : incendie"
)

if st.sidebar.button("Ajouter accident"):
    df.loc[df["Date"] == pd.Timestamp(date_accident), "Accident"] = True
    save_accident_to_excel(date_accident, description)
    st.sidebar.success("✅ Accident enregistré avec succès")

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
# Affichage calendrier par mois
# ======================
st.subheader("📆 Calendrier 2026")

months = df["Date"].dt.month.unique()

for month in months:
    month_df = df[df["Date"].dt.month == month]
    month_name = month_df["Date"].dt.strftime("%B %Y").iloc[0]

    st.markdown(f"### {month_name}")

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

st.metric(
    "Plus longue série de jours sans accident",
    int(df["JoursSansAccident"].max())
)

st.metric(
    "Total d'accidents enregistrés",
    int(df["Accident"].sum())
)

# ======================
# Affichage du fichier Excel
# ======================
if os.path.exists(FILE_NAME):
    st.subheader("📂 Historique des accidents (Excel)")
    df_excel = pd.read_excel(FILE_NAME)
    st.dataframe(df_excel)
