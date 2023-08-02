# Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая” и т.п.
# Преобразуйте его в дату в текущем году.
# Логируйте ошибки, если текст не соответсвует формату.


import logging
import datetime

FORMAT = '{levelname:<8} - {asctime}. В модуле "{name}" ' \
        'в строке {lineno:03d} функция "{funcName}()" ' \
        'в {created} {msg}'

logging.basicConfig(format=FORMAT, style="{", filename="log4", filemode='a', encoding="Utf-8", level=logging.ERROR)
logger = logging.getLogger()


def input_text(text: str):
    days_of_week = {
    'понедельник': 0,
    'вторник': 1,
    'среда': 2,
    'четверг': 3,
    'пятница': 4,
    'суббота': 5,
    'воскресенье': 6
    }
    months = {
    'января': 1,
    'февраля': 2,
    'марта': 3,
    'апреля': 4,
    'мая': 5,
    'июня': 6,
    'июля': 7,
    'августа': 8,
    'сентября': 9,
    'октября': 10,
    'ноября': 11,
    'декабря': 12
    }

    try:
        a, b, c = text.split()
        a = int(a[0])
        weekday = days_of_week[b]
        month = months[c]
        for day in range(1, 32):
            date_res = datetime.datetime(month=month, day=day, year=datetime.datetime.now().year)
            if date_res.weekday() == weekday:
                return date_res
    except Exception as e:
        logger.error(f"Ошибочка вышла:{e}")

# print(input_text("4 четверг ноября"))