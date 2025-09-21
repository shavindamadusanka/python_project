from Person import Person


class Student(Person):
    def __init__(self, name, age, student_id ,max_courses_per_semester=5):
        super().__init__(name, age)
        self._student_id = student_id
        self._enrollments = {}  # {semester: [courses]}
        self._grades = {}  # {semester: {course_code: grade}}
        self._max_courses = max_courses_per_semester
        self.department = None  # link to Department

    @property
    def student_id(self):
        return self._student_id

    @property
    def enrollments(self):
        return self._enrollments

    @property
    def grades(self):
        return self._grades

    @property
    def max_courses(self):
        return self._max_courses

    @student_id.setter
    def student_id(self, value):
        if not value:
            raise ValueError("Student ID cannot be empty")
        self._student_id = value

    @max_courses.setter
    def max_courses(self, value):
        if value < 1:
            raise ValueError("Max courses per semester must be at least 1")
        self._max_courses = value

    def display_info(self):
        super().display_info()  # Call Person's display_info
        print(f"Student ID: {self.student_id}")
        print(f"Enrollments: {self.enrollments}")
        print(f"Grades: {self.grades}")

    def enroll_course(self, semester, course):
        """Enroll a student in a course for a given semester."""
        if semester not in self._enrollments:
            self._enrollments[semester] = []

        if len(self._enrollments[semester]) >= self._max_courses:
            print(f"Cannot enroll {course.name}: max {self._max_courses} courses reached for {semester}")
            return

        if course in self._enrollments[semester]:
            print(f"{course.name} is already enrolled in {semester}")
            return

        self._enrollments[semester].append(course)
        print(f"{self.name} enrolled in {course.name} for {semester}")

    def drop_course(self, semester, course):
        """Drop a course if the student is enrolled in it."""
        if semester in self.enrollments and course in self.enrollments[semester]:
            self.enrollments[semester].remove(course)
            print(f"{self.name} dropped {course.name} from {semester}")

            if semester in self.grades and course.code in self.grades[semester]:
                del self.grades[semester][course.code]
                print(f"Grade for {course.name} removed from {semester}")

    def add_grade(self, semester, course, grade):
        """Store the grade for a course in a given semester."""
        if semester not in self.grades:
            self.grades[semester] = {}
        self.grades[semester][course.code] = grade

    def calculate_gpa(self):
        """Calculate GPA based on all grades across semesters."""
        total_points = 0
        total_courses = 0
        for semester_grades in self._grades.values():
            for grade in semester_grades.values():
                total_points += grade
                total_courses += 1
        return round(total_points / total_courses, 2) if total_courses > 0 else 0.0

    def acedemic_status(self):
        print("Acedemic status: " , self.courses)

    def get_responsibilities(self):
        return "Attend classes, complete assignments, take exams"

    def __str__(self):
        return f"{self.name} ({self.student_id})"

    def __repr__(self):
        return f"{self.name} ({self.student_id})"