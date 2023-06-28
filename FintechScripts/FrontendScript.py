import tkinter as tk
from tkinter import messagebox
import csv
from functools import partial
import subprocess
import matplotlib.pyplot as plt

def scrape_data():
    try:
        subprocess.call(['python', 'YahooMarketScript.py'])
        messagebox.showinfo("Scraping Complete", "Data scraping is complete. Check the output files for the results.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during scraping: {str(e)}")

def display_results(csv_file):
    with open(csv_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)

        result_window = tk.Toplevel(window)
        result_window.title("Scraped Data")

        text_widget = tk.Text(result_window)
        text_widget.pack()

        for row in rows[:10]:
            text_widget.insert(tk.END, ', '.join(row) + '\n')
   
        graph_button = tk.Button(result_window, text="Display Graph", command=partial(display_graph, rows))
        graph_button.pack(pady=10)

def display_graph(data):
    data = data[1:]
    x = [row[0] for row in data]
    y = [float(row[-1].strip('%').replace(',','')) for row in data]
    plt.bar(x, y)
    plt.xticks(rotation=45, ha='right', fontsize=8)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Graph for the scrapped data')
    plt.show()
    plt.tight_layout()


# Create the main window
window = tk.Tk()
window.title("Web Scraping Application")

# Create a button to initiate the scraping process
scrape_button = tk.Button(window, text="Scrape Data", command=scrape_data)
scrape_button.pack(pady=10)

# Create a button to display the most active stocks data
display_stocks_button = tk.Button(window, text="Display Most Active Stocks", command=partial(display_results, 'ResultantResponseData.csv'))
display_stocks_button.pack(pady=10)

# Create a button to display the highest interest options data
display_options_button = tk.Button(window, text="Display Highest Interest Options", command=partial(display_results, 'HighestInterestOptionsData.csv'))
display_options_button.pack(pady=10)

# Run the application
window.mainloop()
