import streamlit as st

st.set_page_config(page_title="Cricket Guru", page_icon="🏏", layout="centered")

st.title("🏏 Cricket Predictor")
st.markdown("### Welcome to your all-in-one Cricket Match Predictor Dashboard!")

col1, col2 = st.columns(2)

with col1:
    if st.button("🏆 **ODI Men's Matches**"):
        st.switch_page("pages/odi-men.py")
    if st.button("💥 **IPL (Indian Premier League)**"):
        st.switch_page("pages/ipl.py")
    if st.button("🎯 **IPL Toss Winner Prediction**"):
        st.switch_page("pages/ipl_toss.py")

with col2:
    if st.button("👩‍🦰 **ODI Women's Matches**"):
        st.switch_page("pages/odi-women.py")
    if st.button("🌍 **PSL (Pakistan Super League)**"):
        st.switch_page("pages/psl.py")

st.markdown("---")

st.markdown("💡 **Tip:** For best results, enter all match context fields correctly, including current score, overs, wickets, and team names.")
st.markdown("🔍 **Note:** This app uses machine learning models trained on historical data to give real-time winning probabilities. It does not give any guarantee on the predictions")



st.markdown(
    """
    <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 5px;
            width: 100%;
            text-align: center;
            font-size: 13px;
            opacity: 0.4;
        }
    </style>
    <div class="footer">
        Copyright © Babuaa, All Rights Reserved, not really ;)
    </div>
    """,
    unsafe_allow_html=True
)
