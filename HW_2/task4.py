# Задача 4

# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

# Нет снятия налога на богатство при пополнении баланса
import math

# Функция для пополнения баланса
def add_money(balance, amount):

    # Если сумма не кратна 50 то выводим сообщение
    if amount % 50 != 0:
        print('Сумма пополнения должна быть кратной 50 у.е.')
        return balance

    # Если кратно то пополняем баланс
    balance += amount
    print(f'Вы пополнили свой баланс на {amount} у.е. Новый баланс: {balance} у.е.')
    return balance

# Функция для снятия денег
def withdraw_money(balance, amount):

    # Если сумма не кратна 50 то выводим сообщение
    if amount % 50 != 0:
        print('Сумма снятия должна быть кратной 50 у.е.')
        return balance

    # Если сумма снятия превышает баланс
    if amount > balance:
        print('Недостаточно средств на счете')
        return balance

    # Если баланс больше 5000000 берем комиссию 10%(налог на богатство) и вычитаем из баланса
    tax = 0
    if balance >= 5000000:
        tax = balance * 0.1
        balance -= tax
        print(f'Налог на богатство: {tax} у.е.')

    # Комиссию с любой суммы берем 1.5%
    commission = amount * 0.015

    # Но не меньше 30 у.е.(если получается меньше то увеличиваем до 30)
    commission = max(commission, 30)

    # Если больше 600 у.е. то уменьшаем до 600
    commission = min(commission, 600)
    balance -= amount + commission
    print(f'Вы сняли со счета {amount} у.е. Комиссия: {commission} у.е. Новый баланс: {balance} у.е.')
    return balance

# Функция банкомат
def atm():

    # Изначально баланс 0, количество операций 0
    balance = 0
    operations_count = 0
    while True:
        print(f'Ваш баланс: {balance} у.е.')
        action = input('Что вы хотите сделать? (пополнить, снять, выйти): ')
        if action == 'пополнить':
            amount = int(input('Введите сумму: '))
            balance = add_money(balance, amount)
        elif action == 'снять':
            amount = int(input('Введите сумму: '))
            balance = withdraw_money(balance, amount)
        elif action == 'выйти':
            break

        # После того как количество операций достигнет 3х к балансу прибавляем 3% от остатка
        operations_count += 1
        if operations_count == 3:
            balance += math.ceil(balance * 0.03)
            print(f'Вам начислены 3% наличных. Новый баланс: {balance} у.е.')

            # Счетчик операций обнуляем
            operations_count = 0

            # Вывод списка операций
            operations_list = []
            print('Список операций:')
            for operation in operations_list:
                print(operation)


atm()