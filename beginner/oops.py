"""
Object-Oriented Programming in Python (OOP)

This file is intended to cover the following concepts related to OOP in Python:
- Object-oriented programming paradigm
- The four pillars of OOP:
  1. Encapsulation: Private and protected attributes
  2. Inheritance: Single, multiple, and multilevel inheritance 
  3. Polymorphism: Method overriding and operator overloading
  4. Abstraction: Abstract classes and interfaces
- Composition vs inheritance
- Mixins and multiple inheritance
- Design patterns in OOP
- Best practices and common pitfalls

The examples in this file will demonstrate how to implement OOP principles effectively in Python.
"""

# TODO: Add OOP examples and implementations
'''(practice ques) Create a student class that takes name & marks of three subjects as 
arguments in constructor. Then create a method to print the average.'''

class Student:                            #defining class
  def __init__(self, name, marks):        ##defining constructor (parameterised)
    self.name = name                      #Assigning the name parameter to the instance variable self.name 
    self.marks = marks                    #Assigning the marks parameter (a list) to the instance variable self.marks
  def get_average(self):                  #defining method with self (default)
    sum = 0
    for value in self.marks:              #looping through list
      sum+=value                            
    print(self.name, "average score is: ", sum/3)   #printing result     
      
s1 = Student("Akhil Choudhary", [67,98,84])     #object created as s1 
s1.get_average()                                #method called

#Method Overriding
class Parent(): 
	 
	def __init__(self): 
		self.value = "Inside Parent"
		
	def show(self): 
		print(self.value) 
		
class Child(Parent): 
	
	def __init__(self): 
		super().__init__()  
		self.value = "Inside Child"
		
	def show(self): 
		print(self.value) 
		
obj1 = Parent() 
obj2 = Child() 
obj1.show()  
obj2.show()

from abc import ABC, abstractmethod

# Define an abstract class
class Animal(ABC):
    
    @abstractmethod
    def sound(self):
        pass  # This is an abstract method, no implementation here.

# Concrete subclass of Animal
class Dog(Animal):
    
    def sound(self):
        return "Bark"  # Providing the implementation of the abstract method

# Create an instance of Dog
dog = Dog()
print(dog.sound())  # Output: Bark

#mixin

class LoggingMixin:
    def log(self, message):
        print(f"LOG: {message}")

class Animal:
    def sound(self):
        return "Some sound"

class Cat(Animal, LoggingMixin):
    def sound(self):
        self.log("Cat says meow")
        return "Woof!"

cat = Cat()
print(cat.sound())

#Composition -> In below example the class Car owns the objects of class engine and class wheel.

class Engine:
  def __init__(self, horse_power):
    self.horse_power = horse_power
    
class Wheel:
  def __init__(self,size):
    self.size = size
    
class Car:
  def __init__(self, make, model, horse_power, wheel_size):
    self.make = make
    self.model = model
    self.engine = Engine(horse_power)
    self.wheels = [Wheel(wheel_size) for wheel in range(4)]

  def display_car(self):
    return f"{self.make} {self.model} {self.engine.horse_power}(hp) {self.wheels[0].size}in"

car1 = Car("Kia", "Seltos", 1200, 20)
car2 = Car("MG", "Astor", 1400, 22)

print(car1.display_car())
print(car2.display_car())

