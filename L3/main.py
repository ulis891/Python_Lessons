"""List Comprehansion"""

list0 = [i for i in range(15)]
print(list0)

list1 = [i for i in range(1, 15) if i % 2 == 0]
print(list1)

list2 = [(i, i ** 2) for i in range(1, 15) if i % 2 == 0]
print(list2)


def f(x):
    return x ** 3


list3 = [f(i) for i in range(1, 15) if i % 2 == 0]
print(list3)

list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
list5 = [(i, i ** 2) for i in list4 if i % 2 == 0]
print(list5)

"""map()"""

li = [i for i in range(1, 20) if i % 2 == 0]

li = list(map(lambda i: i + 10, li))

print(li)

data = list(map(int, input().split()))
print(data)


"""filter()"""

list6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

res = list(filter(lambda x: x%2==0, list6))

print(f'res = {res}')

"""zip"""
res1= list(zip(list6,list3))
print(res1)

"""enumerate()"""

res2 = list(enumerate(res1))
print(res2)