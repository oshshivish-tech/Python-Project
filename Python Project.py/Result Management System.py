# Student Result Management System


FILENAME = "students.txt"

def calculate_total_and_percentage(marks):
    total = sum(marks)
    percentage = total / len(marks)
    return total, percentage

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"

def add_student():
    print("\n--- Add Student Record ---")
    roll = input("Enter Roll Number: ").strip()
    name = input("Enter Name: ").strip()
    try:
        n = int(input("Enter number of subjects: "))
    except ValueError:
        print("Invalid number of subjects.")
        return

    marks = []
    for i in range(1, n + 1):
        try:
            m = float(input(f"Enter marks for Subject {i}: "))
        except ValueError:
            print("Invalid marks, setting 0 for this subject.")
            m = 0.0
        marks.append(m)

    total, percentage = calculate_total_and_percentage(marks)
    grade = calculate_grade(percentage)

    marks_str = ",".join(str(m) for m in marks)
    record = f"{roll}|{name}|{marks_str}|{total}|{percentage:.2f}|{grade}\n"

    with open(FILENAME, "a") as f:
        f.write(record)

    print("Student record added successfully.")

def load_students():
    
    students = []
    try:
        with open(FILENAME, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split("|")
                if len(parts) < 6:
                    continue
                roll = parts[0]
                name = parts[1]
                marks_str = parts[2]
                total = float(parts[3])
                percentage = float(parts[4])
                grade = parts[5]
                marks = [float(m) for m in marks_str.split(",") if m]
                students.append({
                    "roll": roll,
                    "name": name,
                    "marks": marks,
                    "total": total,
                    "percentage": percentage,
                    "grade": grade
                })
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        
        pass
    return students

def save_students(students):
    with open(FILENAME, "w") as f:
        for s in students:
            marks_str = ",".join(str(m) for m in s["marks"])
            record = f"{s['roll']}|{s['name']}|{marks_str}|{s['total']}|{s['percentage']:.2f}|{s['grade']}\n"
            f.write(record)

def display_all_students():
    print("\n--- All Student Records ---")
    students = load_students()
    if not students:
        print("No records found.")
        return

    for s in students:
        print(f"Roll: {s['roll']}")
        print(f"Name: {s['name']}")
        print(f"Marks: {s['marks']}")
        print(f"Total: {s['total']}")
        print(f"Percentage: {s['percentage']:.2f}")
        print(f"Grade: {s['grade']}")
        print("-" * 30)

def search_student():
    print("\n--- Search Student ---")
    roll = input("Enter Roll Number to search: ").strip()
    students = load_students()
    for s in students:
        if s["roll"] == roll:
            print("Record found:")
            print(f"Roll: {s['roll']}")
            print(f"Name: {s['name']}")
            print(f"Marks: {s['marks']}")
            print(f"Total: {s['total']}")
            print(f"Percentage: {s['percentage']:.2f}")
            print(f"Grade: {s['grade']}")
            return
    print("No record found for this roll number.")

def update_student():
    print("\n--- Update Student Record ---")
    roll = input("Enter Roll Number to update: ").strip()
    students = load_students()
    found = False

    for s in students:
        if s["roll"] == roll:
            found = True
            print("Existing record:")
            print(f"Name: {s['name']}")
            print(f"Marks: {s['marks']}")
            new_name = input("Enter new name (leave blank to keep same): ").strip()
            if new_name:
                s["name"] = new_name

            choice = input("Do you want to update marks? (y/n): ").strip().lower()
            if choice == "y":
                try:
                    n = int(input("Enter number of subjects: "))
                except ValueError:
                    print("Invalid number, keeping old marks.")
                    break
                new_marks = []
                for i in range(1, n + 1):
                    try:
                        m = float(input(f"Enter marks for Subject {i}: "))
                    except ValueError:
                        print("Invalid marks, setting 0 for this subject.")
                        m = 0.0
                    new_marks.append(m)
                s["marks"] = new_marks
                total, percentage = calculate_total_and_percentage(new_marks)
                s["total"] = total
                s["percentage"] = percentage
                s["grade"] = calculate_grade(percentage)

            break

    if not found:
        print("No record found for this roll number.")
    else:
        save_students(students)
        print("Record updated successfully.")

def delete_student():
    print("\n--- Delete Student Record ---")
    roll = input("Enter Roll Number to delete: ").strip()
    students = load_students()
    new_list = [s for s in students if s["roll"] != roll]

    if len(new_list) == len(students):
        print("No record found for this roll number.")
    else:
        save_students(new_list)
        print("Record deleted successfully.")

def show_class_topper():
    print("\n--- Class Topper ---")
    students = load_students()
    if not students:
        print("No records found.")
        return
    topper = max(students, key=lambda s: s["percentage"])
    print(f"Topper Roll: {topper['roll']}")
    print(f"Topper Name: {topper['name']}")
    print(f"Percentage: {topper['percentage']:.2f}")
    print(f"Grade: {topper['grade']}")

def main_menu():
    while True:
        print("\n===== Student Result Management System =====")
        print("1. Add Student Record")
        print("2. Display All Records")
        print("3. Search Student by Roll Number")
        print("4. Update Student Record")
        print("5. Delete Student Record")
        print("6. Show Class Topper")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            display_all_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            show_class_topper()
        elif choice == "7":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")



print(main_menu())

