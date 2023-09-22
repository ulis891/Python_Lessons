def show_money(acc):
    """
    Выводит колличество денег на счёте
    """
    print(f"На вашем счету : {acc}")


def show_history(op):
    for i in op:
        print(*i)


def mistake(code: int):
    """
    Выводит сообщение об ошибке
    """
    match code:
        case 1:
            print("Неизвестная команда")
        case 2:
            print("Недостаточно средств")


def menu():
    """
    Выводит меню
    """
    print("Введите команду:")
    return input("1 - показать баланс\n2 - показать историю\n3 - пополнить счёт\n4 - снять наличные\n0 - выход\n")
