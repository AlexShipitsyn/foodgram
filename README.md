[![.github/workflows/main.yml](https://github.com/AlexShipitsyn/foodgram/actions/workflows/main.yml/badge.svg)](https://github.com/AlexShipitsyn/foodgram/actions/workflows/main.yml)

![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white) ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)



### Проект Foodgram

**Foodgram** - продуктовый помощник.

Цель этого сайта — дать возможность пользователям создавать и хранить рецепты на онлайн-платформе. Кроме того, можно скачать список продуктов, необходимых для приготовления блюда, просмотреть рецепты друзей и добавить любимые рецепты в список избранных.

### Технологии, которые применены в этом проекте:

Postgres
Nginx
Python
Django
Django REST Framework
Djoser

### Запуск локально:

- Склонируйте проект из репозитория:

```sh
$ git clone https://github.com/shulikin/foodgram.git
```

- В корне проекта создайте файл .env и заполните своими данными:
```
DEBUG=true  # вкл или выкл дебаг режима


USE_POSTGRES=true #выбор базы
POSTGRES_DB=foodgram
POSTGRES_USER=foodgram_user
POSTGRES_PASSWORD=foodgram_password
DB_NAME=foodgramdb
DB_HOST=db
DB_PORT=5432


SECRET_KEY=<...> # секретный ключ
ALLOWED_HOSTS='localhost,127.0.0.1,'
```

- Создайте и запустите контейнеры Docker:
```
docker compose up
```

- Создайте суперпользователя:
```
docker-compose exec backend python manage.py createsuperuser
```

После запуска проект будут доступен по адресу: [http://localhost/](http://localhost/)

Документация будет доступна по адресу: [http://localhost/api/docs/](http://localhost/api/docs/)

### Добавленение данных:

- Войдите в админ-панель по ссылке:
```
http://localhost:8000/admin/
```
- Добавьте теги для для рецептов.
- В таблице "Ингредиенты" кнопкой "Импорт" импортируйте список ингредиентов из папки "data" (ingredients.csv)
- Эти поля является обязательным для сохранения рецепта и добавляются только администратором.
***

# Ресурсы API Foodgram

**AUTH**: получение/удаление токена авторизации.

**USERS**: пользователи: регистрация, просмотр/изменение личного профиля, просмотр пользовательских профилей, подписка/отписка на пользователей.

**TAGS**: теги категории рецептов (создаются и редактируюся пользователями с правами администратора). Описывается полями:
```sh
- Название.
- Цветовой HEX-код (например, #49B64E).
- Slug.
```

**RECIPES**: рецепты. У каждого авторизованного пользователя есть возможность добавлять рецепт в "Избранное" и в "Список покупок".
Каждый рецепт содержит следующие поля:
```sh
- Автор публикации (пользователь).
- Название.
- Картинка.
- Текстовое описание.
- Ингредиенты: продукты для приготовления блюда по рецепту. Множественное поле, выбор из предустановленного списка, с указанием количества и единицы измерения.
- Тег (можно установить несколько тегов на один рецепт, выбор из предустановленных).
- Время приготовления в минутах.
```

**INGREDIENTS**: ингредиенты.
Поля:
```sh
- Название.
- Количество.
- Единицы измерения.
```

# Пользовательские роли

**Права анонимного пользователя:**
- Создание аккаунта.
- Просмотр: рецепты на главной, отдельные страницы рецептов, страницы пользователей.
- Фильтрация рецептов по тегам.

**Права авторизованного пользователя (USER):**
- Входить в систему под своим логином и паролем.
- Выходить из системы (разлогиниваться).
- Менять свой пароль.
- Создавать/редактировать/удалять собственные рецепты
- Просматривать рецепты на главной.
- Просматривать страницы пользователей.
- Просматривать отдельные страницы рецептов.
- Фильтровать рецепты по тегам.
- Работать с персональным списком избранного: добавлять в него рецепты или удалять их, просматривать свою страницу избранных рецептов.
- Работать с персональным списком покупок: добавлять/удалять любые рецепты, выгружать файл со количеством необходимых ингридиентов для рецептов из списка покупок.
- Подписываться на публикации авторов рецептов и отменять подписку, просматривать свою страницу подписок.

**Права администратора (ADMIN):**
Все права авторизованного пользователя +
- Изменение пароля любого пользователя,
- Создание/блокирование/удаление аккаунтов пользователей,
- Редактирование/удаление любых рецептов,
- Добавление/удаление/редактирование ингредиентов.
- Добавление/удаление/редактирование тегов.

**Администратор Django** — те же права, что и у роли Администратор.

### Алгоритм регистрации пользователей

Для добавления нового пользователя нужно отправить POST-запрос на эндпоинт:

```
POST /api/users/
```

- В запросе необходимо передать поля:

1. ```email``` - (string) почта пользователя;
2. ```username``` - (string) уникальный юзернейм пользователя;
3. ```first_name``` - (string) имя пользователя;
4. ```last_name``` - (string) фамилия пользователя;
5. ```password``` - (string) пароль пользователя.

Пример запроса:

```sh
{
"email": "vpupkin@yandex.ru",
"username": "vasya.pupkin",
"first_name": "Вася",
"last_name": "Пупкин",
"password": "Qwerty123"
}
```

Далее необходимо получить авторизационный токен, отправив POST-запрос на эндпоинт:

```
POST /api/auth/token/login/
```

- В запросе необходимо передать поля:

1. ```password``` - (string) пароль пользователя;
2. ```email``` - (string) почта пользователя.

Пример запроса:

```sh
{
"password": "Qwerty123",
"email": "vpupkin@yandex.ru"
}
```

Пример ответа:

```sh
{
  "auth_token": "string"
}
```

Поученный токен всегда необходимо передавать в заголовке (```Authorization: Token TOKENVALUE```) для всех запросов, которые требуют авторизации.

### Изменение пароля текущего пользователя:

```
POST /api/users/set_password/
```

Пример запроса:

```sh
{
  "new_password": "string",
  "current_password": "string"
}
```

### Удаление токена пользователя:

```
POST /api/auth/token/logout/
```

### Регистрация пользователей админом

Пользователя может создать администратор через админ-зону сайта. Получение токена осуществляется способом, описанным выше.

### Примеры использования API для неавторизованных пользователей:

Для неавторизованных пользователей работа с API доступна в режиме чтения.

```sh
GET /api/users/- получить список всех пользователей.
GET /api/tags/- получить список всех тегов.
GET /api/tags/{id}/ - получить тег по ID.
GET /api/recipes/- получить список всех рецептов.
GET /api/recipes/{id}/ - получить рецепт по ID.
GET /api/users/subscriptions/ - получить список всех пользователей, на которых подписан текущий пользователь. В выдачу добавляются рецепты.
GET /api/ingredients/ - получить список ингредиентов с возможностью поиска по имени.
GET /api/ingredients/{id}/ - получить ингредиент по ID.
```

#### Пример GET-запроса:
```
GET /api/recipes/
```

#### Пример ответа:
- код ответа сервера: 200 OK
- тело ответа:

```sh
{
  "count": 123,
  "next": "http://foodgram.example.org/api/recipes/?page=4",
  "previous": "http://foodgram.example.org/api/recipes/?page=2",
  "results": [
    {
      "id": 0,
      "tags": [
        {
          "id": 0,
          "name": "Завтрак",
          "color": "#E26C2D",
          "slug": "breakfast"
        }
      ],
      "author": {
        "email": "user@example.com",
        "id": 0,
        "username": "string",
        "first_name": "Вася",
        "last_name": "Пупкин",
        "is_subscribed": false
      },
      "ingredients": [
        {
          "id": 0,
          "name": "Картофель отварной",
          "measurement_unit": "г",
          "amount": 1
        }
      ],
      "is_favorited": true,
      "is_in_shopping_cart": true,
      "name": "string",
      "image": "http://foodgram.example.org/media/recipes/images/image.jpeg",
      "text": "string",
      "cooking_time": 1
    }
  ]
}
```

#### Пример GET-запроса с фильтрацией по наименованию:
```
GET /api/ingredients/?name=абри
```

#### Пример ответа:
- код ответа сервера: 200 OK
- тело ответа:

```sh
[
    {
        "id": 1,
        "name": "абрикосовое варенье",
        "measurement_unit": "г"
    },
    ...
        {
        "id": 6,
        "name": "абрикосы консервированные",
        "measurement_unit": "г"
    }
]
```

#### Пример POST-запроса:
```
POST /api/recipes/
```
Авторизация по токену.
Запрос от имени пользователя должен выполняться с заголовком "Authorization: Token TOKENVALUE"

```sh
{
  "ingredients": [
    {
      "id": 1123,
      "amount": 10
    }
  ],
  "tags": [
    1,
    2
  ],
  "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABAgMAAABieywaAAAACVBMVEUAAAD///9fX1/S0ecCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAACklEQVQImWNoAAAAggCByxOyYQAAAABJRU5ErkJggg==",
  "name": "string",
  "text": "string",
  "cooking_time": 1
}
```

#### Пример ответа:
- код ответа сервера: 201
- тело ответа:

```sh
{
"id": 0,
"tags": [
{}
],
"author": {
"email": "user@example.com",
"id": 0,
"username": "string",
"first_name": "Вася",
"last_name": "Пупкин",
"is_subscribed": false
},
"ingredients": [
{
"id": 0,
"name": "Картофель отварной",
"measurement_unit": "г",
"amount": 1
}
],
"is_favorited": true,
"is_in_shopping_cart": true,
"name": "string",
"image": "http://foodgram.example.org/media/recipes/images/image.jpeg",
"text": "string",
"cooking_time": 1
}
```

Документация будет доступна по адресу: [http://localhost/api/docs/](http://localhost/api/docs/)

***
#### Автор:

[Шипицын Александр](https://github.com/AlexShipitsyn).
Проект создан во время обучения в Яндекс Практикуме.

#### Доступ на сервере:

https://foodgram27dfo.zapto.org/

логин        admin@mail.com

пароль      admin12345