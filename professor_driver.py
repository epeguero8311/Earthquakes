import sys
from pathlib import Path

root_folder = Path(__file__).parent.parent
sys.path.insert(0, str(root_folder))

from Functions import clear_screen

def professor_driver(professor):
    while True:
        print("\n===== PROFESSOR MENU =====")
        print("1. View Info")
        print("2. View Assigned Courses")
        print("3. Assign Course")
        print("4. Remove Course")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            clear_screen()
            print(f"Displaying {professor.full_name} Information")
            professor.display_info()
        elif choice == "2":
            clear_screen()
            print(f"\n{professor.full_name}'s Assigned Courses:")
            if professor.assigned_courses:
                for course in professor.assigned_courses:
                    print(f" - {course}")
            else:
                print("No courses assigned.")
        elif choice == "3":
            clear_screen()
            crn = input("Enter course CRN to assign: ")
            professor.assign_course(crn)
        elif choice == "4":
            clear_screen()
            crn = input("Enter course CRN to remove: ")
            professor.remove_course(crn)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")