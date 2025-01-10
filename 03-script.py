from dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient
import json
from pprint import PrettyPrinter

load_dotenv(find_dotenv())
username = os.getenv('MONGODB_USERNAME')
password = os.getenv('MONGODB_PWD')
cluster = os.getenv('MONGODB_CLUSTER')
authSource = os.getenv('MONGODB_AUTH_SOURCE', 'admin')
authMechanism = 'SCRAM-SHA-1'
connection_string = f"mongodb+srv://{username}:{password}@{cluster}/?authSource={authSource}&authMechanism={authMechanism}"

client = MongoClient(connection_string)
db = client.random_db
question = db.random_collectio
printer = PrettyPrinter()


def get_fuzzy_match():
  result = question.aggregate([
    {
      "$search": {
        "index": "language_search",
        "text": {
          "query": "technology",
          "path": "category",
          "fuzzy": {}   # Fuzzy search for flexible search - (optional)
        }
      }
    }
  ])
  printer.pprint(list(result))


def get_synonym_match():
  result = question.aggregate([
    {
      "$search": {
        "index": "language_search",
        "text": {
          "query": "Python",
          "path": "category",
          "synonyms": "synonyms_mapping"
        }
      }
    }
  ])
  printer.pprint(list(result))


def get_autocomplete():
  result = question.aggregate([
      {
          "$search": {
              "index": "language_search",
              "autocomplete": {
                  "query": "What does ",
                  "path": "question",
                  "tokenOrder": "sequential",
                  "fuzzy": {}
              }
          }
      },
      {
          "$project": {
              "_id": 0,
              "question": 1
          }
      }
  ])
  printer.pprint(list(result))


def get_compound_queries():
    result = question.aggregate([
        {
            "$search": {
                "index": "language_search",
                "compound": {
                    "must": [
                        {
                            "text": {
                                "query": ["Geography", "Physics", "Biology", "Chemistry"],
                                "path": "category"
                            }
                        }
                    ],
                    "mustNot": [
                        {
                            "text": {
                                "query": ["Python", "Databases"],
                                "path": "category"
                            }
                        }
                    ],
                    "should": [
                        {
                            "text": {
                                "query": "Technology",
                                "path": "answer"
                            }
                        }
                    ]
                }
            }
        },
        {
            "$project": {
                "question": 1,
                "answer": 1,
                "category": 1,
                "score": { "$meta": "searchScore" }
            }
        }
    ])
    printer.pprint(list(result))


def get_relevance():
    result = question.aggregate([
        {
            "$search": {
                "index": "language_search",
                "compound": {
                    "must": [
                        {
                            "text": {
                                "query": "Geography",
                                "path": "category"
                            }
                        }
                    ],
                    "should": [
                        {
                            "text": {
                                "query": "capital",
                                "path": "question",
                                "score": { "boost": { "value": 3.0 } }
                            }
                        }
                    ]
                }
            }
        },
        {
            "$project": {
                "question": 1,
                "answer": 1,
                "category": 1,
                "round": 1,
                "score": { "$meta": "searchScore" }
            }
        }
    ])
    printer.pprint(list(result))
