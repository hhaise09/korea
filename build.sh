#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py migrate

# Импорт данных если есть экспорт
if [ -f "export_data/cars_data.json" ]; then
    echo "Импорт данных с изображениями..."
    python export_data.py import
else
    echo "Файл экспорта не найден, создание демо данных..."
    # Создание изображений
    python create_images.py
    # Добавление автомобилей с изображениями
    python add_cars_with_images.py
fi

python manage.py collectstatic --no-input 