import tkinter as tk
from tkinter import ttk

# Sample Inventory Data
inventory_data = [
    {'book_id': 'B001', 'title': 'Python Programming', 'status': 'Available'},
    {'book_id': 'B002', 'title': 'Data Structures', 'status': 'Borrowed'},
    {'book_id': 'B003', 'title': 'Machine Learning', 'status': 'Returned'},
    {'book_id': 'B004', 'title': 'Web Development', 'status': 'Available'},
    {'book_id': 'B005', 'title': 'Artificial Intelligence', 'status': 'Borrowed'},
]

def populate_inventory_table(data):
    inventory_table.delete(*inventory_table.get_children())
    for book in data:
        inventory_table.insert('', 'end', values=(book['book_id'], book['title'], book['status']))

def filter_inventory():
    selected_status = status_var.get()
    if selected_status == "All":
        populate_inventory_table(inventory_data)
    else:
        filtered = [book for book in inventory_data if book['status'] == selected_status]
        populate_inventory_table(filtered)

# Root Window Setup
root = tk.Tk()
root.title("📚 Library Inventory Reports")
root.geometry("800x550")
root.configure(bg="#f5f5f5")

# Style Configuration
style = ttk.Style()
style.theme_use("clam")

# Treeview styling
style.configure("Treeview", font=("Arial", 11), rowheight=28, background="white", fieldbackground="white")
style.configure("Treeview.Heading", font=("Arial", 12, "bold"), background="#3e64ff", foreground="white")

# Highlight selected row
style.map("Treeview", background=[('selected', '#d1e0ff')])

# --- Title Label ---
tk.Label(root, text="📊 Inventory Report", font=("Arial", 24, "bold"), bg="#f5f5f5", fg="#333").pack(pady=20)

# --- Filter Section ---
frame_filter = tk.Frame(root, bg="#f5f5f5")
frame_filter.pack(pady=5)

tk.Label(frame_filter, text="Filter by Status:", font=("Arial", 12), bg="#f5f5f5").pack(side=tk.LEFT, padx=5)

status_var = tk.StringVar(value="All")
status_options = ["All", "Available", "Borrowed", "Returned"]
status_menu = ttk.OptionMenu(frame_filter, status_var, status_var.get(), *status_options)
status_menu.pack(side=tk.LEFT, padx=5)

ttk.Button(frame_filter, text="Apply Filter", command=filter_inventory).pack(side=tk.LEFT, padx=10)

# --- Inventory Table Frame ---
frame_table = tk.Frame(root, bg="#f5f5f5")
frame_table.pack(fill="both", expand=True, padx=20, pady=15)

# Inventory Table
inventory_table = ttk.Treeview(frame_table, columns=("ID", "Title", "Status"), show='headings', height=12)
inventory_table.heading("ID", text="Book ID")
inventory_table.heading("Title", text="Book Title")
inventory_table.heading("Status", text="Status")

inventory_table.column("ID", width=100, anchor=tk.CENTER)
inventory_table.column("Title", width=400, anchor=tk.W)
inventory_table.column("Status", width=150, anchor=tk.CENTER)

# Scrollbar
scrollbar = ttk.Scrollbar(frame_table, orient="vertical", command=inventory_table.yview)
inventory_table.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
inventory_table.pack(fill="both", expand=True)

# Load all data initially
populate_inventory_table(inventory_data)

# Run the App
root.mainloop()
