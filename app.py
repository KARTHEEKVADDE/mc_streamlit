import streamlit as st

import numpy as np

import yfinance as yf

st.write("""
            # Stock Price Analyser """)

# get Apple's Stock data
symbol = "AAPL"
symbol = st.selectbox(
    'Select Stock Symbol',
    ('AAPL', 'GOOG', 'TSLA', 'MSFT', 'NFLX')
)
ticker_data = yf.Ticker(symbol)
import datetime

col1, col2 = st.columns(2)

with col1:
    start_date = st.date_input("Please enter start date", datetime.date(2021, 7, 6))
with col2:
    end_date = st.date_input("Please enter end date", datetime.date(2022, 7, 6))

ticker_df = ticker_data.history(period="1d", start=start_date, end=end_date)

st.write(f"""
            ### {symbol}'s Stock Price Data """)

st.dataframe(ticker_df)

st.write(f"""
            ### {symbol}'s Closing Price Line Chart """)

st.line_chart(ticker_df["Close"])

st.write(f"""
            ### {symbol}'s Closing Price Volume Chart """)

st.line_chart(ticker_df["Volume"])