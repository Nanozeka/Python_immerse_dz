# Задача 2

# Возьмите любую из задач с прошлых семинаров (например сериализация данных),
# которые вы уже решали. Превратите функции в методы класса, а параметры в свойства.
# Задачи должны решаться через вызов методов экземпляра.

import os
import json
import csv
import pickle

class DirectoryTraverser:
    def __init__(self, directory):
        self.directory = directory
        self.result = []

    def traverse_directory(self):
        # Делаем рекурсивный обход директорий
        for root, dirs, files in os.walk(self.directory):
            current_dir_size = 0 # Размер текущей директории
            for file in files:
                # Создаем путь к текущему файлу, объединяя текущий каталог и имя файла.
                file_path = os.path.join(root, file)
                # Получаем размер файла в байтах
                file_size = os.path.getsize(file_path)
                # Увеличиваем размер текущей директории на размер текущего файла.
                current_dir_size += file_size
                # Добавляем информацию о текущем файле
                self.result.append({
                    'type': 'file',
                    'name': file,
                    'parent_directory': root,
                    'size': file_size
                })
            self.result.append({
                'type': 'directory',
                'name': os.path.basename(root),
                'parent_directory': os.path.dirname(root),
                'size': current_dir_size
            })

    # Записываем результаты в файлы JSON, CSV и pickle
    def save_results(self):
        # Сохранение результатов в JSON-файл
        with open('result.json', 'w') as json_file:
            json.dump(self.result, json_file)

        # Сохранение результатов в CSV-файл
        with open('result.csv', 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=['type', 'name', 'parent_directory', 'size'])
            writer.writeheader()
            writer.writerows(self.result)

        # Сохранение результатов в файл pickle
        with open('result.pickle', 'wb') as pickle_file:
            pickle.dump(self.result, pickle_file)


if __name__ == '__main__':
    directory = '.'
    directory_traverser = DirectoryTraverser(directory)
    directory_traverser.traverse_directory()
    directory_traverser.save_results()