# Задача 1

# Класс принимает тип животного (название одного из созданных классов) и параметры
# для этого типа. Внутри класса создайте экземпляр на основе переданного типа и верните
# его из класса-фабрики.

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.sound = "Гаф!"

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.sound = "Мяу!"

class Bird(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.sound = "Чирик!"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, name, age):
        if animal_type == "Dog":
            return Dog(name, age)
        elif animal_type == "Cat":
            return Cat(name, age)
        elif animal_type == "Bird":
            return Bird(name, age)
        else:
            raise ValueError("Нет такого типа животного: " + animal_type)


if __name__ == '__main__':
    animal_type = "Dog"
    name = "Полкан"
    age = 5

    animal = AnimalFactory.create_animal(animal_type, name, age)
    print(f"Создано животное типа {animal_type}: {animal.name}, возраст {animal.age}")
    print(f"Звук, который издает животное: {animal.sound}")