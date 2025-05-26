from Tasks import calculator,text_analyzer,Grades,game,to_do_list
def personal_assistant():
    def greet():
        name = input("Can you help me with your name plaese? : ")
        message = print(f"Hello {name}, Your personal assistant is here.")
    greet()

    while True:
        print("/n--Main Menu--")
        print("1. Simple Calculator")
        print("2. Text Analyzer")
        print("3. Grading System")
        print("4. Number Guessing Game")
        print("5. To-Do List Manager")
        print("6. Exit")
        
        main_menu = {'1': calculator, '2': text_analyzer, '3': Grades,
                     '4': game, '5': to_do_list}
            
        task = input("Enter task tou want to perform:  ").lower()   
            
        if task in main_menu:
            perform = main_menu[task]()
            print("Perform: ",perform)
        elif task in ['exit', '6']:
            print("Thank you for using your assistant. Goodbye!")
            break
        else:
            print("Invalid task entered")
personal_assistant()