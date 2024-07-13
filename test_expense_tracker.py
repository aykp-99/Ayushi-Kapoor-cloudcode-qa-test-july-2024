import pytest
import json
import os
from datetime import datetime
from starter import ExpenseTracker, Expense

# Fixture to provide a new instance of ExpenseTracker for each test
@pytest.fixture
def tracker():
    return ExpenseTracker()

# Unit Tests

def test_add_expense(tracker):
    tracker.add_expense(100, "Food", "Lunch")
    assert len(tracker.expenses) == 1
    assert tracker.expenses[0].amount == 100
    assert tracker.expenses[0].category == "Food"
    assert tracker.expenses[0].description == "Lunch"

def test_edit_expense(tracker):
    tracker.add_expense(100, "Food", "Lunch")
    tracker.edit_expense(0, 150, "Food", "Dinner")
    assert tracker.expenses[0].amount == 150
    assert tracker.expenses[0].category == "Food"
    assert tracker.expenses[0].description == "Dinner"

def test_edit_expense_invalid_index(tracker):
    tracker.add_expense(100, "Food", "Lunch")
    tracker.edit_expense(1, 150, "Food", "Dinner")
    assert tracker.expenses[0].amount == 100
    assert tracker.expenses[0].category == "Food"
    assert tracker.expenses[0].description == "Lunch"

def test_delete_expense(tracker):
    tracker.add_expense(100, "Food", "Lunch")
    tracker.add_expense(50, "Transport", "Bus fare")
    tracker.delete_expense(0)
    assert len(tracker.expenses) == 1
    assert tracker.expenses[0].amount == 50
    assert tracker.expenses[0].category == "Transport"
    assert tracker.expenses[0].description == "Bus fare"

def test_delete_expense_invalid_index(tracker):
    tracker.add_expense(100, "Food", "Lunch")
    tracker.delete_expense(1)
    assert len(tracker.expenses) == 1
    assert tracker.expenses[0].amount == 100
    assert tracker.expenses[0].category == "Food"
    assert tracker.expenses[0].description == "Lunch"

def test_list_expenses(tracker, capsys):
    tracker.add_expense(100, "Food", "Lunch")
    tracker.add_expense(50, "Transport", "Bus fare")
    tracker.list_expenses()
    captured = capsys.readouterr()
    assert "Amount: 100, Category: Food, Description: Lunch" in captured.out
    assert "Amount: 50, Category: Transport, Description: Bus fare" in captured.out

def test_save_to_file(tracker, tmp_path):
    tracker.add_expense(100, "Food", "Lunch")
    tracker.add_expense(50, "Transport", "Bus fare")
    file_path = tmp_path / "expenses.json"
    tracker.save_to_file(file_path)
    with open(file_path, 'r') as file:
        data = json.load(file)
        assert len(data) == 2
        assert data[0]['amount'] == 100
        assert data[0]['category'] == "Food"
        assert data[0]['description'] == "Lunch"
        assert data[1]['amount'] == 50
        assert data[1]['category'] == "Transport"
        assert data[1]['description'] == "Bus fare"

def test_load_from_file(tracker, tmp_path):
    data = [
        {"amount": 100, "category": "Food", "description": "Lunch", "date": "2023-07-13"},
        {"amount": 50, "category": "Transport", "description": "Bus fare", "date": "2023-07-13"}
    ]
    file_path = tmp_path / "expenses.json"
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
    tracker.load_from_file(file_path)
    assert len(tracker.expenses) == 2
    assert tracker.expenses[0].amount == 100
    assert tracker.expenses[0].category == "Food"
    assert tracker.expenses[0].description == "Lunch"
    assert tracker.expenses[1].amount == 50
    assert tracker.expenses[1].category == "Transport"
    assert tracker.expenses[1].description == "Bus fare"

# Integration Tests

def test_save_and_load_expenses(tracker, tmp_path):
    tracker.add_expense(100, "Food", "Lunch")
    tracker.add_expense(50, "Transport", "Bus fare")
    file_path = tmp_path / "expenses.json"
    tracker.save_to_file(file_path)
    new_tracker = ExpenseTracker()
    new_tracker.load_from_file(file_path)
    assert len(new_tracker.expenses) == 2
    assert new_tracker.expenses[0].amount == 100
    assert new_tracker.expenses[0].category == "Food"
    assert new_tracker.expenses[0].description == "Lunch"
    assert new_tracker.expenses[1].amount == 50
    assert new_tracker.expenses[1].category == "Transport"
    assert new_tracker.expenses[1].description == "Bus fare"

def test_save_edit_and_load_expenses(tracker, tmp_path):
    tracker.add_expense(100, "Food", "Lunch")
    tracker.add_expense(50, "Transport", "Bus fare")
    tracker.edit_expense(0, 150, "Food", "Dinner")
    file_path = tmp_path / "expenses.json"
    tracker.save_to_file(file_path)
    new_tracker = ExpenseTracker()
    new_tracker.load_from_file(file_path)
    assert len(new_tracker.expenses) == 2
    assert new_tracker.expenses[0].amount == 150
    assert new_tracker.expenses[0].category == "Food"
    assert new_tracker.expenses[0].description == "Dinner"
    assert new_tracker.expenses[1].amount == 50
    assert new_tracker.expenses[1].category == "Transport"
    assert new_tracker.expenses[1].description == "Bus fare"

def test_save_delete_and_load_expenses(tracker, tmp_path):
    tracker.add_expense(100, "Food", "Lunch")
    tracker.add_expense(50, "Transport", "Bus fare")
    tracker.delete_expense(0)
    file_path = tmp_path / "expenses.json"
    tracker.save_to_file(file_path)
    new_tracker = ExpenseTracker()
    new_tracker.load_from_file(file_path)
    assert len(new_tracker.expenses) == 1
    assert new_tracker.expenses[0].amount == 50
    assert new_tracker.expenses[0].category == "Transport"
    assert new_tracker.expenses[0].description == "Bus fare"

if __name__ == "__main__":
    pytest.main()
