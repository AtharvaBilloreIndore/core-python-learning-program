class Book:
    """
    A class to represent a book in a personal library manager.
    
    Attributes:
        id (str): Unique identifier for the book.
        title (str): Title of the book.
        author (str): Author of the book.
        reading_status (str): Reading status: 'unread', 'reading', or 'read'.
    """
    counter = 1
    def __init__(self, title, author):
        """
        Initializes a new book.
        """
        self.id = f"B{Book.counter:03d}"
        Book.counter += 1
        self.title = title
        self.author = author
        self.reading_status = "unread"

    def update_status(self, new_status):
        """
        Updates the reading status of the book.
        Args: new_status (str): New status ('unread', 'reading', 'read').
        """
        valid_statuses = ["unread", "reading", "read"]
        if new_status.lower() in valid_statuses:
            self.reading_status = new_status.lower()
            print(f"Status of '{self.title}' updated to '{self.reading_status}'.")
        else:
            print("Invalid status. Choose from: unread, reading, read.")

    def __str__(self):
        """Returns a user-friendly string representation of the book."""
        return f"[{self.id}] {self.title} by {self.author} - Status: {self.reading_status}"


import csv
import os

class Catalog:
    """
    A class to manage a personal book catalog.
    Attributes: books_list (list): A list of Book objects in the catalog.
    """
    def __init__(self):
        """Initializes an empty catalog."""
        self.books_list = []

    def add_book(self, book):
        """Adds a new Book object to the catalog."""
        self.books_list.append(book)
        print(f"Book '{book.title}' by {book.author} added to your catalog.")

    def remove_book(self, book_id):
        """Removes a book from the catalog based on its ID."""
        book = self.search_by_id(book_id)
        if book:
            self.books_list.remove(book)
            print(f"Book '{book.title}' (ID: {book.id}) removed.")
        else:
            print(f"No book found with ID '{book_id}'.")

    def search_by_id(self, book_id):
        """Returns the Book object matching the given ID."""
        for book in self.books_list:
            if book.id == book_id:
                return book
        return None

    def search_by_title(self, title):
        """Searches and prints books that match the given title."""
        results = [book for book in self.books_list if title.lower() in book.title.lower()]
        if results:
            print(f"Books matching title '{title}':")
            for book in results:
                print(book)
        else:
            print(f"No books found with title containing '{title}'.")
        return results

    def search_by_author(self, author):
        """Searches and prints books written by the given author."""
        results = [book for book in self.books_list if author.lower() in book.author.lower()]
        if results:
            print(f"Books by author '{author}':")
            for book in results:
                print(book)
        else:
            print(f"No books found by author '{author}'.")
        return results

    def update_book_status(self, book_id, new_status):
        """Updates the reading status of a book identified by its ID."""
        book = self.search_by_id(book_id)
        if book:
            book.update_status(new_status)
        else:
            print(f"No book found with ID '{book_id}'.")

    def list_books(self):
        """Prints all books in the catalog."""
        if not self.books_list:
            print("Your personal library is empty.")
        else:
            print("Your Book Catalog:")
            for book in self.books_list:
                print(book)

    def save_to_csv(self, filename="beginner/library_manager/books.csv"):
        """Saves the current catalog to a CSV file."""
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["id", "title", "author", "reading_status"])
            for book in self.books_list:
                writer.writerow([book.id, book.title, book.author, book.reading_status])
        print("Books saved to CSV.")

    def load_from_csv(self, filename="beginner/library_manager/books.csv"):
        """Loads books from a CSV file."""
        try:
            with open(filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    book = Book(row['title'], row['author'])
                    book.id = row['id']
                    book.reading_status = row['reading_status']
                    self.books_list.append(book)
                    Book.counter = max(Book.counter, int(book.id[1:]) + 1)
            print("Books loaded from CSV.")
        except FileNotFoundError:
            print("No existing catalog file found. Starting fresh.")


def main():
    """
    Main function to run the interactive personal library manager.
    """
    catalog = Catalog()
    catalog.load_from_csv() 
    try:
        flag = True
        while flag:
            print("\n--- Personal Library Manager ---")
            print("1. Add Book")
            print("2. View All Books")
            print("3. Search by ID")
            print("4. Search by Title")
            print("5. Search by Author")
            print("6. Update Reading Status")
            print("7. Remove Book")
            print("8. Save & Exit")
            
            choice = input("Choose an option (1-8): ")

            if choice == "1": 
                title = input("Enter title: ")
                if title.isdigit():
                    print("Title cannot be just numbers.")
                    continue
                author = input("Enter author: ")
                if not author.replace(" ", "").isalpha():
                    print("Author name must contain alphabets and spaces only.")
                    continue
                book = Book(title, author)
                catalog.add_book(book)
            elif choice == "2":
                catalog.list_books()
            elif choice == "3":
                book_id = input("Enter Book ID: ")
                book = catalog.search_by_id(book_id)
                print(book if book else "Book not found.")
            elif choice == "4":
                title = input("Enter title to search: ")
                if title.isdigit():
                    print("Title cannot be just numbers.")
                    continue
                catalog.search_by_title(title)
            elif choice == "5":
                author = input("Enter author to search: ")
                if not author.replace(" ", "").isalpha():
                    print("Author name must contain alphabets and spaces only.")
                    continue
                catalog.search_by_author(author)
            elif choice == "6":
                book_id = input("Enter Book ID: ")
                status = input("Enter new status (unread/reading/read): ")
                catalog.update_book_status(book_id, status)
            elif choice == "7":
                book_id = input("Enter Book ID to remove: ")
                catalog.remove_book(book_id)
            elif choice == "8":
                catalog.save_to_csv()
                print("Goodbye! Your books have been saved.")
                flag = False
            else:
                print("Invalid choice. Please select a valid option.")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()