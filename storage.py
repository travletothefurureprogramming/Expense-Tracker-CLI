import json

FILE = "expenses.json"

def initialize_storage():
    try:
        with open(FILE):
            pass
    except:
        with open(FILE, "w"):
            pass


def save_expenses(expense):
    with open(FILE, "a") as f:
        json.dump(expense, f)

def load_expenses():
    with open(FILE) as f:
        data = json.load(f)

    return data

initialize_storage()