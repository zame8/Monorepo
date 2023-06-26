import requests
import csv
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

def scrape_yahoo_markets():
    url = 'https://finance.yahoo.com/most-active'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the table containing the market data
    table = soup.find('table', {'class': 'W(100%)'})
    rows = table.find_all('tr')[1:]  # Exclude the header row

    symbols = []
    changes = []


    # Extract data from each row and write to a CSV file
    with open('ResultantResponseData.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Symbol', 'Name', 'Price', 'Change', 'Percent Change'])  # Write header row

        for row in rows:
            columns = row.find_all('td')
            symbol = columns[0].text
            name = columns[1].text
            price = columns[2].text
            change = float(columns[3].text.replace(',', ''))  
            percent_change = columns[4].text

            writer.writerow([symbol, name, price, change, percent_change])  # Write data row

            print(f"Symbol: {symbol}")
            print(f"Name: {name}")
            print(f"Price: {price}")
            print(f"Change: {change}")
            print(f"Percent Change: {percent_change}")
            print()

            symbols.append(symbol)
            changes.append(change)
        
        positive_changes = [c if c > 0 else 0 for c in changes]
        negative_changes = [c if c < 0 else 0 for c in changes]

        plt.bar(symbols, positive_changes, color='g', label='Positive Changes')
        plt.bar(symbols, negative_changes, color='r', label='Negative Changes')
        plt.bar(symbols, changes)

        plt.xlabel('Symbol')
        plt.ylabel('Change')
        plt.title('Yahoo Finance Most Active Stocks')
        plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
        plt.tight_layout()  # Adjust layout to prevent labels from overlapping
        plt.show()

# Run the scraper
scrape_yahoo_markets()
