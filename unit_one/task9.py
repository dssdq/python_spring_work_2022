# todo:  Даны три переменные: X, Y, Z. Их значения числа.
# Из данных произвольных чисел выбрать наибольшее.

# Пример:
# X = 5
# Y = 10
# Z = 3
# Ответ: Наибольшее число 10.
#
# X = 10
# Y = 12
# Z = -7
# Ответ: Наибольшее число 12.
x = int(input('x='))
y = int(input('y='))
z = int(input('z='))
if x > z and x > y:
    print('Наибольшее число ',x)
elif x < y > z:
    print('Наибольшее число ',y)
else:
    print('Наибольшее число ',z)
