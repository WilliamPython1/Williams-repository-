import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import matplotlib.pyplot as plt
from alpha_vantage.timeseries import TimeSeries
import pandas as pd
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.arima.model import ARIMA as ARIMA_new

api_key = 'O88HIS3IPQSPAIW3'
symbol = 'IBM'

def fetch_alpha_vantage_data(symbol, api_key):
    try:
        ts = TimeSeries(key=api_key, output_format='pandas')
        data, meta_data = ts.get_daily(symbol=symbol, outputsize='full')
        return data
    except Exception as e:
        print(f"Error fetching data from Alpha Vantage: {str(e)}")
        return None

def predict_future_arima(data, periods=30):
    model = ARIMA_new(data, order=(5, 1, 0))  # Adjust order as needed
    model_fit = model.fit()
    future_forecast = model_fit.forecast(steps=periods)
    return future_forecast

# Fetch data from Alpha Vantage and create a pandas DataFrame
stock_data_df = fetch_alpha_vantage_data(symbol, api_key)

if stock_data_df is not None:
    print("Stock data successfully fetched and processed.")
    print("Columns in the dataset:")
    print(stock_data_df.columns)

    columns = stock_data_df.columns
    close_column = next((col for col in columns if 'close' in col.lower()), None)

    if close_column:
        input_data = stock_data_df[close_column].values.astype(np.float32)
        target_data = input_data[1:]
        input_data = torch.from_numpy(input_data[:-1])
        target_data = torch.from_numpy(target_data)

        class StockPredictionNN(nn.Module):
            def __init__(self, input_size, hidden_size, output_size):
                super(StockPredictionNN, self).__init__()
                self.hidden = nn.Linear(input_size, hidden_size)
                self.relu = nn.ReLU()
                self.output = nn.Linear(hidden_size, output_size)

            def forward(self, x):
                out = self.hidden(x)
                out = self.relu(out)
                out = self.output(out)
                return out

        class StockDataset(Dataset):
            def __init__(self, input_data, target_data):
                self.input_data = input_data
                self.target_data = target_data

            def __len__(self):
                return len(self.input_data)

            def __getitem__(self, idx):
                return self.input_data[idx], self.target_data[idx]

        dataset = StockDataset(input_data, target_data)
        dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

        input_size = 1
        hidden_size = 128
        output_size = 1
        learning_rate = 0.01
        num_epochs = 10

        model = StockPredictionNN(input_size, hidden_size, output_size)
        criterion = nn.MSELoss()
        optimizer = optim.Adam(model.parameters(), lr=learning_rate)

        for epoch in range(num_epochs):
            total_loss = 0
            for batch_input, batch_target in dataloader:
                outputs = model(batch_input.unsqueeze(1))
                loss = criterion(outputs, batch_target)
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()
                total_loss += loss.item()

            if (epoch+1) % 10 == 0:
                print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {total_loss / len(dataloader)}')

        current_date = pd.to_datetime('2023-10-14')

        future_dates = pd.date_range(start=current_date, end='2024-12-31', freq='B')

        future_dates_as_input = torch.from_numpy(np.arange(len(stock_data_df), len(stock_data_df) + len(future_dates)).astype(np.float32))

        model.eval()
        with torch.no_grad():
            predicted_data = model(input_data.unsqueeze(1))
            arima_future = predict_future_arima(input_data.numpy(), periods=30)

        last_actual_date = stock_data_df.index[-1]

        arima_predicted_dates = pd.date_range(start=current_date, periods=30, freq='B')

        last_actual_price = target_data[-1]

        arima_future_adjusted = np.concatenate(([last_actual_price], arima_future[1:]))

        plt.figure(figsize=(12, 6))
        plt.plot(stock_data_df.index[1:], target_data, label='Actual Prices', color='blue')
        plt.plot(stock_data_df.index[1:], predicted_data.numpy(), label='Predicted Prices (NN)', color='red')

        plt.plot(arima_predicted_dates, arima_future_adjusted, label='Predicted Future Prices (ARIMA)', color='green', linestyle='dashed')

        plt.xlabel('Date')
        plt.ylabel('Closing Price')
        plt.title(f'{symbol} Stock Prices - Actual vs. Predicted')
        plt.legend()
        plt.show()
