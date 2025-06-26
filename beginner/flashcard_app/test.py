import unittest
from unittest.mock import patch, mock_open
import json
from main import Load, Admin, User, select_subject, main

class TestFlashcardApp(unittest.TestCase):
    """Unit test suite for Flashcard App components."""

    def test_get_subject_path(self):
        """Test if the correct file path is returned for a given subject name."""
        path = Load.get_subject_path("python")
        self.assertIn("python.json", path)

    @patch("builtins.open", new_callable=mock_open, read_data='[{"question": "Q?", "answer": "A"}]')
    @patch("os.path.exists", return_value=True)
    def test_load_subject(self, mock_exists, mock_file):
        """Test if flashcards are properly loaded from a subject file."""
        data = Load.load_subject("test")
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["question"], "Q?")

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.makedirs")
    def test_save_subject(self, mock_makedirs, mock_file):
        """Test saving flashcard data to a subject file."""
        sample = [{"question": "Q?", "answer": "A"}]
        Load.save_subject("test", sample)
        mock_file().write.assert_called()

    @patch("os.listdir", return_value=["python.json", "notes.txt", "dsa.json"])
    @patch("os.path.exists", return_value=True)
    def test_list_subjects(self, mock_exists, mock_listdir):
        """Test listing of subject files (only .json files)."""
        subjects = Load.list_subjects()
        self.assertEqual(subjects, ["python", "dsa"])

    @patch("builtins.input", side_effect=["What is Python?", "A language"])
    @patch("main.Load.save_subject")
    def test_add_flashcard_valid(self, mock_save, mock_input):
        """Test adding a valid flashcard."""
        admin = Admin("test")
        admin.data = []
        admin.add_flashcard()
        self.assertEqual(len(admin.data), 1)
        self.assertIn("question", admin.data[0])

    @patch("builtins.input", side_effect=["1", "What is Python?", "A language"])
    @patch("main.Load.save_subject")
    def test_update_flashcard_valid(self, mock_save, mock_input):
        """Test updating an existing flashcard."""
        admin = Admin("test")
        admin.data = [{"question": "Old?", "answer": "OldA"}]
        admin.update_flashcard()
        self.assertEqual(admin.data[0]["question"], "What is Python?")

    @patch("builtins.input", side_effect=["1"])
    @patch("main.Load.save_subject")
    def test_delete_flashcard_valid(self, mock_save, mock_input):
        """Test deleting a flashcard."""
        admin = Admin("test")
        admin.data = [{"question": "Q1", "answer": "A1"}]
        admin.delete_flashcard()
        self.assertEqual(len(admin.data), 0)
        
    @patch("builtins.input", side_effect=["", ""])
    def test_view_flashcards(self, mock_input):
        """Test viewing flashcards.."""
        user = User("test")
        user.data = [
            {"question": "Q1?", "answer": "A1"},
            {"question": "Q2?", "answer": "A2"}
        ]
        with patch("builtins.print") as mock_print:
            user.view_flashcards()
            mock_print.assert_any_call("A: A1")
            mock_print.assert_any_call("A: A2")

    @patch("builtins.input", side_effect=["1"])
    @patch("main.Load.list_subjects", return_value=["python", "dsa"])
    def test_select_existing_subject(self, mock_list, mock_input):
        """Test selecting an existing subject."""
        subject = select_subject()
        self.assertEqual(subject, "python")

    @patch("builtins.input", side_effect=["3", "maths"])
    @patch("main.Load.list_subjects", return_value=["python", "dsa"])
    @patch("main.Load.save_subject")
    def test_create_new_subject(self, mock_save, mock_list, mock_input):
        """Test creating a new subject when selected from the menu."""
        subject = select_subject()
        self.assertEqual(subject, "maths")
        mock_save.assert_called_once()

    @patch("builtins.input", side_effect=["5"])
    @patch("main.Load.list_subjects", return_value=["python", "dsa"])
    def test_invalid_subject_choice(self, mock_list, mock_input):
        """Test handling of invalid subject selection (index out of range)."""
        subject = select_subject()
        self.assertIsNone(subject)

    @patch("builtins.input", side_effect=["invalid"])
    @patch("main.Load.list_subjects", return_value=["python"])
    def test_non_integer_subject_choice(self, mock_list, mock_input):
        """Test handling of non-integer input."""
        subject = select_subject()
        self.assertIsNone(subject)

    @patch("builtins.input", side_effect=["3", "", "science"])
    @patch("main.Load.list_subjects", return_value=["python", "dsa"])
    @patch("main.Load.save_subject")
    def test_create_subject_with_empty_then_valid(self, mock_save, mock_list, mock_input):
        """Test subject creation with empty input."""
        subject = select_subject()
        self.assertEqual(subject, "science")
        mock_save.assert_called_once()

    @patch("builtins.input", side_effect=["3"])  # Exit immediately
    @patch("builtins.print")
    def test_main_exit_immediately(self, mock_print, mock_input):
        """Test if the application exits properly when 'Exit' is chosen."""
        main()
        mock_print.assert_any_call("Exiting... Goodbye!")

if __name__ == "__main__":
    unittest.main()
