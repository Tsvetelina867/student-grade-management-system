from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.shapes import Drawing


def export_student_data_to_pdf(student, filename="student_report.pdf"):
    c = canvas.Canvas(filename, pagesize=letter)

    c.drawString(100, 750, f"Student Report for {student.name} (ID: {student.student_id})")

    c.drawString(100, 730, f"GPA: {student.get_gpa():.2f}")

    c.drawString(100, 710, "Summary:")
    c.drawString(100, 690, f"Number of Subjects: {len(student.grades)}")

    if student.grades:
        highest_grade = max(student.grades.values())
        lowest_grade = min(student.grades.values())
        c.drawString(100, 670, f"Highest Grade: {int(highest_grade)}")
        c.drawString(100, 650, f"Lowest Grade: {int(lowest_grade)}")

    y_position = 630
    c.drawString(100, y_position, "Grades:")
    y_position -= 20
    for subject, grade in student.grades.items():
        c.drawString(100, y_position, f"{subject}: {int(grade)}")
        y_position -= 20

    if student.grades:
        drawing = Drawing(400, 200)
        bar_chart = VerticalBarChart()
        bar_chart.x = 50
        bar_chart.y = 50
        bar_chart.height = 125
        bar_chart.width = 300
        bar_chart.data = [list(student.grades.values())]
        bar_chart.categoryAxis.categoryNames = list(student.grades.keys())
        drawing.add(bar_chart)
        drawing.drawOn(c, 50, y_position - 250)

    c.save()
