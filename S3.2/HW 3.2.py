from random import randint as r

'''
Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X


Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

ОБЪЕДИНИЛ 2 ЗАДАЧИ В ОДНОМ РЕШЕНИИ
'''


def make_array(array_len: int) -> list:
    """создание массива"""
    array = []
    i = 1
    while i < array_len:
        array.append(r(1, 100))
        i += 1
    print(array)
    return array


def count_x(array: list, number: int) -> int :
    """поиск и подсчёт числа"""
    count = 0
    for i in array:
        if i == number:
            count += 1
    return count

def search_nearest(array: list, number: int) -> list:
    """Поиск ближайших чисел"""
    near = abs(array[0] - number)
    nearest_numbers = []
    nearest_numbers.append(array[0])
    for i in array:
        if abs(i - number) < near:
            nearest_numbers = []
            nearest_numbers.append(i)
            near = abs(i - number)
        elif abs(i - number) == near and i not in nearest_numbers:
            nearest_numbers.append(i)
    return nearest_numbers

n = int(input('Введите количество элементов в масиве: '))
x = int(input('Введите число для поиска: '))

random_list = make_array(n)

print(f'Число {x} встречается {count_x(random_list, x)} раз')
print('Ближайшие числа в массиве', search_nearest(random_list, x))


'''
*Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.

В случае с английским алфавитом очки распределяются так:
    A, E, I, O, U, L, N, S, T, R – 1 очко;
    D, G – 2 очка;
    B, C, M, P – 3 очка;
    F, H, V, W, Y – 4 очка;
    K – 5 очков;
    J, X – 8 очков;
    Q, Z – 10 очков.
    
    А русские буквы оцениваются так:
    А, В, Е, И, Н, О, Р, С, Т – 1 очко;
    Д, К, Л, М, П, У – 2 очка;
    Б, Г, Ё, Ь, Я – 3 очка;
    Й, Ы – 4 очка;
    Ж, З, Х, Ц, Ч – 5 очков;
    Ш, Э, Ю – 8 очков;
    Ф, Щ, Ъ – 10 очков.
    
Напишите программу, которая вычисляет стоимость введенного пользователем слова.
Будем считать, что на вход подается только одно слово, которое содержит либо 
только английские, либо только русские буквы.

*Пример:*

ноутбук
     12
'''

abc_score = {
    'AEIOULNSTRАВЕИНОРСТ': 1,
    'DGДКЛМПУ': 2,
    'BCMPБГЁЬЯ': 3,
    'FHVWYЙЫ': 4,
    'KЖЗХЦЧ': 5,
    'JXШЭЮ': 8,
    'QZФЩЪ': 10,
}

user_word = input('Введите слово:  ').upper()


def score_count(word: str) -> int:
    """подсчет очков"""
    score = 0
    for i in word:
        for j in abc_score.keys():
            if i in j:
                score += abc_score[j]
                break

    return score


print(f'Вы заработали {score_count(user_word)} очков!')
