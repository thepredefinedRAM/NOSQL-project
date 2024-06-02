import tkinter as tk
from tkinter import messagebox
import BackgroundPage  # Assuming medinframain.py is in the same directory

def login():
    username = username_entry.get()
    password = password_entry.get()

    # You can add your authentication logic here
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
        root.destroy()  # Close the login window
        medinframain.main()  # Open the main page
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create the main window
root = tk.Tk()
root.title("Login Page")

# Create username label and entry
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

# Create password label and entry
password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Create login button
login_button = tk.Button(root, text="Login", command=login)
login_button.pack()

# Run the main event loop
root.mainloop()