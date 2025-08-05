#!/usr/bin/env python
"""
Скрипт для добавления демо-данных автомобилей
"""

import os
import sys
import django

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'korean_cars_shop.settings')
django.setup()

from shop.models import Car

def add_demo_cars():
    """Добавляет демо-автомобили в базу данных"""
    
    # Очищаем существующие автомобили
    Car.objects.all().delete()
    
    # Список демо-автомобилей
    demo_cars = [
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
    for car_data in demo_cars:
        car = Car.objects.create(**car_data)
        print(f"✅ Добавлен: {car.brand} {car.model} ({car.year}) - {car.price:,} ₽")
    
    print(f"\n🎉 Добавлено {len(demo_cars)} демо-автомобилей!")

if __name__ == '__main__':
    add_demo_cars() 