import csv
import os
from datetime import datetime, timedelta

class Authenticate:
    """
    Handles user authentication including registration and login.
    """
    users_file = "beginner/expense_tracker/data/users.csv"
    current_user = None

    def __init__(self):
        """
        Initializes the Authenticate class.
        """
        if not os.path.exists(self.users_file):
            with open(self.users_file, mode='w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['username', 'password'])

    def register(self):
        """
        Registers a new user by asking for username and password.
        """
        username = input("Enter a username: ").strip()
        password = input("Enter a password: ").strip()
        if not username or not password:
            return "Username and password cannot be empty."
        try:
            with open(self.users_file, mode='r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row['username'] == username:
                        print("Username already exists. Try a different one.")
                        return
        except FileNotFoundError:
            print("User file not found. Please try again later.")
            return
        except Exception as e:
            print(f"Unexpected error during registration: {e}")
            return
        with open(self.users_file, mode='a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([username, password])
            print("Registration successful.")

    def login(self):
        """
        Logs in a user by validating username and password.
        """
        username = input("Enter your username: ").strip()
        password = input("Enter your password: ").strip()
        try:
            with open(self.users_file, mode='r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row['username'] == username and row['password'] == password:
                        Authenticate.current_user = username
                        print(f"Login successful. Welcome, {username}!")
                        return True
            print("Invalid username or password.")
            return False
        except FileNotFoundError:
            print("User file missing. Please register first.")
            return False
        except Exception as e:
            print(f"Unexpected error during login: {e}")
            return False


class Budget:
    """
    Manages user budgets, including setting and viewing budgets.
    """
    budget_file = "beginner/expense_tracker/data/budgets.csv"

    def __init__(self):
        """
        Initializes the Budget class.
        """
        if not os.path.exists(self.budget_file):
            with open(self.budget_file, mode='w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['username', 'budget_type', 'amount', 'start_date'])

    def set_budget(self):
        """
        Sets a new budget for the currently logged-in user.
        """
        if Authenticate.current_user is None:
            print("You must be logged in to set a budget.")
            return
        print("Options: daily, weekly, monthly, yearly")
        budget_type = input("Enter budget type: ").strip().lower()
        if budget_type not in ['daily', 'weekly', 'monthly', 'yearly']:
            print("Invalid budget type.")
            return
        try:
            amount = float(input("Enter budget amount: ").strip())
        except ValueError:
            print("Amount must be a number.")
            return
        start_date = datetime.today().strftime('%Y-%m-%d')
        try:
            with open(self.budget_file, mode='a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([Authenticate.current_user, budget_type, amount, start_date])
                print("Budget set successfully.")
        except Exception as e:
            print(f"Failed to add budget: {e}")
            return

    def view_budget(self):
        """
        Displays the budget of the currently logged-in user.
        """
        if Authenticate.current_user is None:
            return "You must be logged in to view budget."
        found = False
        try:
            with open(self.budget_file, mode='r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row['username'] == Authenticate.current_user:
                        found = True
            if not found:
                return "No budget records found."
            return "Budget displayed successfully."
        except FileNotFoundError:
            return "Budget file not found."


class Income:
    """
    Handles income-related functionalities like adding and viewing income records.
    """
    income_file = "beginner/expense_tracker/data/incomes.csv"

    def __init__(self):
        """
        Initializes the Income class.
        Creates the income CSV file with headers if it doesn't exist.
        """
        if not os.path.exists(self.income_file):
            with open(self.income_file, mode='w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['username', 'income', 'source', 'date'])

    def add_income(self):
        """
        Adds an income entry for the currently logged-in user.
        """
        if Authenticate.current_user is None:
            return "You must be logged in to add income."
        try:
            income = float(input("Enter your income: "))
        except ValueError:
            return "Income must be in numbers."
        print("Options: salary, bussiness, freelance")
        source = input("Enter source of your income: ").strip()
        if source not in ['salary', 'bussiness', 'freelance']:
            return "Invalid source type."
        date = datetime.today().strftime('%Y-%m-%d')
        try:
            with open(self.income_file, mode='a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([Authenticate.current_user, income, source, date])
                return "Income added successfully."
        except Exception as e:
            return f"Failed to add income: {e}"

    def view_income(self):
        """
        Displays all income entries for the currently logged-in user.
        """
        if Authenticate.current_user is None:
            return "You must be logged in to view income."
        income_data = []
        try:
            with open(self.income_file, mode='r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row['username'] == Authenticate.current_user:
                        income_data.append(
                            f"Source: {row['source']} Income: {row['income']} Date: {row['date']}")
            if not income_data:
                return "No income records found."
            return "\n".join(income_data)
        except Exception as e:
            return f"Failed to get income: {e}"


class Expense:
    """
    Manages expense-related actions like adding and viewing expenses,
    and checks if the expenses exceed the set budget.
    """
    expense_file = "beginner/expense_tracker/data/expenses.csv"

    def __init__(self):
        """
        Initializes the Expense class.
        """
        if not os.path.exists(self.expense_file):
            with open(self.expense_file, mode='w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['username', 'category', 'amount', 'date', 'budget_type'])

    def add_expense(self):
        """
        Adds an expense entry for the current user.
        """
        if Authenticate.current_user is None:
            return "You must be logged in to add income."
        print("Options: food, travel, grocery, daily-needs, miscellaneous, shopping")
        category = input("Enter your expense category: ").strip().lower()
        if category not in ['food', 'travel', 'grocery', 'dailyneeds', 'miscellaneous', 'shopping']:
            return "Invalid category choosen"
        try:
            amount = float(input("Enter spent amount: ").strip())
        except ValueError:
            return "Amount must be a number."
        print("Budget Types: daily, weekly, monthly, yearly")
        budget_type = input("Enter the budget type for this expense: ").strip().lower()
        if budget_type not in ['daily', 'weekly', 'monthly', 'yearly']:
            return "Invalid budget type."
        date = datetime.today().strftime('%Y-%m-%d')
        try:
            with open(self.expense_file, mode='a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([Authenticate.current_user, category, amount, date, budget_type])
                print("Expense added successfully.")
        except Exception as e:
            return f"Failed to add expense: {e}"
        result = self.check_budget_exceeded(Authenticate.current_user, budget_type)
        return result

    def check_budget_exceeded(self, username, budget_type):
        """
        Checks if the total expenses for a user and budget type have exceeded the set budget within the time frame.
        """
        from_date = None
        to_date = datetime.today().date()
        try:
            budget_amount = 0
            with open("beginner/expense_tracker/data/budgets.csv", mode='r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row['username'] == username and row['budget_type'] == budget_type:
                        budget_amount = float(row['amount'])
                        from_date = datetime.strptime(row['start_date'], '%Y-%m-%d').date()
                        break
            if from_date is None:
                return "Start date for the budget not found."
            if budget_amount == 0:
                return f"No budget set for {budget_type} type."
        except Exception as e:
            return f"Error reading budget file: {e}"
        try:
            total_expense = 0
            with open(self.expense_file, mode='r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row['username'] == username and row['budget_type'] == budget_type:
                        exp_date = datetime.strptime(row['date'], '%Y-%m-%d').date()
                        if from_date <= exp_date <= to_date:
                            total_expense += float(row['amount'])
            if total_expense > budget_amount:
                return f"Warning: You have exceeded your {budget_type} budget.\nSpent: {total_expense}, Budget: {budget_amount}"
            else:
                return f"Current total {budget_type} expenses: {total_expense}/{budget_amount}"
        except Exception as e:
            return f"Error reading expense file: {e}"

    def view_expense(self):
        """
        Displays all expense entries for the currently logged-in user.
        """
        if Authenticate.current_user is None:
            return "You must be logged in to view expenses."
        expense_data = []
        try:
            with open(self.expense_file, mode='r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row['username'] == Authenticate.current_user:
                        print(f"Category: {row['category']}, Amount: {row['amount']}, Date: {row['date']}, Type: {row['budget_type']}")
            if not expense_data:
                return "No expense records found."
            return "\n".join(expense_data)
        except Exception as e:
            return f"Failed to get expense: {e}"


def main():
    """
    Main function to run the Expense Tracker.
    """
    auth = Authenticate()
    bud = Budget()
    inc = Income()
    exp = Expense()
    try:
        print("Welcome to Expense Tracker!")
        print("1. Register")
        print("2. Login")
        try:
            choice = int(input("Choose an action (1/2): "))
            if choice not in [1, 2]:
                print("Invalid option.")
                return
        except ValueError:
            print("Invalid input")
            return
        if choice == 1:
            auth.register()
            print("Now please Login to continue.")
        if not auth.login():
            print("Log in failed. Exiting program.")
            return

        flag = True
        while flag:
            print("\nMain Menu:")
            print("1. Set Budget")
            print("2. View Budget")
            print("3. Add Income")
            print("4. View Income")
            print("5. Add Expense")
            print("6. View Expenses")
            print("7. Logout")
            try:
                option = int(input("Enter your choice(1-7): "))
                if option not in range(1, 8):
                    print("Invalid option")
                    continue
            except ValueError:
                print("Invalid input")
                continue
            if option == 1:
                bud.set_budget()
            elif option == 2:
                bud.view_budget()
            elif option == 3:
                inc.add_income()
            elif option == 4:
                inc.view_income()
            elif option == 5:
                exp.add_expense()
            elif option == 6:
                exp.view_expense()
            elif option == 7:
                print(f"Exit successful")
                Authenticate.current_user = None
                flag = False
                break
    except Exception as e:
        print(f"\nUnexpected Error: {e}")
if __name__ == "__main__":
    main()