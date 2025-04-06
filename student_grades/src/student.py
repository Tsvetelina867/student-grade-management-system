
class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        if grade < 2 or grade > 6:
            raise ValueError("Grade must be between 2 and 6.")
        if subject in self.grades:
            raise ValueError(f"Grade for {subject} already entered.")
        self.grades[subject] = grade

    def update_grade(self, subject, grade):
        if grade < 2 or grade > 6:
            raise ValueError("Grade must be between 2 and 6.")
        if subject not in self.grades:
            raise ValueError(f"No grade found for {subject}.")
        self.grades[subject] = grade

    def get_grade(self, subject):
        return self.grades.get(subject, "No grade available")

    def get_gpa(self):
        if not self.grades:
            return 0
        total_points = sum(self.grades.values())
        return total_points / len(self.grades)

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "grades": self.grades,
            "gpa": self.get_gpa(),
        }

    @staticmethod
    def from_dict(data):
        student = Student(data['student_id'], data['name'])
        student.grades = data['grades']
        return student


    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.name}, GPA: {self.get_gpa()}"

