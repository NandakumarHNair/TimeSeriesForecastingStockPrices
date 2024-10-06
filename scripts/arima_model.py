
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Step 1: Ask for the stock ticker from the user
stock_symbol = input("Enter the stock ticker (e.g., AAPL): ").upper()

# Step 2: Load stock price data from CSV
df = pd.read_csv('data/stock_price_data.csv', parse_dates=['date'], index_col='date')

# Step 3: Filter the data for the selected stock ticker
stock_data = df[df['Name'] == stock_symbol]

# Check if stock data exists for the entered ticker
if stock_data.empty:
    print(f"No data available for ticker {stock_symbol}. Please check the input.")
else:
    # Step 4: Train ARIMA model
    model = ARIMA(stock_data['close'], order=(5, 1, 0))
    model_fit = model.fit()

    # Step 5: Forecast the next 10 days
    forecast = model_fit.forecast(steps=10)

    # Step 6: Plot the original data and the forecast
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data.index, stock_data['close'], label='Historical Stock Prices', color='blue')
    plt.plot(pd.date_range(stock_data.index[-1], periods=10, freq='D'), forecast, label='ARIMA Forecast', color='orange')
    plt.title(f'{stock_symbol} Stock Price Forecast with ARIMA')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.legend()
    plt.savefig(f'visualizations/{stock_symbol}_arima_forecast.png')
    plt.show()

    # Print the forecasted values
    print(forecast)
