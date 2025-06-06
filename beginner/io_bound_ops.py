"""
I/O Bound Operations in Python

This file is intended to cover the following concepts related to I/O bound operations in Python:
- File handling (opening, reading, writing, closing)
- Working with text and binary files
- File paths and the os module
- Exception handling for I/O operations
- Working with CSV, JSON, and other data formats
- Network I/O and socket programming
- Database operations
- Asynchronous I/O
- Multithreading for I/O bound tasks
- Context managers for resource handling

The examples in this file will demonstrate how to handle I/O operations efficiently in Python.
"""

# TODO: Add I/O bound operations examples and implementations
from datetime import datetime
def create_entry():
    entry = input("Enter your journal entry: ")
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("journal.txt", "a") as file:
        file.write(f"\n{entry} {date_str}")
    print("Entry saved!\n")
    
def read_entries():
    try:
        with open("journal.txt", "r") as file:
            content = file.read()
            print("\nJournal Entries\n")
            print(content)
    except FileNotFoundError:
        print("No journal entries found yet.\n")
        
def main():
    try:
        flag = True
        while flag:
            print("1. Write a new entry")
            print("2. Read past entries")
            print("3. Exit")
            choice = int(input("Choose an option: "))
            if choice not in [1, 2, 3]:
                raise ValueError("Choice out of valid range.")
            if choice == 1:
                create_entry()
            elif choice == 2:
                read_entries()
            elif choice == 3:
                print("Goodbye!")
                flag = False
                break
            else:
                print("Invalid choice. Try again.\n")      
    except ValueError as e:
            print(f"Invalid input: {e}")
            return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return
main()