#wsl IPADDR: 172.29.183.247
#Currant Bun
#ipaddress: https://cloud.mongodb.com/v2/65901f371e987c37dbe69f44#/security/network/accessList
#users:     https://cloud.mongodb.com/v2/65901f371e987c37dbe69f44#/security/database/users
def create_documents():
    #from pymongo import MongoClient

    # Initialize MongoDB client and database
    #client = MongoClient("your_mongodb_uri")
    #test_db = client["test-db"]

    first_names = ["Tim", "Sarah", "Jennifer", "Jose", "Brad", "Allen", "Dave"]
    last_names = ["Ruscica", "Smith", "Bart", "Cater", "Pit", "Geral", "Smith"]
    ages = [21, 40, 23, 19, 34, 67, 52]

    for i, (first_name, last_name, age) in enumerate(zip(first_names, last_names, ages)):
        # Create the document
        doc = {"_id": i, "first_name": first_name, "last_name": last_name, "age": age}

        # Update the document (upsert if none exists)
        result = test_db["test_collection"].update_one({"_id": i}, {"$set": doc}, upsert=True)

        if result.matched_count == 1:
            updated_doc = test_db["test_collection"].find_one({"_id": doc['_id']})
            print(f"Document updated with id: {updated_doc['_id']}")
        elif result.upserted_id:
            print("Document inserted successfully with id:", result.upserted_id)
        else:
            print(f"An error occurred: {result}")

import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Get username and password from environment variables
username = os.getenv("MONGO_USERNAME")
password = os.getenv("MONGO_PASSWORD")
uri = f"mongodb+srv://{username}:{password}@cluster0.8r76d5y.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"


# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    print("Ping failed, exit now")
    exit()
dbs = client.list_database_names()
print("From here we can identify the database name is test-db (verify):", dbs)
#test_db = client.test
test_db = client["test-db"]
collection_names = test_db.list_collection_names()
#we have 2 collections in the db: test-collection-2, test-collection
for collection_name in collection_names:
    print(f"The collection Name: {collection_name}")

create_documents()

for collection_name in collection_names:
  print(f"\nCollection: {collection_name}")
  # Get the collection object
  collection = client["test-db"][collection_name]
  
  # Find all documents in the collection
  for document in collection.find():
    # Print each document on a new line
    print(document)

# Get the test_db collection object
test_collection = client["test_db"]["test_collection-2"]

collection_names = test_db.list_collection_names()
print(f"Collections in test_db: {collection_names}")

exit()
#EXIT HERE OR DELETE AS BELOW

collection_to_delete = test_db["test-collection"]  # Assuming this is the one you don't need
# Delete the collection
collection_to_delete.drop()

# Verify the changes using list_collection_names
collection_names = test_db.list_collection_names()
print(f"Collections in test_db: {collection_names}")
