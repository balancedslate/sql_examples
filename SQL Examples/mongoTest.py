import pymongo

# Connect to the MongoDB server
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Choose a database and collection
db = client["database_name"]
collection = db["collection_name"]

# Insert a document
document = {"name": "John", "age": 30}
collection.insert_one(document)

# Find all documents
documents = collection.find()

# Iterate over the documents
for document in documents:
    print(document)

# Close the connection
client.close()
