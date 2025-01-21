# FastAPI CSV CRUD Application

This repository contains a simple FastAPI application that demonstrates how to perform CRUD (Create, Read, Update, Delete) operations on a CSV file. The application allows you to interact with a CSV file (`data.csv`) through RESTful API endpoints.

## Features

- **GET**: Fetch all items or a specific item by ID.
- **POST**: Add a new item to the CSV file.
- **PUT**: Update an existing item in the CSV file.
- **DELETE**: Remove an item from the CSV file.

## Prerequisites

- Python 3.7+
- FastAPI
- Uvicorn
- Pandas

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/fastapi-csv-crud.git
   cd fastapi-csv-crud
   ```

2. Install the required dependencies:
   ```bash
   pip install fastapi uvicorn pandas
   ```


## Running the Application

1. Start the application using Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```

2. Open your browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation.

## Endpoints

### 1. Fetch All Items
**GET** `/items`
- Description: Retrieve all items from the CSV file.
- Example Response:
  ```json
  [
    {"id": 1, "name": "Apple", "price": 1.0},
    {"id": 2, "name": "Banana", "price": 0.5},
    {"id": 3, "name": "Cherry", "price": 2.0}
  ]
  ```

### 2. Fetch an Item by ID
**GET** `/items/{item_id}`
- Description: Retrieve a specific item by its ID.
- Example Response:
  ```json
  {"id": 1, "name": "Apple", "price": 1.0}
  ```

### 3. Add a New Item
**POST** `/items`
- Description: Add a new item to the CSV file.
- Request Parameters:
  - `id` (int): Item ID.
  - `name` (str): Item name.
  - `price` (float): Item price.
- Example Request:
  ```json
  {
    "id": 4,
    "name": "Orange",
    "price": 1.5
  }
  ```
- Example Response:
  ```json
  {"message": "Item created successfully"}
  ```

### 4. Update an Existing Item
**PUT** `/items/{item_id}`
- Description: Update the details of an existing item.
- Request Parameters:
  - `name` (str, optional): New name.
  - `price` (float, optional): New price.
- Example Request:
  ```json
  {
    "name": "Green Apple",
    "price": 1.2
  }
  ```
- Example Response:
  ```json
  {"message": "Item updated successfully"}
  ```

### 5. Delete an Item
**DELETE** `/items/{item_id}`
- Description: Remove an item by its ID.
- Example Response:
  ```json
  {"message": "Item deleted successfully"}
  ```

## Project Structure

```
fastapi-csv-crud/
├── main.py        # FastAPI application code
├── data.csv       # CSV file storing items
└── README.md      # Project documentation
```

## Security Best Practices
- Always validate user input using Pydantic models.
- Use HTTPS in production to secure data transmission.
- Implement authentication and authorization for sensitive endpoints.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