#exercise-1 (Library Management)
class Catalog:
  """ 
    A class to represent a catalog of books in a library.
    Attributes: books_list (list): A list to store all book objects added to the catalog.
  """
  def __init__(self,books_list):
    """  Initializes the Catalog with an empty list of books. """
    self.books_list = []
  def add_book(self, book):
    """
      Adds a book to the catalog.
      Args: book (Book): The book object to add to the catalog.
    """
    self.books_list.append(book)
    print(f"Book '{book.title}' by {book.author} added to catalog.")
  def search_by_id(self, book_id):
    """
      Searches for a book in the catalog by its unique ID.
      Args: book_id (str): The ID of the book to search for.
      Returns: Book or None: The book object if found, otherwise None.
    """
    for book in self.books_list:
        if book.id == book_id:
            return book
    return None
  def search_by_title(self, title):
    """
      Searches for books in the catalog by title (partial or full match, case-insensitive).
      Args: title (str): The title or part of the title to search for.
      Returns: list: A list of books matching the given title.
    """
    results = [book for book in self.books_list if title.lower() in book.title.lower()]
    if results:
        print(f"Books matching title '{title}':")
        for book in results:
            print(f"- {book.title} by {book.author} (ID: {book.id})")
    else:
        print(f"No books found with title containing '{title}'.")
    return results
  def search_by_author(self, author):
    """
      Searches for books in the catalog by author name (partial or full match, case-insensitive).
      Args: author (str): The author or part of the author name to search for.
      Returns: list: A list of books written by the specified author.
    """
    results = [book for book in self.books_list if author.lower() in book.author.lower()]
    if results:
        print(f"Books by author '{author}':")
        for book in results:
            print(f"- {book.title} (ID: {book.id})")
    else:
        print(f"No books found by author '{author}'.")
    return results
  def remove_book(self, book_id):
    """
      Removes a book from the catalog using its ID.
      Args: book_id (str): The ID of the book to be removed.
      Returns: None
    """
    book = self.search_by_id(book_id)   
    if book:
        self.books_list.remove(book)
        print(f"Book '{book.title}' (ID: {book.id}) removed from catalog.")
    else:
        print(f"No book found with ID '{book_id}'.")
    
class Book:
  """
    A class to represent the books in the library.
    Attributes: title (str) : The title of the book, author (str) : The author of the book. 
  """
  counter = 1  
  def __init__(self, title, author):
    """
      Initializes the Book class with unique id, title, author and availability. 
      Args: id (str): String store unique id of the book added.
                  title(str): String to store title of the book.
                  author(str): String to store author of the book.
                  is_available(bool): Status of the book.
    """
    self.id = f"B{Book.counter:03d}"
    Book.counter += 1
    self.title = title
    self.author = author
    self.is_available = True

  def mark_as_borrowed(self):
    """
      Display the book status.
      Returns: False if book is borrowed. 
    """
    self.is_available = False

  def mark_as_returned(self):
    """
      Display the book status.
      Returns: True if book is returned. 
    """
    self.is_available = True

class Member:
  """
    A class to represent members and the borrowed book in the library.
    Attributes: id (str): A unique id given to every member registered in the library.
                name(str): Name of the member registered.
                borrowed_book_list(list): List of borrowed books.
  """

  counter = 1
  def __init__(self, name):
    """
      Initializes the Member class with id, name, borrowed_books_list.  
      Args: id (str): String store unique id of the registered member.
            name(str): String store name of member.
            borrowed_book_list(list): List to store number of borrowed books.
    """
    self.id = f"M{Member.counter:02d}"
    Member.counter += 1
    self.name = name
    self.borrowed_books_list = []

  def borrow_book(self, book):
    """
      Appends the borrowed book list.
      Returns: A updated list of borrowed books.
    """
    self.borrowed_books_list.append(book)

  def return_book(self, book):
    """
      Appends the borrowed book list.
      Returns: A updated list after book is returned.
    """
    self.borrowed_books_list.remove(book)

from datetime import datetime, timedelta
class Loan:
  """
    A class of Loan to manage the books in the library.
    Attributes: book(str): The book borrowed by the member of the library.
                member(str): The member who borrowed the book. 
  """
  counter = 1
  def __init__(self, book, member):
    """
      Initializes the Loan class with id, book, member, borrowed_date, due_date, return_date, status of loan.  
      Args: id (str): A unique loan id generated of every book issued in the library.
            book(str): String store book issued to the member.
            member(str): String store member issued the book.
            borrow_date(date): Date on which book is issued.
            due_date(date): Date by which book should be returned.
            return_date(date): Date when the book is returned.
            status(str): Status of loan.
    """
    self.loan_id = f"LN{Loan.counter:04d}"  
    Loan.counter += 1
    self.book = book
    self.member = member
    self.borrow_date = datetime.now()
    self.due_date = self.borrow_date + timedelta(days=14)
    self.return_date = None
    self.status = "active"

  def mark_returned(self):
    """
      Note the return date and update the loan status.
    """
    self.return_date = datetime.now()
    self.status = "returned"
      
