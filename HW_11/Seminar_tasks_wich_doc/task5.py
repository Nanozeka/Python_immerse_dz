# 5)Дорабатываем класс прямоугольник из прошлого семинара. Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр прямоугольника. Складываем и вычитаем периметры,
# а не длинну и ширину. При вычитании не допускайте отрицательных значений.

class Rectangle:
    """Create class Rectangle """

    def __init__(self, *args):
        if len(args) == 1:
            self.length = args[0]
            self.width = self.length
        else:
            self.length, self.width, _ = args

    def get_perimeter(self):
        """Doc1."""
        return self.length * 2 + self.width * 2

    def get_square(self):
        """Doc2."""
        return self.length * self.width

    def __add__(self, other):
        """Doc3."""
        p = self.get_perimeter() + other.get_perimeter()
        return Rectangle(p // 2 / 2)

    def __sub__(self, other):
        """Doc4."""
        p = self.get_perimeter() - other.get_perimeter()
        return Rectangle(abs(p // 2 / 2))


rec_1 = Rectangle(5)
rec_2 = Rectangle(7)
print(f'{rec_1.get_perimeter() = }\n{rec_2.get_perimeter() = }')
rec_3 = rec_1 + rec_2
rec_4 = rec_1 - rec_2
print(f'{rec_3.length = }\n{rec_3.width = }')
print(f'{rec_4.length = }\n{rec_4.width = }')
help(Rectangle)