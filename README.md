# Stock Market Prediction Using Random Forest Classifier

This repository contains Python code for predicting stock market trends using a Random Forest Classifier. The code fetches historical data of the S&P 500 index (^GSPC) from Yahoo Finance, preprocesses the data, trains a Random Forest Classifier model, and evaluates its performance on test data. Additionally, it demonstrates a backtesting method and explores different predictors for improving prediction accuracy.

## Prerequisites
- Python 3.x
- Required libraries: numpy, pandas, yfinance, matplotlib, sklearn

## Getting Started
1. Clone the repository to your local machine:
git clone https://github.com/yourusername/stock-market-prediction.git
2. Install the required libraries:
pip install -r requirements.txt
3. Run the Python script:
python stock_prediction.py

## Overview of the Code
- The code fetches historical data of the S&P 500 index using the Yahoo Finance API and preprocesses it to create a binary target variable indicating whether the price will increase or decrease the next day.
- It trains a Random Forest Classifier model using the historical data from 1990 to the present.
- The model is evaluated using precision score on a test dataset and visualized for comparison.
- The code includes functions for prediction, backtesting, and exploring different predictors such as rolling averages and trend indicators.
- The final model is evaluated using precision score after applying additional predictors and a modified prediction threshold.

## Files in the Repository
- `stock_prediction.py`: Main Python script containing the code for fetching data, preprocessing, training the model, and evaluating performance.
- `requirements.txt`: File containing the list of required libraries and their versions.
- `LICENSE`: Document indicating the project's license (MIT License).

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- The code is inspired by various machine learning tutorials and examples available online.
- Special thanks to the developers of yfinance and scikit-learn libraries for providing powerful tools for financial data analysis and machine learning.
