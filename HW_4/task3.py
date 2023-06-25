# Задача 3

# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.


# Создаем функцию которая принимает именованные аргументы
def map_kwargs(**kwargs):
    result = {}

    # Перебираем элементы словаря
    for key, value in kwargs.items():

        # Если ключ хешируется
        try:
            hash(key)

            # то значение становиться ключем, а ключ значением
            result[value] = key
        except TypeError:

            # Если не хешируется то ключу присваеваем его строковое представление
            result[str(key)] = key
    return result


result = map_kwargs(name='Ivan', age=25, is_student=True, fruits=['apple', 'banana'])
print(result)