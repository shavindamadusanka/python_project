from Student import Student


class UndergraduateStudent(Student):
    def __init__(self, name, age, student_id, year):
        super().__init__(name, age, student_id)
        self.year = year

    def display_info(self):
        super().display_info()
        print(f"Year: {self.year}")

    def __str__(self):
        return f"{self.name} ({self.student_id})"

    def __repr__(self):
        return f"{self.name} ({self.student_id})"