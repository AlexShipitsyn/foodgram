```markdown
# 🍴 Foodgram — Продуктовый помощник

[![CI/CD](https://github.com/AlexShipitsyn/foodgram/actions/workflows/main.yml/badge.svg)](https://github.com/AlexShipitsyn/foodgram/actions)
![Python](https://img.shields.io/badge/Python-3.9-3670A0?logo=python)
![Django](https://img.shields.io/badge/Django-4.2-092E20?logo=django)
![Postgres](https://img.shields.io/badge/Postgres-13-316192?logo=postgresql)

Онлайн-платформа для создания рецептов, управления списком покупок и подписки на авторов.

**[Демо](https://foodgram27dfo.zapto.org/) | [Документация](https://foodgram27dfo.zapto.org/api/docs/)**

## 📦 Возможности
- 🔐 Авторизация по JWT-токену
- 📝 Создание/редактирование рецептов
- 📥 Скачивание списка покупок (PDF/TXT)
- ⭐ Добавление в избранное
- 🔔 Умные подписки на авторов

## 🔧 Технологии
- **Backend**: Django REST Framework
- **База данных**: PostgreSQL
- **Авторизация**: JWT-токены
- **Инфраструктура**: Docker + Nginx
- **CI/CD**: GitHub Actions

## 🚀 Установка локально

### 1. Клонирование репозитория
```bash
git clone https://github.com/AlexShipitsyn/foodgram.git
cd foodgram
```

### 2. Настройка окружения
Создайте файл `.env` в корневой директории, используя шаблон из `.env.example`:
```bash
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

### 3. Сборка Docker-образов
Замените `username` на ваш DockerHub-логин:
```bash
# Сборка фронтенда
cd frontend && docker build -t username/foodgram_frontend .
# Сборка бэкенда
cd ../backend && docker build -t username/foodgram_backend .
# Сборка Nginx
cd ../infra && docker build -t username/foodgram_gateway .
```

### 4. Загрузка образов в DockerHub
```bash
docker push username/foodgram_frontend
docker push username/foodgram_backend
docker push username/foodgram_gateway
```

### 5. Запуск проекта
```bash
docker-compose up --build
```

### 6. Миграции и статика
После запуска выполните:
```bash
docker compose exec backend python manage.py makemigrations
docker compose exec backend python manage.py migrate
```
Проект стал доступен по адресу http://localhost:8000/
Документация по адресу http://localhost:8000/api/docs/

## 🚀 Развёртывание на сервере

### ⚙️ Настройка CI/CD
1. Добавьте секреты в GitHub Actions:
   ```bash
   DOCKER_USERNAME                # имя пользователя в DockerHub
   DOCKER_PASSWORD                # пароль пользователя в DockerHub
   HOST                           # ip_address сервера
   USER                           # имя пользователя
   SSH_KEY                        # приватный ssh-ключ (cat ~/.ssh/id_rsa)
   SSH_PASSPHRASE                 # кодовая фраза (пароль) для ssh-ключа

   TELEGRAM_TO                    # id телеграм-аккаунта (можно узнать у @userinfobot, команда /start)
   TELEGRAM_TOKEN                 # токен бота (получить токен можно у @BotFather, /token, имя бота)
   ```

2. Workflow-файл доступен в:
   ```bash
   .github/workflows/main.yml
   ```

1. Подключитесь к серверу через SSH:
```bash
ssh user@server_ip
```

2. Создайте рабочую директорию и перейдите в неё:
```bash
mkdir foodgram && cd foodgram
```

3. Скопируйте файлы на сервер:
```bash
# Для копирования через SCP (выполнять на локальной машине)
scp .env user@server_ip:/home/user/foodgram/
scp docker-compose.production.yml user@server_ip:/home/user/foodgram/
```

4. Запустите контейнеры в фоновом режиме:
```bash
sudo docker compose -f docker-compose.production.yml up -d --build
```

5. Проверьте статус контейнеров:
```bash
sudo docker compose -f docker-compose.production.yml ps
```

> **Примечание:**  
> - Убедитесь, что порты 80 и 443 открыты в фаерволе  
> - Для HTTPS настройте SSL-сертификаты в Nginx

---

## 📥 Импорт данных
Для заполнения базы ингредиентами:
1. Зайдите в админ-зону `/admin`
2. Откройте раздел **Ингредиенты**
3. Нажмите **Импорт CSV**
4. Загрузите файл в формате:
   ```csv
   name,measurement_unit
   Капуста,кг
   Молоко,л
   ```
5. Подтвердите импорт

---


---

## 📚 Примеры API

### Примеры использования API Foodgram

#### 1. Аутентификация
**Получение токена:**
```http
POST /api/auth/token/login/
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "your_password"
}
```
**Ответ:**
```json
{
  "auth_token": "your_auth_token_here"
}
```

