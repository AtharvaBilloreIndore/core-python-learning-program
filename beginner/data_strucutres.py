"""
Data Structures in Python

This file is intended to cover the following concepts related to Python data structures:
- Lists and list comprehensions
- Tuples and named tuples
- Dictionaries and dictionary comprehensions
- Sets and set operations
- Arrays and NumPy arrays
- Stacks and queues
- Linked lists
- Trees and graphs
- Heaps
- Collections module (Counter, defaultdict, OrderedDict, etc.)

The examples in this file will demonstrate how to use various data structures effectively in Python.
"""

# TODO: Add data structures examples and implementations

#TO -DO LIST
tasks = []

def to_do_list():
    print("\n--- To-Do List ---")
    print("Add Task")
    print("View Tasks")
    print("Delete Task")
    print("Exit")
    
while True:
    to_do_list()
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
                print(f"{i}.{task['desc']}")
    
    elif choice == "delete":
        index = int(input("Enter task number to delete: ")) - 1
        if 0<= index < len(tasks):
            remove = tasks.pop(index)
            print(f"Deleted task: {remove['desc']}")
        else:
            print("Invalid task index.")
    
    elif choice == "exit":
        print("Exiting to-do list.")
        break

    else:
        print("Invalid choice. Please enter correct choice.")
    

#Playlist manager for songs

favourite = []

def plmanager():
    print("\n--- Song List ---")
    print("add song")
    print("view songs")
    print("delete song")
    print("search song")
    print("exit")
    
while True:
    plmanager()
    choice = input("Enter your choice (add,view,delete,search,exit): ").lower()
    
    if choice == "add":
        song = input("Enter the song title").lower()
        if song:
            favourite.append({"title": song})
            print("Song added.")
        else:
            print("Song title cannot be empty.")
    
    elif choice == "view":
        if not favourite:
            print("No songs yet")
        else:
            for i, song in enumerate (favourite,1):
                print(f"{i}.{song['title']}")
    
    elif choice == "delete":
        title = input("Enter song title to delete: ").lower()
        for i, song in enumerate(favourite):
            if song['title'] == title:
                removed = favourite.pop(i)
                print(f"Deleted song {removed['title']}")
                break
        else:
            print("Invalid song title")
        
    elif choice == "search":
        words = input("Enter word(s) to search for songs: ").lower().split()
        found = False
        print("\nMatching Songs:")
        for song in favourite:
            if any(word in song['title'] for word in words):
                print(song['title'])
                found = True
        if not found:
            print("No matching songs found.")
    
    elif choice == "exit":
        print("Exiting the Playlist Manager. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")