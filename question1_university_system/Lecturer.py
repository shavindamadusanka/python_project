from Faculty import Faculty


class Lecturer(Faculty):
    def __init__(self, name, age, faculty_id, subject):
        super().__init__(name, age, faculty_id)
        self.subject = subject

    def display_info(self):
        super().display_info()
        print(f"Subject: {self.subject}")

    def get_responsibilities(self):
        return "Teach lectures, prepare materials"