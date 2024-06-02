import tkinter as tk
from pymongo import MongoClient
from tkinter.font import Font
from PIL import Image, ImageTk

class TopRatedApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Top Rated App")
        self.root.attributes('-fullscreen', True)  # Make the window fullscreen
        #self.root.overrideredirect(True)  # Hide window manager decorations

        # Load background image
        background_image = Image.open("hosppital.jpg")
        resized_image = background_image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.ANTIALIAS)
        self.background_photo = ImageTk.PhotoImage(resized_image)
        self.background_label = tk.Label(root, image=self.background_photo)
        self.background_label.place(x=0, y=0)

        # Configure font
        self.bold_font = Font(family="Times", size=14, weight="bold")

        # Button to get top rated data
        self.button = tk.Button(root, text="KNOW THE TOP RATED", command=self.display_top_rated, font=self.bold_font)
        self.button.place(relx=0.5, rely=0.5, anchor="center")

        # Connect to MongoDB
        self.client = MongoClient('mongodb://localhost:27017')
        self.db = self.client['MEDINFRADB']
        self.collection = self.db['hosinfo']

    def display_top_rated(self):
        top_rated_data = self.get_top_rated_data()
        if top_rated_data:
            self.display_results(top_rated_data)
        else:
            messagebox.showinfo("No Data", "No top-rated data found.")

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

def main():
    root = tk.Tk()
    app = TopRatedApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()