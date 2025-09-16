class Subject:
    def __init__(self, subject_id, subject_name, teacher_name):
        self.subject_id = subject_id
        self.subject_name = subject_name
        self.teacher_name = teacher_name

    def __str__(self):
        return f"{self.subject_name} (Teacher: {self.teacher_name})"
