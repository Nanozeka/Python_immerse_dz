# Задача 4

# Напишите функцию группового переименования файлов. Она должна:
# * принимать в качестве аргумента желаемое конечное имя файлов.
#
# * При переименовании в конце имени добавляется порядковый номер.
#
# * принимать в качестве аргумента расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
#
# * принимать в качестве аргумента расширение конечного файла.
# Шаблон переименованного файла: <original_name>_<new_name>_<position>.<new_extention>

import os

__all__ = ["batch_rename_files"]

def batch_rename_files(directory, new_name, extention, new_extention):
    # Изпользуя библиотеку получаем список файлов в заданой папке
    files = os.listdir(directory)
    count = 1

    for file in files:

        # Проверяем имеет ли файл указанное расширение
        if file.endswith(extention):

            # Извлекаем базовое имя файла
            original_name = os.path.splitext(file)[0]

            # Генерируем новое имя файла, используя указанный шаблон.
            new_file_name = f"{original_name}_{new_name}_{count}.{new_extention}"

            # Создаем новый путь к файлу, объединяя путь к каталогу и новое имя файла.
            new_file_path = os.path.join(directory, new_file_name)

            # Создаем старый путь к файлу, используя тот же подход, но используя исходное имя файла.
            old_file_path = os.path.join(directory, file)

            # Переименовываем файл
            os.rename(old_file_path, new_file_path)
            count += 1



if __name__ == '__main__':
    batch_rename_files("c:\GeekBrains\Pogruzenie_Python\Python_immerse_dz\HW_7", "new_name", ".txt", "jpg")
