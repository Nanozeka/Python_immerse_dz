# Задача 3

# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.

# Хоть с математической точки зрения разницы нет, но все же при отображении суммы есть отличия.!!!!!!!!!!

import math
from fractions import Fraction

def add_fractions(fraction1, fraction2):

    # Через сплит разбиваем на числитель и знаменатель
    num1, den1 = fraction1.split('/')
    num2, den2 = fraction2.split('/')

    # Вычисляем НОК и НОД(берем из фукции mach.gcd)
    lcm = (int(den1) * int(den2)) // math.gcd(int(den1), int(den2))

    sum_num = int(num1) * (lcm // int(den1)) + int(num2) * (lcm // int(den2))
    prod_num = int(num1) * int(num2)
    prod_den = int(den1) * int(den2)

    sum_fraction = str(sum_num) + '/' + str(lcm)
    prod_fraction = str(prod_num) + '/' + str(prod_den)

    return sum_fraction, prod_fraction


fraction1 = input("Введите первую дробь: ")
fraction2 = input("Введите вторую дробь: ")

sum_fraction, prod_fraction = add_fractions(fraction1, fraction2)

print("Сумма дробей:", sum_fraction)
print("Произведение дробей:", prod_fraction)


print('Проверка кода с помощью модуля Fraction')


def add_fractions(fraction1, fraction2):
    f1 = Fraction(fraction1)
    f2 = Fraction(fraction2)

    sum_fraction = f1 + f2
    prod_fraction = f1 * f2

    return str(sum_fraction), str(prod_fraction)


fraction1 = input("Введите первую дробь: ")
fraction2 = input("Введите вторую дробь: ")

sum_fraction, prod_fraction = add_fractions(fraction1, fraction2)

print("Сумма дробей:", sum_fraction)
print("Произведение дробей:", prod_fraction)