from datetime import datetime
import numpy as np
import pandas as pd
import yfinance as yf
import streamlit as st

st.write("""
# Stock Market Web Application
**Annualized return on the stock:** 
""")

st.sidebar.header('User Input')

st_assets = st.sidebar.text_input("Assets" ,'AAPL')
st_start_date = st.sidebar.text_input("Start Date" ,'2021-12-31')
st_end_date = st.sidebar.text_input("End Date" ,'2022-12-31')

start_date = datetime.strptime(st_start_date, "%Y-%m-%d")
end_date = datetime.strptime(st_end_date, "%Y-%m-%d")
days = (end_date - start_date).days

#Tickers of assets
assets = [st_assets]

#Downloading data
data = yf.download(assets, start = st_start_date, end = st_end_date)
data = data['Adj Close']
data.columns = assets

#Calculating annualized returns
def calculate_annualized_return(assets): 
    total_return = (data[-1] - data[0]) / data[0]
    annualized_return = ((1+total_return)**(365/days))-1
    st.write(annualized_return)

calculate_annualized_return(assets)
