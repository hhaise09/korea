# Локальная разработка Korean Cars Shop

## Быстрый запуск

### Вариант 1: Через bat-файл (Windows)
Просто дважды кликните на файл `run_local.bat` в папке проекта.

### Вариант 2: Через командную строку
```bash
# Перейдите в папку проекта
cd korea

# Установите зависимости (если еще не установлены)
pip install -r requirements.txt

# Примените миграции (если нужно)
python manage.py migrate

# Запустите сервер разработки
python manage.py runserver
```

## Настройки окружения

Проект автоматически определяет окружение:
- **Локальная разработка**: `ENVIRONMENT=development` (по умолчанию)
- **Продакшен**: `ENVIRONMENT=production` (для Render.com)

### Переменные окружения для локальной разработки:
- `ENVIRONMENT=development` - режим разработки
- `DEBUG=True` - включен режим отладки
- `SECRET_KEY` - ключ Django (используется значение по умолчанию)

## Особенности локального запуска

1. **WSGI отключен** - для локальной разработки используется встроенный сервер Django
2. **Debug режим включен** - показываются подробные ошибки
3. **Статические файлы** - обрабатываются через Django dev server
4. **База данных** - SQLite для локальной разработки

## Доступ к сайту

После запуска сервера сайт будет доступен по адресу:
- http://127.0.0.1:8000/
- http://localhost:8000/

## Полезные команды

```bash
# Создать суперпользователя
python manage.py createsuperuser

# Создать миграции
python manage.py makemigrations

# Применить миграции
python manage.py migrate

# Собрать статические файлы
python manage.py collectstatic

# Проверить настройки
python manage.py check
```

## Структура проекта

```
korea/
├── korean_cars_shop/     # Основные настройки Django
├── landing/              # Приложение лендинга
├── shop/                 # Приложение магазина
├── templates/            # HTML шаблоны
├── static/               # Статические файлы (CSS, JS, изображения)
├── media/                # Загруженные файлы
├── manage.py             # Управление Django
├── run_local.bat         # Скрипт запуска для Windows
└── requirements.txt      # Зависимости Python
``` 