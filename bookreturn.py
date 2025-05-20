import tkinter as tk
from tkinter import ttk, messagebox

# Sample borrowed books (to simulate borrowed inventory)
borrowed_books = [
    {'book_id': 'B001', 'title': 'Python Programming', 'member_name': 'Ali'},
    {'book_id': 'B002', 'title': 'Data Structures', 'member_name': 'Sara'},
    {'book_id': 'B003', 'title': 'Machine Learning', 'member_name': 'John'}
]

returned_books = []


def update_borrowed_list():
    borrowed_table.delete(*borrowed_table.get_children())
    for index, book in enumerate(borrowed_books):
        borrowed_table.insert('', 'end', iid=index, values=(book['book_id'], book['title'], book['member_name']))


def return_book():
    selected = borrowed_table.selection()
    if not selected:
        messagebox.showwarning("No selection", "Please select a book to return.")
        return

    index = int(selected[0])
    book = borrowed_books.pop(index)
    returned_books.append(book)

    update_borrowed_list()
    returned_table.insert('', 'end', values=(book['book_id'], book['title'], book['member_name']))
    messagebox.showinfo("Success", f"Book '{book['title']}' returned successfully.")


# GUI Setup
root = tk.Tk()
root.title("Library Book Return System")
root.geometry("750x500")
root.resizable(False, False)

tk.Label(root, text="Book Return", font=("Arial", 20), pady=10).pack()

# --- Borrowed Books Table ---
frame_borrowed = tk.LabelFrame(root, text="Borrowed Books", padx=10, pady=10)
frame_borrowed.pack(fill="x", padx=20, pady=5)

borrowed_table = ttk.Treeview(frame_borrowed, columns=("ID", "Title", "Borrowed By"), show='headings', height=6)
borrowed_table.heading("ID", text="Book ID")
borrowed_table.heading("Title", text="Book Title")
borrowed_table.heading("Borrowed By", text="Borrowed By")

borrowed_table.column("ID", width=100)
borrowed_table.column("Title", width=300)
borrowed_table.column("Borrowed By", width=200)
borrowed_table.pack()

update_borrowed_list()

# --- Return Button ---
tk.Button(root, text="Return Selected Book", font=("Arial", 12), bg="green", fg="white",
          command=return_book).pack(pady=10)

# --- Returned Books Table ---
frame_returned = tk.LabelFrame(root, text="Returned Books", padx=10, pady=10)
frame_returned.pack(fill="x", padx=20, pady=5)

returned_table = ttk.Treeview(frame_returned, columns=("ID", "Title", "Returned By"), show='headings', height=6)
returned_table.heading("ID", text="Book ID")
returned_table.heading("Title", text="Book Title")
returned_table.heading("Returned By", text="Returned By")

returned_table.column("ID", width=100)
returned_table.column("Title", width=300)
returned_table.column("Returned By", width=200)
returned_table.pack()

# Start GUI loop
root.mainloop()
