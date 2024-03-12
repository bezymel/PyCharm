class Lector:
    def __init__(self, name, surname, avg_rating):
        self.name = name
        self.surname = surname
        self.avg_rating = avg_rating

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_rating}"

    def __gt__(self, other):
        return self.avg_rating > other.avg_rating

    def __lt__(self, other):
        return self.avg_rating < other.avg_rating

class Student:
    def __init__(self, name, surname, avg_hw_rating, courses_in_progress, completed_courses):
        self.name = name
        self.surname = surname
        self.avg_hw_rating = avg_hw_rating
        self.courses_in_progress = courses_in_progress
        self.completed_courses = completed_courses

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.avg_hw_rating}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.completed_courses)}"

    def __gt__(self, other):
        return self.avg_hw_rating > other.avg_hw_rating

    def __lt__(self, other):
        return self.avg_hw_rating < other.avg_hw_rating

# Пример использования
lector1 = Lector("Иван", "Иванов", 9.7)
lector2 = Lector("Петр", "Петров", 9.9)

student1 = Student("Алексей", "Алексеев", 9.5, ["Python", "Git"], ["Введение в программирование"])
student2 = Student("Сергей", "Сергеев", 9.8, ["JavaScript"], ["ООП в Python"])

# Сравнение лекторов по средней оценке за лекции
if lector1 > lector2:
    print(f"{lector1.name} {lector1.surname} имеет выше среднюю оценку за лекции, чем {lector2.name} {lector2.surname}")
else:
    print(f"{lector2.name} {lector2.surname} имеет выше среднюю оценку за лекции, чем {lector1.name} {lector1.surname}")

# Сравнение студентов по средней оценке за домашние задания
if student1 > student2:
    print(f"{student1.name} {student1.surname} имеет выше среднюю оценку за домашние задания, чем {student2.name} {student2.surname}")
else:
    print(f"{student2.name} {student2.surname} имеет выше среднюю оценку за домашние задания, чем {student1.name} {student1.surname}")
