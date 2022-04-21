#todo: Дан массив размера N. Найти индексы двух ближайших чисел из этого массива.
'''
Пример:
mass = [1,2,17,54,30,89,2,1,6,2]
Для числа 1 индексы двух ближайших чисел: 0 и 7
Для числа 2 индексы двух ближайших чисел: 6 и 9
'''
mass = [1,2,17,54,30,89,2,1,6,2]
print(mass)
user_number = int(input('введите число для поиска индексов в массиве: '))
s = 0
for i in mass:
    if i == user_number and mass.count(user_number) == 1:   #перебираем массив и если только одно число выводим
        print('Индекс числа: ', mass.index(i))
    if i == user_number and mass.count(user_number) == 2: #перебираем массив и если только 2 включения выводим последовательно
        print(mass.index(i), mass.index(i, 1, ))
        break
    if i == user_number and mass.count(user_number) > 2:  # если более двух считаем стартовый индекс, увеличивая
        s = mass.index(i) + 1
        if mass.index(i,s+mass.index(i,s,)) > mass.index(i) < mass.index(i,s,):
            print(mass.index(i, s,) , mass.index(i, s + mass.index(i, s,)) )
            break














