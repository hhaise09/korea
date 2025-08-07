#!/usr/bin/env python
"""
Скрипт для проверки и исправления медиафайлов на сервере
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


def check_media_files():
    """Проверяет медиафайлы на сервере"""
    print("🔍 Проверка медиафайлов на сервере...")
    
    # Проверяем папки
    media_dir = Path('media')
    media_cars_dir = media_dir / 'cars'
    
    print(f"Папка media: {'✅ Существует' if media_dir.exists() else '❌ Не существует'}")
    print(f"Папка media/cars: {'✅ Существует' if media_cars_dir.exists() else '❌ Не существует'}")
    
    if media_cars_dir.exists():
        image_files = list(media_cars_dir.glob('*.webp'))
        print(f"Файлов изображений: {len(image_files)}")
        
        for img_file in image_files:
            print(f"  - {img_file.name}")
    
    # Проверяем данные в БД
    cars = Car.objects.all()
    print(f"\nАвтомобилей в БД: {cars.count()}")
    
    for car in cars:
        print(f"  {car.brand} {car.model}: {car.image.name if car.image else 'Нет изображения'}")
    
    # Проверяем CarImage
    car_images = CarImage.objects.all()
    print(f"Записей CarImage: {car_images.count()}")
    
    for img in car_images:
        print(f"  {img.car.brand} {img.car.model}: {img.image.name if img.image else 'Нет изображения'}")


def fix_media_files():
    """Исправляет медиафайлы на сервере"""
    print("\n🔧 Исправление медиафайлов...")
    
    # Создаем папки
    media_dir = Path('media')
    media_dir.mkdir(exist_ok=True)
    media_cars_dir = media_dir / 'cars'
    media_cars_dir.mkdir(exist_ok=True)
    
    # Проверяем экспортированные данные
    export_dir = Path('export_data')
    if not export_dir.exists():
        print("❌ Папка export_data не найдена!")
        return
    
    images_dir = export_dir / 'images'
    if not images_dir.exists():
        print("❌ Папка images не найдена!")
        return
    
    # Копируем изображения
    image_files = list(images_dir.glob('*.webp'))
    print(f"Найдено {len(image_files)} изображений для копирования")
    
    for img_file in image_files:
        dest_file = media_cars_dir / img_file.name
        shutil.copy2(img_file, dest_file)
        print(f"  ✅ Скопирован: {img_file.name}")
    
    print(f"\n🎉 Исправление завершено!")
    print(f"Файлов в media/cars: {len(list(media_cars_dir.glob('*')))}")


def main():
    """Основная функция"""
    print("🔍 ПРОВЕРКА МЕДИАФАЙЛОВ НА СЕРВЕРЕ")
    print("=" * 50)
    
    check_media_files()
    
    response = input("\nИсправить медиафайлы? (y/n): ")
    if response.lower() == 'y':
        fix_media_files()
        print("\nПроверка после исправления:")
        check_media_files()


if __name__ == '__main__':
    main() 