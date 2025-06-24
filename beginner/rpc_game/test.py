import unittest
from unittest.mock import patch
from main import computer, player, main

class TestRockPaperScissors(unittest.TestCase):
    """
    Unit tests for the Rock-Paper-Scissors game.
    """
    @patch("builtins.input", side_effect=["rock", "no"])
    def test_computer_valid_choice(self, mock_input):
        """Test a valid choice in computer mode."""
        result = computer()
        self.assertIsNone(result)  
    
    @patch("builtins.input", side_effect=["invalid", "rock", "no"])
    def test_computer_invalid_choice(self, mock_input):
        """Test invalid choice in computer mode."""
        result = computer()
        self.assertIsNone(result)

    @patch("builtins.input", side_effect=["rock", "maybe"])
    def test_computer_invalid_play_again(self, mock_input):
        """Test play again is invalid in computer mode."""
        result = computer()
        self.assertIsNone(result)
        
    @patch("builtins.input", side_effect=["rock", "scissors", "no"])
    def test_player1(self, mock_input):
        """Test player mode where Player 1 wins."""
        result = player()
        self.assertIsNone(result)

    @patch("builtins.input", side_effect=["paper", "paper", "no"])
    def test_tie(self, mock_input):
        """Test a tie scenario in player mode."""
        result = player()
        self.assertIsNone(result)

    @patch("builtins.input", side_effect=["banana", "rock", "paper", "scissors", "no"])
    def test_invalid_player1_choice(self, mock_input):
        """Test player mode with an invalid Player 1 input."""
        result = player()
        self.assertIsNone(result)

    @patch("builtins.input", side_effect=["rock", "banana", "rock", "scissors", "no"])
    def test_invalid_player2_choice(self, mock_input):
        """Test player mode with an invalid Player 2 input."""
        result = player()
        self.assertIsNone(result)

    @patch("builtins.input", side_effect=["rock", "scissors", "maybe"])
    def test_invalid_play_again_input(self, mock_input):
        """Test player mode when 'play again' input is invalid."""
        result = player()
        self.assertIsNone(result)

    @patch("builtins.input", side_effect=["computer", "rock", "no"])
    def test_main_computer_mode(self, mock_input):
        """Test the main function when user selects 'computer' mode."""
        result = main()
        self.assertIsNone(result)

    @patch("builtins.input", side_effect=["player", "rock", "paper", "no"])
    def test_main_player_mode(self, mock_input):
        """Test the main function when user selects 'player' mode."""
        result = main()
        self.assertIsNone(result)

    @patch("builtins.input", side_effect=["xyz"])
    def test_main_invalid_mode(self, mock_input):
        """Test the main function with an invalid mode."""
        result = main()
        self.assertEqual(result, "Invalid choice")
        
if __name__ == "__main__":
    unittest.main()
