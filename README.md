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
**Output**
![image](https://github.com/user-attachments/assets/4fe36fea-3a03-4918-8c75-155420a3bf81)


Running Tests::

```sh
pytest test_expense_tracker.py
```
**Test Result**
![image](https://github.com/user-attachments/assets/b525755c-819d-4f4a-b641-2b07dd24e304)


# Additional Feature
 Implemented a CI/CD pipeline for a application using Jenkins, facilitating automated testing and deployment to staging and production environments.
 
### To install Jenkins, you need to follow a series of steps that can vary slightly depending on your operating system. Below, I'll provide a guide for installing Jenkins on a Windows.
- **Go to the Jenkins download page and download the Windows installer**
- **Run the downloaded .msi installer.**
- **Follow the setup wizard steps to complete the installation.**


