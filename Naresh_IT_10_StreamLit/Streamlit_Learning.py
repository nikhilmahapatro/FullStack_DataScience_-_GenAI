
#-------------------------------------STREAMLIT---------------------------------------------#

# CHAPTER 1
# Introduction to Streamlit

import streamlit as st

st.title("STREAMLIT LEARNING")

st.subheader("Let's learn streamlit.")

st.text("Welcome to Streamlit")

st.write("This is the demo write.")

comic_teams = st.selectbox("Choose your favourite comic teams: ", ['X-men','The Avengers','The Suicide Squad',
                                                                   'The Justice League','The Ninja Turtles'])

st.write(f"You selected \"{comic_teams}\", excellent choice!!!")

st.success("Your choice has been updated.")

#---------------------------------------------------------------------------------------------------------------

# CHAPTER 2
# Widgets and Inputs

st.write("Flat 50% off on pizza.")

pizza_type = st.radio("Choose your pizza: ",['Mexican','Italian','Chicago-style','California-style','Indian-style'])
if pizza_type:
    st.write(f"You have selected {pizza_type} pizza.")

extra_cheese = st.checkbox("Add extra cheese")
baked_bread = st.checkbox("Extra baked Bread")

prev_order_rating = st.slider("Can you rate your previous order",0,5)

nums = st.number_input("No of orders: ", min_value=1, max_value=10)

cust_name = st.text_input("Enter your name: ")
if cust_name:
    st.write(f"Welcome, {cust_name}")

dob = st.date_input("Enter your date of birth:")

if st.button("Order now"):
    st.success("Your order has been confirmed.")

#___________________________________________________________________________________________________________________

# CHAPTER 3
# Layouts and Styling

col1, col2 = st.columns(2)

with col1:
    st.header("Real Madrid")
    st.image(r"C:\Users\nikhi\PycharmProjects\NARESH_IT\03_NARESH_IT_STREAMLIT\Naresh_IT_10_StreamLit\realmadrid.jpg", width=200)
    vote1 = st.button("Vote for RMA")

with col2:
    st.header("Barcelona")
    st.image(r"C:\Users\nikhi\PycharmProjects\NARESH_IT\03_NARESH_IT_STREAMLIT\Naresh_IT_10_StreamLit\barcelona.jpg", width=200)
    vote2 = st.button("Vote for FCB")

if vote1:
    st.success("You voted for Real Madrid!!")
elif vote2:
    st.success("You voted for FC Barcelona!!")

city = st.sidebar.text_input("Which city are you from?: ")
fav_sport = st.sidebar.selectbox("Which is your favourite sport?: ",['Football','Cricket','Chess','Badminton','Boxing','F1'])

with st.expander("All about Streamlit"):
    st.write("""
    1. A faster way to build and share data apps. 
    2. Streamlit has 100 repositories available.
    3. Streamlit is an open-source Python library that makes it super easy to create interactive web apps for
       data science, machine learning, and Python scripts — with very little code and no need to know web development.
    4. Streamlit lets you transform Python scripts into interactive web apps in minutes, instead of weeks. Build 
       dashboards, generate reports, or create chat apps.
    """)

st.markdown("# Front End using Python")
st.markdown("> Creating a front end using Python is totally possible — especially for data apps, prototypes, and "
            "internal tools. While Python isn't traditionally used for full-scale front-end web development "
            "(which is usually done with HTML/CSS/JavaScript), there are Python frameworks that let you build "
            "interactive front-end interfaces.")

#____________________________________________________________________________________________________________________

# CHAPTER 4
# Working with Data

import pandas as pd

file = st.file_uploader("Upload your csv file: ", type= ['csv'])

if file:
    df = pd.read_csv(file)
    st.subheader("Dataframe Preview")
    st.dataframe(df)

    st.subheader("Dataframe Summary")
    st.write(df.describe())

#____________________________________________________________________________________________________________________

# CHAPTER 5
# API Integration

import requests

st.subheader("Currency Converter")

INR_input = st.number_input("Enter the amount in INR: ",min_value=1)
target_currency = st.selectbox("Convert to: ",['USD','EUR','GPB','JPY'])

convert = st.button("Convert")

if convert:
    url = "https://api.exchangerate-api.com/v4/latest/INR"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        rate = data['rates'][target_currency]
        output = rate * INR_input
        st.success(f"{INR_input} INR = {output:2f} {target_currency}")
    else:
        st.error("Failed to fetch conversion rate.")

#___________________________________________________________________________________________________________________

# CHAPTER 6
# Dashboards with KPI cards and charts
