import os

def clear_screen():
    os.system('cls')  

def check_answer(guess, answer):
    if guess == answer:
        print(f"You got it! The answer was {answer}.")
        return True 
    elif guess - 1 == answer or guess - 2 == answer:
        print("Very close! Reduce a little.")
    elif guess + 1 == answer or guess + 2 == answer:
        print("Very close! Rise a little.")
    elif guess > answer:
        print("Too high.")
    elif guess < answer:
        print("Too low.")
    return False

def game():
    print("Welcome to the Number Guessing Game!")
    answer = int(input("Player 1, enter the number for Player 2 to guess (1-100): "))

    clear_screen()  

    turns = 7
    guess = None

    while turns > 0:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if check_answer(guess,answer):
            return
        turns -= 1
        if turns == 0:
            print("You've run out of guesses, you lose.")
        else:
            print("Guess again.")

game()

#Pattern printing programs from nested loops
#right angle triangle
rows = int(input("Enter the number of rows: "))
for i in range(0,rows):
    for j in range(0,i+1):
        print("*",end=" ")
    print()
        
#inverted right angle triangle
rows = int(input("Enter the number of rows: "))
for i in range(rows,0,-1):
    for j in range(i):
        print("*",end = " ")
    print()
    
#right aligned triangle
rows = int(input("Enter the number of rows: "))
for i in range(1,rows+1):
    for spaces in range(rows-i):
        print(" ", end = "")
    for stars in range(i):
        print("*",end = " ")
    print()

#inverted right aligned triangle
rows = int(input("Enter the number of rows: "))
for i in range(rows,0,-1):
    for spaces in range(rows-i):
        print(" ", end = "")
    for stars in range(i):
        print("*",end = " ")
    print()