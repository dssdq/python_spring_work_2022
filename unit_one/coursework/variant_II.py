#todo: II вариант (алгоритм сортировки слиянием)
'''Реализовать на Python алгоритм сортировки слиянием представленный в псевдокоде
в учебнике “Introduction to Algorithms”  на стр. 71 - 77.

Задача.
Перепишите процедуру  MERGE_SORT и отсортируйте последовательность'''
#A = [31, 41, 9, 26, 41, 58, -1 , 6 , 101 , 13] по возрастанию
A = [31, 41, 9, 26, 41, 58, -1 , 6 , 101 , 13]

def merge_sort(lst:list):
    if len(lst) > 1:
        mid = len(lst)//2          # разбиваем список пополам
        lefthalf = lst[:mid]               # левая часть
        righthalf = lst[mid:]
        merge_sort(lefthalf)               # вызываем внутри функцию
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len (righthalf):
            if lefthalf[i] < righthalf[j]:
                lst[k] = lefthalf[i]
                i += 1
            else:
                lst[k] = righthalf[j]
                j += 1
            k = k + 1
        while i < len(lefthalf):
            lst[k] = lefthalf[i]
            i += 1
            k +=1
        while j < len(righthalf):
            lst[k] = righthalf[j]
            j += 1
            k += 1
    #print("Сортированный список: ", lst)
    return




merge_sort(A)
print(A)
