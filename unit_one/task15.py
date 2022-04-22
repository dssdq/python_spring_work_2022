import random
words = ["оператор","конструкция","объект"]
desc_  = [ "Это слово обозначает наименьшую автономную часть языка программирования",
           "Это слов означает следование, ветвление и цикл", "Это слово означает некоторую сущность" ]
x = random.choice(words)    #Слово из списка words берется случайно
print(desc_[words.index(x)])   #Выводим описание выбранного слова по индексу из списка
slovo = list(range(0,len(x))) #пустой список куда будем добавлять отгаданные буквы, размера загаданного слова
for i in slovo:
    slovo[i] = '#'       # так больше похоже на загадку
print('Количество букв в слове: ',*slovo,x,'dlina slova:',len(slovo))  #подсказка 
count = 0
s = 0
while count < 10:
    user_input = str(input('Введите букву: '))
    if user_input in x and x.count(user_input) == 1:     # буква одна в слове, тут ясно
        slovo.remove('#')  # удаляем заведомо пустую букву в списке, т.к. дальше будет один insert
        slovo.insert(x.index(user_input), user_input)
        print(slovo)                                       # на слове объект

    if user_input in x and x.count(user_input) == 2:   # если вхождений больше двух
        slovo.remove('#')          # удаляем две буквы так как два вхождения, эти буквы они пустые
        slovo.remove('#')
        '''if slovo.insert(x.index(user_input), user_input) != slovo.index('#'):
            slovo.remove('#')'''
        slovo.insert(x.index(user_input), user_input)       #берём индекс первой буквы
        #slovo.insert(x.index(user_input,1,), user_input)   # затем индекс второй и что то идёт не так, чаще работает
        slovo.insert(x.index(user_input, x.index(user_input)+1, ), user_input)
        print(slovo)


    if user_input in x and x.count(user_input) == 3:
        print('tri vhogdeniya')


    if user_input not in x:
        count += 1
        print('в слове нет такой буквы у вас осталось ', 10-count, 'попыток')

    if slovo == list(x) and count < 10:
        print('Вы отгадали слово с ', count, 'попыток')
        break
