import streamlit
streamlit.title('My Moms New Healty Diner')
streamlit.header('BreakFast Menu')
streamlit.text('🥣 omega 4 & Blureberry Oatmeal')
streamlit.text('🥗 kale, Spinach & Rocket Smoothie')
streamlit.text(' 🥣  Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)
fruits_selected = streamlit.multiselect("Pick Some Fruits:",list(my_fruit_list.index),['Avocado','Strawberries','Apple']) 
fruits_to_display = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_display)
