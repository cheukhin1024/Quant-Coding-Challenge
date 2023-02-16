from datetime import datetime
import numpy as np
import pandas as pd
import yfinance as yf

#Get the input
start = str(input("Enter your start: "))
end = str(input("Enter your end: "))
start_date = datetime.strptime(start, "%Y-%m-%d")
end_date = datetime.strptime(end, "%Y-%m-%d")
days = (end_date - start_date).days
    
#Tickers of assets
assets = [str(input("Enter your assets: "))]

#Downloading data
data = yf.download(assets, start = start, end = end)
data = data['Adj Close']
data.columns = assets

#Calculating annualized returns
def calculate_annualized_return(assets): 
    total_return = (data[-1] - data[0]) / data[0]
    annualized_return = ((1+total_return)**(365/days))-1
    return(annualized_return)

print(calculate_annualized_return(assets))
