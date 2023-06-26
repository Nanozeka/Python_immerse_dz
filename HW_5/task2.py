# Задача 2

# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import os

def split_path(full_path):

    # Сначала разбиваем абсолютный путь на путь до файла и все остальное
    path, full_file_name = os.path.split(full_path)

    # затем все остальное на имя файла и его расширение
    file_name, file_extension = os.path.splitext(full_file_name)

    return path, file_name, file_extension

path, file_name, file_extension = split_path('c:\GeekBrains\Pogruzenie_Python\sem3\Text_wiki.txt')
print(path)
print(file_name)
print(file_extension)