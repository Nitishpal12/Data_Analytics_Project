import json
class Student:
    def __init__(self, student_id, name, age, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 50:
            return "D"
        else:
            return "F"

    def display(self):
        print("ID:", self.student_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)
        print("Grade:", self.calculate_grade())
        print("-" * 30)


# Student Dictionary
students = {}

# Initial Students
students[1] = Student(1, "Nitish", 21, 85)
students[2] = Student(2, "Aman", 22, 72)
students[3] = Student(3, "Priya", 20, 91)


# Add Student
def add_student():
    student_id = int(input("Enter Student ID: "))

    if student_id in students:
        print("Student ID already exists!")
        return

    name = input("Enter Student Name: ")
    age = int(input("Enter Student Age: "))
    marks = float(input("Enter Student Marks: "))

    students[student_id] = Student(
        student_id,
        name,
        age,
        marks
    )

    print("Student added successfully!")


# Update Student
def update_student():
    student_id = int(input("Enter Student ID to update: "))

    if student_id not in students:
        print("Student not found!")
        return

    name = input("Enter New Student Name: ")
    age = int(input("Enter New Student Age: "))
    marks = float(input("Enter New Student Marks: "))

    students[student_id].name = name
    students[student_id].age = age
    students[student_id].marks = marks

    print("Student updated successfully!")


# Delete Student
def delete_student():
    student_id = int(input("Enter Student ID to delete: "))

    if student_id not in students:
        print("Student not found!")
        return

    del students[student_id]

    print("Student deleted successfully!")


# Search Student
def search_student():
    student_id = int(input("Enter Student ID to search: "))

    if student_id not in students:
        print("Student not found!")
        return

    students[student_id].display()


# Display All Students
def display_all_students():
    if not students:
        print("No students available!")
        return

    print("\n===== ALL STUDENTS =====")

    for student in students.values():
        student.display()

def save_students():
    data = {}

    for student_id, student in students.items():
        data[student_id] = {
            "name": student.name,
            "age": student.age,
            "marks": student.marks
        }

    with open("students.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Student data saved successfully!")        



# Main Menu
while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. Search Student")
    print("5. Display All Students")
    print("6. Save Students")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        update_student()

    elif choice == "3":
        delete_student()

    elif choice == "4":
        search_student()

    elif choice == "5":
        display_all_students()

    elif choice == "6":
        save_students()

    elif choice == "7":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice! Please try again.")
