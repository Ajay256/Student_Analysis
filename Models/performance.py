class Performance:
    def __init__(self, student_id, subject_id, semester, marks, attendance):
        self.student_id = student_id
        self.subject_id = subject_id
        self.semester = semester
        self.marks = marks
        self.attendance = attendance

    def __str__(self):
        return f"Student ID: {self.student_id}, Subject ID: {self.subject_id}, Semester: {self.semester}, Marks: {self.marks}, Attendance: {self.attendance}%"
