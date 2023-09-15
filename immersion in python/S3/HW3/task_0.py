"""
Дан список повторяющихся элементов.
Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
"""

my_list = [1, 2, 7, 4, 5, 1, 2, 2, 2, 4]
new_list = []
for i in my_list:
    if i not in new_list and my_list.count(i) > 1:
        new_list.append(i)
print(new_list)