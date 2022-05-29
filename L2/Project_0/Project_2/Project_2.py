t = ()  # кортеж
a = (4,)  # если без запятой то кортеж не получится

dic = {}
dic = \
    {'up': '8',
     'down': '2',
     'left': '4',
     'right': '6'
     }
print(dic)
print(dic['up'])
del dic['left']  # удаление елемента

for item in dic:
    print('{}: {}'.format(item, dic[item]))

a = {1, 2, 3, 4, 5, 6, 7, 8}
b = {5, 6, 7, 8, 9, 0}
c = a.copy()  # копируем множество
u = a.union(b)  # объединяем множества
i = a.intersection(b)  # пересечение множеств
dl = a.difference(b)  # что есть только. в а
dr = b.difference(a)  # что есть толька в b

q = a \
    .union(b) \
    .difference(a.intersection(b))

s = frozenset() # неизменяемое множество

