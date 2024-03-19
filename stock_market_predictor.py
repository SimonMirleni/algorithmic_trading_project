import numpy as np
import pandas as pd
import yfinance as yf
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score


sp500 = yf.Ticker("^GSPC")
sp500 = sp500.history(period = "max")
sp500.plot.line(y="Close", use_index = True)
plt.show()

del sp500["Dividends"]
del sp500["Stock Splits"]
sp500["Tomorrow"] = sp500["Close"].shift(-1)
sp500["Target"] = (sp500["Tomorrow"]>sp500["Close"]).astype(int)

#I will take data from 1990 to now because with stock market data if you go back too far, 
#the market could have shifted fundamentally and some of that old data may not be as useful to make future predictions.
sp500 = sp500.loc["1990-01-01":].copy()