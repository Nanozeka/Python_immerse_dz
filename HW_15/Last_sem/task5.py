# Дорабатываем задачу 4.
# Добавьте возможность запуска из командной строки.
# При этом значение любого параметра можно опустить. В этом случае берётся первый в месяце день недели,
# текущий день недели и/или текущий месяц.


import datetime

from task4 import input_text
import argparse


def pars_date():
    parser = argparse.ArgumentParser(prog="Работа с датой")
    parser.add_argument('-d', metavar='d', default='1-й')
    parser.add_argument('-w', metavar='w', default=datetime.datetime.now().weekday())
    parser.add_argument('-m', metavar='m', default=datetime.datetime.now().month)
    args = parser.parse_args()
    x = input_text(f'{args.d} {args.w} {args.m}')
    return x


if __name__ == "__main__":
    print(pars_date())