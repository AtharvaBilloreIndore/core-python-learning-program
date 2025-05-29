#CONTACT-BOOK
from collections import OrderedDict
import re
contact_book = OrderedDict()

def valid_phone(phone):
    a = str(phone)
    return a.isdigit() and len(a) == 10
def valid_name(name):
    name = name.strip()
    return len(name) >= 2 and name.replace(" ", "").isalpha()
def valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(pattern, email)

def add_contact(phone,name,email):
    name = name.strip()
    email = email.strip()    
    if not valid_phone(phone):
        print("Invalid phone number. It must contain exactly 10 digits.")
        return
    if not valid_email(email):
        print("Invlid email id.")
        return
    if not valid_name(name):
        print("Invalid name.")
        return
    if phone in contact_book:
        print("Contact with this phone number already exists")
    else:
        contact_book[phone] = {"name":name,"email": email}
        print("Contact added successfully")

def view_contact():
    if not contact_book:
        print("Contact book is empty")
    else:
        print("\nAll contacts:")
        for phone, details in contact_book.items():
            print(f"Phone: {phone}, Name: {details['name']}, Email: {details['email']}")

def search_contact(phone):
    if not valid_phone(phone):
        print("Invalid phone number. It must contain exactly 10 digits.")
        return
    if phone in contact_book: 
        details = contact_book[phone]
        print(f"Name: {details['name']}, Email: {details['email']}")
    else:
        print("Contact not found")

def update_contact(phone, new_name, new_email):
    new_name = new_name.strip()
    new_email = new_email.strip()
    if not valid_phone(phone):
        print("Invalid phone number.")
        return
    if not valid_name(new_name):
        print("Invalid name.")
        return
    if not valid_email(new_email):
        print("Invalid email.")
        return
    if phone not in contact_book:
        print("Contact not found.")
        return
    contact_book[phone] = {"name": new_name, "email": new_email}
    print("Contact updated successfully.")
    
def delete_contact(phone):
    if not valid_phone(phone):
        print("Invalid phone number.")
        return
    if phone in contact_book:
        del contact_book[phone]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def main():
    print("Welcome to Contact Book")
    try:
        run = True
        while run:
            print("\n===== Contact Book Menu =====")
            print("1. Add Contact")
            print("2. Search Contact by Phone")
            print("3. Display All Contacts")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")
            choice = input("Choose an option (1-6): ").strip()

            if choice == "1":
                phone = int(input("Enter phone number: "))
                name = input("Enter name: ")
                email = input(f"Enter email: ")
                add_contact(phone, name, email)

            elif choice == "2":
                phone = int(input("Enter phone number to search: "))
                search_contact(phone)

            elif choice == "3":
                display_contacts()

            elif choice == "4":
                phone = int(input("Enter phone number to update: "))
                new_name = input("Enter new name: ")
                new_email = input("Enter new email: ")
                update_contact(phone, new_name, new_email)

            elif choice == "5":
                phone = int(input("Enter phone number to delete: "))
                delete_contact(phone)

            elif choice == "6":
                print("Exiting Contact Book.")
                run = False
            else:
                print("Invalid choice. Please select 1-6.")
                
    except ValueError:
        print("Invalid input. Please enter correct values.")
main()