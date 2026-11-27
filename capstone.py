# Student Marks Management System

students = {}

def add_student():
    name = input("Enter student name: ")
    marks = float(input("Enter student marks: "))
    students[name] = marks
    print("Student added successfully!")

def display_students():
    if len(students) == 0:
        print("No student records found!")
    else:
        print("\n--- Student Records ---")
        for name, marks in students.items():
            print(name, ":", marks)

def search_student():
    name = input("Enter student name to search: ")
    if name in students:
        print("Marks:", students[name])
    else:
        print("Student not found!")

def calculate_average():
    if len(students) == 0:
        print("No marks available!")
    else:
        total = sum(students.values())
        average = total / len(students)
        print("Average Marks:", average)

while True:
    print("\n===== Student Marks Management =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Calculate Average Marks")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        calculate_average()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
