import streamlit as st

home_pg= st.Page(
    page='pages/home.py',
    title= 'Home',
    icon= '🏡',
    default= True
)

odi_men_pg= st.Page(
    page='pages/odi-men.py',
    title= 'ODI Men Win Predictor',
    icon= '1️⃣'
)

odi_women_pg= st.Page(
    page='pages/odi-women.py',
    title= 'ODI Women Win Predictor',
    icon= '2️⃣'
)

ipl_pg= st.Page(
    page='pages/ipl.py',
    title= 'IPL Win Predictor',
    icon= '3️⃣'
)

ipl_toss_pg= st.Page(
    page='pages/ipl_toss.py',
    title= 'IPL Toss Predictor',
    icon= '4️⃣'
)

psl_pg= st.Page(
    page='pages/psl.py',
    title= 'PSL Win Predictor',
    icon= '5️⃣'
)

pg= st.navigation(pages=[home_pg, odi_men_pg, odi_women_pg, ipl_pg, ipl_toss_pg, psl_pg])

st.sidebar.text("Made with 🎧 by Babuaa T_T")

pg.run()
