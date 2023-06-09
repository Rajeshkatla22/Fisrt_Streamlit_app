import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My Moms New Healty Diner')
streamlit.header('BreakFast Menu')
streamlit.text('🥣 omega 4 & Blureberry Oatmeal')
streamlit.text('🥗 kale, Spinach & Rocket Smoothie')
streamlit.text(' 🥣  Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)
fruits_selected = streamlit.multiselect("Pick Some Fruits:",list(my_fruit_list.index),['Avocado','Strawberries','Apple']) 
fruits_to_display = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_display)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")

streamlit.header("Fruityvice Fruit Advice!")
try:
fruit_choice = streamlit.text_input('What fruit would you like information about?')
if not fruit_choice:
  streamlit.error("Please select a fruit to get information.")
  else:
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)

excepy UELError as e:
  streamlit.error()


streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

fruit_choice = streamlit.text_input('What fruit would you like information about?','jackfruit')
streamlit.write('The user entered ', fruit_choice)

my_cur.execute("insert into fruit_load_list values ('my streamlit')")
