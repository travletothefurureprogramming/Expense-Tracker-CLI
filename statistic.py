import storage


def calculate_total():
    data = storage.load_expenses()
    total = 0
    for expense in data:
        amount = expense["amount"]
        total += amount

    print(f"Total expenses: {total}")

def category_summary():
    data = storage.load_expenses() 
    Housing, Groceries, Food_Dining, Transport, Health, Entertainment, Shopping, Bills_Subscriptions, Other = 0, 0, 0, 0, 0, 0, 0, 0, 0

    for expense in data:
        category = expense["category"]
        amount = expense["amount"]

        if category == "Housing":
            Housing += amount
        elif category == "Groceries":
            Groceries += amount
        elif category == "Food & Dining":
            Food_Dining += amount
        elif category == "Transport":
            Transport += amount
        elif category == "Health":
            Health += amount
        elif category == "Entertainment":
            Entertainment += amount
        elif category == "Shopping":
            Shopping += amount
        elif category == "Bills & Subscriptions":
            Bills_Subscriptions += amount
        elif category == "Other":
            Other += amount

    print("=========================Category Summary=========================")
    print(f"Housing: {Housing}")
    print(f"Groceries: {Groceries}")
    print(f"Food & Dining: {Food_Dining}")
    print(f"Transport: {Transport}")
    print(f"Health: {Health}")
    print(f"Entertainment: {Entertainment}")
    print(f"Shopping: {Shopping}")
    print(f"Bills & Subscriptions: {Bills_Subscriptions}")
    print(f"Other: {Other}")
    print("==================================================================")


def average_expense():
    data = storage.load_expenses()
    expenses_amount = []

    for expense in data:
        amount = expense["amount"]
        expenses_amount.append(amount)

    average = sum(expenses_amount) / len(expenses_amount)

    print(f"Average Expense: {int(average)}")