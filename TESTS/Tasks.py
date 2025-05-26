def calculator():
        
    def sum():
        n1 = float(input("Enter 1st number: "))
        n2  = float(input("Enter 2nd number: "))
        sum1 = n1 + n2
        return sum1
    
    def difference():
        n1 = float(input("Enter 1st number: "))
        n2  = float(input("Enter 2nd number: "))
        dif = n1 - n2
        return dif

    def product():
        n1 = float(input("Enter 1st number: "))
        n2  = float(input("Enter 2nd number: "))
        pro = n1 * n2
        return pro
    
    def division():
        n1 = float(input("Enter 1st number: "))
        n2  = float(input("Enter 2nd number: "))
        if n2 == 0: 
            raise ZeroDivisionError("Cannot divide by zero")
        quo = n1 / n2
        return quo

    operations = {
        'add': sum,
        'subtract': difference,
        'multiply': product,
        'divide': division
    }
    op = input("Operation you want to perform (add,subtract,multiply divide): ").lower()

    if op in operations:
        try:
            result = operations[op]()
            print("Result:", result)
        except ArithmeticError as e:
            print("Arithmetic Error:", e)
    else:
        print("Invalid operation.")


def text_analyzer():
    text = input("Enter a paragraph: ")

    character_count = len(text.split())

    reversed_text = text[::-1]
    uppercase_text = text.upper()
    lowercase_text = text.lower()
    
    print("\n--- Text Analyzer ---")
    print(f"Character Count: {character_count}")
    print(f"Word Count: {word_count}")
    print(f"Reversed Text: {reversed_text}")
    print(f"Uppercase Text: {uppercase_text}")
    print(f"Lowercase Text: {lowercase_text}")

def Grades():
    marks = int(input("Enter marks from (0-100): ")) 
    try:
        match marks:
            case marks if marks >= 90:
                print("Grade: A")
            case marks if 80<= marks < 90:
                print("Grade: B")
            case marks if 70<= marks <80:
                print("Grade: C")
            case marks if 60<= marks <70:
                print("Grade: D")
            case marks if 33<= marks<60:
                print("Grade: E")
            case marks if marks<33:
                print("Grade: F")
    except ValueError as e:
        print("\nInvalid input.")

import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear') 

def check_answer(guess, answer, turns):
    if guess == answer:
        print(f"You got it! The answer was {answer}.")
        return turns  
    elif guess - 1 == answer or guess - 2 == answer:
        print("Very close! Reduce a little.")
    elif guess + 1 == answer or guess + 2 == answer:
        print("Very close! Rise a little.")
    elif guess > answer:
        print("Too high.")
    elif guess < answer:
        print("Too low.")
    return turns - 1

def game():
    print("Welcome to the Number Guessing Game!")
    answer = int(input("Player 1, enter the number for Player 2 to guess (1-100): "))

    clear_screen()  

    turns = 7
    guess = 0

    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        else:
            print("Guess again.")

tasks = []

def to_do_list():
    print("\n--- To-Do List ---")
    print("Add Task")
    print("View Tasks")
    print("Delete Task")
    print("Exit")
    
    while True:
        choice = input("Enter your choice (add,view,delete,exit): ").lower()
    
        if choice == "add":
            task = input("Enter the task")
            tasks.append({"desc": task})
            print("Task added")
    
        elif choice == "view":
            if not tasks:
                print("No tasks yet")
            else:
                for i, task in enumerate (tasks,1):
                    print(f"{i}.{task["desc"]}")
    
        elif choice == "delete":
            index = int(input("Enter task number to delete: ")) - 1
            if 0<= index < len(tasks):
                remove = tasks.pop(index)
                print(f"Deleted task: {remove['desc']}")
            else:
                print("Invalid task index.")
    
        elif choice == "exit":
            print("Exit to main menu.")

        else:
            print("Invalid choice. Please enter correct choice.")
        break