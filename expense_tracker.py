class Expense:
    def __init__(self, date, category, amount, description):
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description

    def __str__(self):
        return (
            f"{self.date} | {self.category} | ${self.amount:.2f} | {self.description}"
        )


import csv

expenses = []


def add_expense(date, category, amount, description):
    expense = Expense(date, category, amount, description)
    expenses.append(expense)


def view_expense():
    for expense in expenses:
        print(expense)


def save_expenses(filename):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount", "Description"])
        for expense in expenses:
            writer.writerow(
                [expense.date, expense.category, expense.amount, expense.description]
            )


def load_expenses(filename):
    global expenses
    expenses = []
    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        for row in reader:
            date, category, amount, description = row
            add_expense(date, category, float(amount), description)


def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Save Expenses")
        print("4. Load Expenses")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            category = input("Enter the category: ")
            amount = float(input("Enter the amount: "))
            description = input("Enter a description: ")
            add_expense(date, category, amount, description)

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            filename = input("Enter the filename to save to: ")
            save_expenses(filename)
            print(f"Expenses saved to {filename}")

        elif choice == "4":
            filename = input("Enter the filename to load from: ")
            load_expenses(filename)
            print(f"Expenses loaded from {filename}")

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please try again.")
