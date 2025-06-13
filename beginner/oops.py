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