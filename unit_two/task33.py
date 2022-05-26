#todo: Написать авторизацию пользователя в систему.
'''Приложение в начале должно предлагать меню
1. Вход
2. Регистрация

1. При выборе пункта "Вход" пользователю необходимо ввести
логин и пароль, поэтапно.
login: _________
password: ________
При вводе данных авторизации, система проверяет есть ли данный
пользователь в БД (логин) если нет то предлагает зарегистрироваться.
Если есть и пароли совпадают, то происходит вход в систему. Пользователю показывается
приглашение вида "Добро пожаловать Вася Пупкин!" и выпадает меню
выбора билетов для тестирования(пока заглушка).

2. При выборе "Регистрация" пользователю необходимо ввести новый
логин, пароль, фио, почту, телефон, группу. После система заводит
запись в БД если пользователя под данным логином нет. Если такой пользователь
уже существует то программа выдает об этом сообщение. Пароль необходимо хранить в БД
в виде хеша + соль.

По хешированию прочитать статью
https://pythonist.ru/heshirovanie-parolej-v-python-tutorial-po-bcrypt-s-primerami/
для хеширования пароля воспользоваться библиотекой bcrypt'''

import psycopg
import bcrypt

action = int(input('Выберите действие:\n'
                   '1. Войти\n'
                   '2. Зарегистрироваться\n'))

def new_user():
    print('Регистрация в системе тестирования')
    u_name = str(input('Введите своё имя: '))
    u_sname = str(input('Введите свою фамилию: '))
    u_age = int(input('Введите свой возраст: '))
    u_phone = str(input('Введите свой телефон: '))
    u_email = str(input('Введите свой email: '))
    u_group = str(input("Введите номер своей группы: "))
    u_login = str(input('Введите желаемый логин(eng): '))
    u_psw = str(input('Введите пароль: '))
    conn = psycopg.connect("dbname=testsystem user=testsystem password=123 host = localhost")
    print('Подключение к базе данных выполнено')
    cur = conn.cursor()
    cur.execute("""
    insert into "user" (first_name, surname, age, phone, email)
    values (%s, %s, %s, %s, %s)""", (u_name, u_sname, u_age, u_phone, u_email))

    cur.execute("""
        insert into "profile" (login, password)
        values (%s, %s)""", (u_login, u_psw))
    print(f" Пользователь {u_name} {u_sname} зарегистрирован с логином - {u_login} Сейчас вы получите свой тест"
          f"\nВызвать функцию выдачи теста")
    cur.close()
    conn.commit()

if action == 1:
    lgn = str(input("Введите имя пользователя (login): "))
    psw = str(input("Введите пароль: "))
    conn = psycopg.connect("dbname=testsystem user=testsystem password=123 host = localhost")
    print("database connect successfully")
    cur = conn.cursor()
    cur.execute("""
    select login, password from profile where login like (%s)
    and password like (%s)""", (lgn, psw))
    user_auth = cur.fetchone()
    if user_auth is None:
        print('Введены не корректные данные либо пользователь с таким логином\паролем не существует\n'
              'Переходим к регистрации')
        new_user()
    else:
        print('Добро пожаловать, пользователь c login: ', user_auth[0],'\n Сейчас вы получите свой тест (вызываем функцию выдачи теста)')
    cur.close()
    conn.commit()
elif action == 2:
    new_user()
else:
    print("Ввод некоректный!")






