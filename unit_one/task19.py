#todo: Требуется создать csv-файл «algoritm.csv» со следующими столбцами:
'''– id - номер по порядку (от 1 до 10);
– текст из списка algoritm"
'''
#Каждое значение из списка должно находится на отдельной строке.
algoritm = [ "C4.5" , "k - means" , "Метод опорных векторов" , "Apriori" ,
"EM" , "PageRank" , "AdaBoost", "kNN" , "Наивный байесовский классификатор" , "CART" ]

f = open("algoritm.csv", mode="wt", encoding="utf-8")
id = list(range(1,11))     #генерируем список

for index in range(len(id)):      #для индексов из обоих списков в 10 строк
    f.writelines(str(id[index]) + ';' + str(algoritm[index] + "\r"))    #соединяем в столбцы по индексу из цикла

f.close()
