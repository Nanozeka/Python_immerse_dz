# Напишите функцию, которая генерирует псевдоимена.
# Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# Полученные имена сохраните в файл.

from random import choice, randint

__all__ = ['task2']


VOWELS = 'eyuioa'
CONSONANT = 'qwertyuiopasdfghjklzxcvbnm'
MIN_LENGTH = 4
MAX_LENGHT = 7

def task2(count_names, filename):
    names = []
    for _ in range(count_names):
        len = randint(MAX_LENGHT, MAX_LENGHT)
        name = []
        letter = choice(VOWELS)
        name.append(letter)
        for _ in range(len - 1):
            name.append(choice(CONSONANT))
        name = ''.join(name).capitalize()
        print(f'{name = }')
        names.append(name)


    with open(filename, 'w', encoding='utf-8') as f:
        f.write('\n'.join(names))

if __name__ == '__main__':
    filename = 'names.txt'
    task2(5, filename)