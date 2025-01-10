import os
import pprint
from datetime import datetime as dt
from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient

import pyarrow
from pymongoarrow.api import Schema
from pymongoarrow.monkey import patch_all
import pymongoarrow as pma
from bson import ObjectId

load_dotenv(find_dotenv())
username = os.getenv('MONGODB_USERNAME')
password = os.getenv('MONGODB_PWD')
cluster = os.getenv('MONGODB_CLUSTER')
authSource = os.getenv('MONGODB_AUTH_SOURCE', 'admin')
authMechanism = 'SCRAM-SHA-1'
connection_string = f"mongodb+srv://{username}:{password}@{cluster}/?authSource={authSource}&authMechanism={authMechanism}"

client = MongoClient(connection_string)
dbs = client.list_database_names()
production = client.production
printer = pprint.PrettyPrinter()


def create_book_collection():
  book_validator = {
      "$jsonSchema": {
        "bsonType": "object",
        "required": ["title", "authors", "publish_date", "type", "copies"],
        "properties": {
          "title": {
            "bsonType": "string",
            "description": "Title must be a string and is required."
          },
          "authors": {
            "bsonType": "array",
            "items": {
              "bsonType": "objectId",
              "description": "Each author must be a string."
            },
            "description": "Authors must be an array of strings and is required."
          },
          "publish_date": {
            "bsonType": "date",
            "description": "Publish date must be a valid date and is required."
          },
          "type": {
            "enum": ["Fiction", "Non-Fiction"],
            "description": "Type must be one of 'book', 'magazine', 'journal', or 'ebook'."
          },
          "copies": {
            "bsonType": "int",
            "minimum": 0,
            "description": "Copies must be a non-negative integer and is required."
          }
        }
      }
    }

  try:
    production.create_collection("book")
  except Exception as e:
    print(e)

  production.command("collMod", "book", validator=book_validator)

def create_author_collection():
  author_validator = {
      "$jsonSchema": {
        "bsonType": "object",
        "required": ["first_name", "last_name", "date_of_birth"],
        "properties": {
          "first_name": {
            "bsonType": "string",
            "description": "First name must be a string and is required."
          },
          "last_name": {
            "bsonType": "string",
            "description": "Last name must be a string and is required."
          },
          "date_of_birth": {
            "bsonType": "date",
            "description": "Date of birth must be a valid date and is required."
          }
        }
      }
    }
  
  try:
    production.create_collection('author')
  except Exception as e:
    print(e)
  
  production.command("collMod", "author", validator=author_validator)


def create_data():
  author_data = [
    {
      "first_name": "Alice",
      "last_name": "Johnson",
      "date_of_birth": dt(1980, 4, 12)
    },
    {
      "first_name": "Bob",
      "last_name": "Smith",
      "date_of_birth": dt(1975, 8, 25)
    },
    {
      "first_name": "Catherine",
      "last_name": "Williams",
      "date_of_birth": dt(1988, 11, 15)
    },
    {
      "first_name": "David",
      "last_name": "Brown",
      "date_of_birth": dt(1990, 3, 10)
    },
    {
      "first_name": "Emma",
      "last_name": "Jones",
      "date_of_birth": dt(1995, 7, 19)
    },
    {
      "first_name": "Frank",
      "last_name": "Garcia",
      "date_of_birth": dt(1983, 2, 5)
    },
    {
      "first_name": "Grace",
      "last_name": "Martinez",
      "date_of_birth": dt(1992, 6, 30)
    },
    {
      "first_name": "Henry",
      "last_name": "Lopez",
      "date_of_birth": dt(1985, 12, 21)
    },
    {
      "first_name": "Isabella",
      "last_name": "Clark",
      "date_of_birth": dt(1997, 1, 14)
    },
    {
      "first_name": "Jack",
      "last_name": "Lewis",
      "date_of_birth": dt(1983, 9, 2)
    }
  ]

  authors = production.author.insert_many(author_data).inserted_ids

  book_data = [
      {
          "title": "Introduction to Data Science",
          "authors": [authors[0]],
          "publish_date": dt(2018, 5, 12),
          "type": "Non-Fiction",
          "copies": 5
      },
      {
          "title": "Advanced Machine Learning",
          "authors": [authors[1]],
          "publish_date": dt(2020, 8, 25),
          "type": "Non-Fiction",
          "copies": 10
      },
      {
          "title": "The AI Detective",
          "authors": [authors[2], authors[3]],
          "publish_date": dt(2021, 11, 15),
          "type": "Fiction",
          "copies": 8
      },
      {
          "title": "Python for Data Science",
          "authors": [authors[0], authors[4]],
          "publish_date": dt(2019, 7, 19),
          "type": "Non-Fiction",
          "copies": 15
      },
      {
          "title": "The Code Chronicles",
          "authors": [authors[5]],
          "publish_date": dt(2022, 2, 5),
          "type": "Fiction",
          "copies": 12
      },
      {
          "title": "Data-Driven World",
          "authors": [authors[6]],
          "publish_date": dt(2020, 6, 15),
          "type": "Non-Fiction",
          "copies": 7
      },
      {
          "title": "Tales from the Cloud",
          "authors": [authors[7], authors[8]],
          "publish_date": dt(2021, 12, 1),
          "type": "Fiction",
          "copies": 9
      },
      {
          "title": "AI Ethics",
          "authors": [authors[9]],
          "publish_date": dt(2022, 1, 14),
          "type": "Non-Fiction",
          "copies": 6
      },
      {
          "title": "Exploring the Future",
          "authors": [authors[3], authors[4]],
          "publish_date": dt(2023, 3, 22),
          "type": "Non-Fiction",
          "copies": 11
      },
      {
          "title": "Virtual Realities",
          "authors": [authors[0], authors[2]],
          "publish_date": dt(2022, 5, 9),
          "type": "Fiction",
          "copies": 4
      }
  ]

  production.book.insert_many(book_data).inserted_ids


