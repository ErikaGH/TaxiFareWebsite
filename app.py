import streamlit as st
import requests

st.markdown('''

# NY taxi fare predictor

''')

pickup_date = st.date_input('Pickup date:')
pickup_time = st.time_input('Pickup time:')
pickup_longitude = st.number_input('Pickup longitude:')
pickup_latitude = st.number_input('Pickup latitude:')
dropoff_longitude = st.number_input('Dropoff longitude:')
dropoff_latitude = st.number_input('Dropoff latitude:')
passenger_count = st.number_input('How many passengers?')


url = 'http://taxifare.lewagon.ai/predict_fare/'
params =  {
    "key": '2012-10-06 20:10:20.0000001',
    "pickup_datetime": str(pickup_date) + ' ' + str(pickup_time) + ' UTC',
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": int(passenger_count)
}

r = requests.get(url, params=params).json()

st.markdown('''

**Predicted fare:**

''')

r['prediction']

