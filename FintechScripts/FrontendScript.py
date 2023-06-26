import tkinter as tk
from tkinter import messagebox
import subprocess

def scrape_data():
    try:
        subprocess.call(['python', 'YahooMarketScript.py'])
        messagebox.showinfo("Scraping Complete", "Data scraping is complete. Check the output files for the results.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during scraping: {str(e)}")

# Create the main window
window = tk.Tk()
window.title("Web Scraping Application")

# Create a button to initiate the scraping process
scrape_button = tk.Button(window, text="Scrape Data", command=scrape_data)
scrape_button.pack(pady=10)

# Run the application
window.mainloop()
