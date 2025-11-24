import tkinter as tk
import json

class NewsApp:
    def __init__(self, master):
        self.master = master
        master.title("News Aggregator")

        self.listbox = tk.Listbox(master, width=50, height=15)
        self.listbox.pack(side="left", padx=10, pady=10)
        self.listbox.bind("<<ListboxSelect>>", self.show_article)

        self.text = tk.Text(master, width=60, height=15)
        self.text.pack(side="right", padx=10, pady=10)

        self.load_news()

    def load_news(self):
        with open("newsapp/data/news.json", "r", encoding="utf-8") as f:
            self.news = json.load(f)

        for article in self.news:
            self.listbox.insert(tk.END, article["title"])

    def show_article(self, event):
        index = self.listbox.curselection()[0]
        self.text.delete("1.0", tk.END)
        self.text.insert(tk.END, self.news[index]["content"])

root = tk.Tk()
app = NewsApp(root)
root.mainloop()
