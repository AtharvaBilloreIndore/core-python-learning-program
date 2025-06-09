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