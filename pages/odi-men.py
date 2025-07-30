import streamlit as st
import pandas as pd
import pickle

teams= ['Bangladesh', 'India', 'New Zealand', 'United Arab Emirates',
       'United States of America', 'Australia', 'England', 'South Africa',
       'Nepal', 'West Indies', 'Pakistan', 'Sri Lanka', 'Ireland',
       'Netherlands', 'Zimbabwe', 'Afghanistan', 'Scotland', 'Oman',
       'Namibia', 'Hong Kong', 'Canada']

cities= ['Karachi', 'London', 'Aberdeen', 'Pearland', 'Delhi', 'Durban',
       'Townsville', 'Leeds', 'Al Amarat', 'Gwalior', 'Bloemfontein',
       'Rawalpindi', 'Bulawayo', 'Kirtipur', 'Johannesburg', 'Rajkot',
       'St Vincent', 'Southampton', 'Hyderabad', 'Napier', 'Nagpur',
       'Abu Dhabi', 'Birmingham', 'Belfast', 'St Lucia', 'Colombo',
       'Fatullah', 'Rotterdam', 'Hamilton', 'Cuttack', 'Chittagong',
       'Wellington', 'Brisbane', 'Manchester', 'Mirpur', 'Guwahati',
       'Nairobi', 'Hobart', 'Ranchi', 'Harare', 'Ahmedabad', 'Canterbury',
       'East London', 'Nelson', 'Amstelveen', 'Edinburgh', 'Peshawar',
       'Mount Maunganui', 'Kanpur', 'Antigua', 'Dhaka', 'Lucknow',
       'Dublin', 'Bridgetown', 'Doha', 'Greater Noida', 'Sharjah',
       'Dubai', 'Guyana', 'Cape Town', 'Centurion', 'Vadodara',
       'Dehra Dun', 'Hambantota', 'Kolkata', 'Sydney', 'Margao',
       'St Kitts', 'Perth', 'Chandigarh', 'Port Elizabeth', 'Dunedin',
       'Grenada', 'Pune', 'Ayr', 'Chennai', 'Dambulla', 'Canberra',
       'Jamaica', 'Nottingham', 'Trinidad', 'Mumbai', 'Cardiff', 'Sylhet',
       'Kingstown', 'Paarl', 'Kuala Lumpur', 'Jamshedpur', 'Indore',
       'Kimberley', 'Lahore', 'Pietermaritzburg', 'Adelaide',
       'Chelmsford', 'Queenstown', 'Benoni', 'Jaipur', 'Multan',
       'Chattogram', 'Melbourne', 'Windhoek', 'Kochi', 'Khulna', 'Sind',
       'Faisalabad', 'Barbados', 'Christchurch', 'Chester-le-Street',
       'Port of Spain', 'Bogra', 'Visakhapatnam', 'Potchefstroom',
       'Taunton', 'Bangalore', 'Dominica', 'Bengaluru', 'Kandy',
       'Whangarei', 'North Sound', 'Bready', 'Auckland', 'Kingston',
       "St George's", 'Cairns', 'Port Moresby', 'Bristol', 'Lauderhill',
       'Darwin', 'Gqeberha', 'Providence', 'Glasgow', 'Deventer',
       'Dharamsala', 'Dharmasala', 'Faridabad', 'Gros Islet', 'Utrecht',
       'Tarouba', 'Raipur', 'Thiruvananthapuram', 'King City']

pipe= pickle.load(open('notebook/odi/men_odi_pipe.pkl', 'rb'))

st.title('🏏ODI Men Win Predictor')

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
