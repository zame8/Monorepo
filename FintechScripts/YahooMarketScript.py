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


    # Extract data from each row and store in a list
    for row in rows:
        columns = row.find_all('td')

    options_data = []

    # Extract data from each row and store in a list
    for row in rows:
        columns = row.find_all('td')
        symbol = columns[0].text
        contract_name = columns[2].text
        strike_price = columns[3].text
        expiry = columns[4].text
        bid_price = columns[5].text
        volume = columns[10].text
        open_interest = columns[11].text

        options_data.append([symbol, contract_name, strike_price, expiry, bid_price, volume, open_interest])

    # Write data to a CSV file
    with open('HighestInterestOptionsData.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Symbol', 'Contract Name', 'Strike Price', 'Last Price', 'Bid Price', 'Ask Price', 'Volume', 'Open Interest'])  # Write header row
        writer.writerows(options_data)

    print("Scraping complete. Data saved to HighestInterestOptionsData.csv.")

def scrape_stock_data(symbol):
    url = f"https://finance.yahoo.com/quote/{symbol}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Scrape specific data from the webpage
    # Example: Get the current price
    price_element = soup.find("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
    current_price = price_element.text.strip() if price_element else "N/A"

    # Example: Get the company name
    name_element = soup.find("h1", class_="D(ib) Fz(18px)")
    company_name = name_element.text.strip() if name_element else "N/A"

    # Return the scraped data as a dictionary
    return {
        "symbol": symbol,
        "company_name": company_name,
        "current_price": current_price,
        # Add other data points here
    }

# Example usage
stock_symbol = "AAPL"
stock_data = scrape_stock_data(stock_symbol)

# Accessing the scraped data
symbol = stock_data["symbol"]
company_name = stock_data["company_name"]
current_price = stock_data["current_price"]

# Printing the scraped data
print("Stock Symbol:", symbol)
print("Company Name:", company_name)
print("Current Price:", current_price)

# Run the scraper
#scrape_yahoo_markets()
def main():
    scrape_Highest_Interest_Rate()
    scrape_most_active_Stocks()

main()