class Library:
  """
    A class Library to integrate classes Catalog, Books, Member, Loans by involving functionality of the library.
    Attributes: Catalog (catalog): A instance of catalog class to manage books.
                members_list (list): List of registered members in the library.
                loans_list (list): List of current and past book loans.
                books_list (list): List of all books.
  """

  def __init__(self, catalog, member_list, loan_list, book_list):
    """
      Initializes the Library with catalog, member_list, loan_list, book_list.
      Args: catalog (Catalog): Catalog object to manage books.
            member_list (list): List to store registered members.
            loan_list (list): List to store loan records.
            book_list (list): List of book objects.
    """    
    self.catalog = catalog
    self.members_list = member_list
    self.loans_list = loan_list
    self.books_list = book_list
  
  def add_book(self, book):
    """
      Adds a book to the library's catalog.
      Args: book(book): The book instance to be added.
    """
    self.catalog.add_book(book)
    
  def register_member(self, member):
    """
      Register member to the library.
      Args: member(str): The member instance to be added.
    """  
    for m in self.members_list:
      if m.id == member.id:
        print(f"Member with ID '{member.id}' is already registered")
        return
    self.members_list.append(member)
    print(f"Member '{member.name}' registered successfully.")

  def lend_book(self, book_id, member_id):
    """
      Issues a book to the registered member if book is available.
      Args: book_id(str): Unique id of each book.
            member_id(str): Unique id of every registered member.
    """
    book = self.catalog.search_by_id(book_id)
    if not book:
      print(f"Book with ID '{book_id}' not found.")
      return
    if not book.is_available:
      print(f"Book '{book.title}' is currently not available.")
      return
    member = None
    for m in self.members_list:
      if m.id == member_id:
        member = m
        break
    if not member:
      print(f"Member with ID '{member_id}' not found.")
      return
    loan = Loan(book, member)
    book.mark_as_borrowed()
    member.borrow_book(book)
    self.loans_list.append(loan)
  
    print(f"Loan created: Book '{book.title}' lent to '{member.name}'. Due on {loan.due_date.date()}.")
  
  def return_book(self, book_id, member_id):
    """
      Processes the return of the book by a member and updates the loan status.
      Args: book_id(str): Unique id of each book.
            member_id(str): Unique id of every registered member.
    """
    member = None
    for m in self.members_list:
      if m.id == member_id:
        member = m
        break
    if not member:
      print(f"Member with ID '{member_id}' not found.")
      return    
    book = self.catalog.search_by_id(book_id)    
    if not book:
      print(f"Book with ID '{book_id}' not found in member's borrowed list.")
      return
    loan = None
    for l in self.loans_list:
      if l.book.id == book_id and l.member.id == member_id and l.status == "active":
        loan = l
        break
    if not loan:
      print(f"No active loan found for book ID '{book_id}' and member ID '{member_id}'.")
      return
    book.mark_as_returned()
    member.return_book(book)
    loan.mark_returned()

    print(f"Book '{book.title}' returned successfully by member '{member.name}'. Loan closed.")
  
def main():
  """
    The main function that demonstrates usage of the Library system:
    - Adds books to the catalog.
    - Registers members.
    - Lends books to members.
    - Returns some of the books.
    - Searches books by title and author.
  """
  member_list = []
  loan_list = []
  books_list = []
  catalog = Catalog(books_list)
  library = Library(catalog, member_list, loan_list, books_list)

  book1 = Book("The secret", "John Smith")
  book2 = Book("Bravo two zero", "Andy Mcnab")
  book3 = Book("OOP in Python", "Bob Miller")
  library.add_book(book1)
  library.add_book(book2)
  library.add_book(book3)

  member1 = Member("Akhil")
  member2 = Member("Nayan")
  member3 = Member("Ritu")
  library.register_member(member1)
  library.register_member(member2)
  library.register_member(member3)

  library.lend_book("B001", "M01")
  library.lend_book("B002", "M01")
  library.lend_book("B003", "M03")

  library.return_book("B001", "M01")
  library.return_book("B002", "M04")
  library.return_book("B004", "M02")
  
  catalog.search_by_title("python")
  catalog.search_by_author("johnson")

  catalog.remove_book("B003")
  catalog.remove_book("B004")

