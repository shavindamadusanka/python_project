from Department import Department
from Course import Course
from Faculty import Faculty
from Student import Student
from UndergraduateStudent import UndergraduateStudent

# create a department
cs_department = Department("IT department")

# create courses
c1 = Course("C001" , "Intro to the python" ,4 , max_students=3)
c2 = Course("C002" , "Intro to the java" ,3.5 , prerequisites=[c1])
c3 = Course("C003" , "Intro to the c" ,3 , prerequisites=[c2] )

# add courses to the department
cs_department.add_course(c1)
cs_department.add_course(c2)
cs_department.add_course(c3)

# create a faculty
faculty1 = Faculty("sumanadasa" ,12 , "F001" , cs_department)

# assign courses to the faculty
faculty1.assign_course(c1)
faculty1.assign_course(c2)
faculty1.assign_course(c3)

# add faculty to the department
cs_department.add_faculty(faculty1)

# create students
student1 = UndergraduateStudent("shavinda", 32, "S001", 2024)
student2 = UndergraduateStudent("pasan", 21, "S002", 2024)

# add students to the department
cs_department.add_student(student1)
cs_department.add_student(student2)

faculty1.display_info()

# enroll students to the courses
c1.enroll_student(student1 , "L1S1")
c1.enroll_student(student2 , "L1S2")

# add grades to the students relevant to the certain semester and the course
student1.add_grade("L1S1" , c1 , 3.4)
student2.add_grade("L1S2" , c2 , 3.2)


# print details of all the students
print("All student informations")
for student in [student1, student2]:
    student.display_info()
    print(f"GPA :" , {student.calculate_gpa()})


c1.display_info();

cs_department.info()