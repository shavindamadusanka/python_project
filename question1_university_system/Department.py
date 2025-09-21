class Department:
    def __init__(self, name):
        self.name = name
        self.courses = []
        self.faculty = []
        self.students = []

    def add_course(self, course):
        self.courses.append(course)

    def add_faculty(self, faculty):
        self.faculty.append(faculty)

    def add_student(self, student):
        self.students.append(student)
        student.department = self

    def info(self):
        print("department info:")
        print("department name :" , self.name)
        print("department courses :" , self.courses)
        print("department students :" , self.students)
        print("department faculty :" , self.faculty)

    def __str__(self):
        return f"{self.name} "

    def __repr__(self):
        return f"{self.name} "