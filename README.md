# Yatube_API
## Описание
API приложения Yatube. 

Через API доступно создание постов, комментариев к ним, а также возможность подписки на других пользователей.
### Доступ к API
Через JWT (JSON Web Token). 
### Ограничения
* GET запросы доступны всем пользователям
* POST запросы только авторизованным
* UPDATE / DELETE только пользователям являющимися автором/создателем.
### Цель создания
Создан в учебных целях, в рамках обучения на Яндекс Практикуме.
____
## Установка

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Comsomolec/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
____
## Документация на API:

Изучить документацию на API в удобном формате через Redoc:
```
http://127.0.0.1:8000/redoc/
```
Внутри проекта схема лежит по адресу:
```
api_final_yatube/yatube_api/static/redoc.yaml
```