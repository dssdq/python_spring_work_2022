#todo: Выведите все строки данного файла в обратном порядке.
# Для этого считайте список всех строк при помощи метода readlines().

'''Содержимое файла import_this.txt
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.

выходные данные
Complex is better than complicated.
Simple is better than complex.
Explicit is better than implicit.
Beautiful is better than ugly.'''

f = open("import_this.txt", mode="r", encoding="utf-8")
x = f.readlines()
#print(type(x))
x.reverse()                               # список с конца
for i in x:
    print(i)

f.close()
