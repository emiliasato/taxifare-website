import streamlit as st
import datetime

'''
# TaxiFareModel front
'''
st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''
date_and_time = st.text_input('Date and Time')

st.write('Date and time is ', date_and_time)

d = st.date_input(
    "When's your birthday",
    datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)

pickup_longitude = st.text_input('Pickup longitude', 'Life of Brian')

st.write('Pickup longitude is ',pickup_longitude)

pickup_latitude = st.text_input('Pickup latitude', 'Life of Brian')

st.write('Pickup longitude is ',pickup_latitude)

dropoff_latitude = st.text_input('Dropoff Latitude', 'Life of Brian')

st.write('Dropoff latitude is ',dropoff_latitude )

dropoff_longitude = st.text_input('Dropoff Longitude', 'Life of Brian')

st.write('Dropoff longitude is ',dropoff_longitude)

passenger_count = st.text_input('Passenger Count', 'Life of Brian')

st.write('Passnenger Count is ',passenger_count)

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
