def display_menu():
    print("\nStudent Management System")
    print("1. Add student")
    print("2. View students")
    print("3. Search student")
    print("4. Exit")


def get_menu_choice():
    while True:
        choice = input("Enter your choice (1-4): ").strip()
        if choice in ["1", "2", "3", "4"]:
            return choice
        print("Invalid choice. Please enter a number from 1 to 4.")


def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty.")


def get_student_id():
    while True:
        student_id = input("Enter student ID: ").strip()
        if student_id.isdigit():
            return student_id
        print("Student ID must contain numbers only.")


def get_contact_number():
    while True:
        contact_number = input("Enter contact number: ").strip()
        if contact_number.isdigit() and len(contact_number) >= 7:
            return contact_number
        print("Contact number must be numeric and at least 7 digits.")


def student_exists(students, student_id):
    for student in students:
        if student["student_id"] == student_id:
            return True
    return False


def find_student(students, student_id):
    for student in students:
        if student["student_id"] == student_id:
            return student
    return None


def add_student(students):
    print("\nAdd Student")
    student_id = get_student_id()

    if student_exists(students, student_id):
        print("Student ID already exists.")
        return

    name = get_non_empty_input("Enter student name: ")
    course = get_non_empty_input("Enter course: ")
    year_level = get_non_empty_input("Enter year level: ")
    contact_number = get_contact_number()

    student = {
        "student_id": student_id,
        "name": name,
        "course": course,
        "year_level": year_level,
        "contact_number": contact_number,
    }
    students.append(student)
    print("Student added successfully.")


def view_students(students):
    print("\nStudent List")
    if len(students) == 0:
        print("No student records available.")
        return

    for index, student in enumerate(students, start=1):
        print(f"\nStudent #{index}")
        print(f"ID: {student['student_id']}")
        print(f"Name: {student['name']}")
        print(f"Course: {student['course']}")
        print(f"Year Level: {student['year_level']}")
        print(f"Contact Number: {student['contact_number']}")
def search_student(students):
    print("\nSearch Student")
    if len(students) == 0:
        print("No student records available.")
        return

    student_id = get_student_id()
    student = find_student(students, student_id)

    if student is None:
        print("Student not found.")
        return

    print("\nStudent Found")
    print(f"ID: {student['student_id']}")
    print(f"Name: {student['name']}")
    print(f"Course: {student['course']}")
    print(f"Year Level: {student['year_level']}")
    print(f"Contact Number: {student['contact_number']}")
def main():
    students = []

    while True:
        display_menu()
        choice = get_menu_choice()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        else:
            print("Exiting program.")
            break


if __name__ == "__main__":
    main()
