#!/usr/bin/env python
"""
Скрипт для проверки базы данных
"""

import os
import django

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'korean_cars_shop.settings')
django.setup()

from shop.models import Car

def check_database():
    """Проверяет состояние базы данных"""
    
    print("🔍 Проверка базы данных...")
    
    # Проверяем количество автомобилей
    total_cars = Car.objects.count()
    print(f"📊 Всего автомобилей: {total_cars}")
    
    if total_cars == 0:
        print("❌ Автомобили не найдены!")
        print("💡 Запустите: python manage_demo.py")
        return
    
    # Показываем все автомобили
    print("\n📋 Список автомобилей:")
    for car in Car.objects.all():
        print(f"  - {car.brand} {car.model} ({car.year}) - {car.price:,} ₽")
        print(f"    Пробег: {car.mileage:,} км")
        print(f"    Трансмиссия: {car.get_transmission_display()}")
        print(f"    Топливо: {car.get_fuel_type_display()}")
        print(f"    Доступен: {'Да' if car.is_available else 'Нет'}")
        print()
    
    # Проверяем доступные автомобили
    available_cars = Car.objects.filter(is_available=True).count()
    print(f"✅ Доступных автомобилей: {available_cars}")

if __name__ == '__main__':
    check_database() 