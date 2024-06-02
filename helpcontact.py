import tkinter as tk

def show_contact_info():
    # Create a new window for contact information
    contact_window = tk.Toplevel()
    contact_window.title("Contact Information")

    # Define background colors
    name_bg_color = "#87CEEB"  # Sky Blue
    contact_bg_color = "#87CEEB"
    email_bg_color = "#FFE4C4"

    # Create labels for name and address with background colors
    name_label = tk.Label(contact_window, text="Name of the creators: MED-INFRA PVT", padx=20, pady=20, bg=name_bg_color)
    name_label.pack(anchor='w', fill='x')

    address_label = tk.Label(contact_window, text="Address: 123 Main St, City, Country", padx=20, pady=20, bg=contact_bg_color)
    address_label.pack(anchor='w', fill='x')

    contact_label = tk.Label(contact_window, text="Contact : 99999999999", padx=20, pady=20, bg=contact_bg_color)
    contact_label.pack(anchor='w', fill='x')

    email_label = tk.Label(contact_window, text="Email: 123 Main St, City, Country", padx=20, pady=20, bg=email_bg_color)
    email_label.pack(anchor='w', fill='x')

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Main Application")

    # Create a button to trigger the show_contact_info function
    button = tk.Button(root, text="Show Contact Info", command=show_contact_info)
    button.pack()

    root.mainloop()