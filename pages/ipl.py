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

pipe= pickle.load(open('notebook/ipl/ipl_pipe.pkl', 'rb'))

st.title('🏏IPL Win Predictor')

col1, col2= st.columns(2)

with col1:
    batting_team= st.selectbox('Select the batting team', sorted(teams))
    teams.remove(batting_team)
with col2:
    bowling_team= st.selectbox('Select the bowling team', sorted(teams))

selected_city= st.selectbox('Select the host city', sorted(cities))

target= st.number_input('Target runs', min_value=0, max_value=350, value=0, step=1, format="%d")

col3, col4, col5= st.columns(3)

with col3:
    overs = st.number_input('Over completed', min_value=1, max_value=19, value=1, step=1, format="%d")
with col4:
    score= st.number_input('Current runs', min_value=0, max_value=350, value=0, step=1, format="%d")
with col5:
    wickets= st.number_input('Wickets fallen', min_value=0, max_value=9, value=0, step=1, format="%d")

if st.button('Predict Winner Probability'):
    runs_left= target - score
    balls_left= 120 - (overs*6)
    wickets_left= 10 - wickets
    crr= score / overs
    rrr= (runs_left*6) / balls_left

    input_df= pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'city':[selected_city],'runs_left':[runs_left],'balls_left':[balls_left],'wickets':[wickets_left],'total_runs_x':[target],'crr':[crr],'rrr':[rrr]})
    #st.dataframe(input_df)
    res= pipe.predict_proba(input_df)
    bowling_team_proba= res[0][0]
    batting_team_proba= res[0][1]

    st.header(batting_team + ': ' + str(round(batting_team_proba*100)) + '%')
    st.header(bowling_team + ': ' + str(round(bowling_team_proba * 100)) + '%')