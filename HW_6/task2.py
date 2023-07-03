# Задача 2

# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

# Код из семинара

# Вводить нужно в терминале формата (python task2.py 29.02.2102)

import sys
def input_data(date):
    m_30 = [4, 6, 9, 11]
    m_31 = [1, 3, 5, 7, 8, 10, 12]
    day, month, year = map(int, date.split('.'))
    if 1 <= year <= 9999:
        if 1 <= month <= 12:
            if month == 2:
                if _visokos(year):
                    if 1 <= day <= 29:
                        return True
                else:
                    if 1 <= day <= 28:
                        return True
            if month in m_30 and 1 <= day <= 30:
                return True
            if month in m_31 and 1 <= day <= 31:
                return True
    return False


def _visokos(year):

    ULIAN = 4
    GRIG_1 = 400
    GRIG_2 = 100

    return year % GRIG_1 == 0 or year % GRIG_2 != 0 and year % ULIAN == 0


if __name__ == '__main__':
    date = sys.argv[1]
print(input_data(date))