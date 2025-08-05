#!/usr/bin/env python
"""
Скрипт для добавления демо-данных автомобилей
"""

import os
import django

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'korean_cars_shop.settings')
django.setup()

from shop.models import Car

def add_demo_cars():
    """Добавляет демо-автомобили с изображениями"""
    
    # Очищаем существующие автомобили
    Car.objects.all().delete()
    print("🗑️ Очищены существующие автомобили")
    
    # Создаем демо-автомобили
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
        },
    ]
    
    # Создаем автомобили
    for i, data in enumerate(cars_data):
        car = Car.objects.create(**data)
        print(f"✅ Добавлен: {car.brand} {car.model} ({car.year}) - {car.price:,} ₽")
    
    # Проверяем количество автомобилей
    total_cars = Car.objects.count()
    print(f"\n🎉 Всего автомобилей в базе: {total_cars}")
    
    # Показываем все автомобили
    print("\n📋 Список всех автомобилей:")
    for car in Car.objects.all():
        print(f"  - {car.brand} {car.model} ({car.year}) - {car.price:,} ₽")

if __name__ == '__main__':
    add_demo_cars() 