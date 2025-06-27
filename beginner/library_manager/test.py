import unittest
from unittest.mock import mock_open, patch
from main import Book, Catalog

class TestBook(unittest.TestCase):
    """
    Unit tests for the Book class.
    """
    def test_book_initialization(self):
        """
        Test that a book is correctly initialized.
        """
        book = Book("Nightangle", "Yuval Noah Harari")
        self.assertEqual(book.title, "Sapiens")
        self.assertEqual(book.author, "Yuval Noah Harari")
        self.assertEqual(book.reading_status, "unread")
        self.assertTrue(book.id.startswith("B"))
    def test_book_update_status_valid(self):
        """
        Test that the reading status of a book.
        """
        book = Book("Nightngle", "Yuval Noah Harari")
        book.update_status("reading")
        self.assertEqual(book.reading_status, "reading")

    def test_book_update_status_invalid(self):
        """
        Test that the reading status is invalid of a book.
        """
        book = Book("Nightangle", "Yuval Noah Harari")
        book.update_status("completed") 
        self.assertNotEqual(book.reading_status, "completed")
        self.assertEqual(book.reading_status, "unread") 

    def test_book_str(self):
        """
        Test the string representation of a book object.
        """
        book = Book("Titanic", "George Orwell")
        output = str(book)
        self.assertIn(book.title, output)
        self.assertIn(book.author, output)
        self.assertIn(book.id, output)

class TestCatalog(unittest.TestCase):
    """
    Unit tests for the Catalog class.
    """
    def setUp(self):
        """
        Set up a catalog with two books.
        """
        self.catalog = Catalog()
        self.book1 = Book("Titanic", "George Orwell")
        self.book2 = Book("Nightangle", "Yuval Noah Harari")
        self.catalog.add_book(self.book1)
        self.catalog.add_book(self.book2)

    def test_add_book(self):
        """
        Test that books are added to the catalog list.
        """
        self.assertEqual(len(self.catalog.books_list), 2)

    def test_remove_existing_book(self):
        """
        Test that an existing book can be removed by ID.
        """
        self.catalog.remove_book(self.book1.id)
        self.assertEqual(len(self.catalog.books_list), 1)

    def test_remove_nonexistent_book(self):
        """
        Test that removing a book with an invalid ID.
        """
        initial_count = len(self.catalog.books_list)
        self.catalog.remove_book("B999")
        self.assertEqual(len(self.catalog.books_list), initial_count)

    def test_search_by_id_found(self):
        """
        Test searching a book by a valid ID.
        """
        result = self.catalog.search_by_id(self.book1.id)
        self.assertEqual(result, self.book1)

    def test_search_by_id_not_found(self):
        """
        Test that searching with a nonexistent ID.
        """
        result = self.catalog.search_by_id("B999")
        self.assertIsNone(result)

    def test_search_by_title_match(self):
        """
        Test that searching by title.
        """
        results = self.catalog.search_by_title("Titanic")
        self.assertEqual(len(results), 1)

    def test_search_by_title_no_match(self):
        """
        Test that searching for a non-existent title.
        """
        results = self.catalog.search_by_title("Unknown")
        self.assertEqual(results, [])

    def test_search_by_author_match(self):
        """
        Test that searching by author name.
        """
        results = self.catalog.search_by_author("George")
        self.assertEqual(len(results), 1)

    def test_search_by_author_no_match(self):
        """
        Test that searching for a non-existent.
        """
        results = self.catalog.search_by_author("Nonexistent Author")
        self.assertEqual(results, [])

    def test_update_book_status_valid(self):
        """
        Test updating the reading status of a valid book ID.
        """
        self.catalog.update_book_status(self.book1.id, "read")
        self.assertEqual(self.book1.reading_status, "read")

    def test_update_book_status_invalid_id(self):
        """
        Test that updating the reading status for an invalid ID.
        """
        self.catalog.update_book_status("B999", "read")  

    @patch("builtins.open", new_callable=mock_open)
    def test_save_to_csv_creates_file(self, mock_file):
        """
        Test that saving to CSV calls.
        """
        self.catalog.save_to_csv("test_books.csv")
        mock_file.assert_called_with("test_books.csv", mode="w", newline='', encoding='utf-8')

    @patch("builtins.open", new_callable=mock_open, read_data="id,title,author,reading_status\nB001,Test Book,Test Author,read\n")
    def test_load_from_csv_populates_catalog(self, mock_file):
        """
        Test that loading from CSV file.
        """
        new_catalog = Catalog()
        new_catalog.load_from_csv("test_books.csv")
        self.assertEqual(len(new_catalog.books_list), 1)
        self.assertEqual(new_catalog.books_list[0].title, "Test Book")
        self.assertEqual(new_catalog.books_list[0].reading_status, "read")

    @patch("os.path.exists", return_value=False)
    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_load_from_csv_file_not_found(self, mock_open, mock_exists):
        """
        Test that loading from a nonexistent file.
        """
        new_catalog = Catalog()
        new_catalog.load_from_csv("nonexistent.csv")
        self.assertEqual(len(new_catalog.books_list), 0)

if __name__ == "__main__":
    unittest.main()
