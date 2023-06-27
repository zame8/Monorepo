import requests
import csv
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

def scrape_most_active_Stocks():
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

            symbols.append(symbol)
            changes.append(change)



def scrape_Highest_Interest_Rate():
    url = 'https://finance.yahoo.com/options/highest-open-interest'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Find the table containing the option data
    tables = soup.find_all('table')
    table = None

    for t in tables:
        if 'W(100%)' in str(t):
            table = t
            break

    if table is None:
        print("Table not found. Please check the webpage structure.")
        return

    rows = table.find_all('tr')[1:]  # Exclude the header row

    options_data = []

    # Extract data from each row and store in a list
    for row in rows:
        columns = row.find_all('td')

    options_data = []

    # Extract data from each row and store in a list
    for row in rows:
        columns = row.find_all('td')
        symbol = columns[0].text
        contract_name = columns[1].text
        strike_price = columns[2].text
        last_price = columns[3].text
        bid_price = columns[4].text
        ask_price = columns[5].text
        volume = columns[6].text
        open_interest = columns[7].text

        options_data.append([symbol, contract_name, strike_price, last_price, bid_price, ask_price, volume, open_interest])

    # Write data to a CSV file
    with open('HighestInterestOptionsData.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Symbol', 'Contract Name', 'Strike Price', 'Last Price', 'Bid Price', 'Ask Price', 'Volume', 'Open Interest'])  # Write header row
        writer.writerows(options_data)

    print("Scraping complete. Data saved to HighestInterestOptionsData.csv.")

# Run the scraper
#scrape_yahoo_markets()
def main():
    scrape_Highest_Interest_Rate()
    scrape_most_active_Stocks()

main()
