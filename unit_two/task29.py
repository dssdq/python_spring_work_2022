#todo Задача 2. Транспонирование матрицы, transpose(matrix)
'''Написать функцию transpose(matrix), которая выполняет транспонирование матрицы. Решить с использованием списковых включений.

Пример:
>>> transpose([[1, 2, 3], [4, 5, 6]])

[[1, 4], [2, 5], [3, 6]]

||1 2 3||      ||1 4||
||4 5 6||  =>  ||2 5||
               ||3 6||'''
list = [[1, 4], [2, 5], [3, 6]]

def transpose(matrix: list):
    trans1 = [[matrix[j][i] for j in range(len(matrix))] for i in range (len(matrix[0]))]
    trans2 = [[trans1[j][i] for j in range(len(trans1))] for i in range(len(trans1[0]))]
    return trans1, trans2

print(transpose(list))

