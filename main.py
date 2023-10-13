import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import matplotlib.pyplot as plt
from alpha_vantage.timeseries import TimeSeries

# Alpha Vantage API credentials
api_key = 'YOUR_API_KEY'
symbol = 'IBM'

# Function to fetch data from Alpha Vantage and return as a pandas DataFrame
def fetch_alpha_vantage_data(symbol, api_key):
    try:
        ts = TimeSeries(key=api_key, output_format='pandas')
        data, meta_data = ts.get_daily(symbol=symbol, outputsize='full')
        return data  # Return the DataFrame directly
    except Exception as e:
        print(f"Error fetching data from Alpha Vantage: {str(e)}")
        return None

# Fetch data from Alpha Vantage and create a pandas DataFrame
stock_data_df = fetch_alpha_vantage_data(symbol, api_key)

if stock_data_df is not None:
    print("Stock data successfully fetched and processed.")
    print("Sample data:")
    print(stock_data_df.head())

    # Determine the correct column name for closing prices
    columns = stock_data_df.columns
    close_column = next((col for col in columns if 'close' in col.lower()), None)
    if close_column:
        # Plot the stock data with the specified colors and style
        plt.figure(figsize=(12, 6))
        plt.plot(stock_data_df[close_column], label='Closing Prices', color='#001f3f')
        plt.xlabel('Date')
        plt.ylabel('Closing Price')
        plt.title(f'{symbol} Stock Prices')
        plt.legend()
        plt.show()
    else:
        print("No column found for closing prices.")
else:
    print("Failed to fetch and process stock data.")