if __name__ == "__main__":
  main()
  
#Banking System
from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from typing import List

class Account(ABC):
  """
    Abstract base class representing a bank account.
    Attributes:
        account_number (str): Unique ID of the account.
        holder_name (str): Name of the account holder.
        balance (float): Current balance in the account.
  """
  counter = 1
  def __init__(self, account_number, holder_name, balance = 0.0):
    """
        Initialize a new account with a unique account number, holder name, and balance.
        Args:
            account_number (str): Not used (auto-generated internally).
            holder_name (str): Name of the account holder.
            balance (float, optional): Initial balance. Defaults to 0.0.
    """
    self.account_number = f"AT{Account.counter:03d}"
    Account.counter += 1
    self.holder_name = holder_name
    self.balance = balance
  @abstractmethod
  def deposit(self,amount):
    """Deposit a certain amount into the account."""
    pass
  @abstractmethod
  def withdraw(self,amount):
    """Withdraw a certain amount from the account."""
    pass
  def get_balance(self):
    """Returns:float: The current balance of the account."""
    return self.balance
  
class SavingsAccount(Account):
  """
    Savings account with a fixed interest rate.
    Attributes:
        interest_rate (float): Interest rate for the savings account (default is 4%).
  """
  def __init__(self, account_number, holder_name, balance=0.0):
    """
    Initialize a SavingsAccount instance.
    Args: account_number (str): The account number for the savings account.
          holder_name (str): The name of the account holder.
          balance (float, optional): The initial balance of the account. Defaults to 0.0.
    Attributes: interest_rate (float): The interest rate for the savings account, set to 4%.
    """
    super().__init__(account_number, holder_name, balance)
    self.interest_rate = 4  
  def deposit(self, amount):
    """Add the deposit amount to the balance."""
    self.balance += amount
  def withdraw(self,amount):
    """Withdraw amount if sufficient balance is available."""
    if amount <= self.balance:
      self.balance -= amount
    else:
      raise ValueError("Insufficient balance")
  def calculate_interest(self):
    """
        Calculate interest on current balance.
        Returns: float: Interest earned.
    """
    return self.balance * self.interest_rate/ 100

class CurrentAccount(Account):
  """
    Current account with an overdraft limit of 3% of balance.
    Attributes: overdraft_limit (float): Maximum allowable overdraft.
  """
  def __init__(self,account_number, holder_name, balance=0.0):
    """
        Initialize a current account with an overdraft limit.
        Args: account_number (str): Not used directly.
              holder_name (str): Name of the account holder.
              balance (float, optional): Initial balance. Defaults to 0.0.
        Attributes: overdraft_limit (float): Maximum amount that can be withdrawn beyond the current balance.
    """
    super().__init__(account_number, holder_name, balance)
    self.overdraft_limit = balance * 0.03 
  def deposit(self, amount):
    """Add deposit amount to the account balance."""
    self.balance += amount
  def withdraw(self, amount):
    """
        Withdraw amount if within balance and overdraft limit.
        Raises: ValueError: If withdrawal exceeds overdraft limit.
    """
    if amount <= self.balance + self.overdraft_limit:
      self.balance -= amount
    else:
      raise ValueError("Exceeds overdraft limit")

class FixedDepositAccount(Account):
  """
    Fixed deposit account with fixed interest and maturity date.
    Attributes: interest_rate (float): Interest rate for FD.
                maturity_date (date): Date when funds can be withdrawn.
    """
  def __init__(self, account_number, holder_name, deposit_amount):
    """
        Initializes FD with a deposit amount and sets maturity date.
        Args: deposit_amount (float): Amount to be deposited.
    """
    super().__init__(account_number, holder_name, balance=deposit_amount)
    self.interest_rate = 7
    self.maturity_date =  datetime.now().date() + timedelta(days = 365)
  def deposit(self, amount):
    """
        Disallowed operation for FD accounts.
        Raises: NotImplementedError: Always, since FD can't accept further deposits.
    """
    raise NotImplementedError("Cannot deposit to a fixed deposit account")
  def withdraw(self, amount):
    """
        Withdraw amount if on or after maturity date.
        Raises: ValueError: If trying to withdraw before maturity or insufficient balance.
    """
    today = datetime.now().date()
    if today >= self.maturity_date:
      if amount <= self.balance:
        self.balance -= amount
      else:
        raise ValueError("Insufficient balance")
    else:
      raise ValueError("Cannot withdraw before Maturity")
  def calculate_interest(self):
    """
        Calculates interest earned.
        Returns: float: Interest on deposit amount.
    """
    return self.balance * self.interest_rate / 100
  
