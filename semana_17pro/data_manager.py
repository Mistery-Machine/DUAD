import json

DATA_FILE = "finances_data.json"

def load_data(): 
  try: 
    with open(DATA_FILE, "r") as file: 
      return json.load(file)
  except FileNotFoundError: 
    return {"categories": [], "transactions": []}

def save_data(data): 
  with open(DATA_FILE, "w")as file: 
    json.dump(data, file, indent=4)

def add_category(category): 
  data=load_data()
  if category not in data["categories"]: 
    data["categories"].append(category) 
    save_data(data)

def add_transaction(transaction_type, category, amount):
  data=load_data()
  data["transactions"].append({"type": transaction_type, "category": category, "amount": amount})
  save_data(data)