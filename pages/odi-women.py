import streamlit as st
import pandas as pd
import pickle

teams= ['Ireland', 'South Africa', 'West Indies', 'New Zealand', 'England',
       'India', 'Pakistan', 'Sri Lanka', 'Netherlands', 'Zimbabwe',
       'Bangladesh', 'Australia', 'Thailand']

cities= ['Lahore', 'Christchurch', 'North Sound', 'Auckland', 'Canterbury',
       'Lincoln', 'Taunton', 'Mumbai', 'Hambantota', 'Derby', 'Coolidge',
       'Hamilton', 'Colombo', 'Coffs Harbour', 'Chiang Mai', 'Harare',
       'Queenstown', 'Leicester', 'Vadodara', "Cox's Bazar", 'Bangalore',
       'Hobart', 'Lucknow', 'Potchefstroom', 'Kuala Lumpur', 'Karachi',
       'East London', 'Mount Maunganui', 'Pretoria', 'Bloemfontein',
       'Bristol', 'London', 'Wellington', 'Paarl', 'Melbourne',
       'Brisbane', 'Worcester', 'Hove', 'Dublin', 'Kandy', 'Dunedin',
       'Durban', 'Southampton', 'Sydney', 'Johannesburg', 'Kimberley',
       'Bowral', 'Mackay', 'Leeds', 'Bangkok', 'FTZ Sports Complex',
       'Kurunegala', 'Nagpur', 'Benoni', 'Chelmsford', 'Brighton',
       'Gros Islet', 'Centurion', 'Adelaide', 'Perth', 'Nelson',
       'Northampton', 'Canberra', 'Katunayake', 'Dubai', 'Chennai',
       'Barbados', 'The Hague', 'Dhaka', 'Napier', 'Scarborough',
       'Amstelveen', 'Galle', 'Loughborough', 'Bulawayo']

pipe= pickle.load(open('notebook/odi/women_odi_pipe.pkl', 'rb'))

st.title('🏏ODI Women Win Predictor')

col1, col2= st.columns(2)

with col1:
    batting_team= st.selectbox('Select the batting team', sorted(teams))
    teams.remove(batting_team)
with col2:
    bowling_team= st.selectbox('Select the bowling team', sorted(teams))

selected_city= st.selectbox('Select the host city', sorted(cities))

target= st.number_input('Target runs', min_value=0, max_value=650, value=0, step=1, format="%d")

col3, col4, col5= st.columns(3)

with col3:
    overs = st.number_input('Over completed', min_value=1, max_value=49, value=1, step=1, format="%d")
with col4:
    score= st.number_input('Current runs', min_value=0, max_value=650, value=0, step=1, format="%d")
with col5:
    wickets= st.number_input('Wickets fallen', min_value=0, max_value=9, value=0, step=1, format="%d")

if st.button('Predict Winner Probability'):
    runs_left= target - score
    balls_left= 300 - (overs*6)
    wickets_left= 10 - wickets
    crr= score / overs
    rrr= (runs_left*6) / balls_left

    input_df= pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'city':[selected_city],'runs_left':[runs_left],'balls_left':[balls_left],'wickets_left':[wickets_left],'total_runs_x':[target],'crr':[crr],'rrr':[rrr]})
    #st.dataframe(input_df)
    res= pipe.predict_proba(input_df)
    bowling_team_proba= res[0][0]
    batting_team_proba= res[0][1]

    st.header(batting_team + ': ' + str(round(batting_team_proba*100)) + '%')
    st.header(bowling_team + ': ' + str(round(bowling_team_proba * 100)) + '%')