**Удаление токена:**
```http
POST /api/auth/token/logout/
Authorization: Token your_auth_token_here
```

---

#### 2. Пользователи
**Регистрация:**
```http
POST /api/users/
Content-Type: application/json

{
  "email": "newuser@example.com",
  "username": "new_user",
  "first_name": "Иван",
  "last_name": "Петров",
  "password": "secure_password123"
}
```
**Ответ (201 Created):**
```json
{
  "email": "newuser@example.com",
  "id": 1,
  "username": "new_user",
  "first_name": "Иван",
  "last_name": "Петров"
}
```

**Получение текущего пользователя:**
```http
GET /api/users/me/
Authorization: Token your_auth_token_here
```
**Ответ:**
```json
{
  "email": "user@example.com",
  "id": 1,
  "username": "test_user",
  "first_name": "Алексей",
  "last_name": "Смирнов",
  "is_subscribed": false,
  "avatar": "http://foodgram.example.org/media/users/avatar.png"
}
```

---

#### 3. Рецепты
**Получение списка рецептов с фильтрами:**
```http
GET /api/recipes/?tags=breakfast&author=1&is_in_shopping_cart=1
```
**Ответ:**
```json
{
  "count": 5,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "tags": [{"id": 1, "name": "Завтрак", "slug": "breakfast"}],
      "author": {"id": 1, "username": "test_user"},
      "ingredients": [{"id": 1, "name": "Яйцо", "measurement_unit": "шт", "amount": 2}],
      "is_favorited": true,
      "is_in_shopping_cart": true,
      "name": "Омлет",
      "image": "http://foodgram.example.org/media/recipes/omelette.jpg",
      "text": "Простой рецепт омлета.",
      "cooking_time": 10
    }
  ]
}
```

**Создание рецепта:**
```http
POST /api/recipes/
Authorization: Token your_auth_token_here
Content-Type: application/json

{
  "ingredients": [{"id": 1, "amount": 2}],
  "tags": [1],
  "image": "data:image/png;base64,...",
  "name": "Салат Цезарь",
  "text": "Классический рецепт.",
  "cooking_time": 20
}
```
**Ответ (201 Created):**
```json
{
  "id": 2,
  "name": "Салат Цезарь",
  "image": "http://foodgram.example.org/media/recipes/caesar.jpg",
  "cooking_time": 20
}
```

---

#### 4. Подписки
**Подписаться на пользователя:**
```http
POST /api/users/3/subscribe/
Authorization: Token your_auth_token_here
```
**Ответ (201 Created):**
```json
{
  "email": "author@example.com",
  "id": 3,
  "username": "chef",
  "recipes": [
    {"id": 5, "name": "Паста", "image": "...", "cooking_time": 15}
  ],
  "recipes_count": 10,
  "is_subscribed": true
}
```

**Список подписок:**
```http
GET /api/users/subscriptions/?recipes_limit=2
Authorization: Token your_auth_token_here
```
**Ответ:**
```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 3,
      "username": "chef",
      "recipes": [
        {"id": 5, "name": "Паста", "image": "...", "cooking_time": 15},
        {"id": 6, "name": "Пицца", "image": "...", "cooking_time": 25}
      ],
      "recipes_count": 10
    }
  ]
}
```

---

#### 5. Список покупок
**Добавить рецепт в список покупок:**
```http
POST /api/recipes/5/shopping_cart/
Authorization: Token your_auth_token_here
```
**Ответ (201 Created):**
```json
{
  "id": 5,
  "name": "Паста",
  "image": "http://foodgram.example.org/media/recipes/pasta.jpg",
  "cooking_time": 15
}
```

**Скачать список покупок:**
```http
GET /api/recipes/download_shopping_cart/
Authorization: Token your_auth_token_here
Accept: text/plain
```
**Ответ (файл в формате TXT):**
```
Ингредиенты:
- Мука: 500 г
- Сахар: 200 г
```

---

#### 6. Ингредиенты
**Поиск ингредиентов:**
```http
GET /api/ingredients/?name=яйцо
```
**Ответ:**
```json
[
  {
    "id": 1,
    "name": "Яйцо куриное",
    "measurement_unit": "шт"
  }
]
```

---

#### 7. Ошибки
**Пример ошибки валидации (400 Bad Request):**
```json
{
  "ingredients": [
    {},
    {"amount": ["Убедитесь, что это значение больше либо равно 1."]},
    {}
  ]
}
```

**Ошибка доступа (403 Forbidden):**
```json
{
  "detail": "У вас недостаточно прав для выполнения данного действия."
}
``` 

---

Полную документацию API можно найти в [Документации](https://foodgram27dfo.zapto.org/api/docs/).

---



## 🧑💻 Автор
Александр Шипицын  
[GitHub](https://github.com/AlexShipitsyn) | [Яндекс.Практикум](https://praktikum.yandex.ru)

*Проект разработан в рамках курса "Python-разработчик"*
