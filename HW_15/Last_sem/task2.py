# На семинаре про декораторы был создан логирующий декоратор.
# Он сохранял аргументы функции и результат её работы в файл.
# Напишите аналогичный декоратор, но внутри используйте модуль logging.

import math
import logging

logging.basicConfig(filename="log2", filemode='a', encoding="Utf-8", level=logging.INFO)
logger = logging.getLogger(__name__)


def deco(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(f"{args} {result}")

    return wrapper


@deco
def homework_9(a, b, c):
    if a == 0:
        return None
    dis = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis))
    if dis > 0:
        return [(-b + sqrt_val) / (2 * a), (-b - sqrt_val) / (2 * a)]
    elif dis == 0:
        return [(-b / (2 * a))]
    else:
        x = (- b / (2 * a))
        return [f"{x}+ i*{sqrt_val}", f"{x}- i*{sqrt_val}"]


if __name__ == "__main__":
    homework_9(3, 4, 5)