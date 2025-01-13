import json
import pprint

def insert_json_data(path, collection):
  with open(path, 'r') as file:
    data = json.load(file)
    result = collection.insert_many(data)
  print('Inserted document amount: ', len(result.inserted_ids))
  print('Inserted document IDs:', result.inserted_ids)

def get_printer():
  return pprint.PrettyPrinter()
