import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import matplotlib.pyplot as plt
from alpha_vantage.timeseries import TimeSeries

# Alpha Vantage API credentials
api_key = 'O88HIS3IPQSPAIW3'
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
    print("Columns in the dataset:")
    print(stock_data_df.columns)  # Print columns to identify the correct column name

    # Determine the correct column name for closing prices
    columns = stock_data_df.columns
    close_column = next((col for col in columns if 'close' in col.lower()), None)

    if close_column:
        # Modify the way we access the 'close' column
        input_data = stock_data_df[close_column].values.astype(np.float32)
        target_data = input_data[1:]  # Shifted by one day for prediction
        input_data = torch.from_numpy(input_data[:-1])
        target_data = torch.from_numpy(target_data)

        # Define the neural network architecture
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

        # Define the dataset and dataloader
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

        # Initialize the neural network, loss function, and optimizer
        input_size = 1  # Only using the 'close' column for prediction
        hidden_size = 64
        output_size = 1  # Predicting the 'close' value
        learning_rate = 0.001
        num_epochs = 100

        model = StockPredictionNN(input_size, hidden_size, output_size)
        criterion = nn.MSELoss()
        optimizer = optim.Adam(model.parameters(), lr=learning_rate)

        # Train the neural network
        for epoch in range(num_epochs):
            total_loss = 0
            for batch_input, batch_target in dataloader:
                outputs = model(batch_input.unsqueeze(1))  # Adjust input shape
                loss = criterion(outputs, batch_target)
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()
                total_loss += loss.item()

            if (epoch+1) % 10 == 0:
                print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {total_loss / len(dataloader)}')

        # Plot the predicted stock prices
        model.eval()
        with torch.no_grad():
            predicted_data = model(input_data.unsqueeze(1))  # Adjust input shape
            plt.figure(figsize=(12, 6))
            plt.plot(stock_data_df.index[1:], target_data, label='Actual Prices', color='blue')
            plt.plot(stock_data_df.index[1:], predicted_data.numpy(), label='Predicted Prices', color='red')
            plt.xlabel('Date')
            plt.ylabel('Closing Price')
            plt.title(f'{symbol} Stock Prices - Actual vs. Predicted')
            plt.legend()
            plt.show()
    else:
        print("No column found for closing prices.")
else:
    print("Failed to fetch and process stock data.")
