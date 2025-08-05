# 🚀 Настройка GitHub и деплой на Render.com

## Шаг 1: Подготовка проекта

Все файлы готовы! Проект полностью настроен для деплоя.

## Шаг 2: Отправка в GitHub

Выполните следующие команды в терминале:

```bash
# Инициализация Git
git init

# Добавление всех файлов
git add .

# Первый коммит
git commit -m "Initial commit: Korean Cars Shop Django project"

# Переименование ветки в main
git branch -M main

# Добавление удаленного репозитория
git remote add origin https://github.com/hhaise09/korea.git

# Отправка в GitHub
git push -u origin main
```

## Шаг 3: Настройка Render.com

1. **Зайдите на [render.com](https://render.com)**
2. **Создайте аккаунт** (если еще нет)
3. **Создайте новый Web Service**
4. **Подключите GitHub репозиторий:**
   - Выберите репозиторий `hhaise09/korea`
   - Выберите ветку `main`

## Шаг 4: Настройка параметров на Render

### Build Command:
```bash
./build.sh
```

### Start Command:
```bash
gunicorn korean_cars_shop.wsgi:app
```

### Environment Variables:
```
DEBUG=False
SECRET_KEY=your-super-secret-key-here-change-this
ALLOWED_HOSTS=your-app-name.onrender.com
```

## Шаг 5: Деплой

1. Нажмите "Create Web Service"
2. Дождитесь завершения сборки (обычно 2-3 минуты)
3. Получите URL вашего сайта

## Шаг 6: Настройка базы данных

После успешного деплоя:

1. **Создайте суперпользователя:**
   - Зайдите в Render Dashboard
   - Найдите ваш сервис
   - Перейдите в "Shell"
   - Выполните команду:
   ```bash
   python manage.py createsuperuser
   ```

2. **Добавьте автомобили:**
   - Зайдите в админку: `https://your-app-name.onrender.com/admin/`
   - Войдите с созданными учетными данными
   - Добавьте несколько автомобилей

## Структура готового проекта

```
korea/
├── korean_cars_shop/     # Настройки Django
├── landing/              # Приложение лендинга
├── shop/                 # Приложение магазина
├── templates/            # HTML шаблоны
├── static/               # CSS, JS, изображения
│   ├── css/style.css
│   ├── js/main.js
│   └── images/cars/
├── media/                # Загруженные файлы
├── build.sh              # Скрипт сборки для Render
├── gunicorn.conf.py      # Конфигурация Gunicorn
├── requirements.txt      # Зависимости
├── .gitignore           # Исключения Git
├── README.md            # Документация
├── DEPLOY.md            # Инструкции по деплою
├── QUICK_START.md       # Быстрый старт
└── GITHUB_SETUP.md      # Эта инструкция
```

## Проверка работы

После деплоя проверьте:

- ✅ **Главная страница:** `https://your-app-name.onrender.com/`
- ✅ **Каталог:** `https://your-app-name.onrender.com/shop/`
- ✅ **Админка:** `https://your-app-name.onrender.com/admin/`

## Возможные проблемы

### 1. Ошибка сборки
- Проверьте, что все файлы добавлены в Git
- Убедитесь, что `build.sh` имеет права на выполнение

### 2. Ошибка запуска
- Проверьте переменные окружения
- Убедитесь, что `DEBUG=False` в продакшене

### 3. Статические файлы не загружаются
- Проверьте, что WhiteNoise настроен правильно
- Убедитесь, что `collectstatic` выполнен

## Полезные ссылки

- 🌐 **Render.com:** https://render.com
- 📚 **Документация Django:** https://docs.djangoproject.com
- 🎨 **Font Awesome:** https://fontawesome.com
- 📖 **GitHub:** https://github.com/hhaise09/korea

## Поддержка

Если возникли проблемы:
1. Проверьте логи в Render Dashboard
2. Убедитесь, что все переменные окружения настроены
3. Проверьте, что база данных создана
4. Создайте Issue в GitHub репозитории

---

**🎉 Поздравляем! Ваш интернет-магазин автомобилей из Кореи готов к работе!** 