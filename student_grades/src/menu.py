from student_grades.src.grade_management import GradeManagement

def display_menu():
    print("\nStudent Grade Management System")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Add Grade")
    print("4. Update Grade")
    print("5. Display Student Info")
    print("6. Display All Students")
    print("7. Simulate Future Grade Impact")
    print("8. Export Student Data to PDF")
    print("9. Exit")

def main():
    grade_mgmt = GradeManagement()

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            student_id = int(input("Enter student ID: "))
            name = input("Enter student name: ")
            try:
                grade_mgmt.add_student(student_id, name)
                print(f"Student {name} added successfully.")
            except ValueError as e:
                print(e)

        elif choice == "2":
            student_id = int(input("Enter student ID to remove: "))
            try:
                grade_mgmt.remove_student(student_id)
                print(f"Student {student_id} removed successfully.")
            except ValueError as e:
                print(e)

        elif choice == "3":
            student_id = int(input("Enter student ID: "))
            subject = input("Enter subject name: ")
            grade = float(input("Enter grade (2-6): "))
            try:
                grade_mgmt.add_grade(student_id, subject, grade)
                print(f"Grade for {subject} added successfully.")
            except ValueError as e:
                print(e)

        elif choice == "4":
            student_id = int(input("Enter student ID: "))
            subject = input("Enter subject name: ")
            grade = float(input("Enter new grade (2-6): "))
            try:
                grade_mgmt.update_grade(student_id, subject, grade)
                print(f"Grade for {subject} updated successfully.")
            except ValueError as e:
                print(e)

        elif choice == "5":
            student_id = int(input("Enter student ID: "))
            try:
                grade_mgmt.display_student_info(student_id)
            except ValueError as e:
                print(e)

        elif choice == "6":
            grade_mgmt.display_all_students()

        elif choice == "7":
            student_id = int(input("Enter student ID: "))
            subject = input("Enter subject name: ")
            future_grade = float(input("Enter possible future grade (2-6): "))

            try:
                grade_mgmt.simulate_future_grade(student_id, subject, future_grade)
            except ValueError as e:
                print(e)

        elif choice == "8":
            student_id = int(input("Enter student ID: "))
            try:
                grade_mgmt.export_to_pdf(student_id)
            except ValueError as e:
                print(e)

        elif choice == "9":
            print("Exiting system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
