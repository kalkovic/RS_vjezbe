import tkinter as tk
from tkinter import ttk
from typing import List

from newsapp.core import services
from newsapp.core.domain import NewsItem

WINDOW_TITLE = "News Aggregator - Checkpoint 1"

def truncate(text: str, length: int = 38) -> str:
    return text if len(text) <= length else text[:length].rstrip() + "..."

class NewsApp:
    def __init__(self, master):
        self.master = master
        master.title(WINDOW_TITLE)
        master.geometry("900x550")
        master.minsize(780, 500)

        self.style = ttk.Style(master)
        try:
            self.style.theme_use("clam")
        except:
            pass

        # Tabs
        self.tabs = ttk.Notebook(master)
        self.tab_list = ttk.Frame(self.tabs)
        self.tab_search = ttk.Frame(self.tabs)

        self.tabs.add(self.tab_list, text="Sve vijesti")
        self.tabs.add(self.tab_search, text="Filtriranje")
        self.tabs.pack(fill=tk.BOTH, expand=True)

        self._build_list_tab(self.tab_list)
        self._build_search_tab(self.tab_search)

        self._load_all()

    # -----------------------
    #   TAB 1 - sve vijesti
    # -----------------------
    def _build_list_tab(self, parent):
        container = ttk.Frame(parent, padding=10)
        container.pack(fill=tk.BOTH, expand=True)

        left = ttk.Frame(container, width=1080)
        left.pack(side=tk.LEFT, fill=tk.Y, padx=(0,10))

        right = ttk.Frame(container)
        right.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.news_listbox = tk.Listbox(left, activestyle="dotbox")
        self.news_listbox.pack(fill=tk.BOTH, expand=True)
        self.news_listbox.bind("<<ListboxSelect>>", self._on_select)

        self.title_label = ttk.Label(right, text="Odaberi vijest", font=("Segoe UI", 12, "bold"))
        self.title_label.pack(anchor="nw")

        self.category_label = ttk.Label(right, text="", font=("Segoe UI", 9, "italic"))
        self.category_label.pack(anchor="nw", pady=(0,6))

        self.content_text = tk.Text(right, wrap=tk.WORD)
        self.content_text.pack(fill=tk.BOTH, expand=True)
        self.content_text.configure(state="disabled")

    # -----------------------
    #   TAB 2 - kategorije / filtriranje
    # -----------------------
    def _build_search_tab(self, parent):
        container = ttk.Frame(parent, padding=10)
        container.pack(fill=tk.BOTH, expand=True)

        top = ttk.Frame(container)
        top.pack(fill=tk.X, pady=(0,10))

        ttk.Label(top, text="Kategorija:").pack(side=tk.LEFT)
        self.category_cb = ttk.Combobox(top, state="readonly")
        self.category_cb.pack(side=tk.LEFT, padx=(6,6))
        self.category_cb.bind("<<ComboboxSelected>>", self._on_category_selected)

        ttk.Button(top, text="Osvježi kategorije", command=self._load_categories).pack(side=tk.LEFT)

        self.search_result_list = tk.Listbox(container)
        self.search_result_list.pack(fill=tk.BOTH, expand=True)
        self.search_result_list.bind("<<ListboxSelect>>", self._on_search_select)

        bottom = ttk.Frame(container)
        bottom.pack(fill=tk.X, pady=(10,0))
        ttk.Button(bottom, text="Idi na sve vijesti", command=lambda: self.tabs.select(self.tab_list)).pack(side=tk.RIGHT)

    # -----------------------
    #   Podaci i prikaz
    # -----------------------
    def _load_all(self):
        self.news_items: List[NewsItem] = services.get_all_news()
        self._populate_listbox()
        self._load_categories()

    def _populate_listbox(self):
        self.news_listbox.delete(0, tk.END)
        for n in self.news_items:
            short = truncate(n.title, 38)
            self.news_listbox.insert(tk.END, f"{short}  [{n.category}]")

    def _load_categories(self):
        cats = services.get_categories()
        self.category_cb["values"] = ["(sve)"] + cats
        self.category_cb.set("(sve)")
        self._apply_category_filter("(sve)")

    # -----------------------
    #   event funkcije
    # -----------------------
    def _on_select(self, event):
        sel = self.news_listbox.curselection()
        if not sel:
            return
        idx = sel[0]
        self._show_details(self.news_items[idx])

    def _on_search_select(self, event):
        sel = self.search_result_list.curselection()
        if not sel:
            return
        idx = sel[0]
        selected_title = self.search_result_list.get(idx).split(" — ")[0]

        for i, n in enumerate(self.news_items):
            if n.title == selected_title:
                self.tabs.select(self.tab_list)
                self.news_listbox.selection_clear(0, tk.END)
                self.news_listbox.selection_set(i)
                self.news_listbox.see(i)
                self._show_details(n)
                break

    def _on_category_selected(self, event):
        cat = self.category_cb.get()
        self._apply_category_filter(cat)

    def _apply_category_filter(self, category):
        self.search_result_list.delete(0, tk.END)

        if category == "(sve)":
            filtered = self.news_items
        else:
            filtered = [n for n in self.news_items if n.category == category]

        for n in filtered:
            preview = n.content[:120].replace("\n", " ")
            self.search_result_list.insert(tk.END, f"{n.title} — {preview}...")

    def _show_details(self, item: NewsItem):
        self.title_label.config(text=item.title)
        self.category_label.config(text=f"Kategorija: {item.category}")

        self.content_text.configure(state="normal")
        self.content_text.delete("1.0", tk.END)
        self.content_text.insert(tk.END, item.content)
        self.content_text.configure(state="disabled")

def run_app():
    root = tk.Tk()
    NewsApp(root)
    root.mainloop()
