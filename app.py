import streamlit as st

home_pg= st.Page(
    page='pages/home.py',
    title= 'Home',
    icon= '🏡',
    default= True
)

ipl_pg= st.Page(
    page='pages/ipl.py',
    title= 'IPL Win Predictor',
    icon= '1️⃣'
)

ipl_toss_pg= st.Page(
    page='pages/ipl_toss.py',
    title= 'IPL Toss Predictor',
    icon= '2️⃣'
)

psl_pg= st.Page(
    page='pages/psl.py',
    title= 'PSL Win Predictor',
    icon= '3️⃣'
)

pg= st.navigation(pages=[home_pg, ipl_pg, ipl_toss_pg, psl_pg])

pg.run()