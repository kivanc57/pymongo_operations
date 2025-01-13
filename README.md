
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

⚙️ **MongoDB Connection**: Make sure to configure your MongoDB connection in a `.env` file with the necessary credentials (e.g., `MONGODB_USERNAME`, `MONGODB_PASSWORD`, `MONGODB_CLUSTER`, `MONGODB_AUTH_SOURCE`).

⚙️ **MongoDB Atlas Setup**: If you are using MongoDB Atlas, ensure that your cluster is configured and accessible, and the relevant MongoDB Atlas Search index (`language_search`) is created.

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
