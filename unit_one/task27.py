#todo: Для игры "Отгадай число от 0 до 100" реализованной на занятии 4 homework/task3
'''написать Save Game по следующему сценарию:
В запущенной игре по нажатию клавиши S появляется вывод:
1. Продолжить
2. Сохранить игру

При выборе пункта 1. игра продолжается.
При выборе пункта 2. пользователю предлагается ввести название для
сохранения, после чего нужно сделать сериализацию состояния игры.
Законсервировать все объекты которые отвечают за состоянии игры в файл
game_dump.pkl   Сериализацию и десериализацию сделать на базе библиотеки pickle.

При старте игры пользователю должен предлагатся выбор
1. Новая игра
2. Восстановить игру
При выборе 1. начинается новая игра.
При выборе 2. пользователю выводится список всех сохраненных игр(происходит десериализация).
Из них он выберает нужную, после чего загружается состояние игры на момент сохранения.'''
import pickle
import random
from serializer.serializer import to_pickle
from serializer.deserializer import from_pickle

x = random.randint(0, 100)
print(x)
count = 0

menu = int((input('Добро пожаловать в игру "отгадай число"\n Выберите вариант: \n 1. Новая игра \n 2. Восстановить игру\n')))

def save_game(S: str):
    print(" Выберите вариант: \n1. Продолжить\n2. Сохранить игру")
    user_input2 = int(input())
    if user_input2 == 1:
        print('Игра продолжается')
        block_game(x, count)
    pass
    if user_input2 == 2:
        print('Переходим к сохранению игры....')
        name_save = input("Введите имя сохранения:\n>>")
        f = open("list_save.txt", mode="at", encoding="UTF-8")  # В отдельный файл пишу название сохранения
        f.write(name_save + " ")  # Разделяю сохранения пробелом
        list_x = []
        list_x = x, count  # В список принимаю загаданное число и кол-вао попыток
        f.write(str(list_x))
        f.close()
        to_pickle(str(list_x), name_save + ".pkl")  # Серелизую список(обьект) в файл по введенному названию


def block_game(x:int, count: int):
    while count < 10:
        user_input = input('Введите число: ')
        if user_input.isdigit() == True:  # если введено число продолжаем стандартный блок игры
            user_input = int(user_input)
            if user_input < x:
                print(f'Загаданное число больше, кол-во попыток {count - 9}')
            if user_input > x:
                print(f'Загаданное число меньше, кол-во попыток {count - 9}')
            count += 1
            number_count = count
            if user_input == x:
                print(f'Вы отгадали число за {count} попыток. Поздравляем!')
                break
            if user_input != x and count == 10:
                print(f'Вы не отгадали число за {count} попыток, загаданное число было {x}')
                break
        if user_input == 'S' or user_input == 's':
            save_game('S')  # Вызываем меню сохранения
            break
    return count
def start_game(start: int):
    if start == 1:
        print('Игра началась')
        block_game(x, count)
    if start == 2:
        print('Переходим к восстановлению игры')
        fx = open("list_save.txt", mode="r", encoding="UTF-8")  # Читаю из файла названия сохранений
        print("Список сохранений\n", fx.readlines())  #
        input_save = input('Введите имя сохранения: ')
        list_save = from_pickle(input_save + ".pkl")
        print(list_save)


start_game(menu)      # старт игры


