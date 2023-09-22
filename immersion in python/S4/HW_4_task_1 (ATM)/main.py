import UI as ui
import operations as op

"""
Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления и снятия средств в список.
"""

"""
Банкомат
Начальная сумма равна - 0
Допустимые действия: пополнить, снять, выйти
Сумма пополнения и сянятия - кратно 50
Процент за снятие 1.5% от суммы снятия, но не менее 30 и не более 600
После каждой 3 операции пополнения или снятия, начисляются проценты - 3%
При превышении суммы в 5 млн., вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
Любое действие выводит сумму на счете
"""

operation_list = []
account = 0

flag = True


def exit():
    """
    Закрытие программы
    """
    global flag
    flag = False


def comand(cmd: str):
    """
    Запускает функцию в зависимости от команды
    """
    global account, operation_list
    if cmd == "1":
        op.wealth_tax(account, operation_list)
        ui.show_money(account)
    elif cmd == "2":
        op.wealth_tax(account, operation_list)
        ui.show_history(operation_list)
    elif cmd == "3":
        op.wealth_tax(account, operation_list)
        account = op.cash_in(account, operation_list)
    elif cmd == "4":
        op.wealth_tax(account, operation_list)
        account = op.cash_out(account, operation_list)
    elif cmd == "0":
        exit()
    else:
        ui.mistake(1)


def atm():
    """
    Запускает работу банкомата
    """
    global flag
    while flag:
        comand(ui.menu())


atm()
