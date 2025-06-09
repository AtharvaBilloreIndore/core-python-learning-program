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

import csv
import json

def read_csv(filename):
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        return list(reader)
    
def read_json(filename):
    with open(filename, mode='r') as file:
        return json.load(file)

def filter_by_grade(data, grade):
    return [student for student in data if student["grade"] == grade]

def calculate_average_age(data):
    ages = [int(student["age"]) for student in data]
    return sum(ages) / len(ages) if ages else 0

def save_as_json(data, filename):
    if not data:
        print("No data to save.")
        return
    with open(filename, mode='w') as file:
        json.dump(data, file, indent=4)

def save_as_csv(data, filename):
    if not data:
        print("No data to save.")
        return
    with open(filename, mode='w', newline='') as file:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    print(f"Data saved to '{filename}'")

def main():
    try: 
        file_format = input("Enter file format (csv/json): ").strip().lower()
        filename = input("Enter the file name (with path if needed): ").strip()
        if file_format == "csv":
            try:
                data = read_csv(filename)
            except FileNotFoundError:
                print(f"File '{filename}' not found.")
                return
        elif file_format == "json":
            try:
                data = read_json(filename)
            except FileNotFoundError:
                print(f"File '{filename}' not found.")
                return
        else:
            print("Invalid format. Please enter either 'csv' or 'json'.")
            return
    
        print("\nAll Students:")
        print(data)
    
        grade_a_students = filter_by_grade(data, "A")
        print("\nStudents with grade A:")
        print(grade_a_students)

        avg_age = calculate_average_age(data)
        print(f"\nAverage age of students: {avg_age:.2f}")

        save_as_json(grade_a_students, "grade_a_students.json")
        print("\nFiltered data saved to grade_a_students.json")

        save_as_csv(grade_a_students, "grade_a_students.csv")
        print("\nFiltered data saved to grade_a_students.csv")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return
main()