import random
import os

def computer():
    """
    Runs the Rock-Paper-Scissors game in computer mode.
    Returns: "Invalid choice" if the input is not one of the expected options.
    """
    option = ['rock', 'paper', 'scissors']
    flag = True
    while flag:
        try:
            user = input("Enter your choice (rock, paper, scissors): ").strip().lower()
            if user not in option:
                raise ValueError("Invalid choice")
        except ValueError as e:
            print(e)
            continue

        computer_choice = random.choice(option)
        print(f"Computer choose: {computer_choice}")

        if user == computer_choice:
            print("Tie")
        elif (user == 'rock' and computer_choice == 'scissors') or \
             (user == 'paper' and computer_choice == 'rock') or \
             (user == 'scissors' and computer_choice == 'paper'):  # Fixed typo: 'scissor' → 'scissors'
            print("You win")
        else:
            print("Computer wins")

        play = input("Want to play again?(yes, no): ").strip().lower()
        try:
            if play not in ['yes', 'no']:
                raise ValueError("Invalid choice")
            if play == 'no':
                flag = False
        except ValueError as e:
            print(e)
            flag = False

def player():
    """
    Runs the Rock-Paper-Scissors game in two-player mode.
    Returns: "Invalid choice" if the input is not one of the expected options.
    """
    option = ['rock', 'paper', 'scissors']
    flag = True
    while flag:
        try:
            player1 = input("Player1 enter your choice(rock paper scissors): ").strip().lower()
            if player1 not in option:
                raise ValueError("Invalid choice")
            os.system('cls')  # Clears screen on Windows for fairness
            player2 = input("Player2 enter your choice(rock, paper, scissors): ").strip().lower()
            if player2 not in option:
                raise ValueError("Invalid choice")
        except ValueError as e:
            print(e)
            continue

        if player1 == player2:
            print("Tie")
        elif (player1 == 'rock' and player2 == 'scissors') or \
             (player1 == 'paper' and player2 == 'rock') or \
             (player1 == 'scissors' and player2 == 'paper'):
            print("Player 1 wins")
        else:
            print("Player 2 wins")

        play = input("Want to play again?(yes, no): ").strip().lower()
        try:
            if play not in ['yes', 'no']:
                raise ValueError("Invalid choice")
            if play == 'no':
                flag = False
        except ValueError as e:
            print(e)
            flag = False

def main():
    """
    Entry point for the Rock-Paper-Scissors game.
    Returns: "Invalid choice" if the input is not one of the expected options.
    """
    print("Welcome to Rock-Paper-Scissors game")
    a = ['computer', 'player']
    try:
        choice = input("Whom you want to play with? (1. computer, 2. player): ")
        if choice not in a:
            return "Invalid choice"
    except ValueError:
        print("Invalid input")
        return

    if choice == 'computer':
        computer()
    else:
        player()

if __name__ == "__main__":
    main()
