"""
Python Data Types

This file is intended to cover the following concepts related to Python data types:
- Numeric types (int, float, complex)
- String type and string operations
- Boolean type and logical operations
- Type conversion and type checking
- None type
- Sequences, mappings, and sets
- Mutable vs immutable types
- Memory management and references
- Type annotations (Python 3.5+)

The examples in this file will demonstrate how to work with various data types in Python.
"""

# TODO: Add data types examples and implementations

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
            return "Cannot divide by zero"
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
        result = operations[op]()  
        print("Result:", result)
    else:
        print("Invalid operation.")

calculator()

def greet():
    name = input("Enter your name: ")
    message = print("Hey,",name,  "I welcome you to python community of Hyderabad." )
greet()

def text_analyzer():
    text = input("Enter some text: ")

    character_count = len(text)
    word_count = len(text.split())
    reversed_text = text[::-1]
    uppercase_text = text.upper()
    lowercase_text = text.lower()
    
    print("\n--- Text Analyzer ---")
    print(f"Character Count: {character_count}")
    print(f"Word Count: {word_count}")
    print(f"Reversed Text: {reversed_text}")
    print(f"Uppercase Text: {uppercase_text}")
    print(f"Lowercase Text: {lowercase_text}")

    substring = input("\nEnter a substring to find: ")
    index = text.find(substring)
    if index != -1:
        print(f"Substring '{substring}' found at index {index}.")
    else:
        print(f"Substring '{substring}' not found.")

    old_substring = input("\nEnter a substring to replace: ")
    new_substring = input("Enter the new substring: ")
    replaced_text = text.replace(old_substring, new_substring)
    print(f"Text after replacement: {replaced_text}")

text_analyzer()