#todo: Числа в буквы
'''Замените числа, написанные через пробел, на буквы. Не числа не изменять.

Пример.
Input	                            Output
8 5 12 12 15	                    hello
8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!'''

#user_input = input('vvedite chisla: ').split()
input_str2 = '8 5 12 12 15 , 0 23 15 18 12 4 !'
alphabet = "abcdefghijklmnopqrstuvwxyz"
out = []
input_str = input_str2.split(' ')

for i in input_str:  #
    encrypted = ''
    if i.isdigit() == True:
        if int(i) == 0:                     # если индекс ноль
            encrypted += (' ')      # добавляем пробелы
        else:
            encrypted = (alphabet[int(i) - 1]) + encrypted    # берём индекс из алфавита минус один
    else:
        encrypted += i
    out.append(encrypted)

print(*out)



# ord() - преобразование символа в код ascii
# chr() - преобразование ascii в код





