# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# * имя файла без расширения или название каталога,
# * расширение, если это файл,
# * флаг каталога,
# * название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.


import os
import logging
from collections import namedtuple


# Создаем логгер
logging.basicConfig(filename='app.log', filemode='w', encoding="Utf-8", level=logging.INFO)
logger = logging.getLogger(__name__)


# Хранение информации о файле/папке
FileInfo = namedtuple('FileInfo', ['name', 'ext', 'is_dir', 'parent'])

# Функция для проверки является ли путь папкой или файлом и есть ли у него расширение
def get_file_info(path):
    name = os.path.basename(path)
    is_dir = os.path.isdir(path)
    parent = os.path.dirname(path)

    if not is_dir:
        ext = os.path.splitext(path)[1]
    else:
        ext = ''

    return FileInfo(name, ext, is_dir, parent)

# Делаем цикл обхода и сбор данных в список
def collect_data(start_path):
    data = []
    for root, dirs, files in os.walk(start_path):
        for f in files:
            filepath = os.path.join(root, f)
            info = get_file_info(filepath)
            data.append(info)
        for d in dirs:
            dirpath = os.path.join(root, d)
            info = get_file_info(dirpath)
            data.append(info)

    return data


def main(start_path):

    data = collect_data(start_path)

    for d in data:
        logging.info(d)

    print(f'Сохранено {len(data)} объектов в файл(app.log)')


if __name__ == "__main__":
    main(start_path = '.')
