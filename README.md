# Проект Foodgram «Продуктовый помощник»
![push](https://github.com/Cocok-ylitki/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg?event=push)
## Описание:

### Проект Foodgram представляет собой одностраничное приложение на фреймворке React и API для него на Django REST Framework. На этом сервисе пользователи могут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

![image](https://user-images.githubusercontent.com/86740068/164313048-7d86dc4c-b6b0-4fb7-8384-da955d327040.png)

## Проект доступен по ссылке:
### http://51.250.97.31/

## Наполнение env-файла:
```py
- DB_ENGINE=django.db.backends.postgresql - используемая БД
- DB_NAME=postgres - имя БД
- POSTGRES_USER - логин для подключения к БД
- POSTGRES_PASSWORD - пароль для подключения к БД
- DB_HOST - название сервиса (контейнера)
- DB_PORT - порт для подключения к БД
```

## Как запустить проект в контейнерах:

Клонировать репозиторий и перейти в директорию с файлом docker-compose.yaml:

```
https://github.com/Cocok-ylitki/foodgram-project-react.git
```

```
cd foodgram-project-react/infra/
```

Собрать проект в контейнеры и запустить:

```
docker-compose up -d --build
```

Выполнить миграции:

```
docker-compose exec backend python manage.py migrate
```

Собрать статические файлы:

```
docker-compose exec backend python manage.py collectstatic --no-input
```

Создать суперпользователя:

```
docker-compose exec backend python manage.py createsuperuser
```
Потребуется ввести почту, имя пользователя и пароль.


## Наполнение базы данных
- Для переноса данных с файла ingredients.json на PostgreSQL выполним несколько команд:
    ```
    docker-compose exec backend python manage.py shell 
    ```
    ```
    exec(open("backend/data/filldb.py").read())
    ``` 


## Автор

### Разработчик бэкенда - Зиев Марат


## Технологии

![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![PostgresSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=whit)
