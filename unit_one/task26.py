#todo: Изучаем пакет pandas
# После установки библиотеки pandas выполните следующие действия:
# Изучите справку по модулю (для чего нужен модуль , какие возможности предоставляет)
# Найдите расположение директории модуля pandas и изучите его содержимое
# Получите список доступных атрибутов модуля pandas
# Импортируйте модуль pandas в исполняемый скрипт
# С помощью модуля pandas ознакомьтесь со структурой  DataFrame, фильтрации данных,
# загрузки данных из формата сsv (рассмотрите примеры статьи)
# Установите библиотеку matplotlib, создайте график на своем наборе данных.

#Опорная статья:  https://egorovegor.ru/pandas-obrabotka-i-analiz-dannyh-v-python/
import matplotlib.axes
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("titanic.csv")
#print(df.head(5))    # показать первые пять строчек файла
#print(df.info())     # показать инфо по фрейму
#print(df.describe(include= 'all'))    # статистика по данным
#df.dropna(inplace = True)    # удалить пустые занчения в исходном файле

#print(df["Cabin"])       # выгрузка отдельного столбца
df.pivot_table('PassengerId', 'Pclass', 'Survived', 'count','Age').plot(kind='bar',stacked = True)

plt.show()

print(df[df.Age < 26])       # сортировка по возрасту
df.Age.plot.hist()
plt.show()
