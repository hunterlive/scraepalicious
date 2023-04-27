import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup

def scrape_website():
    query = entry.get()
    if not query:
        messagebox.showerror("Error", "Please enter a query")
        return

    url = f"https://www.toughstart.org{query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    results = soup.find_all("div", class_="result")

    with open("output.txt", "w") as output_file:
        for result in results:
            output_file.write(result.text + "\n")

    messagebox.showinfo("Success", "Results saved to output.txt")

root = tk.Tk()
root.title("Web Scraper")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

label = tk.Label(frame, text="Enter your query:")
label.pack()

entry = tk.Entry(frame)
entry.pack()

button = tk.Button(frame, text="Scrape", command=scrape_website)
button.pack()

root.mainloop()