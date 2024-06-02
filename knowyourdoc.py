import tkinter as tk
from tkinter import font, Label, Entry, Button, Text
from pymongo import MongoClient

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

if __name__ == "__main__":
    app = DoctorSearchApp()
    app.mainloop()