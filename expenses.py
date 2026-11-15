import math
import storage


def add_expense(amount: float, category: str, description: str | None = None):
    if isinstance(amount, bool) or not isinstance(amount, (int, float)):
        raise ValueError("Amount must be a valid number.")

    if not math.isfinite(amount) or amount <= 0:
        raise ValueError("Amount must be greater than 0.")

    if not isinstance(category, str) or not category.strip():
        raise ValueError("Category cannot be empty.")

    if description is not None and not isinstance(description, str):
        raise ValueError("Description must be a string or None.")

    expenses = storage.load_expenses()

    id_ = 1

    for existing_expense in expenses:
        if existing_expense["id"] >= id_:
            id_ = existing_expense["id"] + 1

    expense = {
        "id": id_,
        "amount": amount,
        "category": category.strip(),
        "description": "" if description is None else description.strip()
    }

    storage.save_expenses(expense)

    return expense

def view_expenses():
    data = storage.load_expenses()

    for expense in data:
        id = expense["id"]
        category = expense["category"]
        amount = expense["amount"]
        description = expense["description"]

        print(f"=============== EXPENSE {id} ===============")
        print(f"ID: {id}")
        print(f"Amount: {amount}")
        print(f"Category: {category}")
        print(f"Description: {description}")
        print(f"==========================================\n\n")
def delete_expense():
    pass

def filter_expenses():
    pass

def validate_expense():
    pass