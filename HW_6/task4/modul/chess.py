# Задача 4

# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной
# расстановки ферзей в задаче выше. Проверяйте различные случайные варианты и выведите
# 4 успешных расстановки. *Выведите все успешные варианты расстановок

import random
def check_queens(queens):
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            x1, y1 = queens[i]
            x2, y2 = queens[j]

            # Проверка, бьют ли ферзи друг друга по вертикали, горизонтали или диагонали
            if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
                return False

    return True


# Пример ввода координат ферзей
queens = [(1, 3), (2, 7), (3, 2), (4, 8), (5, 5), (6, 1), (7, 4), (8, 6)]

# Проверка битья ферзей
result = check_queens(queens)

# Вывод результата
if result:
    print("Ферзи не бьют друг друга")
else:
    print("Ферзи бьют друг друга")


# Создаем функцию, которая генерирует случайным образом расстановку ферзей
# И создает список с координатами пар ферзей и вызывает функцию(check_queens) для проверки правильности расстановки
def random_queen_arrangement():
    while True:
        queens = [(i, random.randint(1, 8)) for i in range(1, 9)]
        result = check_queens(queens)

        if result:
            return queens


successful_arrangements = []
count = 0

# В цикле добавляем успешные расстановки
while count < 4:
    queens = random_queen_arrangement()

    if queens not in successful_arrangements:
        successful_arrangements.append(queens)
        count += 1

print("Успешные расстановки ферзей:")

for queens in successful_arrangements:
    print(queens)
