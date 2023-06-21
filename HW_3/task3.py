# Задача 3

# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии
# или из документации к языку.

import collections


# загрузка текста из файла
with open('c:\GeekBrains\Pogruzenie_Python\Python_immerse_dz\HW_3\Text_wiki.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# удаление всех знаков препинания
text = text.replace('\n', '')

# преобразование к нижнему регистру и разбиение на слова
words = text.lower().split()

# подсчет количества слов
word_count = len(words)
print("Количество слов:", word_count)

# подсчет слов
word_counter = collections.Counter(words)

# вывод 10 самых частых слов
most_common_words = word_counter.most_common(10)
print("10 самых частых слов:")
for word, count in most_common_words:
    print(word, count)