import streamlit as st
import pandas as pd
import requests as rq

st.title("My Mom's New Healthy Diner")

st.header('Breakfast Favorites')
st.text('🥣 Omega 3 & Blueberry Oatmeal')
st.text('🥗 Kale, Spinach & Rocket Smoothie')
st.text('🐔 Hard-Boiled Free-Range Egg')
st.text('🥑🍞 Avocado Toast')


st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')

#Put a list for the user to select the fruit they want to include
fruits_selected = st.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#Display table on the page
st.dataframe(fruits_to_show)


#display fruityvice api response
st.header('Fruityvice Fruit Advice!')
fruit_choice = st.text_input('What fruit would you like information about?', 'Kiwi')
st.write('The user entered', fruit_choice)

fruityvice_response = rq.get("https://fruityvice.com/api/fruit/" + fruit_choice)


#Take the json version of the response and normalize it
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
#place normalized data on the screen as a table
st.dataframe(fruityvice_normalized)
