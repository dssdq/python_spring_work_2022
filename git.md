+ git congig --global user.name dssdq
+ git config --global user.email oagoth@yandex.ru

+ git config --list

+ git init #каталог под наблюдение
+ git add file.xx # файл под версионирование
+ git add . #все файлы в каталоге под версионирование
+ .gitignore   # в файл заносим то, что не наблюдаем


- git status

- git rm –cashed имя_файла # Удаление индексации файла
- git rm -f имя_файла  # Удаление из индекса и  из проекта

- git commit -m "Комментарий к коду"

- git log # Просмотр истории коммитов

- git remote add origin git@github.com:dssdq/python_spring_work_2022.git # Связываение локального репозитория с GitHub

- git remote get-url origin # Проверка свызывания 

- git remote remove origin  # Удаление свызывания  

- git push origin master # Отправка изменений в удаленный репозиторий origin ветки master

- git push # Отправка изменений c текущей ветки


- git pull # Получение изменений из удалённого репозитория

- git clone url