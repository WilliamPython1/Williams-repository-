import yfinance as yf
import pandas as pd
import datetime
import os

# os for creating document and replacing data if it already exists.

stock_symbols = ['AAPL', 'MSFT', 'GOOGL']

# Get the date one week ago and four days ago
end_date = datetime.datetime.now().date() - datetime.timedelta(days=4)
start_date = datetime.datetime.now().date() - datetime.timedelta(days=11)  # 7 days plus 4 more days

data = yf.download(stock_symbols, start=start_date, end=end_date)
df = pd.DataFrame(data)

# Get the user's Documents directory and save the file there
documents_dir = os.path.join(os.path.expanduser('~'), 'Documents')
excel_file_path = os.path.join(documents_dir, 'Book1.xlsx')

print(f"Saving data to: {excel_file_path}")

# Close the file if it's open, won't work without.
try:
    df.to_excel(excel_file_path, index=True)
except PermissionError:
    print("Please close the Excel file and run the script again.")

print(f"Data saved to {excel_file_path}")
print(f"Start date: {start_date}")
print(f"End date: {end_date}")
