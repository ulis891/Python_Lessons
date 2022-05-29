def new_string(symbol, count=3):
    return symbol * count


print(new_string('!', 50))


def concatenation(*params):  # неограниченное колличество аргументов
    res: str = ""  # явно указываем тип аргумента
    for item in params:
        res += item
    return res


print(concatenation('a', 'r', '5', 'rtd'))


def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


list = []
for e in range(1, 10):
    list.append(fib(e))
print(list)
