import datetime as dt
import chekers
import UI as ui

oper_count = 0  # Считает количество операций для начисления процентов


def cash_in(acc: int, ol: list):
    """
    Пополненике счёта
    """
    global oper_count
    try:
        summ = abs(int(input("Введите сумму пополнения кратную 50\nИли введите 0 для отмены\n")))
        if summ != 0:
            if chekers.chek_summ(summ):
                acc += summ
                ol.append(f"{dt.datetime.now()} : приход : {summ}")
                oper_count += 1
                if chekers.chek_ops(oper_count):
                    acc = income(acc, ol)
            else:
                print("Введите число кратное 50!")
                cash_in(acc, ol)
    except ValueError:
        print("Введите число!")
        cash_in(acc, ol)
    finally:
        ui.show_money(acc)
        return acc


def cash_out(acc: int, ol: list):
    """
    Снятие наличных
    """
    global oper_count
    try:
        summ = abs(int(input("Введите сумму снятия кратную 50\nИли введите 0 для отмены\n")))
        if summ != 0:
            if chekers.chek_summ(summ):
                summ += pay_tax(summ, ol)
                if summ > acc:
                    ui.mistake(2)
                else:
                    acc -= summ
                    ol.append(f"{dt.datetime.now()} : снятие : {summ}")
                    oper_count += 1
                    if chekers.chek_ops(oper_count):
                        acc = income(acc, ol)
            else:
                print("Введите число кратное 50!")
                cash_out(acc, ol)
    except ValueError:
        print("Введите число!")
        cash_out(acc, ol)
    finally:
        ui.show_money(acc)
        return acc


def wealth_tax(acc: int, ol: list):
    """
    Налог на богатсво
    :param acc: Аккаунт с которого будет взываться налог
    :param ol: Список для внесения информации об операции
    """
    if chekers.chek_richness(acc):
        tax = acc * 0.1
        acc -= float(format(tax, ".2f"))
        print(f"Оплата налога на богатство : {tax}")
        ol.append(f"{dt.datetime.now()} : оплата налога на богатство : {tax}")


def pay_tax(cash, ol):
    """
    Комисия за операции
    """
    tax = cash * 0.015
    if tax < 30:
        tax = 30
    elif tax > 600:
        tax = 600
    print(f"Комиссия за операцию составит {tax}")
    ol.append(f"{dt.datetime.now()} : оплата комисси за операцию : {tax}")
    return float(format(tax, ".2f"))


def income(acc, ol):
    """
    Выплата процентов
    :param acc: Счет на который будут выплачиватся ошибки
    :param ol: Список для внесения записи об операции
    :return: Счет с внесенными изменениями
    """
    prc = float(format(acc * 0.03, ".2f"))
    acc += prc
    ol.append(f"{dt.datetime.now()} : приход процентов : {prc}")
    print(f"Вам начисленны проценты в количестве {prc}")
    return acc
