import yfinance as yf
import pandas as pd
from pandas_datareader import data
from datetime import datetime

stock_name = "2330.TW"
start_date =  datetime.strptime("2010-01-01", "%Y-%m-%d").date()
end_date = datetime.strptime("2020-06-30", "%Y-%m-%d").date()

stock = yf.Ticker(stock_name)
hist = stock.history(start=start_date, end=end_date)
filename = f'./{stock_name}.csv'

hist.to_csv(filename, mode='w+')