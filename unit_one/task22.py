# todo: Шифр Цезаря

f = open("message.txt", mode="r", encoding="utf-8")
lines = f.readlines()
alpha_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alpha_upper = alpha_lower.upper()
shift = int(input('Введите сдвиг для шифра Цезаря: '))
#print(lines)


def number_strok(lines: list) -> int:
    ''''эта функция возвращает кол-во строк
    в исходном сообщении для шифрования построчно'''
    number_strok = str(lines).count("\\n")
    return number_strok

def translate(c: str, alphabet: str, shift: int):
    '''Эта функция транслирует символ "с"
    со смещением на shift в заданном алфвавите "alphabet
    и его возвращает"'''
    alphabet = [c for c in alphabet]        # справедливо для с в выбраном ниже алфавите
    index = (alphabet.index(c) + shift) % len(alphabet)    # формула насколько я понял универсальная
    return alphabet[index]


result = []
# сначала цикл по строкам, получаем индекс и значение одновременно
for i, l in enumerate(lines):
    #шифрованная строка изначально пустая
    encrypted = ""
    #цикл по символам строки
    for c in l:
        #менять только если кириллица
        if c in alpha_lower:
            c = translate(c,alpha_lower,i+shift)
        if c in alpha_upper:
            c = translate(c,alpha_upper,i+shift)
        #записываем в шифрованную строку
        encrypted += c
    #добавляем в результат
    result.append(encrypted)
print(result)



# ord() - преобразование символа в код ascii
# chr() - преобразование ascii в код обратно

'''for count, value in enumerate(lines):   # считываем индекс строки и саму строку
    encrypted = ""  # строка куда будем добавлять зашифрованное сообщение
    for c in value:           # проверяем символ на вхождение в заданную строку
        if c in alpha_lower:         # проверяем каждый символ по отдельности на вхождение в алфавит
            t = alpha_lower.find(c)        # получаем правильный индекс итерируемой буквы из алфавита
            new_key = t + 1         # смещаем это дело на один символ
            #print(t,new_key)
            result.insert(new_key,c)       # это неверное решение, так замещаются и символы и буквы и рандомно
print(*result)'''



