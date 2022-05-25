# todo: Написать скрипт создания базы данных(ER-модели) TestSystem
# Скрипт  create_db.py  должен создавать таблицы, индексы , констрейнты в СУБД PostgresSQL
# В задании использовать библиотеку psycopg
#Ссылка на документацию
#https://www.psycopg.org/psycopg3/docs/basic/usage.html
#Для подключения использовать пользователя и базу отличную от postgres
# Note: the module name is psycopg, not psycopg3
import psycopg
conn = psycopg.connect("dbname=testsystem user=testsystem password=123 host = localhost")
cur = conn.cursor()
cur.execute("""create table "user" (
id_user serial primary key,
first_name varchar(25) not null,
surname varchar(25) not null,
age integer,
dt_create timestamp,
status boolean)""")
cur.execute("""create table "profile" (
id_profile serial primary key,
id_users integer,
login text not null,
password text not null,
dt_reg date,
avatar text,
dt_last_login date,
status boolean)""")
cur.execute("""create index "idx_profile_id_users" on "profile" ("id_users")
""")   # создаём индекс
cur.execute("""
alter table "profile" add constraint "fk_profile_id_users" foreign key ("id_users")
references "user" ("id_user")
""")    # констрейн, добавялем в таблицу профиль вторичный ключ id_users
cur.execute("""
insert into "profile" (login, password)
values ('vika_gr','12345')""")
cur.execute("""
insert into "profile" (login, password)
values ('dima_eg','12345')""")
cur.execute("""
insert into "user" (first_name, surname, age)
values ('Vika','Gromova', '25')""")
cur.execute("""
insert into "user" (first_name, surname, age)
values ('Dima','Edji', '27')""")
cur.execute("SELECT * FROM profile")
res = cur.fetchall()
for i in res:
    print(i)
cur.close()
conn.commit()


