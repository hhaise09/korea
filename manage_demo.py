#!/usr/bin/env python
"""
Простой скрипт для добавления демо-данных
"""

import os
import django

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'korean_cars_shop.settings')
django.setup()

from shop.models import Car

def add_demo_cars():
    """Добавляет демо-автомобили"""
    
    # Очищаем существующие автомобили
    Car.objects.all().delete()
    
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
    ]
    
    for data in cars_data:
        Car.objects.create(**data)
        print(f"✅ Добавлен: {data['brand']} {data['model']}")
    
    print(f"🎉 Добавлено {len(cars_data)} автомобилей!")

if __name__ == '__main__':
    add_demo_cars() 