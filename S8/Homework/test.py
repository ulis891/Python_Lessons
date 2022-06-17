import user_interface as ui

# with open('DataBase/Parents.txt', 'r', encoding='utf-8') as f:
#     data = csv.reader(f, delimiter=' ', quotechar='|')
#     for row in data:
#         if ', '.join(row)[-1] == '5':
#             print(', '.join(row))

with open('DataBase/Students.txt', encoding='utf-8') as f:
    for row in f:
        print(row.split(';')[0])

