import json
import re

from student import Student
from report import export_student_data_to_pdf

class GradeManagement:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = self.load_students()

    def load_students(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                return {student["student_id"]: Student.from_dict(student) for student in data}
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_students(self):
        with open(self.filename, "w") as file:
            data = [student.to_dict() for student in self.students.values()]
            json.dump(data, file)

    def validate_name(self, name):
        if not name.strip():
            raise ValueError("Name cannot be empty.")
        if not re.match(r"^[A-Za-z\s]+$", name):
            raise ValueError("Name can only contain letters and spaces.")
        return name

    def add_student(self, student_id, name):
        if student_id <= 0:
            raise ValueError("Student ID must be a positive integer.")
        if student_id in self.students:
            raise ValueError(f"Student with ID {student_id} already exists.")

        validated_name = self.validate_name(name)

        self.students[student_id] = Student(student_id, validated_name)
        self.save_students()

    def remove_student(self, student_id):
        if student_id not in self.students:
            raise ValueError(f"Student with ID {student_id} not found.")
        del self.students[student_id]
        self.save_students()

    def get_student(self, student_id):
        student = self.students.get(student_id)
        if not student:
            raise ValueError(f"Student with ID {student_id} not found.")
        return student

    def add_grade(self, student_id, subject, grade):
        student = self.get_student(student_id)
        student.add_grade(subject, grade)
        self.save_students()

    def update_grade(self, student_id, subject, grade):
        student = self.get_student(student_id)
        student.update_grade(subject, grade)
        self.save_students()

    def display_student_info(self, student_id):
        student = self.get_student(student_id)
        self._print_student_details(student)

    def display_all_students(self):
        if not self.students:
            print("\nNo students available.\n")
            return

        print("\n" + "=" * 40)
        print("ALL STUDENTS")
        print("=" * 40)

        for student in self.students.values():
            self._print_student_details(student)
            print("-" * 40)

        print("=" * 40 + "\n")

    def _print_student_details(self, student):
        print("\n" + "=" * 30)
        print(f"Student ID: {student.student_id}")
        print(f"Name: {student.name}")
        print(f"GPA: {student.get_gpa():.2f}")
        print("Grades:")

        if not student.grades:
            print("  No grades available.")
        else:
            for subject, grade in student.grades.items():
                print(f"  {subject}: {int(grade)}")

        print("=" * 30 + "\n")

    def simulate_future_grade(self, student_id, subject, future_grade):
        if future_grade < 2 or future_grade > 6:
            print("Invalid grade. Must be between 2 and 6.")
            return

        student = self.students.get(student_id)
        if not student:
            print(f"Student with ID {student_id} not found.")
            return

        temp_grades = student.grades.copy()
        temp_grades[subject] = future_grade

        simulated_gpa = sum(temp_grades.values()) / len(temp_grades)

        print(f"\n📊 Prediction Result:")
        print(f"  - If you score {int(future_grade)} in {subject}, your GPA would be: {simulated_gpa}")

    def export_to_pdf(self, student_id):
        student = self.get_student(student_id)
        if student:
            print(f"Exporting student {student_id} data to PDF...")
            export_student_data_to_pdf(student)
        else:
            print(f"Student with ID {student_id} not found.")