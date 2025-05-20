import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Settings
FINE_PER_DAY = 10

# --- Fine Calculation Logic ---
def calculate_fine():
    member = entry_member.get()
    book = entry_book.get()
    due_date_str = entry_due.get()
    return_date_str = entry_return.get()

    if not member or not book or not due_date_str or not return_date_str:
        messagebox.showwarning("⚠️ Missing Info", "Please fill all the fields.")
        return

    try:
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
        return_date = datetime.strptime(return_date_str, "%Y-%m-%d")
    except ValueError:
        messagebox.showerror("❌ Invalid Date", "Please use YYYY-MM-DD format.")
        return

    days_late = (return_date - due_date).days
    fine = max(0, days_late * FINE_PER_DAY)

    result_text = (
        f"👤 Member: {member}\n"
        f"📚 Book: {book}\n"
        f"📅 Days Late: {max(0, days_late)}\n"
        f"💸 Fine Amount: ₹{fine}"
    )

    result_label.config(text=result_text, fg="#28a745" if fine > 0 else "#007bff")

# --- GUI Setup ---
root = tk.Tk()
root.title("💸 Fine Calculator - Library System")
root.geometry("600x500")
root.configure(bg="#f0f2f5")

# --- Fonts & Styles ---
title_font = ("Arial", 22, "bold")
label_font = ("Arial", 12)
entry_font = ("Arial", 12)
button_font = ("Arial", 14, "bold")
result_font = ("Arial", 13)

# --- Title ---
tk.Label(root, text="📄 Library Fine Calculator", font=title_font, bg="#f0f2f5", fg="#333").pack(pady=25)

# --- Form Frame ---
form_frame = tk.Frame(root, bg="#f0f2f5")
form_frame.pack(pady=10)

def add_field(row, label_text, entry_var):
    tk.Label(form_frame, text=label_text, font=label_font, bg="#f0f2f5").grid(row=row, column=0, sticky="w", padx=10, pady=10)
    entry = tk.Entry(form_frame, font=entry_font, width=30, textvariable=entry_var, relief="groove", bd=2)
    entry.grid(row=row, column=1, pady=10, padx=5)
    return entry

# Entry fields
member_var = tk.StringVar()
book_var = tk.StringVar()
due_var = tk.StringVar()
return_var = tk.StringVar()

entry_member = add_field(0, "👤 Member Name / ID:", member_var)
entry_book = add_field(1, "📘 Book Title:", book_var)
entry_due = add_field(2, "📅 Due Date (YYYY-MM-DD):", due_var)
entry_return = add_field(3, "📆 Return Date (YYYY-MM-DD):", return_var)

# --- Button ---
tk.Button(
    root,
    text="🧮 Calculate Fine",
    font=button_font,
    bg="#007bff",
    fg="white",
    activebackground="#0056b3",
    activeforeground="white",
    width=20,
    height=2,
    command=calculate_fine
).pack(pady=20)

# --- Result Label ---
result_label = tk.Label(root, text="", font=result_font, bg="#f0f2f5", justify="left")
result_label.pack(pady=10)

# --- Run ---
root.mainloop()
