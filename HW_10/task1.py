# Задача 1

# Класс принимает тип животного (название одного из созданных классов) и параметры
# для этого типа. Внутри класса создайте экземпляр на основе переданного типа и верните
# его из класса-фабрики.

# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# class Dog(Animal):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#         self.sound = "Гаф!"
#
# class Cat(Animal):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#         self.sound = "Мяу!"
#
# class Bird(Animal):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#         self.sound = "Чирик!"
#
# class AnimalFactory:
#     # Статический метод убрать.Сделать конструктор
#     @staticmethod
#     def create_animal(animal_type, name, age):
#         if animal_type == "Dog":
#             return Dog(name, age)
#         elif animal_type == "Cat":
#             return Cat(name, age)
#         elif animal_type == "Bird":
#             return Bird(name, age)
#         else:
#             raise ValueError("Нет такого типа животного: " + animal_type)

# Задание указано, что класс фабрики принимает имя одного из классов животных. А вы передаете строковый параметр
#
# if __name__ == '__main__':
#     animal_type = "Dog"
#     name = "Полкан"
#     age = 5
#
#     animal = AnimalFactory.create_animal(animal_type, name, age)
#     print(f"Создано животное типа {animal_type}: {animal.name}, возраст {animal.age}")
#     print(f"Звук, который издает животное: {animal.sound}")


    # Лучшее решение

class AnimalFactory:
    def __init__(self, animal_class):
        self.animal_class = animal_class

    def create_animal_instance(self, *args, **kwargs):
        return self.animal_class(*args, **kwargs)


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name} сказал ГАФ!")


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name} сказал МЯУ!")

if __name__ == '__main__':
    # Создание экземпляра класса фабрики с передачей класса животного в качестве параметра
    animal_factory = AnimalFactory(Dog)

    # Создание экземпляра животного с использованием фабрики
    dog_instance = animal_factory.create_animal_instance("Полкан", 5)
    dog_instance.speak()
