# Expense_Tracker_Application
## Overview
The Expense Tracker application helps users manage their expenses efficiently. It allows users to add, edit, delete expenses, list all expenses, and save/load them from a JSON file.

## Technology Stack

- **Python**: Core language for application logic.
- **Pytest**: Testing framework for unit and integration tests.
- **JSON**: File format used for saving and loading expense data

## Testing Strategy
### Unit Tests
- **Expense Class**: Tests creation from and conversion to dictionaries.
- **ExpenseTracker Class**:
Tests for adding, editing, and deleting expenses.
Tests for listing expenses and verifying correct outputs.
Tests for saving to and loading from a file.
### Integration Tests
- **Method Interactions**: Test scenarios where multiple methods of ExpenseTracker are used sequentially.
- **File Operations**: Test saving expenses to a file and loading them back, verifying data integrity.
## Installation
Ensure Python and pytest are installed.
```sh
pip install pytest
```
Running the application :

```sh
python starter.py
```

Running Tests::

```sh
pytest test_expense_tracker.py
```
