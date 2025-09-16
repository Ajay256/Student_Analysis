class Student:
    def __init__(self, student_id, name, roll_no, student_class, semester):
        self.student_id = student_id
        self.name = name
        self.roll_no = roll_no
        self.student_class = student_class
        self.semester = semester

    def __str__(self):
        return f"{self.name} ({self.roll_no}) - Class {self.student_class} Semester {self.semester}"
