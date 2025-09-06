import unittest
from unittest.mock import patch, mock_open
import builtins
import os
import json

from beginner.quiz_data.main import access_questions, quiz, main

class TestQuizApp(unittest.TestCase):
    #Unit test class for testing the functionality of the Quiz App.
    def setUp(self):
        #Prepare sample quiz data for use in multiple test cases.
        self.sample_json = {
            "title": "Sample Quiz",
            "questions": [
                {
                    "question_text": "What is AI?",
                    "options": {
                        "A": "Artificial Intelligence",
                        "B": "Automated Interface",
                        "C": "Analog Input",
                        "D": "None"
                    },
                    "correct_option": "A"
                }
            ]
        }

    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps({
        "title": "Sample Quiz",
        "questions": [
            {
                "question_text": "What is AI?",
                "options": {
                    "A": "Artificial Intelligence",
                    "B": "Automated Interface",
                    "C": "Analog Input",
                    "D": "None"
                },
                "correct_option": "A"
            }
        ]
    }))
    def test_access_questions_valid(self, mock_file):
        #Test whether access_questions correctly reads and parses valid JSON data.
        questions = access_questions("dummy_file.json")
        self.assertEqual(len(questions), 1)
        self.assertEqual(questions[0]['question_text'], "What is AI?")
        self.assertEqual(questions[0]['correct_option'], "A")

    @patch("builtins.input", side_effect=["A"])
    def test_quiz_correct_answer(self, mock_input):
        #Test quiz function with correct user answer.
        with patch("builtins.print") as mock_print:
            quiz(self.sample_json['questions'])
            mock_print.assert_any_call("Correct")
            mock_print.assert_any_call("\n Final score: 1/1")

    @patch("builtins.input", side_effect=["Z"])
    def test_quiz_invalid_option(self, mock_input):
        #Test quiz function with an invalid option (not A/B/C/D).
        with patch("builtins.print") as mock_print:
            quiz(self.sample_json['questions'])
            mock_print.assert_any_call("Invalid option.")
            mock_print.assert_any_call("\n Final score: 0/1")

    @patch("builtins.input", side_effect=["maths", "easy"])
    def test_main_invalid_subject(self, mock_input):
        #Test main function behavior when an invalid subject is given.
        with patch("builtins.print") as mock_print:
            main()
            mock_print.assert_any_call("Invalid subject. Exit!")

    @patch("builtins.input", side_effect=["ai_ml", "hard"])
    def test_main_invalid_level(self, mock_input):
        #Test main function behavior when an invalid quiz level is given.
        with patch("builtins.print") as mock_print:
            main()
            mock_print.assert_any_call("Invalid level. Exit!")

    @patch("builtins.input", side_effect=["ai_ml", "easy"])
    @patch("os.path.exists", return_value=False)
    def test_main_file_not_found(self, mock_exists, mock_input):
        #Test main function when the expected quiz file is not found in the path.
        with patch("builtins.print") as mock_print:
            main()
            mock_print.assert_any_call("No quiz found for subject.")
