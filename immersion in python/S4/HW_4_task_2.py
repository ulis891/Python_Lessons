"""
Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления и снятия средств в список.
"""

"""
Банкомат
Начальная сумма равна - 0
Допустимые действия: пополнить, снять, выйти
Сумма пополнения и сянятия - 50
Процент за снятие 1.5% от суммы снятия, но не менее 30 и не более 600
После каждой 3 операции пополнения или снятия, начисляются проценты - 3%
При превышении суммы в 5 млн., вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
Любое действие выводит сумму на счете
"""



def show_money(account):
    print(account)


def replenishment(account, operation_list):
    try:
        summ = int(input("Введите сумму пополнения кратную 50\nИли введите 0 для отмены\n"))
    except ValueError:
        print("Введите число!")
        replenishment(account, operation_list)
    if summ == 0:
#         todo дописать приложение так, что бы можно было выходить обратно в меню


def withdrawal():
    pass


def wealth_tax():
    pass


def tax():
    pass


def income():
    pass


def exit():
    pass


def mistake():
    print("Неизвестная команда")


def menu():
    print("Введите команду:")
    return input("1 - показать баланс\n2 - пополнить счёт\n3 - снять наличные\n4 - выход\n")


def atm():
    flag = True
    account = 0
    operation_list = []
    while flag:
        comand = menu()
        if comand == "1":
            show_money(account)
        elif comand == "2":
            replenishment(account, operation_list)
        elif comand == "3":
            withdrawal()
        elif comand == "4":
            exit()
        else:
            mistake()


atm()
