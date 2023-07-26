# 1)
# Создайте класс студента. Используя дескрипторы проверяйте ФИО на первую заглавную букву
#  и наличие только букв. Названия предметов должны загружаться из файла CSV
#  при создании экземпляра. Другие предметы в экземпляре недопустимы.
#  Для каждого предмета можно хранить оценки (от 2 до 5)
#  и результаты тестов (от 0 до 100). Также экземпляр должен сообщать средний балл
#  по тестам для каждого предмета и по оценкам всех предметов вместе взятых.



# Если развивать логику задачи, то можно сделать следующее. Расширить содержимое csv файла:
# помимо имен предметов, там еще будут оценки и результаты тестов. Далее сделать классовый метод,
# который будет на основании данных из csv файла создавать класс студента. И реализовать метод,
# который будет сохранять данные студента, то есть результаты его оценок и тестов обратно в csv файл.

import csv

class Name:
    """Сохранение имени атрибута"""
    # Нехарактерное получение атрибута.Это ведь протокол, то есть все действия строго предопределены.
    def __set_name__(self, owner, name):
        self.name = name

    """Получение значения атрибута"""
    # И тут   тожt
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    """Установка значения с валидацией"""
    def __set__(self, instance, value):
        if value[0].isupper() and value.isalpha():
            instance.__dict__[self.name] = value
            # Можно  обойтись   без else, если  поменять условия   местами.
        else:
            raise ValueError("Неверное имя")


class Subject:
    """Аналогично классу Name"""

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value
        # Этот дескриптор  вы не  использовали, почему?

class Student:
    """Использование класса Name для валидации"""

    first_name = Name()
    last_name = Name()
    patronymic = Name()

    """Загрузка предметов из CSV"""
    def __init__(self):
        self.subjects = {}
        with open('subjects.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                subject = row[0]
                self.subjects[subject] = []

    """Методы добавления оценок и результатов тестов"""
    def add_grade(self, subject, grade):
        if subject not in self.subjects:
            raise ValueError("Недопустимая тема")

        if not 2 <= grade <= 5:
            raise ValueError("Неправильная оценка")

        self.subjects[subject].append(grade)

    def add_test(self, subject, result):
        if subject not in self.subjects:
            raise ValueError("Недопустимая тема")

        if not 0 <= result <= 100:
            raise ValueError("Неверный результат теста")

        self.subjects[subject].append(result)

    """Методы подсчета средних баллов"""
    def avg_test(self, subject):
        results = [x for x in self.subjects[subject] if isinstance(x, int)]
        return sum(results) / len(results)

    def avg_grade(self):
        grades = []
        for subject in self.subjects:
            grades.extend(x for x in self.subjects[subject] if isinstance(x, int) and 2 <= x <= 5)
        return sum(grades) / len(grades)


    
"""Создание экземпляра Student"""
if __name__ == '__main__':
    student = Student()
    student.first_name = "Иван"
    student.last_name = "Петров"
    student.patronymic = "Михайлович"

    print(f"Студент: {student.first_name} {student.last_name} {student.patronymic}")

    """Добавление оценок и результатов тестов"""
    student.add_grade("mathematics", 5)
    student.add_grade("literature", 4)
    student.add_grade("biology", 3)

    student.add_test("mathematics", 85)
    student.add_test("literature", 90)
    student.add_test("biology", 75)

    print(f"Средний балл по тестам:")
    print(student.avg_test("mathematics"))
    print(student.avg_test("literature"))
    print(student.avg_test("biology"))

    print(f"Средний балл по оценкам: {student.avg_grade()}")