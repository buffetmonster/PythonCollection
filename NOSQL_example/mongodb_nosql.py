#below didn't work but looks like it's because db not present?
#python3 -m pip install pymongo
#Mongodb - nosql
import pymongo

# Connect to the MongoDB database
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Create a database called "mydatabase"
db = client["mydatabase"]

# Create a collection called "mycollection"
collection = db["mycollection"]

# Insert a document into the collection
document = {
  "name": "John Doe",
  "age": 30,
  "city": "New York"
}
collection.insert_one(document)

# Get all documents in the collection
documents = collection.find()
for document in documents:
  print(document)

# Update a document in the collection
query = {"name": "John Doe"}
update = {"$set": {"age": 31}}
collection.update_one(query, update)

# Delete a document from the collection
query = {"city": "New York"}
collection.delete_many(query)