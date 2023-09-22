def chek_summ(summ: int) -> bool:
    """
    Проверка суммы на кратность 50
    """
    if summ % 50 == 0:
        return True
    else:
        return False


def chek_ops(oc) -> bool:
    """
    Проверка колличества операций
    """
    if oc % 3 == 0:
        return True
    else:
        return False


def chek_richness(acc):
    """
    Проверка на богатсво
    """
    if acc > 5000000:
        return True
    return False
