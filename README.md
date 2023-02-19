# Quant-Coding-Challenge

## Libaries:
- Numpy
- Pandas
- yfinance
- streamlit

## How to use the Application
Youtube Demonstration:
https://youtu.be/uqb2hkZ1UeE


There are 3 user inputs:
- Asset (Yahoo Finance Ticker Symbol)
- Start Date (Format: YYYY-MM-DD)
- End Date (Format: YYYY-MM-DD)

After entering 3 user input and pressing "Enter", it shows annualized return on the stock.

###### Test Case 1:
- Asset: AAPL (Apple.Inc)
- Start Date: 2021-12-31
- End Date: 2022-12-31

- The annualized return on the AAPL is: -0.26404 (-26.404%)
<img width="1440" alt="Screenshot 2023-02-20 at 2 35 14 AM" src="https://user-images.githubusercontent.com/70860455/219968178-936d598a-2346-41bc-a13b-dfddf0053ec7.png">

###### Test Case 2:
- Asset: MSFT (Microsoft Cooperation)
- Start Date: 2012-12-31
- End Date: 2022-12-31

- The annualized return on the MSFT is: 0.26952 (26.952%)
- <img width="1440" alt="Screenshot 2023-02-20 at 2 35 30 AM" src="https://user-images.githubusercontent.com/70860455/219968163-8218c4d6-93b6-457a-bf81-161c87a6dbcf.png">

###### Test Case 3:
- Asset: 0700.HK (Tencent Hong Kong stock)
- Start Date: 2012-12-31
- End Date: 2022-12-31

- The annualized return on the MSFT is: 0.20669 (20.669%)
<img width="1440" alt="Screenshot 2023-02-20 at 2 39 27 AM" src="https://user-images.githubusercontent.com/70860455/219968257-0b77b036-b1ce-42d7-a4f0-92e9fe53a563.png">

###### Test Case 4:
- Asset: ^GSPC (S&P 500 index)
- Start Date: 2008-12-31
- End Date: 2022-12-31

- The annualized return on the MSFT is: 0.10882 (10.882%)
<img width="1440" alt="Screenshot 2023-02-20 at 2 36 51 AM" src="https://user-images.githubusercontent.com/70860455/219968156-fc13041f-9865-4056-9572-cd928a44c243.png">
