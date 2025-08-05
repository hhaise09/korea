# 🚀 Быстрый старт

## Локальный запуск

1. **Клонируйте репозиторий**
   ```bash
   git clone https://github.com/hhaise09/korea.git
   cd korea
   ```

2. **Создайте виртуальное окружение**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # Linux/Mac
   ```

3. **Установите зависимости**
   ```bash
   pip install -r requirements.txt
   ```

4. **Примените миграции**
   ```bash
   python manage.py migrate
   ```

5. **Создайте суперпользователя**
   ```bash
   python manage.py createsuperuser
   ```

6. **Запустите сервер**
   ```bash
   python manage.py runserver
   ```

7. **Откройте браузер**
   - http://127.0.0.1:8000/ - Главная страница
   - http://127.0.0.1:8000/admin/ - Админка

## Деплой на Render.com

1. **Отправьте код в GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Настройте Render.com**
   - Зайдите на https://render.com
   - Создайте новый Web Service
   - Подключите GitHub репозиторий
   - Настройте переменные окружения

3. **Переменные окружения на Render:**
   ```
   DEBUG=False
   SECRET_KEY=your-secret-key-here
   DATABASE_URL=postgresql://... (автоматически)
   ALLOWED_HOSTS=your-app-name.onrender.com
   ```

4. **Build Command:**
   ```bash
   ./build.sh
   ```

5. **Start Command:**
   ```bash
   gunicorn korean_cars_shop.wsgi:app
   ```

## Добавление автомобилей

1. Зайдите в админку: `/admin/`
2. Войдите с созданными учетными данными
3. В разделе "Автомобили" нажмите "Добавить автомобиль"
4. Заполните поля:
   - Марка (например: Hyundai)
   - Модель (например: Sonata)
   - Год выпуска
   - Пробег (км)
   - Трансмиссия
   - Тип топлива
   - Цена
   - Загрузите изображение
5. Сохраните

## Структура проекта

```
korea/
├── korean_cars_shop/     # Настройки Django
├── landing/              # Лендинг
├── shop/                 # Магазин
├── templates/            # HTML шаблоны
├── static/               # CSS, JS, изображения
├── media/                # Загруженные файлы
├── build.sh              # Скрипт сборки
├── requirements.txt      # Зависимости
└── README.md            # Документация
```

## Основные URL

- `/` - Главная страница (лендинг)
- `/shop/` - Каталог автомобилей
- `/shop/car/<id>/` - Детальная страница автомобиля
- `/admin/` - Админка
- `/shop/my-orders/` - Мои заказы (требует авторизации)

## Полезные команды

```bash
# Создание миграций
python manage.py makemigrations

# Применение миграций
python manage.py migrate

# Создание суперпользователя
python manage.py createsuperuser

# Сборка статических файлов
python manage.py collectstatic

# Запуск сервера разработки
python manage.py runserver

# Проверка кода
python manage.py check
```

## Поддержка

Если возникли проблемы:
1. Проверьте, что все зависимости установлены
2. Убедитесь, что миграции применены
3. Проверьте логи сервера
4. Создайте Issue в репозитории 