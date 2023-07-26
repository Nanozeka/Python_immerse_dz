# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# Напишите к ним классы исключения с выводом подробной информации. Поднимайте исключения внутри основного кода.
# Например нельзя создавать прямоугольник со сторонами отрицательной длины.


from Base_Exception import NegativeSideError, UnequalSidesError

LENGTH = 5
WIDTH = 10

class Rectangle:

    def __init__(self, side1, side2):
        if side1 < 0 or side2 < 0:
            raise NegativeSideError(side1, side2)
        elif side1 != side2:
            raise UnequalSidesError(side1, side2)


if __name__ == '__main__':
    rect1 = Rectangle(LENGTH, WIDTH)

