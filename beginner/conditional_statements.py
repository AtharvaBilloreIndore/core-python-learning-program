"""
Conditional Statements in Python

This file is intended to cover the following concepts related to conditional statements in Python:
- if, elif, and else statements
- Comparison operators (==, !=, >, <, >=, <=)
- Logical operators (and, or, not)
- Nested conditional statements
- Conditional expressions (ternary operators)
- Truth value testing
- Short-circuit evaluation
- Pattern matching

The examples in this file will demonstrate how to use conditional statements effectively in Python.
"""

# TODO: Add conditional statements examples and implementations

def grading(marks=[]):
    grades = []
    for el in marks :
        if (el >= 90) :
            grades.append("Grade A")
    
        elif (80 <= el < 90) :
            grades.append("Grade B")
    
        elif (70 <= el < 80) :
            grades.append("Grade C")
    
        else:
            grades.append("Grade D")
    print(("Marks: ", marks))
    print(("Grades: ", grades))
    return (grades)
    
Grades(marks=[65,45,34,89,75,85,83,91])

def decision_maker():
    try: 
        age = int(input("Enter age: "))
        match age:
            case age if 21 <= age <= 60:
                salary = int(input("Enter monthly salary: ")) 
                employer_type = input("Enter type of employer: (Private, PSU, Government)")
                working_years = int(input("Enter no of years you worked: "))
                wyears = int(input("Enter no of years with current employer: "))
                is_eligible = (
                   (salary >= 30000) and
                    (employer_type in ("Private", "PSU", "Government")) and
                    (working_years >= 2) and
                    (wyears >= 1)
                )
                return ("Eligible for Loan" if is_eligible else "Not Eligible for Loan")
            case _:
                return ("Not Eligible for Loan (Invalid employer type)")
    except ValueError as e:
        print("\nInvalid input! You must enter numbers for age.")
        choice = input("Do you want to restart the program? (yes/no): ").strip().lower()
        
        if choice == "yes":
            Decision_Maker() 
        else:
            print("Program terminated")    
value = Decision_Maker()
print (value)

        