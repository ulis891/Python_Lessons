# This is a sample Python script.

# import zipfile
# import os
#
# dir_path = os.getcwd() # Получаем путь до исполняемого файла
# files_path = [file_path for file_path in os.listdir(dir_path) if os.path.isfile(file_path)] # Итерируемся по файлам в дериктории и проверяем является ли элемент файлом
# zip_path = os.path.join(dir_path, 'new.zip') # добавляем путь до нового zip файла
# zip_file = zipfile.ZipFile(zip_path, 'w') # Создаем zip фаил
# for file_path in files_path:
#     zip_file.write(file_path) # Записываем файлы в zip фаил
# zip_file.close() # закрвваем фаил (обязательно) или исползовать with

# Для натурального n создать словарь индекс - значение, состоящий из элементов последовательности 3n + 1
#
# n = int(input('Введите n'))
# dic_result = {}
# for i in range(1, n + 1):
#     dic_result.update({i: 3 * i + 1})
# print(dic_result)

# Напишите программу, в которой пользователь буде задавать две строки, а программа - определять количество
# входлений одной строки в другой

# string_one = input('Введите первые данные: ')
# string_two = input('Введите вторые данные: ')
# result = set(string_one) & set(string_two)
#
# print(len(result))


# Напишите программу, которая принимает на вход вещественное число и
# и показывает её сумму

number = (input('Введите число: ')).replace(',', '0')
sum_numbers = 0
for i in number:
    sum_numbers += int(i)
print(sum_numbers)