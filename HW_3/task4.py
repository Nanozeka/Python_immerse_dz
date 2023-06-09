# Задача 4

# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

# Определяеем грузоподъемность рюкзака
MAX_WEIGHT = 5000

# Сщздаем список вещей
items = {
    'Спальник': 1200,
    'Насос': 200,
    'Палатка': 3000,
    'Коврик': 600,
    'Фонарик': 150,
    'Аптечка': 600,
    'Кружка': 200,
    'Обеденный набор': 400,
    'Сапоги': 1500,
    'Куртка': 1200
}

# Создаем пустой рюкзак
backpack = []

# Проходим по списку пар
for item, weight in items.items():

    # Если вес меньше равен макс то
    if weight <= MAX_WEIGHT:

        # Вещь добавляем в рюкзак
        backpack.append(item)
        MAX_WEIGHT -= weight

print(f'Набор вещей, которые влезут в рюкзак: ', backpack)