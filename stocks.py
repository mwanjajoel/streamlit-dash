import yfinance as yf
import streamlit as st
import pandas as pd

# lets begin streamlit
st.write("""

# Simple stock price app

Shown are the stock closing price and volume of Google!

"""
)

# set the ticker symbol
ticker_symbol = 'GOOGL'

# get data from that ticker symbol
ticker_data = yf.Ticker(ticker_symbol)

# get the historical prices 
ticker_df = ticker_data.history(period='1d', start='2010-5-31', end='2021-5-31')

# plot on the charts
st.line_chart(ticker_df.Close)
st.line_chart(ticker_df.Volume)
