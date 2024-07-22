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
### Implemented a CI/CD pipeline for a application using Jenkins, facilitating automated testing and deployment to staging and production environments.
 
### To install Jenkins, you need to follow a series of steps that can vary slightly depending on your operating system. Below, I'll provide a guide for installing Jenkins on a Windows.
- **Go to the Jenkins download page and download the Windows installer.**
- **Run the downloaded .msi installer.**
- **Follow the setup wizard steps to complete the installation.**
- **After installation, open a web browser and go to http://localhost:9090.**
- **Follow the instructions to unlock Jenkins, using the password from C:\Program Files (x86)\Jenkins\secrets\initialAdminPassword.**

### Try running this command in your terminal to run and check the jenkins is installed or not.
```sh
java -jar "C:/Program Files/Jenkins/Jenkins.war" --version

```
### Now to start the jenkins dashboard run this command in terminal 
```sh
java -jar "C:/Program Files/Jenkins/Jenkins.war" --httpPort=9090
```
### Visit localhost:9090 to make sure the app run successfully
- **Create Pipeline**: At Jenkins’s dashboard page, Click New Item, then fill pipeline name you’d want
In section Build Trigger, there are several option for trigger Jenkins pipeline. for this, let’s choose Poll SCM. in the text-box write for schedule H/5 * * * *. with this configuration, Jenkins will check the repository every 5 minutes.
Scroll down, in section Definition, choose option Pipeline script from SCM. this option will instruct Jenkins to create Pipeline from Source Control Management
At coloumn SCM, checklist Git
 Fill URL Repository with URL from your github directory & save.
From the pipeline, we can see there are 3 stages : Build image, Push Docker hub and Deploy to server.

Furthermore about Jenkinsfile, you can read from this article

2. The job will start and do every step in stages. If success, it will have check mark
   


  


