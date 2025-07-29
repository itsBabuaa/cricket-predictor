import streamlit as st
import pandas as pd
import pickle

teams= ['Mumbai Indians',
        'Kolkata Knight Riders',
        'Chennai Super Kings',
        'Rajasthan Royals',
        'Sunrisers Hyderabad',
        'Delhi Capitals',
        'Punjab Kings',
        'Lucknow Super Giants',
        'Gujarat Titans',
        'Royal Challengers Bengaluru']

cities= ['Mumbai', 'Delhi', 'Kolkata', 'Chennai', 'Chandigarh', 'Hyderabad',
       'Jaipur', 'Navi Mumbai', 'Centurion', 'Port Elizabeth', 'Dubai',
       'Abu Dhabi', 'Bengaluru', 'Indore', 'Lucknow',
       'Sharjah', 'Ahmedabad', 'Cuttack', 'Visakhapatnam', 'Durban',
       'Ranchi', 'Dharamsala', 'Cape Town', 'East London', 'Raipur',
       'Pune', 'Kimberley', 'Johannesburg', 'Nagpur', 'Mohali',
       'Guwahati', 'Bloemfontein']

match_type= ['League', 'Final', 'Qualifier 1', 'Qualifier 2', 'Eliminator']

pipe_t= pickle.load(open('notebook/ipl/ipl_toss_pipe.pkl', 'rb'))

st.title('🪙IPL Toss Predictor')

col1, col2= st.columns(2)

with col1:
    team1= st.selectbox('Select the batting team', sorted(teams))
    teams.remove(team1)
with col2:
    team2= st.selectbox('Select the bowling team', sorted(teams))

col3, col4= st.columns(2)

with col3:
    selected_city= st.selectbox('Select the host city', sorted(cities))
with col4:
    selected_match_type= st.selectbox('Select the match type', sorted(match_type))

if st.button('Predict Probability'):

    input_df= pd.DataFrame({'team1':[team1], 'team2':[team2], 'city':[selected_city], 'match_type':[selected_match_type]})
    res= pipe_t.predict_proba(input_df)
    team2_pro= res[0][0]
    team1_pro= res[0][1]

    st.header(team1 + ' Probability: ' + str(round(team1_pro * 100)) + '%')
    st.header(team2 + ' Probability: ' + str(round(team2_pro * 100)) + '%')