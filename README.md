
# Time Series Forecasting for Stock Market Prices

## Overview

This project performs time series analysis and forecasting on historical stock prices using ARIMA models and moving averages. The goal is to predict future stock prices based on historical data and provide insights through visualizations. The project allows you to specify a stock ticker and perform analysis based on the chosen stock. The CSV file was orginally from Kaggle and it contains a lot of stock tickers and it's details. Since GitHub doesn't allow files of more than 25mb. I won't be uploading the csv file, but I will leave a link to the dataset in Kaggle below. Additionally, I am implementing auto_arima from the pmdarima library to automatically optimize the ARIMA model parameters (p, d, and q) for each stock, improving forecast accuracy. The project is still in development, with ongoing efforts to fix dependency issues through Python virtual environments (python -m venv) and further refine the model’s performance.  However, you can still test it out without the auto arima using the setup instructions I have given below.

Link to Kaggle Dataset used for this Project: https://www.kaggle.com/datasets/camnugent/sandp500

## Technologies Used

- **Programming Language**: Python
- **Libraries**: Pandas, NumPy, Matplotlib, statsmodels (for ARIMA)
- **Database**: CSV data
- **Version Control**: Git & GitHub

## Project Structure

```
TimeSeriesForecastingStockPrices/
├── data/
│   └── stock_price_data.csv                  # Historical stock prices data
├── sql/
│   └── extract_stock_data.sql                # SQL script to retrieve stock price data (optional)
├── scripts/
│   ├── arima_model.py                        # Python script to implement ARIMA model
│   ├── moving_average.py                     # Python script for moving average analysis
├── visualizations/                           # Directory to save the generated plots
│   ├── AAPL_stock_trends.png                 # Example Stock price trends visualization
│   ├── AAPL_arima_forecast.png               # Example ARIMA model forecast visualization
├── README.md                                 # Documentation
└── requirements.txt                          # Python dependencies
```

## Setup Instructions

### 1. Set up a virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Perform Moving Average Analysis:

```bash
python3 scripts/moving_average.py
```

You will be prompted to enter the stock ticker (e.g., AAPL). The script will calculate the 7-day and 30-day moving averages for that stock and visualize the trends.

### 3. Perform ARIMA Model Forecasting:

```bash
python3 scripts/arima_model.py
```

You will be prompted to enter the stock ticker (e.g., AAPL). The script will apply the ARIMA model to forecast the next 10 days of stock prices and visualize the predictions.

## Results and Visualizations

The project produces two visualizations:
- **Stock Price Trends with Moving Averages**: Shows the actual stock prices alongside the 7-day and 30-day moving averages for a chosen stock.
- **Stock Price Forecast using ARIMA**: Shows the forecasted stock prices for the next 10 days based on historical data.


## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests. Please follow the code of conduct when contributing.