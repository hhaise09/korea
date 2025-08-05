#!/usr/bin/env python
"""
Скрипт для добавления автомобилей с изображениями из media/cars
"""

import os
import django

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'korean_cars_shop.settings')
django.setup()

from shop.models import Car

def add_cars_with_images():
    """Добавляет автомобили с изображениями из media/cars"""
    
    # Очищаем существующие автомобили
    Car.objects.all().delete()
    print("🗑️ Очищены существующие автомобили")
    
    # Список автомобилей с данными
    cars_data = [
        {
            'brand': 'Hyundai',
            'model': 'Sonata',
            'year': 2022,
            'mileage': 15000,
            'transmission': 'automatic',
            'fuel_type': 'gasoline',
            'price': 2500000,
            'is_available': True,
            'image': 'cars/1.webp'
        },
        {
            'brand': 'Kia',
            'model': 'Rio',
            'year': 2021,
            'mileage': 25000,
            'transmission': 'manual',
            'fuel_type': 'gasoline',
            'price': 1800000,
            'is_available': True,
            'image': 'cars/2.webp'
        },
        {
            'brand': 'Genesis',
            'model': 'G80',
            'year': 2023,
            'mileage': 5000,
            'transmission': 'automatic',
            'fuel_type': 'gasoline',
            'price': 4500000,
            'is_available': True,
            'image': 'cars/3.webp'
        },
        {
            'brand': 'Hyundai',
            'model': 'Tucson',
            'year': 2022,
            'mileage': 20000,
            'transmission': 'automatic',
            'fuel_type': 'hybrid',
            'price': 3200000,
            'is_available': True,
            'image': 'cars/4.webp'
        },
        {
            'brand': 'Kia',
            'model': 'Sportage',
            'year': 2021,
            'mileage': 30000,
            'transmission': 'automatic',
            'fuel_type': 'diesel',
            'price': 2800000,
            'is_available': True,
            'image': 'cars/5.webp'
        },
        {
            'brand': 'Genesis',
            'model': 'GV70',
            'year': 2023,
            'mileage': 8000,
            'transmission': 'automatic',
            'fuel_type': 'gasoline',
            'price': 5200000,
            'is_available': True,
            'image': 'cars/6.webp'
        },
        {
            'brand': 'Hyundai',
            'model': 'Santa Fe',
            'year': 2022,
            'mileage': 18000,
            'transmission': 'automatic',
            'fuel_type': 'hybrid',
            'price': 3800000,
            'is_available': True,
            'image': 'cars/7.webp'
        },
        {
            'brand': 'Kia',
            'model': 'K5',
            'year': 2021,
            'mileage': 22000,
            'transmission': 'automatic',
            'fuel_type': 'gasoline',
            'price': 2200000,
            'is_available': True,
            'image': 'cars/8.webp'
        },
        {
            'brand': 'Genesis',
            'model': 'G90',
            'year': 2023,
            'mileage': 3000,
            'transmission': 'automatic',
            'fuel_type': 'gasoline',
            'price': 6500000,
            'is_available': True,
            'image': 'cars/9.webp'
        },
        {
            'brand': 'Hyundai',
            'model': 'Elantra',
            'year': 2022,
            'mileage': 12000,
            'transmission': 'manual',
            'fuel_type': 'gasoline',
            'price': 1900000,
            'is_available': True,
            'image': 'cars/10.webp'
        },
        {
            'brand': 'Kia',
            'model': 'Sorento',
            'year': 2021,
            'mileage': 28000,
            'transmission': 'automatic',
            'fuel_type': 'diesel',
            'price': 3500000,
            'is_available': True,
            'image': 'cars/11.webp'
        },
        {
            'brand': 'Genesis',
            'model': 'GV80',
            'year': 2023,
            'mileage': 6000,
            'transmission': 'automatic',
            'fuel_type': 'gasoline',
            'price': 5800000,
            'is_available': True,
            'image': 'cars/12.webp'
        },
    ]
    
    # Создаем автомобили с изображениями
    for i, data in enumerate(cars_data):
        # Проверяем существование файла изображения
        image_path = os.path.join('media', data['image'])
        if os.path.exists(image_path):
            car = Car.objects.create(**data)
            print(f"✅ Добавлен: {car.brand} {car.model} ({car.year}) - {car.price:,} ₽ - {data['image']}")
        else:
            # Создаем без изображения, если файл не найден
            image_path = data.pop('image')
            car = Car.objects.create(**data)
            print(f"⚠️ Добавлен без изображения: {car.brand} {car.model} ({car.year}) - {car.price:,} ₽ (файл {image_path} не найден)")
    
    # Проверяем количество автомобилей
    total_cars = Car.objects.count()
    print(f"\n🎉 Всего автомобилей в базе: {total_cars}")
    
    # Показываем все автомобили
    print("\n📋 Список всех автомобилей:")
    for car in Car.objects.all():
        image_status = "✅" if car.image else "❌"
        print(f"  {image_status} {car.brand} {car.model} ({car.year}) - {car.price:,} ₽")

if __name__ == '__main__':
    add_cars_with_images() 