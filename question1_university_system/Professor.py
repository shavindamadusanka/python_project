from Faculty import Faculty


class Professor(Faculty):
    def __init__(self, name, age, faculty_id, department):
        super().__init__(name, age, faculty_id)
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department} ")

    def get_responsibilities(self):
        return "Teach advanced courses, supervise research"