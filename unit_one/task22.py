# todo: Шифр Цезаря

f = open("message.txt", mode="r", encoding="utf-8")
lines2 = f.readlines()
lines = str(lines2).lower()          # исходное сообщение переведём в все строчные символы
alpha_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alpha_upper = alpha_lower.upper()
result = []
encrypted = ""                         # строка куда будем добавлять зашифрованное сообщение
i = 0
s = 0
for count, value in enumerate(lines):   # считываем индекс строки и саму строку
    encrypted = ""  # строка куда будем добавлять зашифрованное сообщение
    for c in value:           # проверяем символ на вхождение в заданную строку
        if c in alpha_lower:         # проверяем каждый символ по отдельности на вхождение в алфавит
            t = alpha_lower.find(c)        # получаем правильный индекс итерируемой буквы из алфавита
            new_key = t + 1         # смещаем это дело на один символ
            print(t,new_key)
#что делать дальше я так и не понял
        #encrypted = c + encrypted                                            # добавить в строку encrypted букву с индексом new_key



            #encrypted = ''.join(new_key)

#print(encrypted)


    #print(count,value)




# ord() - преобразование символа в код ascii
# chr() - преобразование ascii в код обратно