class Transaction:
  def __init__(self, from_account: Account, to_account: Account, amount: float, txn_type: str):
    """
    Represents a transaction between accounts.
    Attributes:
        from_account (Account): Sender account.
        to_account (Account): Receiver account.
        amount (float): Amount to be transferred.
        timestamp (datetime): Time of transaction.
        type (str): Type of transaction ('deposit', 'withdraw', 'transfer').
    """
    self.from_account = from_account
    self.to_account = to_account
    self.amount = amount
    self.timestamp = datetime.now()
    self.type = txn_type
  def execute(self):
    """
        Execute the transaction based on type.
        Raises: ValueError: If transaction type is invalid.
    """
    if self.type == "transfer":
      self.from_account.withdraw(self.amount)
      self.to_account.deposit(self.amount)
    elif self.type == "deposit":
      self.to_account.deposit(self.amount)
    elif self.type == "withdraw":
      self.from_account.withdraw(self.amount)
    else:
      raise ValueError("Invalid transaction type")
       
class Bank:
  """
    Represents a bank that holds multiple accounts.
    Attributes: accounts (List[Account]): List of all accounts in the bank.
  """
  def __init__(self):
    """
    Initialize a Bank instance.
    Attributes: accounts (List[Account]): A list to store all accounts associated with the bank.
    """
    self.accounts: List[Account] = []

  def add_account(self, account: Account):
      """
        Add a new account to the bank.
        Args: account (Account): The account to add.
      """
      self.accounts.append(account)

  def find_account(self, account_number):
      """
        Find an account by account number.
        Args: account_number (str): The account number to search.
        Returns: Account: The matching account.
        Raises: ValueError: If account is not found.
      """
      for acc in self.accounts:
          if acc.account_number == account_number:
              return acc
      raise ValueError("Account not found")
   
def main():
    """
    The main function that demonstrates usage of the Bank system:
    - Creates different types of accounts.
    - Performs deposits, withdrawals, and transfers.
    - Displays balances.
    """
    bank = Bank()
    """Create and add accounts"""
    acc1 = SavingsAccount(None, "Anil", balance=10000)
    acc2 = CurrentAccount(None, "Namit", balance=5000)
    acc3 = FixedDepositAccount(None, "Vaishali", deposit_amount=15000)

    bank.add_account(acc1)
    bank.add_account(acc2)
    bank.add_account(acc3)

    """Perform Transactions"""
    try:
        txn1 = Transaction(None, acc1, 2000, "deposit")
        txn1.execute()
    except Exception as e:
        print("Transaction Error:", e)

    try:
        txn2 = Transaction(acc2, None, 1000, "withdraw")
        txn2.execute()
    except Exception as e:
        print("Transaction Error:", e)

    try:
        txn3 = Transaction(acc1, acc2, 3000, "transfer")
        txn3.execute()
    except Exception as e:
        print("Transaction Error:", e)

    try:
        txn4 = Transaction(acc3, None, 5000, "withdraw")  
        txn4.execute()
    except Exception as e:
        print("Transaction Error:", e)

    """Display Balances"""
    print(f"Balance of {acc1.account_number} (Savings): ₹{acc1.get_balance():.2f}")
    print(f"Balance of {acc2.account_number} (Current): ₹{acc2.get_balance():.2f}")
    print(f"Balance of {acc3.account_number} (Fixed Deposit): ₹{acc3.get_balance():.2f}")

    """Calculate Interest"""
    print(f"Interest on Savings Account: ₹{acc1.calculate_interest():.2f}")
    print(f"Interest on Fixed Deposit Account: ₹{acc3.calculate_interest():.2f}")

if __name__ == "__main__":
    main()   