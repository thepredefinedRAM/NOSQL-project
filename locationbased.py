import tkinter as tk
from pymongo import MongoClient

class SearchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Search App")
        
        self.search_label = tk.Label(root, text="Enter Location:")
        self.search_label.pack()
        
        self.search_entry = tk.Entry(root, width=30)
        self.search_entry.pack()
        
        self.search_button = tk.Button(root, text="Search", command=self.search)
        self.search_button.pack()
        
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()
        
        # Connecting to MongoDB
        self.client = MongoClient("mongodb://localhost:27017")
        self.db = self.client['MEDINFRADB']
        self.collection = self.db['Hospital info']
        
        # Add a text widget to display search results
        self.result_text = tk.Text(root, height=10, width=50)
        self.result_text.pack()

    def search(self):
        # Retrieving data from MongoDB based on search criteria
        search_query = self.search_entry.get()
        try:
            collection_name = "Hospital info"
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

def main():
    root = tk.Tk()
    app = SearchApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()