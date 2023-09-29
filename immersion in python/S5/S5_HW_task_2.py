"""
Создайте функцию генератор чисел Фибоначчи
"""


def fibogen(n: int):
    """
    Генерирует ряд фибоначи
    @param n: Число выводимых чисел
    @return: число ряда Фибоначчи
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


for j in fibogen(10):
    print(j)
