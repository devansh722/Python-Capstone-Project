# Student Marks Management System

A simple menu-driven Python program that stores student names and marks and lets you add, view, search and average them from the terminal.

This is a beginner-level Python programming project for B.Tech CSE AI/ML.

---

## Features

- **Add Student** – enter a name and marks, and save them.
- **Display All Students** – show every saved record.
- **Search Student** – find a student's marks by name.
- **Calculate Average Marks** – get the average of all saved marks.
- **Menu Interface** – a simple 5-option menu that keeps running until you exit.

---

## Menu Options

```
===== Student Marks Management =====
1. Add Student
2. Display All Students
3. Search Student
4. Calculate Average Marks
5. Exit
```

Type a number from 1 to 5 and press Enter. If you type anything else, the program prints `Invalid choice!` and shows the menu again.

---

## Sample Output

```
Enter your choice: 1
Enter student name: Rahul
Enter student marks: 85
Student added successfully!

Enter your choice: 1
Enter student name: Aman
Enter student marks: 90
Student added successfully!

Enter your choice: 2

--- Student Records ---
Rahul : 85.0
Aman : 90.0

Enter your choice: 3
Enter student name to search: Rahul
Marks: 85.0

Enter your choice: 4
Average Marks: 87.5
```

---

## How It Works

All records are kept in one dictionary called `students`. The student name is the key and the marks are the value.

```python
students = {}
```

| Function | What it does |
|---|---|
| `add_student()` | Takes a name and marks, then stores them with `students[name] = marks`. |
| `display_students()` | Loops through the dictionary and prints every record. Shows `No student records found!` if it is empty. |
| `search_student()` | Checks if the name is in the dictionary. Shows the marks, or `Student not found!`. |
| `calculate_average()` | Adds all marks with `sum()` and divides by `len(students)`. Shows `No marks available!` if it is empty. |

The main `while True` loop shows the menu again and again. Choosing option `5` prints `Thank you!` and uses `break` to stop the program.

---

## Program Flow

```
Start
  |
  v
Display Menu  <-----------------------------+
  |                                         |
  v                                         |
User selects option                         |
  |-- 1 -> Enter name and marks -> Save ----+
  |-- 2 -> Show all records ----------------+
  |-- 3 -> Enter name -> Check if exists ---+
  |-- 4 -> Add marks -> Divide by count ----+
  |-- other -> "Invalid choice!" -----------+
  |
  '-- 5 -> "Thank you!" -> End
```

---

## Python Concepts Used

- **Dictionary** – stores names and marks as key-value pairs
- **Functions** – split the program into small reusable parts
- **While loop** – keeps the menu running
- **If-elif-else** – runs the right action for each choice
- **For loop** – displays all student records
- **Built-in functions** – `input()` reads text, `sum()` adds marks, `len()` counts students

---

## Author

**Devansh Gupta**
Mangalam University

