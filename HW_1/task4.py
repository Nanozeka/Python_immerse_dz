# Задача 4

# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки


import random


def guess_game(num_attempts):
    number = random.randint(0, 100)

    # Проходим циклом по длине количества попыток(на каждой итерации количество попыток уменьшается)
    for attempt in range(num_attempts):
        guess = int(input(f'Введите число от 0 до 1000 (осталось попыток: {num_attempts - attempt}): '))

        if guess == number:
            print('Поздравляю, вы угадали число!')

        elif guess < number:
            print('Загаданное число больше вашего.')
        else:
            print('Загаданное число меньше вашего.')

    print(f'К сожалению, вы не угадали число. Оно было {number}.')



num_attempts = int(input('Введите количество попыток: '))
guess_game(num_attempts)