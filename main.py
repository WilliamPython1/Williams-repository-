import yfinance as yf
import pandas as pd

stock_symbols = ['AAPL', 'MSFT', 'GOOGL']
data = yf.download(stock_symbols, start='2023-01-01', end='2023-08-19')
df = pd.DataFrame(data)

excel_file_path = 'C:\\Users\\willi\\Downloads\\Book1.xlsx'
df.to_excel(excel_file_path, index=True)

print(f"Data saved to {excel_file_path}")
