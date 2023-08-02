class BaseException(Exception):
    pass

class NegativeSideError(BaseException):
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def __str__(self):
        return f'Длины сторон {self.side1} и {self.side2} не могут быть отрицательными'


class UnequalSidesError(BaseException):
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def __str__(self):
        return f'Длины сторон {self.side1} и {self.side2} должны быть равны для квадрата'