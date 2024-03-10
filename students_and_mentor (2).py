class Reviewer:
    def grade_homework(self, student, course, grade):
        if isinstance(student, Student):
            student.receive_grade(course, grade)
        else:
            print("Error: Reviewer can only grade homework for students.")


class Student:
    def __init__(self):
        self.grades = {}

    def receive_grade(self, course, grade):
        if course in self.grades:
            self.grades[course].append(grade)
        else:
            self.grades[course] = [grade]


class Lecturer:
    def __init__(self):
        self.grades = {}

    def assign_grade(self, student, course, grade):
        if isinstance(student, Student):
            student_record = student.get_course_record(course)
            if student_record:
                student_record.append(grade)
            else:
                student.set_course_record(course, [grade])
        else:
            print("Error: Lecturer can only assign grades to students.")


# Пример использования:

student1 = Student()
lecturer1 = Lecturer()

lecturer1.assign_grade(student1, "Python Basics", 8)
lecturer1.assign_grade(student1, "Python Basics", 9)

print(student1.grades)