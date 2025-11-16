import subprocess
from load_student import load_student_data
from student_driver import student_driver

def main_menu():
    while True:
        print("\n===== MAIN MENU =====")
        print("1. Sign Up")
        print("2. Log In")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            run_java_signup()

        elif choice == "2":
            login()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

def run_java_signup():
    subprocess.run(["java", "SignUp"])

def login():
    print("\n=== LOGIN ===")
    name = input("Enter your name: ").strip()
    user_id = input("Enter your ID: ").strip()

    if user_id.startswith("900"):
        student = load_student_data(name, user_id)

        if student is None:
            print("Name or ID incorrect or student not found.")
            return
        for _ in range(50):
            print("\n")
        print(f"Welcome {student.full_name}!")
        student_driver(student)
    else:
        print("Non-student logins not implemented yet.")
        

    if user_id.startswith("800"):
        print("Admin login not implemented yet.")

    if user_id.startswith("700"):
        print("Professor login not implemented yet.")

if __name__ == "__main__":
    main_menu()
