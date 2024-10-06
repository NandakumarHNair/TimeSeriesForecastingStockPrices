
import pandas as pd
import matplotlib.pyplot as plt

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
    # Step 4: Calculate moving averages (7-day and 30-day)
    stock_data['7_day_MA'] = stock_data['close'].rolling(window=7).mean()
    stock_data['30_day_MA'] = stock_data['close'].rolling(window=30).mean()

    # Step 5: Plot the stock prices and moving averages
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data.index, stock_data['close'], label='Stock Price', color='blue')
    plt.plot(stock_data.index, stock_data['7_day_MA'], label='7-day MA', color='orange')
    plt.plot(stock_data.index, stock_data['30_day_MA'], label='30-day MA', color='green')
    plt.title(f'{stock_symbol} Stock Price with Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.legend()
    plt.savefig(f'visualizations/{stock_symbol}_stock_trends.png')
    plt.show()
