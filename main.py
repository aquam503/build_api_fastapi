from fastapi import FastAPI, HTTPException
import pandas as pd

app = FastAPI()
CSV_FILE = "data.csv"

def read_csv():
    return pd.read_csv(CSV_FILE)

def write_csv(df):
    df.to_csv(CSV_FILE, index=False)

@app.get("/items")
def get_items():
    """Fetch all items from the CSV file."""
    df = read_csv()
    return df.to_dict(orient="records")

@app.get("/items/{item_id}")
def get_item(item_id: int):
    """Fetch a specific item by ID."""
    df = read_csv()
    item = df[df["id"] == item_id]
    if item.empty:
        raise HTTPException(status_code=404, detail="Item not found")
    return item.to_dict(orient="records")[0]

@app.post("/items")
def create_item(id: int, name: str, price: float):
    """Add a new item to the CSV file."""
    df = read_csv()
    if id in df["id"].values:
        raise HTTPException(status_code=400, detail="Item with this ID already exists")
    new_item = pd.DataFrame([{"id": id, "name": name, "price": price}])
    df = pd.concat([df, new_item], ignore_index=True)
    write_csv(df)
    return {"message": "Item created successfully"}

@app.put("/items/{item_id}")
def update_item(item_id: int, name: str = None, price: float = None):
    """Update an existing item in the CSV file."""
    df = read_csv()
    if item_id not in df["id"].values:
        raise HTTPException(status_code=404, detail="Item not found")
    if name:
        df.loc[df["id"] == item_id, "name"] = name
    if price is not None:
        df.loc[df["id"] == item_id, "price"] = price
    write_csv(df)
    return {"message": "Item updated successfully"}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    """Delete an item from the CSV file."""
    df = read_csv()
    if item_id not in df["id"].values:
        raise HTTPException(status_code=404, detail="Item not found")
    df = df[df["id"] != item_id]
    write_csv(df)
    return {"message": "Item deleted successfully"}