# books_containing_a = production.book.find({'title': {'$regex': 'a{1}'}})
# printer.pprint(list(books_containing_a))

# authors_and_books = production.author.aggregate([
#   {
#   "$lookup": {
#     "from": "book",
#     "localField": "_id",
#     "foreignField": "authors",
#     "as": "books"
#   }
# }
# ])
# printer.pprint(list(authors_and_books))


# authors_book_count = production.author.aggregate([
#     {
#         "$lookup": {
#             "from": "book",
#             "localField": "_id",
#             "foreignField": "authors",
#             "as": "books"
#         }
#     },
#     {
#         "$addFields": {
#             "total_books": {"$size": "$books"}
#         }
#     },
#     {
#         "$project": {
#             "first_name": 1,
#             "last_name": 1,
#             "total_books": 1,
#             "_id": 0
#         }
#     }
# ])
# printer.pprint(list(authors_book_count))

# authors_book_count = production.author.aggregate([
#     {
#         "$lookup": {
#             "from": "book",
#             "localField": "_id",
#             "foreignField": "authors",
#             "as": "books"
#         }
#     },
#     {
#         "$addFields": {
#             "total_books": {"$size": "$books"}
#         }
#     },
#     {
#         "$project": {
#             "first_name": 1,
#             "last_name": 1,
#             "total_books": 1,
#             "_id": 0
#         }
#     }
# ])
# printer.pprint(list(authors_book_count))

# books_with_old_authors = production.book.aggregate([
#   {
#     "$lookup": {
#       "from": "author",
#       "localField": "authors",
#       "foreignField": "_id",
#       "as": "authors"
#     },
#   },
#   {
#     "$set": {
#       "authors": {
#         "$map": {
#           "input": "$authors",
#           "in": {
#             "age": {
#               "$dateDiff": {
#                 "startDate": "$$this.date_of_birth",
#                 "endDate": "$$NOW",
#                 "unit": "year"
#               }
#             },
#             "first_name": "$$this.first_name",
#             "last_name": "$$this.last_name",
#           }
#         }
#       }
#     }
#   },
#   {
#     "$match": {
#       "$and": [
#         {"authors.age": {"$gte":50}},
#         {"authors.age": {"$lte":150}},
#       ]
#     }
#   },
#   {
#     "$sort": {
#       "age":1
#     }
#   }
# ])
# printer.pprint(list(books_with_old_authors))

#--------------------------------------------------------------

patch_all()

schema_author = Schema({"_id": ObjectId,
                 "first_name": pyarrow.string(),
                 "last_name": pyarrow.string(),
                 "date_of_birth": dt})

df = production.author.find_pandas_all({},schema=schema_author)
arrow_table = production.author.find_arrow_all({}, schema=schema_author)
ndarrays = production.author.find_numpy_all({}, schema=schema_author)
print(ndarrays)
