
# MongoDB Operations 🥭

This project provides a series of Jupyter Notebooks that cover various aspects of **MongoDB** operations, including *CRUD* operations, data modeling, and data processing using `pymongo`, `pandas`, and `pyarrow'.

It also includes MongoDB Atlas Search capabilities such as *fuzzy search*, *synonym matching*, *autocomplete*, *relevence ranking* and other methods.

⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

## Table of Contents
- [📦 Features](#features)
- [📑 Notebooks](#notebooks)
- [🛠️ Setup](#setup)
- [🏃 How to Run](#how-to-run)
- [📜 License](#license)
- [📬 Contact](#contact)

⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

## Features <a id="features"></a>

📦 **CRUD Operations**: Learn how to interact with MongoDB collections and perform basic CRUD operations.

📦 **Data Modeling**: Implement schema validation, use PyArrow for efficient data manipulation, and explore MongoDB as a document store.

📦 **Atlas Search**: Understand how to use MongoDB's powerful Atlas Search features, including fuzzy matching, synonym matching, and autocomplete.

⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

## Notebooks <a id="notebooks"></a>

### 📑 `crud.ipynb` 
This notebook demonstrates how to connect to MongoDB and perform **Create, Read, Update, and Delete (CRUD)** operations. It also showcases how to set up collections and handle data insertion.

### 📑 `data_modeling.ipynb`
This notebook focuses on data modeling techniques using MongoDB. It includes defining schemas with validation, working with data in MongoDB, and storing data efficiently. It also demonstrates the use of **Pandas** and **PyArrow** for more efficient handling of large datasets.

### 📑 `match.ipynb`
This notebook explores **MongoDB Atlas Search** capabilities, including:
- **Fuzzy Search**: Flexible text search with support for minor typos.
- **Synonym Search**: Searching with synonyms using a predefined synonyms mapping.
- **Autocomplete**: Efficient search for partial input using the autocomplete feature.
- **Relevence Ranking**: A crucial method to rank the findings based on their relevency.

### 📑 `arrow.ipynb`
This notebook demonstrates how to use **PyArrow** with MongoDB, particularly for efficient data processing and storage using the **pymongoarrow** library. It shows how to read and write data using Arrow format, convert between **NumPy** arrays and MongoDB, and perform various operations on data stored in MongoDB.

⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

## Setup <a id="setup"></a>

### Prerequisites

🛠 **MongoDB**: You need a MongoDB instance (locally or using MongoDB Atlas) for storing and querying data.

🛠 **Python**: This project is compatible with Python 3.x.

🛠 **Required Libraries**:
  - `pymongo`: MongoDB driver for Python
  - `pandas`: Data manipulation and analysis
  - `pyarrow`: Efficient data serialization for large datasets
  - `pymongoarrow`: Extends PyMongo for better performance with Arrow and NumPy
  - `dotenv`: Manage environment variables securely

You can install the required libraries using the following command:
```bash
pip install pymongo pandas pyarrow pymongoarrow python-dotenv
```

### Configuration

⚙️ **MongoDB Connection**:  
Ensure your MongoDB connection is properly configured in a `.env` file. This file should contain the necessary environment variables for your connection, such as:
- `MONGODB_USERNAME`: Your MongoDB username.
- `MONGODB_PASSWORD`: Your MongoDB password.
- `MONGODB_CLUSTER`: The MongoDB cluster URL (for example, `cluster0.mongodb.net`).
- `MONGODB_AUTH_SOURCE`: The authentication source, typically `admin` unless otherwise specified.

The connection setup in this project uses **`dotenv`** to load the environment variables from the `.env` file. The **`get_client()`** function from the `db_connection.py` file fetches these variables and establishes a connection to MongoDB.

```python
def get_client():
  try:
    # Load environmental variables
    load_dotenv(find_dotenv())
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
```

⚙️ **MongoDB Atlas Search** index (`language_search`) is created and indexed for the appropriate fields, such as `category` or `question`. The `aggregate()` function in the `utils.py` file can be used to query the database using this index and perform various search operations such as fuzzy matching, synonym matching, and autocomplete.

```python
def aggregate(collection, pipeline, printer):
    result = collection.aggregate(pipeline)
    printer.pprint(list(result))
```


⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

## How to Run <a id="how-to-run"></a>

🏃 Clone the repository:

   ```bash
   git clone https://github.com/kivanc57/mongodb_operations.git
   cd mongodb-project
   ```

🏃 Open the Jupyter notebooks:

   ```bash
   jupyter notebook
   ```

🏃 Navigate to the relevant notebook and run the cells sequentially and start your journey!

⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

## 📜 License <a id="license"></a>
This project is licensed under the GNU GENERAL PUBLIC LICENSE - see the [LICENSE](https://github.com/kivanc57/pymongo_operations/blob/main/LICENSE) file for details.

⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

## 📬 Contact <a id="contact"></a>

For any inquiries or contributions, please feel free to reach out.
- **GitHub Profile**: [kivanc57](https://github.com/kivanc57)
- **Email**: [kivancgordu@hotmail.com](mailto:kivancgordu@hotmail.com)
