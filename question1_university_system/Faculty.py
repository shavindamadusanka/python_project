from Person import Person


class Faculty(Person):
    def __init__(self, name, age, faculty_id , department=None):
        super().__init__(name, age)
        self.faculty_id = faculty_id
        self.department = department
        self.courses = []

    def assign_course(self, course):
        self.courses.append(course)
        print(f"{self.name} assigned to {course.name}")

    def display_info(self):
        super().display_info()
        print(f"Faculty ID: {self.faculty_id}")
        print(f"Department: {self.department}")
        print(f"Courses: {self.courses}")

    def get_responsibilities(self):
        return "Teach courses, advise students"