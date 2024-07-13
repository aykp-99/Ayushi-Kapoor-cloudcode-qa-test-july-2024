import json
import os
from datetime import datetime

class Expense:
    def __init__(self, amount, category, description, date=None):
        #Initialize an Expense object.

        self.amount = amount
        self.category = category
        self.description = description
        self.date = date or datetime.now().strftime("%Y-%m-%d")

    def to_dict(self):
        #Convert the Expense object to a dictionary representation.

        return {
            'amount': self.amount,
            'category': self.category,
            'description': self.description,
            'date': self.date
        }

    @classmethod
    def from_dict(cls, data):
        #Create an Expense object from a dictionary representation.

        return cls(data['amount'], data['category'], data['description'], data['date'])

class ExpenseTracker:
    def __init__(self):
        #Initialize an ExpenseTracker object with an empty list of expenses.

        self.expenses = []

    def add_expense(self, amount, category, description):
        #Add a new expense to the tracker.

        expense = Expense(amount, category, description)
        self.expenses.append(expense)

    def edit_expense(self, index, amount, category, description):
        #Edit an existing expense at the specified index.

        if 0 <= index < len(self.expenses):
            self.expenses[index].amount = amount
            self.expenses[index].category = category
            self.expenses[index].description = description
            self.expenses[index].date = datetime.now().strftime("%Y-%m-%d")

    def delete_expense(self, index):
        # Delete an expense at the specified index.

        if 0 <= index < len(self.expenses):
            self.expenses.pop(index)

    def list_expenses(self):
        #List all expenses, displaying amount, category, description, and date.

        for i, expense in enumerate(self.expenses):
            print(f"Index: {i}, Amount: {expense.amount}, Category: {expense.category}, Description: {expense.description}, Date: {expense.date}")

    def save_to_file(self, filename):
        #Save all expenses to a JSON file.

        with open(filename, 'w') as file:
            json.dump([expense.to_dict() for expense in self.expenses], file, indent=4)

    def load_from_file(self, filename):
        #Load expenses from a JSON file.
        if not os.path.exists(filename):
            raise FileNotFoundError(f"The file {filename} does not exist.")
        with open(filename, 'r') as file:
            expenses_list = json.load(file)
            self.expenses = [Expense.from_dict(expense) for expense in expenses_list]

if __name__ == "__main__":
    tracker = ExpenseTracker()

    tracker.add_expense(5000, "Electronics", "Mobiles")
    tracker.add_expense(50, "Transport", "Bus fare")
    tracker.add_expense(100, "Food", "Dinner")
    tracker.add_expense(700, "Sports", "Basket Ball")
    tracker.add_expense(3000, "Vehicle", "Bycycle")
    tracker.list_expenses()
    tracker.edit_expense(0, 120, "Food", "Lunch at a restaurant")
    tracker.list_expenses()
    tracker.delete_expense(1)
    tracker.list_expenses()
    tracker.save_to_file('expenses.json')
    tracker.load_from_file('expenses.json')
    tracker.list_expenses()
