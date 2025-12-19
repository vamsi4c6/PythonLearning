import pandas as pd
import matplotlib.pyplot as plt


# Load Excel file
df = pd.read_excel('C:\\Learning\\Python\\MyHoldings.xlsx', sheet_name='Sheet1')

print(df)


# Extract data
ticker = df['Ticker']
totalDividend = df['Total Dividend Per Month']
dividendAllocation = df['Dividend Allocation']

# Create a figure with 1 row and 2 columns
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# Bar chart
axs[0].bar(ticker, totalDividend, color='steelblue')
axs[0].set_title('Total Dividend earned per month based on each ticker(Bar Chart)')
axs[0].set_ylabel('Dividend/Month')
axs[0].set_xlabel('Ticker')

# Pie chart
axs[1].pie(dividendAllocation, labels=ticker, autopct='%1.1f%%', startangle=90)
axs[1].set_title('Dividend Allocation (Pie Chart)')

# Layout adjustment
plt.tight_layout()
plt.show()


