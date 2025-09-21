from Student import Student


class GraduateStudent(Student):
    def __init__(self, name, age, student_id, thesis_topic):
        super().__init__(name, age, student_id)
        self.thesis_topic = thesis_topic

    def display_info(self):
        super().display_info()
        print(f"Thesis Topic: {self.thesis_topic}")
