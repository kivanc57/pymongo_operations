import json
import pprint

def get_printer():
  return pprint.PrettyPrinter()

def aggregate(collection, pipeline, printer):
  result = collection.aggregate(pipeline)
  printer.pprint(list(result))

def read_json_data(path):
  try:
    with open(path, 'r') as file:
      return json.load(file)
  except Exception as e:
    print(f"Failed reading '{path}': {e}")

def insert_json_data(collection, path):
  try:
      data = read_json_data(path)
      result = collection.insert_many(data)
      print('Inserted document amount: ', len(result.inserted_ids))
      print('Inserted document IDs:', result.inserted_ids)
  except Exception as e:
    print(f"Failed inserting '{path}': {e}")
