import streamlit as st
import pandas as pd
import requests

st.title('Hello World')
st.write("Welcome to your first streamlit application")


# get URL data

API_URL = 'https://cleanuri.com/api/v1/shorten'

st.subheader("URL shortner")
text_box_value = st.text_input("Enter URL")
pressed = st.button('Get Short Link')

if pressed:
    if text_box_value:
        data = {'url': text_box_value}
        response = requests.post(API_URL, data=data)
        st.write(response.content)
        
        # st.write("Shortened URL:", response['result_url'][0])
    else:
        st.error("Please enter a valid URL")
