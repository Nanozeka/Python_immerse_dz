# 3) Добавьте к задачам 1 и 2 строки документации для классов.


import time

class My_String(str):
    """A My_String training class"""

    def __new__(cls, value, name):
        """Added the name and the time parameters"""
        instance = super().__new__(cls, value)
        instance.name = name
        instance.time = time.time()
        return instance


string_1 = My_String('new', 'string_1')
print(string_1)
print(string_1.upper())
print(string_1.title())
print(string_1.time)
print(string_1.name)
help(My_String)