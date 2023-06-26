import requests
from bs4 import BeautifulSoup

def scrape_yahoo_markets():
    url = 'https://finance.yahoo.com/most-active'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the table containing the market data
    table = soup.find('table', {'class': 'W(100%)'})
    rows = table.find_all('tr')[1:]  # Exclude the header row

    # Extract data from each row
    for row in rows:
        columns = row.find_all('td')
        symbol = columns[0].text
        name = columns[1].text
        price = columns[2].text
        change = columns[3].text
        percent_change = columns[4].text

        print(f"Symbol: {symbol}")
        print(f"Name: {name}")
        print(f"Price: {price}")
        print(f"Change: {change}")
        print(f"Percent Change: {percent_change}")
        print()

# Run the scraper
scrape_yahoo_markets()
