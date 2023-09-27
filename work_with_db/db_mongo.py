import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Create or select a database
db = client["mydatabase"]

# Create or select a collection (equivalent to a table in SQL)
collection = db["mycollection"]

# Function to add data to the collection
def add_data(name, age):
    data = {"name": name, "age": age}
    collection.insert_one(data)

# Function to retrieve data from the collection
def retrieve_data():
    return list(collection.find())

# Function to update data in the collection
def update_data(id, name, age):
    collection.update_one({"_id": id}, {"$set": {"name": name, "age": age}})

# Function to delete data from the collection
def delete_data(id):
    collection.delete_one({"_id": id})

# Usage examples
add_data("Alice", 30)
add_data("Bob", 25)

print("Initial data:")
print(retrieve_data())

update_data(retrieve_data()[0]["_id"], "Alice Johnson", 31)

print("Data after update:")
print(retrieve_data())

delete_data(retrieve_data()[1]["_id"])

print("Data after delete:")
print(retrieve_data())

# Close the MongoDB client
client.close()
