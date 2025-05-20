import tkinter as tk
from tkinter import messagebox

class LoginWindow:
    def __init__(self, master):
        self.master = master
        master.title("Library Login")
        master.geometry("350x220")
        master.configure(bg="#f0f4f7")

        tk.Label(master, text="Library Admin Login", font=("Arial", 14, "bold"), bg="#f0f4f7").pack(pady=15)

        frame = tk.Frame(master, bg="#f0f4f7")
        frame.pack(pady=5)

        tk.Label(frame, text="Username:", font=("Arial", 10), bg="#f0f4f7").grid(row=0, column=0, padx=10, pady=5, sticky='e')
        self.username_entry = tk.Entry(frame, width=25)
        self.username_entry.grid(row=0, column=1, pady=5)

        tk.Label(frame, text="Password:", font=("Arial", 10), bg="#f0f4f7").grid(row=1, column=0, padx=10, pady=5, sticky='e')
        self.password_entry = tk.Entry(frame, show="*", width=25)
        self.password_entry.grid(row=1, column=1, pady=5)

        tk.Button(master, text="Login", width=15, bg="#1976D2", fg="white", command=self.login).pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "admin":
            messagebox.showinfo("Login", "Login successful!")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")
