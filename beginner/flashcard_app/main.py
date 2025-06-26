import os
import json
SUBJECT_FOLDER = "beginner/flashcard_app/subjects"
class Load:
    """Handles all loading, saving, and listing operations for flashcard subjects."""
    @staticmethod
    def get_subject_path(subject_name):
        """Returns the full path to the JSON file."""
        return os.path.join(SUBJECT_FOLDER, f"{subject_name}.json")

    @staticmethod
    def load_subject(subject_name):
        """Loads and returns the flashcard list for a subject."""
        path = Load.get_subject_path(subject_name)
        if not os.path.exists(path):
            return []
        with open(path, "r") as f:
            return json.load(f)

    @staticmethod
    def save_subject(subject_name, data):
        """Saves the provided flashcard list to the corresponding JSON file."""
        os.makedirs(SUBJECT_FOLDER, exist_ok=True)
        path = Load.get_subject_path(subject_name)
        with open(path, "w") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def list_subjects():
        """Returns a list of all subject names in the subject folder."""
        if not os.path.exists(SUBJECT_FOLDER):
            return []
        return [f[:-5] for f in os.listdir(SUBJECT_FOLDER) if f.endswith(".json")]

class Admin:
    """Provides administrative functions for a specific subject."""

    def __init__(self, subject):
        """
        Initializes the admin panel for a given subject.
        Args: subject (str): The name of the subject to manage.
        """
        self.subject = subject
        self.data = Load.load_subject(subject)

    def add_flashcard(self):
        """Adds a new flashcard to the current subject."""
        while True:
            question = input("Enter question: ").strip()
            if not question:
                print("Question cannot be empty.")
            elif question.isdigit():
                print("Question cannot be only numbers.")
            else:
                break
        while True:
            answer = input("Enter answer: ").strip()
            if not answer:
                print("Answer cannot be empty.")
            else:
                break
        self.data.append({"question": question, "answer": answer})
        Load.save_subject(self.subject, self.data)
        print("Flashcard added.")

    def update_flashcard(self):
        """Updates an existing flashcard."""
        if not self.data:
            print("No flashcards to update.")
            return
        for idx, card in enumerate(self.data):
            print(f"{idx + 1}. Q: {card['question']}")
        try:
            choice = int(input("Select flashcard number to update: ")) - 1
            if 1 <= choice < len(self.data):
                card = self.data[choice - 1]
                while True:
                    new_question = input("Enter new question: ").strip()
                    if not new_question:
                        print("❗ Question cannot be empty.")
                    elif new_question.isdigit():
                        print("❗ Question cannot be only numbers.")
                    elif "?" not in new_question:
                        print("❗ Question must include a question mark.")
                    else:
                        break
                while True:
                    new_answer = input("Enter new answer: ").strip()
                    if not new_answer:
                        print("❗ Answer cannot be empty.")
                    else:
                        break 
                card["question"] = new_question
                card["answer"] = new_answer
                Load.save_subject(self.subject, self.data)
                print("Flashcard updated.")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a valid number.")

    def delete_flashcard(self):
        """Deletes a selected flashcard from the current subject."""
        if not self.data:
            print("No flashcards to delete.")
            return
        for idx, card in enumerate(self.data):
            print(f"{idx + 1}. Q: {card['question']}")
        try:
            choice = int(input("Select flashcard number to delete: ")) - 1
            if 0 <= choice < len(self.data):
                del self.data[choice]
                Load.save_subject(self.subject, self.data)
                print("Flashcard deleted.")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a valid number.")

class User:
    """Allows a user to view flashcards from a selected subject."""

    def __init__(self, subject):
        """
        Initializes the user view for a given subject.
        Args: subject (str): The subject whose flashcards are to be viewed.
        """
        self.subject = subject
        self.data = Load.load_subject(subject)

    def view_flashcards(self):
        """Displays each flashcard's question and answer."""
        if not self.data:
            print("No flashcards found in this subject.")
            return
        for card in self.data:
            while True:
                response = input(f"\nQ: {card['question']} [Press only Enter to view answer]: ").strip()
                if response == "":
                    break
                else:
                    print("Please do not type anything. Just press Enter.")
            print(f"A: {card['answer']}")

def select_subject():
    """
    Allows user/admin to select an existing subject or create a new one.
    Returns: str or None: The chosen subject name, or None if the operation was cancelled/invalid.
    """
    subjects = Load.list_subjects()
    if subjects:
        print("\nAvailable Subjects:")
        for idx, subject in enumerate(subjects, 1):
            print(f"{idx}. {subject}")
    else:
        print("\nNo subjects found.")

    print(f"{len(subjects) + 1}. Create New Subject")
    try:
        choice = int(input("Choose a subject: ")) - 1
        if 0 <= choice < len(subjects):
            return subjects[choice]
        elif choice == len(subjects):
            while True:
                new_subject = input("Enter new subject name: ").strip()
                if not new_subject:
                    print("Subject name cannot be empty. Try again.")
                elif not new_subject.isalpha():
                    print("Subject name should contain only letters. Try again.")
                elif new_subject.lower() in [s.lower() for s in subjects]:
                    print("Subject already exists. Please choose another name.")
                else:            
                    Load.save_subject(new_subject, [])
                    print(f"Subject '{new_subject}' created.")
                    return new_subject
        else:
            print("Invalid choice.")
            return None
    except ValueError:
        print("Enter a valid number.")
        return None

def main():
    """
    Main function that runs the Flashcard App.
    """
    flag = True
    while flag:
        print("\nWelcome to Flashcard App")
        print("1. Admin Panel")
        print("2. User Panel")
        print("3. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            subject = select_subject()
            if subject:
                admin = Admin(subject)
                while True:
                    print(f"\n-- Admin Panel: {subject} --")
                    print("1. Add Flashcard")
                    print("2. Update Flashcard")
                    print("3. Delete Flashcard")
                    print("4. Back to Main Menu")
                    admin_choice = input("Choose an option: ").strip()
                    if admin_choice == "1":
                        admin.add_flashcard()
                    elif admin_choice == "2":
                        admin.update_flashcard()
                    elif admin_choice == "3":
                        admin.delete_flashcard()
                    elif admin_choice == "4":
                        break
                    else:
                        print("Invalid choice.")
        elif choice == "2":
            subject = select_subject()
            if subject:
                user = User(subject)
                print(f"\n-- Viewing Flashcards for '{subject}' --")
                user.view_flashcards()
        elif choice == "3":
            print("Exiting... Goodbye!")
            flag = False
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()