from pymongo import MongoClient
from convert_csv import *
import json


username = 'admin'
password = 'admin'
db_name = 'demo'
collection_name = 'demo'
HOST = f"mongodb+srv://{username}:{password}@info7275-group1.vfvn5.mongodb.net/<dbname>?retryWrites=true&w=majority"

client = MongoClient(HOST)
db = client[db_name]
collection_demo = db[collection_name]
# get the server information
server_info = client.server_info()
print(server_info)
print("\nserver info keys:", server_info.keys())

# get the MongoDB server version string
print("\nserver version:", server_info["version"])

# get the database_names from the MongoClient()
database_names = client.list_database_names()
print("\ndatabases:", database_names)

demo_filename = 'covid19-data-generator/generated-data/demo.csv'
distinationfile = './demo.json'

csv_to_json(demo_filename,'./demo.json')

with open(distinationfile) as file:
    file_data = json.load(file)
    print(file_data)

# Inserting the loaded data in the Collection 
# if JSON contains data more than one entry 
# insert_many is used else inser_one is used 
if isinstance(file_data, list): 
    collection_demo.insert_many(file_data)   
else: 
    collection_demo.insert_one(file_data) 

print("inserted!")

client.close()



