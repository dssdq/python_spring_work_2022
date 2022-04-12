# todo: Даны переменные A, B, C. Изменить их значения, переместив содержимое A в B, B — в C, C — в A,
# и вывести новые значения переменных A, B, C.
A = int(input())
B = int(input())
C = int(input())
A,B,C=B,C,A
print(A,B,C)
