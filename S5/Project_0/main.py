l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

list(filter(lambda x: max(x) > 5, l))

"""В файле находится N натуральных числел, записанных через пробел. Среди них не хватает одного,
что бы выполнить условие A[i] - 1 = A[i-1]. Найдите его."""

with open('Task_1.txt') as numbers:
    for num in numbers:
        num_list = list(map(int, num.split(' ')))

new_num_list = []
for i in range(len(num_list)):
    if num_list[i] - 1 != num_list[i-1]:
        new_num_list.append(num_list[i] - 1)

print(new_num_list)


"""Дан список чисел. Выделить среди них числа, удовлетворяющие условию: следующее больше предыдущего."""