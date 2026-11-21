import csv
import json
from pathlib import Path

FILE = Path(__file__).parent / "expenses.json"


def initialize_storage():

    if not FILE.exists():
        with open(FILE, "w", encoding="utf-8") as f:
            json.dump([], f, indent=4)

    with open(FILE, "r", encoding="utf-8") as f:
        content = f.read()

    if not content.strip():
        with open(FILE, "w", encoding="utf-8") as f:
            json.dump([], f, indent=4)

def load_expenses():

    initialize_storage()

    try:
        with open(FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, list):
            raise ValueError("Invalid expenses data format.")

        return data

    except json.JSONDecodeError as error:
        raise ValueError("The expenses.json file contains invalid JSON.") from error


def save_expenses(expense):

    expenses = load_expenses()

    expenses.append(expense)

    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(expenses, f, indent=4, ensure_ascii=False)

def clear_file():
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump([], f, indent=4)

def save_all_expenses(expenses):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(expenses, f, indent=4, ensure_ascii=False)

def export_to_csv():
    
    with open(FILE) as jf:
        jd = json.load(jf)

    df = open("expenses.csv", 'w', newline='')
    cw = csv.writer(df)

    c = 0
    for data in jd:
        if c == 0:
            header = data.keys()
            cw.writerow(header)
            c += 1
        cw.writerow(data.values())

    df.close()

if __name__ == "__main__":
    initialize_storage()

    save_expenses({
        "id": 1,
        "amount": 15.50,
        "category": "Car"
    })

    print("Expense saved successfully!")
