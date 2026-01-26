# safeyear2026.py
import streamlit as st
import pandas as pd
import datetime

# ======================
# CONFIGURATION PAGE
# ======================
st.set_page_config(page_title="SafeYear 2026", layout="wide")

st.markdown(
    """
    <h1 style='text-align: center;'>
        <span style='color: blue;'>ONE</span><span style='color: orange;'>TECH</span>
    </h1>
    """,
    unsafe_allow_html=True
)

st.subheader("🚨 Suivi des accidents")

# ======================
# DATES UTILES
# ======================
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)

# ======================
# CRÉATION DU CALENDRIER 2026
# ======================
@st.cache_data
def create_calendar():
    dates = pd.date_range(
        start=datetime.date(2026, 1, 1),
        end=datetime.date(2026, 12, 31)
    )
    df = pd.DataFrame(dates, columns=["Date"])
    df["NbAccidents"] = 0
    df["Descriptions"] = [[] for _ in range(len(df))]
    return df

df = create_calendar()

# ======================
# ACCIDENTS INITIAUX
# ======================
initial_accidents = [
    (datetime.date(2026, 1, 14),
     "Accident de manutention : chute d’une bobine sur le genou gauche de l’opérateur."),

    # 🔴 2 ACCIDENTS LE MÊME JOUR
    (datetime.date(2026, 1, 20),
     "Accident de trajet dû à une vitesse excessive et à un dos-d’âne non visible. Traumatisme dorsal."),

    (datetime.date(2026, 1, 20),
     "Glissade lors d’une opération de nettoyage sur sol humide. Blessure au poignet."),

    (datetime.date(2026, 1, 22),
     "Lors du changement de la lame de la machine de coupe, le technicien s’est blessé à la main droite.")
]

# ======================
# APPLICATION DES ACCIDENTS
# ======================
for date, desc in initial_accidents:
    idx = df["Date"] == pd.Timestamp(date)
    df.loc[idx, "NbAccidents"] += 1
    df.loc[idx, "Descriptions"].iloc[0].append(desc)

# ======================
# FILTRAGE JUSQU'À HIER
# ======================
df = df[df["Date"] <= pd.Timestamp(yesterday)]

# ======================
# CALCUL DES JOURS SANS ACCIDENT
# ======================
def calculate_days_without_accident(df):
    count = 0
    result = []
    for nb in df["NbAccidents"]:
        if nb > 0:
            count = 0
        else:
            count += 1
        result.append(count)
    df["JoursSansAccident"] = result
    return df

df = calculate_days_without_accident(df)

# ======================
# DERNIER ACCIDENT
# ======================
if (df["NbAccidents"] > 0).any():
    last_row = df[df["NbAccidents"] > 0].iloc[-1]
    last_accident_date = last_row["Date"].date()
    last_descriptions = last_row["Descriptions"]
else:
    last_accident_date = None
    last_descriptions = ["Aucun accident enregistré."]

days_since_last_accident = (
    (yesterday - last_accident_date).days if last_accident_date else 0
)

# ======================
# AFFICHAGE DERNIER ACCIDENT
# ======================
st.markdown(
    f"""
    <div style='text-align:center;'>
        <h3>Dernier accident ({last_accident_date.strftime('%d/%m/%Y') if last_accident_date else 'N/A'})</h3>
        <h2>{days_since_last_accident} jours sans accident</h2>
    </div>
    """,
    unsafe_allow_html=True
)

for desc in last_descriptions:
    st.markdown(
        f"<p style='color:lightcoral; font-weight:bold;'>• {desc}</p>",
        unsafe_allow_html=True
    )

st.divider()

# ======================
# STATISTIQUES
# ======================
st.subheader("📊 Statistiques globales")
st.metric("Total accidents", int(df["NbAccidents"].sum()))
st.metric("Jours sans accident (actuel)", df["JoursSansAccident"].iloc[-1])

st.divider()

# ======================
# CALENDRIER
# ======================
st.subheader("📅 Calendrier 2026")

months = df["Date"].dt.month.unique()

for month in months:
    month_df = df[df["Date"].dt.month == month]
    month_name = month_df["Date"].dt.strftime("%B %Y").iloc[0]
    st.markdown(f"### {month_name}")

    display_df = pd.DataFrame({
        "Jour": month_df["Date"].dt.day,
        "Accidents": month_df["NbAccidents"].apply(
            lambda x: "🟢" if x == 0 else f"🔴 {x}"
        ),
        "Jours consécutifs sans accident": month_df["JoursSansAccident"]
    })

    st.table(display_df)
