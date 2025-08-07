#!/usr/bin/env python
"""
Скрипт для экспорта данных с изображениями
Используется для сохранения данных при деплое на Render
"""
import os
import sys
import django
import json
import shutil
from pathlib import Path
from datetime import datetime

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'korean_cars_shop.settings')
django.setup()

from shop.models import Car, CarImage, Category, Order
from django.core.files import File


def export_cars_data():
    """Экспорт данных автомобилей с изображениями"""
    export_dir = Path('export_data')
    export_dir.mkdir(exist_ok=True)
    
    # Создаем папки для изображений
    images_dir = export_dir / 'images'
    images_dir.mkdir(exist_ok=True)
    
    cars_data = []
    
    for car in Car.objects.all():
        car_data = {
            'brand': car.brand,
            'model': car.model,
            'year': car.year,
            'mileage': car.mileage,
            'transmission': car.transmission,
            'fuel_type': car.fuel_type,
            'price': str(car.price),
            'is_available': car.is_available,
            'created_at': car.created_at.isoformat(),
            'images': []
        }
        
        # Экспортируем изображения
        if car.image:
            # Получаем оригинальное имя файла
            original_filename = os.path.basename(car.image.name)
            # Создаем новое имя для экспорта
            image_filename = f"car_{car.id}_main{os.path.splitext(original_filename)[1]}"
            image_path = images_dir / image_filename
            
            # Копируем файл
            if car.image.path and os.path.exists(car.image.path):
                shutil.copy2(car.image.path, image_path)
                car_data['main_image'] = image_filename
                print(f"Экспортировано главное изображение: {image_filename}")
        
        # Экспортируем дополнительные изображения
        for car_image in car.images.all():
            if car_image.image:
                original_filename = os.path.basename(car_image.image.name)
                image_filename = f"car_{car.id}_image_{car_image.id}{os.path.splitext(original_filename)[1]}"
                image_path = images_dir / image_filename
                
                if car_image.image.path and os.path.exists(car_image.image.path):
                    shutil.copy2(car_image.image.path, image_path)
                    car_data['images'].append({
                        'filename': image_filename,
                        'is_main': car_image.is_main
                    })
                    print(f"Экспортировано дополнительное изображение: {image_filename}")
        
        cars_data.append(car_data)
    
    # Сохраняем данные в JSON
    with open(export_dir / 'cars_data.json', 'w', encoding='utf-8') as f:
        json.dump(cars_data, f, ensure_ascii=False, indent=2)
    
    print(f"Экспортировано {len(cars_data)} автомобилей")
    print(f"Данные сохранены в {export_dir}")


def import_cars_data():
    """Импорт данных автомобилей с изображениями"""
    export_dir = Path('export_data')
    cars_data_file = export_dir / 'cars_data.json'
    images_dir = export_dir / 'images'
    
    if not cars_data_file.exists():
        print("Файл с данными не найден!")
        return
    
    with open(cars_data_file, 'r', encoding='utf-8') as f:
        cars_data = json.load(f)
    
    for car_data in cars_data:
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
                # Создаем правильный путь для Django
                django_path = f"cars/{car_data['main_image']}"
                car.image = django_path
                car.save()
                
                # Создаем все необходимые папки
                media_dir = Path('media')
                media_dir.mkdir(exist_ok=True)
                media_cars_dir = media_dir / 'cars'
                media_cars_dir.mkdir(exist_ok=True)
                
                # Копируем файл в media папку
                media_image_path = media_cars_dir / car_data['main_image']
                shutil.copy2(image_path, media_image_path)
                print(f"Импортировано главное изображение: {car_data['main_image']}")
        
        # Импортируем дополнительные изображения
        for img_data in car_data['images']:
            image_path = images_dir / img_data['filename']
            if image_path.exists():
                # Создаем правильный путь для Django
                django_path = f"cars/{img_data['filename']}"
                car_image = CarImage.objects.create(
                    car=car,
                    is_main=img_data['is_main']
                )
                car_image.image = django_path
                car_image.save()
                
                # Создаем все необходимые папки
                media_dir = Path('media')
                media_dir.mkdir(exist_ok=True)
                media_cars_dir = media_dir / 'cars'
                media_cars_dir.mkdir(exist_ok=True)
                
                # Копируем файл в media папку
                media_image_path = media_cars_dir / img_data['filename']
                shutil.copy2(image_path, media_image_path)
                print(f"Импортировано дополнительное изображение: {img_data['filename']}")
    
    print(f"Импортировано {len(cars_data)} автомобилей")


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'import':
        import_cars_data()
    else:
        export_cars_data() 