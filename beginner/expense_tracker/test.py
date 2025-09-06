import unittest
from unittest.mock import patch, mock_open
from datetime import datetime
from main import Authenticate, Budget, Income, Expense 

class TestExpenseTracker(unittest.TestCase):
    """
    Unit test class for testing the functionality of the Expense Tracker application.
    """
    @patch("builtins.input", side_effect=["testuser", "testpass"])
    @patch("builtins.open", new_callable=mock_open, read_data="username,password\n")
    def test_register_success(self, mock_file, mock_input):
        """
        Test successful user registration.
        """
        auth = Authenticate()
        auth.register()
        self.assertTrue(mock_file.called)
    
    @patch("builtins.input", side_effect=["", "pass"])
    def test_register_invalid_username(self, mock_input):
        """
        Test registration with an empty username.
        """
        auth = Authenticate()
        result = auth.register()
        self.assertEqual(result, "Username and password cannot be empty.")

    @patch("builtins.input", side_effect=["testuser", "testpass", "testuser", "testpass"])
    def test_login_success(self, mock_input):
        """
        Test successful login after registration.
        """
        m = mock_open()
        auth = Authenticate()
        auth.users_file = "dummy.csv" 
        with patch("builtins.open", m):
            auth.register()
        written = "username,password\ntestuser,testpass\n"
        m_read = mock_open(read_data=written)
        with patch("builtins.open", m_read):
            result = auth.login()
        self.assertTrue(result)
        
    @patch("builtins.input", side_effect=["testuser", "pass"])
    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_login_file_not_found(self, mock_open, mock_input):
        """
        Test login failure when user file is missing.
        """
        auth = Authenticate()
        result = auth.login()
        self.assertFalse(result)

    @patch("builtins.input", side_effect=["monthly", "5000"])
    @patch("builtins.open", new_callable=mock_open)
    def test_set_budget_valid(self, mock_file, mock_input):
        """
        Test set a valid monthly budget.
        """
        Authenticate.current_user = "testuser"
        budget = Budget()
        budget.set_budget()
        self.assertTrue(mock_file.called)
        
    @patch("builtins.open", new_callable=mock_open, read_data="wrong,data,format\n")
    def test_view_budget_wrong_headers(self, mock_file):
        """
        Test viewing budget with incorrectly formatted headers.
        """
        Authenticate.current_user = "testuser"
        budget = Budget()
        result = budget.view_budget()
        self.assertIn("No budget records found.", result)
    
    @patch("builtins.input", side_effect=["food", "1000", "monthly"])
    def test_budget_exceeded_warning(self, mock_input):
        """
        Test budget exceeded scenario.
        """
        budget_data = "username,budget_type,amount,start_date\n" \
                      "testuser,monthly,500,2024-01-01\n"
        expense_data = "username,category,amount,date,budget_type\n" \
                       "testuser,food,600,2024-06-20,monthly\n"
        mock_budget_file = mock_open(read_data=budget_data)
        mock_expense_file = mock_open(read_data=expense_data)
        mock_write_file = mock_open()

        def open_side_effect(file, mode='r', *args, **kwargs):
            if "budget" in file:
                return mock_budget_file.return_value
            elif "expense" in file and 'r' in mode:
                return mock_expense_file.return_value
            elif "expense" in file and ('a' in mode or 'w' in mode):
                return mock_write_file.return_value
            else:
                raise FileNotFoundError(f"Unexpected file: {file}")

        with patch("builtins.open", side_effect=open_side_effect):
            Authenticate.current_user = "testuser"
            expense = Expense()
            result = expense.add_expense()
        self.assertIn("Warning: You have exceeded your monthly budget", result)
    
    @patch("builtins.open", new_callable=mock_open)
    @patch("builtins.input", side_effect=["4000", "salary"])
    def test_add_income_valid(self, mock_input, mock_file):
        """
        Test adding valid income entry.
        """
        Authenticate.current_user = "testuser"
        income = Income()
        result = income.add_income()
        self.assertTrue(mock_file.called)
        self.assertIn("Income added successfully", result)

    @patch("builtins.input", side_effect=["food", "100", "monthly"])
    @patch("builtins.open", new_callable=mock_open)
    def test_add_expense_valid(self, mock_file, mock_input):
        """
        Test adding a valid expense entry.
        """
        Authenticate.current_user = "testuser"
        expense = Expense()
        expense.add_expense()
        self.assertTrue(mock_file.called)

    @patch("builtins.open", new_callable=mock_open, read_data="username,budget_type,amount,start_date\n")
    def test_view_budget_empty(self, mock_file):
        """
        Test viewing budget when no records exist for the user.
        """
        Authenticate.current_user = "testuser"
        budget = Budget()
        result = budget.view_budget()
        self.assertEqual(result, "No budget records found.")

    @patch("builtins.open", new_callable=mock_open, read_data="username,income,source,date\n")
    def test_view_income_empty(self, mock_file):
        """
        Test viewing income when no records exist.
        """
        Authenticate.current_user = "testuser"
        income = Income()
        result = income.view_income()
        self.assertEqual(result, "No income records found.")

    @patch("builtins.open", new_callable=mock_open, read_data="username,category,amount,date,budget_type\n")
    def test_view_expense_empty(self, mock_file):
        """
        Test viewing expenses when no entries are available.
        """
        Authenticate.current_user = "testuser"
        expense = Expense()
        result = expense.view_expense()
        self.assertEqual(result, "No expense records found.")
if __name__ == '__main__':
    unittest.main()