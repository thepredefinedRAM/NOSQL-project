from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017')

# Switch to or create a database
db = client['MEDINFRADB']
collection=db['Hospital info']
#collection=db['Hospital images']
#collection=db['customized info']
#collection=db['reccomended details']
#collection=db['Doctor info']
# Insert a document into a collection
data=collection.find({"State":"Tamilnadu","Hospital":"A A Hospital"})
for document in data:
    print(document)