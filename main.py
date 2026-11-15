import questionary
import expenses
import statistic
import sys

print("""
|-----------------------|
|  Expense Tracker CLI  |
|-----------------------|
""")

while True:

    choice = questionary.select("Select one of the following: ",
                   choices=[
                       "1. Add Expense",
                       "2. View Expenses",
                       "3. Delete Expense",
                       "4. Filter Expenses",
                       "5. View Statistics",
                       "6. Exit"
                   ]).ask()

    if choice == "1. Add Expense":
        amount = questionary.text("Enter the amount: ").ask()
        category = questionary.select("Select the category: ",choices = [
            "Housing",
            "Groceries",
            "Food & Dining",
            "Transport",
            "Health",
            "Entertainment",
            "Shopping",
            "Bills & Subscriptions",
            "Other"
        ]).ask()
        description = questionary.text("Enter a description (optional): ").ask()

        expenses.add_expense(amount=float(amount),category=category,description=description)

    elif choice == "2. View Expenses":
        expenses.view_expenses()

    elif choice == "3. Delete Expense":
        expenses.delete_expense()

    elif choice == "4. Filter Expenses":
        expenses.filter_expenses()

    elif choice == "5. View Statistics":
        pass

    elif choice == "6. Exit":
        if questionary.confirm("Are you sure you want to exit?").ask():
            sys.exit()
        else:
            continue
