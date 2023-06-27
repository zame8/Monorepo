import tkinter as tk
from tkinter import messagebox
import csv
from functools import partial
import subprocess

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

        # Create a new window to display the results
        result_window = tk.Toplevel(window)
        result_window.title("Scraped Data")

        # Create a text widget to display the results
        text_widget = tk.Text(result_window)
        text_widget.pack()

        # Display the first few rows of the results
        for row in rows[:10]:
            text_widget.insert(tk.END, ', '.join(row) + '\n')

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
