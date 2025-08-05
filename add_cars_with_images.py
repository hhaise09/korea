#!/usr/bin/env python
"""
Скрипт для добавления автомобилей с изображениями
"""

import os
import django

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'korean_cars_shop.settings')
django.setup()

from shop.models import Car

def add_cars_with_images():
    """Добавляет автомобили с изображениями"""
    
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
        {
            'brand': 'Hyundai',
            'model': 'Santa Fe',
            'year': 2022,
            'mileage': 18000,
            'transmission': 'automatic',
            'fuel_type': 'hybrid',
            'price': 3800000,
            'is_available': True,
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
    add_cars_with_images() 