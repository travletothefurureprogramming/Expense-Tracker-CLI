import questionary
import expenses
import statistic
import sys
import storage

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
                       "6. Export to CSV",
                       "7. Exit"
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
        expenses.view_expenses()
        id = questionary.text("Enter id to delete: ").ask()
        expenses.delete_expense(id)

    elif choice == "4. Filter Expenses":
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
        expenses.filter_expenses(category_filter=category)

    elif choice == "5. View Statistics":
        choice = questionary.select("Select type of statistics: ",choices=[
            "Total expenses",
            "Category Summary",
            "Average Expense"
        ]).ask()

        if choice == "Total expenses":
            statistic.calculate_total()

        elif choice == "Category Summary":
            statistic.category_summary()

        elif choice == "Average Expense":
            statistic.average_expense()

    elif choice == "6. Export to CSV":
        storage.export_to_csv()

    elif choice == "7. Exit":
        if questionary.confirm("Are you sure you want to exit?").ask():
            sys.exit()
        else:
            continue
