from Faculty import Faculty


class TA(Faculty):
    def __init__(self, name, age, faculty_id, assisting_course):
        super().__init__(name, age, faculty_id)
        self.assisting_course = assisting_course

    def display_info(self):
        super().display_info()
        print(f"Assisting Course: {self.assisting_course}")

    def get_responsibilities(self):
        return "Assist lectures, hold labs, grade assignments"