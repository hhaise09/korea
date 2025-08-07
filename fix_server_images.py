#!/usr/bin/env python
"""
Скрипт для ручного исправления изображений на сервере Render
Используется если автоматический импорт не сработал
"""
import os
import sys
import django
import shutil
from pathlib import Path

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'korean_cars_shop.settings')
django.setup()

from shop.models import Car, CarImage


def fix_server_images():
    """Исправляет изображения на сервере"""
    print("🔧 Исправление изображений на сервере...")
    
    # Создаем папки
    media_dir = Path('media')
    media_dir.mkdir(exist_ok=True)
    media_cars_dir = media_dir / 'cars'
    media_cars_dir.mkdir(exist_ok=True)
    
    print(f"✅ Папки созданы: {media_cars_dir}")
    
    # Очищаем старые данные
    print("🗑️ Очистка старых данных...")
    Car.objects.all().delete()
    CarImage.objects.all().delete()
    
    # Проверяем наличие экспортированных данных
    export_dir = Path('export_data')
    if not export_dir.exists():
        print("❌ Папка export_data не найдена!")
        return
    
    cars_data_file = export_dir / 'cars_data.json'
    if not cars_data_file.exists():
        print("❌ Файл cars_data.json не найден!")
        return
    
    images_dir = export_dir / 'images'
    if not images_dir.exists():
        print("❌ Папка images не найдена!")
        return
    
    # Импортируем данные
    import json
    with open(cars_data_file, 'r', encoding='utf-8') as f:
        cars_data = json.load(f)
    
    print(f"📦 Найдено {len(cars_data)} автомобилей для импорта")
    
    for car_data in cars_data:
        print(f"\n🚗 Импорт: {car_data['brand']} {car_data['model']}")
        
        # Создаем автомобиль
        car = Car.objects.create(
            brand=car_data['brand'],
            model=car_data['model'],
            year=car_data['year'],
            mileage=car_data['mileage'],
            transmission=car_data['transmission'],
            fuel_type=car_data['fuel_type'],
            price=car_data['price'],
            is_available=car_data['is_available']
        )
        
        # Импортируем главное изображение
        if 'main_image' in car_data:
            image_path = images_dir / car_data['main_image']
            if image_path.exists():
                django_path = f"cars/{car_data['main_image']}"
                car.image = django_path
                car.save()
                
                # Копируем файл
                media_image_path = media_cars_dir / car_data['main_image']
                shutil.copy2(image_path, media_image_path)
                print(f"  ✅ Главное изображение: {car_data['main_image']}")
            else:
                print(f"  ❌ Файл не найден: {car_data['main_image']}")
        
        # Импортируем дополнительные изображения
        for img_data in car_data['images']:
            image_path = images_dir / img_data['filename']
            if image_path.exists():
                django_path = f"cars/{img_data['filename']}"
                car_image = CarImage.objects.create(
                    car=car,
                    is_main=img_data['is_main']
                )
                car_image.image = django_path
                car_image.save()
                
                # Копируем файл
                media_image_path = media_cars_dir / img_data['filename']
                shutil.copy2(image_path, media_image_path)
                print(f"  ✅ Дополнительное изображение: {img_data['filename']}")
            else:
                print(f"  ❌ Файл не найден: {img_data['filename']}")
    
    print(f"\n🎉 Импорт завершен!")
    print(f"📊 Статистика:")
    print(f"  - Автомобилей: {Car.objects.count()}")
    print(f"  - Изображений: {CarImage.objects.count()}")
    print(f"  - Файлов в media/cars: {len(list(media_cars_dir.glob('*')))}")


if __name__ == '__main__':
    fix_server_images() 