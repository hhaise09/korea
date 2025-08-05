# Деплой на Render.com

## Шаги для деплоя:

### 1. Подготовка GitHub репозитория
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/hhaise09/korea.git
git push -u origin main
```

### 2. Настройка Render.com

1. Зайдите на [render.com](https://render.com)
2. Создайте новый Web Service
3. Подключите GitHub репозиторий
4. Настройте следующие параметры:

**Build Command:**
```bash
./build.sh
```

**Start Command:**
```bash
gunicorn korean_cars_shop.wsgi:app
```

**Environment Variables:**
- `DEBUG`: `False`
- `SECRET_KEY`: `your-secret-key-here`
- `DATABASE_URL`: `postgresql://...` (Render автоматически создаст)
- `ALLOWED_HOSTS`: `your-app-name.onrender.com`

### 3. Настройка базы данных

После первого деплоя:
1. Зайдите в админку: `https://your-app-name.onrender.com/admin/`
2. Создайте суперпользователя через Django shell:
```bash
python manage.py createsuperuser
```

### 4. Проверка работы

- Главная страница: `https://your-app-name.onrender.com/`
- Каталог: `https://your-app-name.onrender.com/shop/`
- Админка: `https://your-app-name.onrender.com/admin/`

## Структура проекта

```
korean_cars_shop/
├── korean_cars_shop/     # Настройки проекта
├── landing/              # Приложение лендинга
├── shop/                 # Приложение магазина
├── templates/            # HTML шаблоны
├── static/               # Статические файлы
├── media/                # Загруженные файлы
├── build.sh              # Скрипт сборки
├── gunicorn.conf.py      # Конфигурация Gunicorn
├── requirements.txt       # Зависимости
└── README.md            # Документация
```

## Особенности деплоя

- Используется PostgreSQL в продакшене
- Статические файлы обрабатываются WhiteNoise
- Gunicorn для запуска сервера
- Автоматическая миграция базы данных
- Сборка статических файлов при деплое 