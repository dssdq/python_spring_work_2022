#todo: Задан словарь, его значения необходимо внести по соответвющим тегам и атрибутам вместо
# вопросов (?)
# заполненный шаблон записать в файл index.html   #
page = {"title": "Тег BODY",
        "charset": "utf-8",
        "alert": "Документ загружен",
        "p": "Ut wisis enim ad minim veniam,  suscipit lobortis nisl ut aliquip ex ea commodo consequat."}
vstavit = []
key_page = []
for key, values in page.items():    # вытащить ключ - значение в список
        vstavit.append(values)
        key_page.append(key)

f = open("index_origin.html", mode="r", encoding="utf-8")
f2 = open('index.html', mode='w',encoding='utf-8')     #куда будем писать готовый файл
x = f.readlines()       #считываем первый файл с шаблоном
stroka = ''.join(x)       # преобразуем список в строку
s = 1
m = 0
f2.write(stroka)                     # записываем во второй файл шаблон
#print(type(x),type(key_page))
for key_page in stroka:              # условие для ключей словаря которые есть в шаблоне
        print(stroka.index('?', s))
        position = f.seek(stroka.index('?', s))
        f2.seek(position)
        f2.write(vstavit[m] + stroka[position + 1:])
        s = s + stroka.index('?', 1)
        m = m + 1




#position = f.seek(41)   # найти позицию





f.close()





#сделать реплайс на тег боди или
#спозиционировать корретку приоритетней!
#либо как форматированный текст


#коретка обратить внимание на начало чтения позицию каретки
