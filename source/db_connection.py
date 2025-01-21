import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def check_connection(uri):
  client = MongoClient(uri)
  try:
    client.admin.command('ping')
    print(f"Connection to MongoDB is succesful!")
    return client
  except Exception as e:
    print(f"Connection to MongoDB failed: {e}")
    return None

def get_client():
  try:
    # Load environmental variables
    username = os.getenv('MONGODB_USERNAME')
    password = os.getenv('MONGODB_PWD')
    cluster = os.getenv('MONGODB_CLUSTER')
    authSource = os.getenv('MONGODB_AUTH_SOURCE', 'admin')
    authMechanism = "SCRAM-SHA-1"
  except Exception as e:
    print(f"Fetching environment variables failed: {e}")
    return None

  # Establish the uri
  try:
    uri = f"mongodb+srv://{username}:{password}@{cluster}/?authSource={authSource}&authMechanism={authMechanism}"
    return check_connection(uri)
  except Exception as e:
    print(f"Building URI or connection failed: {e}")
    return None

def main():
  client = get_client()
  if client:
    print("You can now interact with MongoDB!")
  else:
    print("Fail. Please try again...")

if __name__ == '__main__':
  main()
