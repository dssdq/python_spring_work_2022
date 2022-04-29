#todo: Взлом шифра
'''Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
Попробуйте все возможные сдвиги и расшифруйте фразу.'''

fraza = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."
alpha_lower = 'abcdefghijklmnopqrstuvwxyz'
alpha_upper = alpha_lower.upper()
shift = int(input('Введите сдвиг для расшифровки шифра Цезаря: '))

i = 1




'''def unlock_shift(shift: int) -> int:
    while shift < len(fraza):                 # генерация shift по длине загаданной фразе, для вывода всех комбинаций
        shift = i + shift
        return shift



unlock_shift(shift)'''

def retranslate(c: str, alphabet: str, shift: int):
    '''Эта функция транслирует символ "с"
    со смещением на shift в заданном алфвавите "alphabet
    и его возвращает"'''
    alphabet = [c for c in alphabet]        # справедливо для с в выбраном ниже алфавите
    index = (alphabet.index(c) - shift) % len(alphabet)    # меняем при дешифровке знак на минус
    return alphabet[index]

result = []

for i, l in enumerate(fraza):    # сначала цикл по строке, получаем индекс и значение одновременно
    #шифрованная строка изначально пустая
    encrypted = ""
    #print(i,l)
    #цикл по символам строки
    for c in l:
        #менять только если кириллица
        if c in alpha_lower:
            c = retranslate(c,alpha_lower,i-shift)
        #записываем в шифрованную строку
        encrypted += c
    #добавляем в результат
    result.append(encrypted)
print(*result)