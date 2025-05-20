import tkinter as tk
from tkinter import messagebox

class BookDashboard:
    def __init__(self, master):
        self.master = master
        master.title("Manage Books")
        master.geometry("500x400")
        master.configure(bg="#f7f7f7")

        self.books = []  # Local list to store books

        tk.Label(master, text="Add / Remove Books", font=("Arial", 14, "bold"), bg="#f7f7f7").pack(pady=10)

        form_frame = tk.Frame(master, bg="#f7f7f7")
        form_frame.pack(pady=5)

        tk.Label(form_frame, text="Book Title:", font=("Arial", 10), bg="#f7f7f7").grid(row=0, column=0, padx=10, pady=5, sticky='e')
        self.title_entry = tk.Entry(form_frame, width=30)
        self.title_entry.grid(row=0, column=1, pady=5)

        tk.Label(form_frame, text="Author:", font=("Arial", 10), bg="#f7f7f7").grid(row=1, column=0, padx=10, pady=5, sticky='e')
        self.author_entry = tk.Entry(form_frame, width=30)
        self.author_entry.grid(row=1, column=1, pady=5)

        btn_frame = tk.Frame(master, bg="#f7f7f7")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Add Book", width=15, bg="#388E3C", fg="white", command=self.add_book).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="Remove Book", width=15, bg="#D32F2F", fg="white", command=self.remove_book).grid(row=0, column=1, padx=10)

        # Book list display
        list_frame = tk.Frame(master, bg="#f7f7f7")
        list_frame.pack(pady=10)

        tk.Label(list_frame, text="Books in Inventory:", font=("Arial", 12, "bold"), bg="#f7f7f7").pack()

        self.book_listbox = tk.Listbox(list_frame, width=60, height=8, font=("Arial", 10))
        self.book_listbox.pack(pady=5)

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()

        if title and author:
            entry = f"{title} by {author}"
            self.books.append(entry)
            self.book_listbox.insert(tk.END, entry)
            self.title_entry.delete(0, tk.END)
            self.author_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Missing Info", "Please enter both title and author.")

    def remove_book(self):
        selected = self.book_listbox.curselection()
        if selected:
            index = selected[0]
            removed = self.books.pop(index)
            self.book_listbox.delete(index)
            messagebox.showinfo("Removed", f"Book removed: {removed}")
        else:
            messagebox.showwarning("Select Book", "Please select a book to remove.")
