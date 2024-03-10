class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"Имя: {self.first_name}\nФамилия: {self.last_name}"


class Reviewer(Person):
    def __str__(self):
        return super().__str__()


class Lecturer(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.average_grade = 0

    def __str__(self):
        return f"{super().__str__()}\nСредняя оценка за лекции: {self.average_grade}"


class Student(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.average_grade = 0
        self.courses_in_progress = []
        self.completed_courses = []

    def __str__(self):
        return f"{super().__str__()}\nСредняя оценка за домашние задания: {self.average_grade}\n" \
               f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n" \
               f"Завершенные курсы: {', '.join(self.completed_courses)}"


# Создаем экземпляры классов
reviewer1 = Reviewer("John", "Smith")
reviewer2 = Reviewer("Alice", "Doe")

lecturer1 = Lecturer("Emily", "Jones")
lecturer2 = Lecturer("Michael", "Brown")

student1 = Student("Anna", "Lee")
student2 = Student("David", "Clark")

# Вызываем методы для созданных экземпляров
print(reviewer1)
print(reviewer2)
print(lecturer1)
print(lecturer2)
print(student1)
print(student2)

# Функция для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса
def average_homework_grade(students_list, course):
    total_grade = 0
    count = 0
    for student in students_list:
        if course in student.completed_courses:
            total_grade += student.average_grade
            count += 1
    if count == 0:
        return 0
    return total_grade / count

# Пример вызова функции для подсчета средней оценки за домашние задания по студентам в рамках курса "Python"
students = [student1, student2]
python_average_grade = average_homework_grade(students, "Python")
print(f"Средняя оценка за домашние задания по курсу Python: {python_average_grade}")

# Функция для подсчета средней оценки за лекции всех лекторов в рамках курса
def average_lecture_grade(lecturers_list, course):
    total_grade = 0
    count = 0
    for lecturer in lecturers_list:
        if course in lecturer.completed_courses:
            total_grade += lecturer.average_grade
            count += 1
    if count == 0:
        return 0
    return total_grade / count

# Пример вызова функции для подсчета средней оценки за лекции лекторов в рамках курса "Python"
lecturers = [lecturer1, lecturer2]
python_lecturer_average_grade = average_lecture_grade(lecturers, "Python")
print(f"Средняя оценка за лекции по курсу Python: {python_lecturer_average_grade}")