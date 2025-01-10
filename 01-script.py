from dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient

load_dotenv(find_dotenv())
username = os.getenv('MONGODB_USERNAME')
password = os.getenv('MONGODB_PWD')
cluster = os.getenv('MONGODB_CLUSTER')
authSource = os.getenv('MONGODB_AUTH_SOURCE', 'admin')
authMechanism = 'SCRAM-SHA-1'
connection_string = f"mongodb+srv://{username}:{password}@{cluster}/?authSource={authSource}&authMechanism={authMechanism}"

client = MongoClient(connection_string)
dbs = client.list_database_names()
test_db = client.test
collection = test_db.list_collection_names()
printer = pprint.PrettyPrinter()

def insert_test_doc():
  collection = test_db.test
  test_document = {
    "name": "Kivanc",
    "type": "test"
  }
  inserted_doc = collection.insert_one(test_document)
  print(inserted_doc)


production = client.production
person_collection = production.person_collection


def create_documents():
  first_names = ["Kiwi", "Jan", "Jennifer"]
  last_names = ["Gordu", "Bart", "Pit"]
  ages = [25, 30, 10]

  docs = []

  for first_name, last_name, age in zip(first_names, last_names, ages):
    doc = {"first_name": first_name, "last_name": last_name, "age": age}
    docs.append(doc)
  
  person_collection.insert_many(docs)

def find_all_people():
  people = person_collection.find()

  for person in people:
    printer.pprint(person)

def find_kiwi():
  kiwi = person_collection.find_one({"first_name": "Kiwi"})
  printer.pprint(kiwi)

def count_all_people():
  count = person_collection.count_documents(filter={})
  print(f"Number of People: {count}")

def get_person_by_id(person_id):
  from bson.objectid import ObjectId

  _id = ObjectId(person_id)
  person= person_collection.find_one({"_id": _id})
  printer.pprint(person)

def get_age_range(min_age, max_age):
  query = {"$and": [
      {"age": {"$gte": min_age}},
      {"age": {"$lte": max_age}}
    ]}

  filtered_people = person_collection.find(query).sort("age")

  for person in filtered_people:
    printer.pprint(person)

def project_columns():
  columns = {"_id":0, "first_name": 1, "last_name": 1}
  filtered_people = person_collection.find({}, columns)
  for person in filtered_people:
    printer.pprint(person)

def update_person_by_id(person_id):
  from bson.objectid import ObjectId
  _id = ObjectId(person_id)

  # all_updates = {
  #   "$set": {"new_field": True},
  #   "$inc": {"age": 1},
  #   "$rename": {"first_name": "first", "last_name": "last"}
  # }

  person_collection.update_one({"_id": _id}, {"$unset": {"new_field": ""}})

def replace_one(person_id):
  from bson.objectid import ObjectId
  _id = ObjectId(person_id)

  new_doc = {
    "first_name": "new first name",
    "last_name": "new last name",
    "age": 100
  }

  person_collection.replace_one({"_id": _id}, new_doc)

def delete_doc_by_id(person_id):
  from bson.objectid import ObjectId
  _id = ObjectId(person_id)
  person_collection.delete_one({"_id": _id})
