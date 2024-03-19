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

