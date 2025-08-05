#!/bin/bash

# Инициализация Git репозитория
echo "Инициализация Git репозитория..."

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
echo "Отправка в GitHub..."
git push -u origin main

echo "✅ Проект успешно отправлен в GitHub!"
echo "🌐 Репозиторий: https://github.com/hhaise09/korea"
echo ""
echo "📋 Следующие шаги для деплоя на Render.com:"
echo "1. Зайдите на https://render.com"
echo "2. Создайте новый Web Service"
echo "3. Подключите GitHub репозиторий"
echo "4. Настройте переменные окружения"
echo "5. Деплой!" 