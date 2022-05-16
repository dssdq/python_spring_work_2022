'''#todo: Найти сумму элементов матрицы,
Написать msum(matrix)  которая подсчитывает сумму всех элементов функцию Найти сумму всех элементов матрицы:

>>> matrix = [[1, 2, 3], [4, 5, 6]]
>>> msum(matrix)
21'''

matrix = [[1, 2, 3], [4, 5, 6]]

def msym(matrix: list):
    list = [x for i in matrix for x in i]
    return sum(list)

print(msym(matrix))
