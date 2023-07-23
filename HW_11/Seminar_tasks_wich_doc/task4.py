# 4) Доработаем класс Архив из задачи 2. Добавьте методы представления экземпляра
# для программиста и для пользователя.


class Archive:
    """Doc1."""

    my_list_number = []
    my_list_string = []

# def __new__(cls, *args, **kwargs):
# instance = super().__new__(cls, *args, **kwargs)

    def __init__(self, number, my_string):
        """Doc2."""
        self.number = number
        self.my_string = my_string
        self.my_list_number.append(number)
        self.my_list_string.append(my_string)

    def __str__(self):
        """Doc3."""
        return f'Экземпляр класса Archive с числом "{self.number}" и строкой "{self.my_string}"'

    def __repr__(self):
        """Doc4."""
        return f'Archive({self.number}, {self.my_string})'



a = Archive(5, 'five')
print(f'{a.my_list_number = }, {a.my_list_string = }')
b = Archive(4, 'four')
print(f'{b.my_list_number = }, {b.my_list_string = }')
help(Archive)
print(a)
print(repr(b))
help(Archive)