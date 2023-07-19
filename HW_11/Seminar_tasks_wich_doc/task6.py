# 6) Доработайте прошлую задачу. Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения

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

    def __eq__(self, other):
        """Doc5."""
        return self.get_square() == other.get_square()

    def __gt__(self, other):
        """Doc6."""
        return self.get_square() > other.get_square()

    def __lt__(self, other):
        """Doc7."""
        return self.get_square() < other.get_square()

    def __ge__(self, other):
        """Doc8."""
        return self.get_square() >= other.get_square()

    def __le__(self, other):
        """Doc9."""
        return self.get_square() <= other.get_square()

rec_1 = Rectangle(5)
rec_2 = Rectangle(5)
print(f'{rec_1.get_perimeter() = }\n{rec_2.get_perimeter() = }')
rec_3 = rec_1 + rec_2
rec_4 = rec_1 - rec_2
print(f'{rec_3.length = }\n{rec_3.width = }')
print(f'{rec_4.length = }\n{rec_4.width = }')
print(rec_1 == rec_2)
print(rec_3 <= rec_4)
help(Rectangle)