class Course:
    def __init__(self, code, name, credits, max_students=30, prerequisites=None):
        self.code = code
        self.name = name
        self.credits = credits
        self.max_students = max_students
        self.prerequisites = prerequisites or []  # list of Course objects
        self.enrolled_students = []


    def __str__(self):
        return f"{self.code} - {self.name} ({self.credits} credits)"

    def __repr__(self):
          return f"Course({self.code!r}, {self.name!r}, {self.credits!r})"

    def enroll_student(self, student , semester):
        # Check if student completed prerequisites
        for prereq in self.prerequisites:
            if prereq.code not in student.grades or student.grades[prereq.code] < 2.0:
                print(f"{student.name} cannot enroll in {self.name}: missing prerequisite {prereq.name}")
                return False
        # Check enrollment limit
        if len(self.enrolled_students) >= self.max_students:
            print(f"{self.name} is full. Cannot enroll {student.name}")
            return False

        # Enroll student
        self.enrolled_students.append(student)
        student.enroll_course(semester,self)
        print(f"{student.name} enrolled in {self.name}")
        return True

    def drop_student(self, student):
        if student in self.enrolled_students:
            self.enrolled_students.remove(student)
            student.drop_course(self)
            print(f"{student.name} dropped {self.name}")

    def display_info(self):
        print("------------------------------")

        print(f"{self.code} - {self.name} ({self.credits} credits)")
        print(self.enrolled_students)

        print("-----------------------------")