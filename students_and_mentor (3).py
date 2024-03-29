class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"Имя: {self.first_name}\nФамилия: {self.last_name}"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return (self.first_name, self.last_name) < (other.first_name, other.last_name)

    def __le__(self, other):
        return (self.first_name, self.last_name) <= (other.first_name, other.last_name)

    def __gt__(self, other):
        return (self.first_name, self.last_name) > (other.first_name, other.last_name)

    def __ge__(self, other):
        return (self.first_name, self.last_name) >= (other.first_name, other.last_name)


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

# Пример использования
some_reviewer = Reviewer("Some", "Buddy")
print(some_reviewer)

some_lecturer = Lecturer("Some", "Buddy")
some_lecturer.average_grade = 9.9
print(some_lecturer)

some_student = Student("Ruoy", "Eman")
some_student.average_grade = 9.9
some_student.courses_in_progress = ["Python", "Git"]
some_student.completed_courses = ["Введение в программирование"]
print(some_student)

# Тестирование методов сравнения
p1 = Person("John", "Doe")
p2 = Person("Jane", "Doe")
print(p1 == p2)  # False
print(p1 != p2)  # True
print(p1 < p2)   # True
print(p1 > p2)   # False
