from Student import Student

def load_student_data(name, user_id, database="Database/Accounts.txt"):
    try:
        with open(database, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                parts = [p.strip().strip('"') for p in line.split(",")]

                if len(parts) < 6:
                    continue

                if parts[0] == "STUDENT" and parts[1] == user_id and parts[2].lower() == name.lower():
                    return Student(
                        student_num=parts[1],
                        full_name=parts[2],
                        classification=parts[3],
                        major=parts[4],
                        fiscal_clearance=parts[5]
                    )

    except FileNotFoundError:
        print("ERROR: Accounts.txt not found.")

    return None
