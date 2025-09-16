class Teacher:
    def __init__(self, teacher_id, name, email):
        self.teacher_id = teacher_id
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name} ({self.email})"
