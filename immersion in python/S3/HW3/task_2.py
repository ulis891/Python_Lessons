"""
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант.

*Верните все возможные варианты комплектации рюкзака.
"""

staf = {"палатка": 15,
        "нож": 5,
        "спички": 1,
        "фонарь": 5,
        "трусы": 5,
        "носки": 4,
        "шапка": 3,
        "котелок": 20,
        "консервы": 25
        }

bag = 50

staf_list = sorted(staf.items(), key=lambda item: item[1], reverse=True)
bag_list = []
for k, v in staf_list:
    if bag - v >= 0:
        bag -= v
        bag_list.append(k)

print(bag_list)

"""
Решение ниже я разработал не сам а с помощю ChatGPT. Оставил для дальнейшего изучения
"""
def find_combinations(items, max_capacity):
    combinations = []  # список для хранения всех возможных вариантов комплектации рюкзака

    # Функция, реализующая рекурсивный процесс поиска вариантов комплектации рюкзака
    def find_combs(item_lst, capacity, cur_comb):
        if capacity == 0:  # Если рюкзак заполнен до максимальной грузоподъемности
            combinations.append(list(cur_comb))  # Добавляем найденную комплектацию в список combinations
            return
        elif capacity < 0 or len(item_lst) == 0:  # Если превышена грузоподъемность или нет больше предметов
            return

        # Перебираем все возможные варианты:
        # Вариант, в котором текущий предмет исключается из комплектации
        find_combs(item_lst[1:], capacity, cur_comb)

        # Вариант, в котором текущий предмет включается в комплектацию
        if item_lst[0][1] <= capacity:  # Проверяем, что предмет можно положить в рюкзак
            cur_comb.append(item_lst[0][0])  # Добавляем предмет в комплектацию
            find_combs(item_lst[1:], capacity - item_lst[0][1],
                       cur_comb)  # Рекурсивно вызываем функцию для следующих предметов
            cur_comb.pop()  # Удаляем последний добавленный предмет, чтобы попробовать другие варианты

    find_combs(items, max_capacity, [])
    return combinations


# Преобразуем словарь в список кортежей для более удобной обработки
items_list = list(staf.items())

max_capacity = 50  # Максимальная грузоподъемность рюкзака

# Получаем все возможные варианты комплектации рюкзака
combinations = find_combinations(items_list, max_capacity)

# Выводим результаты
for i, comb in enumerate(combinations):
    print(f'Вариант {i + 1}:')
    for item in comb:
        print(item)
    print()