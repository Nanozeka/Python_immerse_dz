# Напишите программу, которая использует модуль logging для вывода сообщения об ошибке в файл.
# Например отлавливаем ошибку деления на ноль.


import logging
FORMAT = '{levelname:<8} - {asctime}. В модуле "{name}" ' \
            'в строке {lineno:03d} функция "{funcName}()" ' \
            'в {created} {msg}'

logging.basicConfig(format=FORMAT, style="{", filename="log", filemode='a', encoding="Utf-8", level=logging.ERROR)
logger=logging.getLogger(__name__)

def divivsion (a,b):
    try:
        return a / b
    except ZeroDivisionError:
        logger.error("Деление на 0")



divivsion(2,0)