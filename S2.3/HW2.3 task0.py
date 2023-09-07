"""
Напишите программу, которая получает целое число и возвращает
его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
"""

hex_dic = {"10": "A",
           "11": "B",
           "12": "C",
           "13": "D",
           "14": "E",
           "15": "F"}


def ten_to_hex(ten: int) -> str:
    """
    Приевращает из десятичного числа, шестнадцатиричное в виде строки
    """
    if (ten // 16) > 16:
        res.append(str(ten % 16))
        ten_to_hex(ten // 16)
    else:
        res.append(str(ten % 16))
        res.append(str(ten // 16))
    res.reverse()
    if res[0] == "0":
        res.pop(0)
    for i in range(len(res)):
        if res[i] in hex_dic:
            res[i] = hex_dic[res[i]]
    return "0x" + "".join(res)


num = int(input("Введите число: "))
res = []

print("Результат полученый через вручную - " + ten_to_hex(num))
print("Результат полученый через hex() - " + hex(num))
