import tkinter as tk
from tkinter import font, Entry, Button, Label, Text, Toplevel, messagebox
from PIL import Image, ImageTk
from pymongo import MongoClient

from toprateddisplay import TopRatedApp


class LoginPage(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Login Page")
        self.attributes("-fullscreen", True)  # Set fullscreen mode

        # Set background image
        img = Image.open("Hosppital.jpg")
        img = img.resize((self.winfo_screenwidth(), self.winfo_screenheight()), Image.ANTIALIAS)
        self.background_image = ImageTk.PhotoImage(img)
        background_label = tk.Label(self, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Styling for userid and password fields
        entry_style = {"background": "white", "foreground": "black", "font": ("Arial", 16)}

        # Label and entry for userid
        userid_label = tk.Label(self, text="Username:", bg="white", fg="black", font=("Helvetica", 20, "bold"))
        userid_label.place(relx=0.5, rely=0.4, anchor="center")
        self.username_entry = Entry(self, **entry_style)  # Corrected entry name
        self.username_entry.place(relx=0.5, rely=0.45, anchor="center")

        # Label and entry for password
        password_label = tk.Label(self, text="Password:", bg="white", fg="black", font=("Helvetica", 20, "bold"))
        password_label.place(relx=0.5, rely=0.5, anchor="center")
        self.password_entry = Entry(self, show="*", **entry_style)  # Corrected entry name
        self.password_entry.place(relx=0.5, rely=0.55, anchor="center")

        # Login button
        login_button = tk.Button(self, text="Login", command=self.login, bg="green", fg="white", font=("Helvetica", 16, "bold"))
        login_button.place(relx=0.5, rely=0.6, anchor="center")

    def login(self):
        username = self.username_entry.get()  # Corrected entry name
        password = self.password_entry.get()  # Corrected entry name

        # Authentication logic
        if username == "admin" and password == "password":
            messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
            self.destroy()  # Close the login window
            background_page = BackgroundPage()
            background_page.mainloop()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
import tkinter as tk
from tkinter import font, Entry, Button, Label, Text, Toplevel, messagebox
from PIL import Image, ImageTk
from pymongo import MongoClient

# DoctorSearchApp class
class DoctorSearchApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Doctor Search")
        self.geometry("600x400")

        # Set custom font
        label_font = font.Font(family="Arial", size=12)
        entry_font = font.Font(family="Arial", size=12)
        button_font = font.Font(family="Arial", size=12, weight="bold")

        # Hospital Name Entry
        self.hospital_name_label = Label(self, text="Hospital Name:", font=label_font)
        self.hospital_name_label.pack(anchor="center", pady=10)
        self.hospital_name_entry = Entry(self, font=entry_font)
        self.hospital_name_entry.pack(anchor="center", pady=10)

        # Department Entry
        self.department_label = Label(self, text="Department:", font=label_font)
        self.department_label.pack(anchor="center", pady=10)
        self.department_entry = Entry(self, font=entry_font)
        self.department_entry.pack(anchor="center", pady=10)

        # Experience Entry
        self.experience_label = Label(self, text="Experience (years):", font=label_font)
        self.experience_label.pack(anchor="center", pady=10)
        self.experience_entry = Entry(self, font=entry_font)
        self.experience_entry.pack(anchor="center", pady=10)

        # Search Button
        self.search_button = Button(self, text="Search", font=button_font, command=self.search_doctors)
        self.search_button.pack(anchor="center", pady=20)

        # Results Text Widget
        self.results_text = Text(self, font=entry_font, wrap=tk.WORD, height=10, width=60)
        self.results_text.pack(anchor="center", pady=10)

        # MongoDB connection
        self.client = MongoClient("mongodb://localhost:27017")
        self.db = self.client["MEDINFRADB"]
        self.collection = self.db["docinfo"]

    def search_doctors(self):
        # Clear previous results
        self.results_text.delete("1.0", tk.END)

        # Get values entered by the user
        hospital = self.hospital_name_entry.get()
        area_of_expertise = self.department_entry.get()  # Assuming "Department" corresponds to "Area of Expertise"

        # Check if Experience (years) is provided
        experience_text = self.experience_entry.get()
        if experience_text:
            experience = int(experience_text)
            # Define the query with experience
            query = {
                "Doctor_name": {"$exists": True},  # Ensuring the field exists, as it's used as a primary identifier
                "Hospital": hospital,
                "years_exp": {"$lte": experience},  # Assuming you want doctors with less or equal experience
                "Area_of_expertise": area_of_expertise
            }
        else:
            # Define the query without experience
            query = {
                "Doctor_name": {"$exists": True},  # Ensuring the field exists, as it's used as a primary identifier
                "Hospital": hospital,
                "Area_of_expertise": area_of_expertise
            }

        # Execute the query
        matching_doctors = self.collection.find(query)

        # Display the results in the text widget
        for doctor in matching_doctors:
            result_text = f"Doctor Name: {doctor['Doctor_name']}\nHospital: {doctor['Hospital']}\nExperience: {doctor['years_exp']} years\nArea of Expertise: {doctor['Area_of_expertise']}\n\n"
            self.results_text.insert(tk.END, result_text)
            

class BackgroundPage(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)
        


        self.title("MED-INFRA")
        self.attributes("-fullscreen", True)

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        img1 = Image.open("hosppital.jpg")
        img1 = img1.resize((screen_width, screen_height))
        self.img1 = ImageTk.PhotoImage(img1)
        label1 = Label(self, image=self.img1)
        label1.place(x=0, y=0)

        heading_font = font.Font(family="COPPERPLATE GOTHIC BOLD", size=56, weight="bold")
        self.button_font = font.Font(family="Roman", size=20)  # Button font as instance attribute
        
        heading_label = tk.Label(self, text="MED-INFRA", font=heading_font, fg="red", bg="white")
        heading_label.place(relx=0.5, rely=0.1, anchor="center")

        # Other buttons
        button1 = tk.Button(self, text="Location Based", font=self.button_font, fg="red", bg="white", command=self.redirect_to_search)
        button1.place(relx=0.5, rely=0.3, anchor="center")

        button2 = tk.Button(self, text="Customise", font=self.button_font, fg="red", bg="white", command=self.redirect_to_customise)
        button2.place(relx=0.5, rely=0.4, anchor="center")

        button3 = tk.Button(self, text="Top Rated", font=self.button_font,fg="red", bg="white", command=self.redirect_to_top_rated)
        button3.place(relx=0.5, rely=0.5, anchor="center")

        button4 = tk.Button(self, text="Help/Contact", command=self.show_contact_info, font=self.button_font, fg="red", bg="white")
        button4.place(relx=0.5, rely=0.6, anchor="center")

        button5 = tk.Button(self, text="Know Your Doctor", font=self.button_font, fg="red", bg="white",command=self.redirect_to_doctor_search)
        button5.place(relx=0.5, rely=0.7, anchor="center")


# Connect to MongoDB
        self.client = MongoClient('mongodb://localhost:27017')
        self.db = self.client['MEDINFRADB']
        self.collection = self.db['hosinfo']
    def get_top_rated_data(self):
        try:
            data = self.collection.find({"Ratings": {"$gt": 4}}).limit(20)
            top_rated_data = list(data)
            return top_rated_data
        except Exception as e:
            print("Error:", e)

    def display_results(self, top_rated_data):
        self.result_window = tk.Toplevel(self.root)
        self.result_window.title("Top Rated Results")
        self.result_window.configure(bg="blue")
        self.result_window.attributes('-fullscreen', True)  # Make the result window fullscreen
        #self.result_window.overrideredirect(True)  # Hide window manager decorations

        if not top_rated_data:
            tk.Label(self.result_window, text="No top-rated data found", bg="blue", fg="white").pack()
        else:
            for record in top_rated_data:
                hospital = record.get('Hospital', 'N/A')
                ratings = record.get('Ratings', 'N/A')
                tk.Label(self.result_window, text=f"Hospital: ", bg="blue", fg="white", font=self.bold_font).pack()
                tk.Label(self.result_window, text=hospital, bg="blue", fg="white", font=self.bold_font).pack()
                tk.Label(self.result_window, text=f"Ratings: ", bg="blue", fg="white", font=self.bold_font).pack()
                tk.Label(self.result_window, text=ratings, bg="blue", fg="white", font=self.bold_font).pack()
    def redirect_to_doctor_search(self):
        doctor_search_app = DoctorSearchApp()
        doctor_search_app.mainloop()  # Now use mainloop directly here

    def show_contact_info(self):
        contact_window = tk.Toplevel(self)
        contact_window.attributes("-fullscreen", True)
        contact_window.title("Contact Information")

        label_bg_color = "#87CEEB"  # Sky Blue
        
        name_label = tk.Label(contact_window, text="Name of the creators: MED-INFRA PVT", padx=20, pady=20, bg=label_bg_color)
        name_label.pack(anchor='w', fill='x')
        
        contact_label = tk.Label(contact_window, text="Contact : 99999999999", padx=20, pady=20, bg=label_bg_color)
        contact_label.pack(anchor='w', fill='x')

        email_label = tk.Label(contact_window, text="Email: medinfrahelp@medinfra.com", padx=20, pady=20, bg=label_bg_color)
        email_label.pack(anchor='w', fill='x')

        address_label = tk.Label(contact_window, text="ABC County west coast 68989", padx=20, pady=20, bg=label_bg_color)
        address_label.pack(anchor='w', fill='x')

        # Back button
        back_button = tk.Button(contact_window, text="Back", command=contact_window.destroy, font=self.button_font, fg="red", bg="white")
        back_button.pack()

    def redirect_to_search(self):
        search_app = SearchApp(self)
        search_app.mainloop()  # Now use mainloop directly here

    def redirect_to_customise(self):
        customise_app = CustomisePage(self)
        customise_app.mainloop()  # Now use mainloop directly here

    def redirect_to_top_rated(self):
            try:
                top_rated_app = TopRatedApp(self)
                top_rated_app.mainloop()
            except Exception as ee:
                messagebox.showerror("Error",str(e))

class SearchApp(tk.Toplevel):  # Inherit from tk.Toplevel instead of tk.Tk
    def __init__(self, root):
        self.root = root
        tk.Toplevel.__init__(self, self.root)  # Initialize as a Toplevel window
        self.title("Search App")
        
        self.search_label = tk.Label(self, text="Enter Location:")
        self.search_label.pack()
        
        self.search_entry = tk.Entry(self, width=30)
        self.search_entry.pack()
        
        self.search_button = tk.Button(self, text="Search", command=self.search)
        self.search_button.pack()
        
        self.result_label = tk.Label(self, text="")
        self.result_label.pack()
        
        # Connecting to MongoDB
        self.client = MongoClient("mongodb://localhost:27017")
        self.db = self.client['MEDINFRADB']
        self.collection = self.db['hosinfo']
        
        # Add a text widget to display search results
        self.result_text = tk.Text(self, height=10, width=50)
        self.result_text.pack()

    def search(self):
        # Retrieving data from MongoDB based on search criteria
        search_query = self.search_entry.get()
        try:
            collection_name = "hosinfo"
            collection = getattr(self.db, collection_name)
            data = collection.find({"City":"Chennai"})
        
            # Clear previous search results
            self.result_label.config(text="Search Results:")
            self.result_text.delete(1.0, tk.END)
            
            # Displaying search results
            count = 0
            for document in data:
                self.result_text.insert(tk.END, str(document) + "\n")
                count += 1

            # Check if any data is retrieved
            if count == 0:
                self.result_text.insert(tk.END, "No matching documents found.")
        except Exception as e:
            self.result_text.insert(tk.END, "Error: " + str(e))

    def go_back(self):
        self.root.destroy()  # Close the current window
        self.root.parent.deiconify()  # Show the parent window

class CustomisePage(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.parent = parent
        self.title("Customise Page")
        self.attributes("-fullscreen", True)

        label_font = ('Helvetica', 12)
        entry_font = ('Helvetica', 12)

        tk.Label(self, text="Name:", font=label_font, bg='dark blue', fg='white').pack()
        self.name_entry = tk.Entry(self, font=entry_font)
        self.name_entry.pack(pady=5)

        tk.Label(self, text="Age:", font=label_font, bg='dark blue', fg='white').pack()
        self.age_entry = tk.Entry(self, font=entry_font)
        self.age_entry.pack(pady=5)

        tk.Label(self, text="Case:", font=label_font, bg='dark blue', fg='white').pack()
        self.case_entry = tk.Entry(self, font=entry_font)
        self.case_entry.pack(pady=5)

        tk.Label(self, text="Condition:", font=label_font, bg='dark blue', fg='white').pack()
        self.condition_entry = tk.Entry(self, font=entry_font)
        self.condition_entry.pack(pady=5)

        tk.Label(self, text="Location:", font=label_font, bg='dark blue', fg='white').pack()
        self.location_entry = tk.Entry(self, font=entry_font)
        self.location_entry.pack(pady=5)

        submit_button = tk.Button(self, text="Submit", font=label_font, command=self.submit_form, bg='white', fg='dark blue')
        submit_button.pack(pady=10)

        self.result_label = tk.Label(self, text="", font=label_font, bg='dark blue', fg='white')
        self.result_label.pack()

        back_button = tk.Button(self, text="Back", font=label_font, command=self.go_back, bg='white', fg='dark blue')
        back_button.pack(pady=10)

    def submit_form(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        case = self.case_entry.get()
        condition = self.condition_entry.get()
        location = self.location_entry.get()
        
        # Connect to MongoDB
        client = MongoClient('mongodb://localhost:27017')
        db = client['MEDINFRADB']
        
        # Query Hospital info collection based on user inputs
        hospital_collection = db['hosinfo']
        # Construct query based on location and case matching criteria
        query = {
            'State': location,  # Assuming 'State' field stores location information
            'Department': case  # Assuming 'Department' field stores department information
        }
        hospital_info = hospital_collection.find_one(query)
        
        if hospital_info:
            self.result_label.config(text="Hospital Information:\nName: {}\nState: {}\nCity: {}\nLocal Address: {}\nDepartment: {}\nRatings: {}".format(
                hospital_info.get('Hospital'), hospital_info.get('State'), hospital_info.get('City'), 
                hospital_info.get('LocalAddress'), hospital_info.get('Department'), hospital_info.get('Ratings')))
        else:
            self.result_label.config(text="No hospital found for the given criteria.")
        
        # Clear the form fields
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.case_entry.delete(0, tk.END)
        self.condition_entry.delete(0, tk.END)
        self.location_entry.delete(0, tk.END)
        
        print("Form submitted successfully.")

    def go_back(self):
        self.destroy()  # Close the current window
        self.parent.deiconify()  # Show the parent window

if __name__ == "__main__":
    login_page = LoginPage()
    login_page.mainloop()