import json
import os

def access_questions(filename):
    """
    Loads quiz questions from a JSON file.
    Args: filename (str): The path to the JSON file containing quiz data.
    Returns: list: A list of question dictionaries loaded from the file.
    Side Effects: Prints the title of the quiz to the console.
    """
    with open(filename, 'r') as f:
        data = json.load(f)
        print(f"\nTitle: {data['title']}")
        return data['questions']

def quiz(questions):
    """
    Quiz is conducted by iterating over the questions and collecting user answers.
    Args: questions (list): A list of dictionaries where each dictionary represents a question.
    Side Effects: Prompts user for input, prints each question and final score.
    Exceptions: Handles invalid choices and unexpected exceptions during quiz execution.
    """
    score = 0
    for index, q in enumerate(questions, start=1):
        print(f"\nQ{index}: {q['question_text']}")
        for label, option in q['options'].items():
            print(f"{label}. {option}")

        try:
            choice = input("Your choice (A-D): ").strip().upper()
            if choice not in q['options']:
                raise ValueError("Invalid option.")
            if choice == q['correct_option']:
                print("Correct")
                score += 1
            else:
                print(f"Wrong. Correct answer: {q['correct_option']}")
        except ValueError as ve:
            print(f"{ve}")
        except Exception as e:
            print(f" Unexpected error: {e}")
    
    print(f"\n Final score: {score}/{len(questions)}")

def main():
    """
    Main function to run the quiz application.
    Side Effects: Prints prompts, errors, and quiz content to the console.
    Exceptions: Handles missing files and unexpected errors.
    """
    try:
        valid_subjects = ["ai_ml", "aptitude", "economics", "gk", "programming"]
        levels = ["easy", "medium", "advance"]
        
        print("Welcome to the Quiz!")
        print("Subjects available: ai_ml, aptitude, economics, gk, programming")
        
        subject = input("Which subject you want to play the quiz? ").strip().lower()
        if subject not in valid_subjects:
            print("Invalid subject. Exit!")
            return
        
        level = input("Choose the level of difficulty: (easy, medium, advance): ").strip().lower()
        if level not in levels:
            print("Invalid level. Exit!")
            return
        
        filename = f"beginner/quiz_data/{subject}/{subject}_{level}.json"
        
        if not os.path.exists(filename):
            print(f"No quiz found for subject.")
        else:
            questions = access_questions(filename)
            quiz(questions)
    
    except FileNotFoundError:
        print("Quiz file not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
