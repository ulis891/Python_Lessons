"""
Напишите функцию для транспонирования матрицы
"""

a = [[12, 4],
     [5, 6],
     [7, 11],
     [3, 25]]


def trans_matrix(matrix: list) -> list:
    """
    Транспонирует матрицу
    """
    res = [[0]]
    line_size = len(matrix[0])
    col_size = len(matrix)
    for i in range(line_size):
        for j in range(col_size):
            if i >= len(res):
                res.append([0])
            if j == 0:
                res[i][j] = a[j][i]
            else:
                res[i].append(a[j][i])
    return res


def print_matrix(matrix: list) -> None:
    """
    Печатает матрицу
    """
    for i in matrix:
        print(*i)
    print()


def chek_matrix(matrix: list) -> bool:
    """
    Проверяет матрицу
    """
    len_chek = len(matrix[0])
    for el in matrix:
        if len(el) != len_chek:
            return False
    return True


def main(matrix: list):
    if chek_matrix(matrix):
        print("Начальная матрица", end="\n")
        print_matrix(matrix)
        print("Транспонированная матрица", end="\n")
        print_matrix(trans_matrix(matrix))


main(a)
