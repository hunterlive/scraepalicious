import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk

def scrape_data(url, tag):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.find_all(tag)
    return [element.text for element in elements]

def start_scraping():
    url = url_entry.get()
    tag = tag_entry.get()
    data = scrape_data(url, tag)
    result.delete(1.0, tk.END)
    result.insert(tk.END, '\n'.join(data))

app = tk.Tk()
app.title("Web Scraper")

frame = ttk.Frame(app, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

url_label = ttk.Label(frame, text="URL:")
url_label.grid(row=0, column=0, sticky=tk.W)
url_entry = ttk.Entry(frame, width=50)
url_entry.grid(row=0, column=1)

tag_label = ttk.Label(frame, text="Tag:")
tag_label.grid(row=1, column=0, sticky=tk.W)
tag_entry = ttk.Entry(frame, width=50)
tag_entry.grid(row=1, column=1)

scrape_button = ttk.Button(frame, text="Scrape", command=start_scraping)
scrape_button.grid(row=2, column=0, columnspan=2)

result = tk.Text(frame, wrap=tk.WORD, width=60, height=20)
result.grid(row=3, column=0, columnspan=2)

app.mainloop()