students = []


def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    marks = int(input("Enter student marks: "))

    student = {
        "name": name,
        "age": age,
        "marks": marks
    }

    students.append(student)
    print(" Student added successfully!")


def view_students():
    if len(students) == 0:
        print("No students found.")
        return

    print("\n--- Student List ---")

    for student in students:
        print(f"Name  : {student['name']}")
        print(f"Age   : {student['age']}")
        print(f"Marks : {student['marks']}")
        print("-" * 20)


def search_student():
    name = input("Enter student name to search: ")

    for student in students:
        if student["name"].lower() == name.lower():
            print("\nStudent Found!")
            print(f"Name  : {student['name']}")
            print(f"Age   : {student['age']}")
            print(f"Marks : {student['marks']}")
            return

    print(" Student not found.")


def delete_student():
    name = input("Enter student name to delete: ")

    for student in students:
        if student["name"].lower() == name.lower():
            students.remove(student)
            print(" Student deleted successfully!")
            return

    print(" Student not found.")


def main():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            print("EXITS!")
            break

        else:
            print("Invalid choice. Try again.")


main()