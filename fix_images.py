#!/usr/bin/env python
"""
Скрипт для проверки и исправления связей изображений с автомобилями
"""
import os
import sys
import django
from pathlib import Path

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'korean_cars_shop.settings')
django.setup()

from shop.models import Car, CarImage
from django.core.files import File


def check_and_fix_images():
    """Проверяет и исправляет связи изображений с автомобилями"""
    print("Проверка связей изображений...")
    
    # Получаем все автомобили
    cars = Car.objects.all()
    print(f"Найдено автомобилей: {cars.count()}")
    
    for car in cars:
        print(f"\nАвтомобиль: {car.brand} {car.model} (ID: {car.id})")
        
        # Проверяем главное изображение
        if car.image:
            print(f"  ✓ Главное изображение: {car.image.name}")
            if not os.path.exists(car.image.path):
                print(f"  ⚠ Файл не найден: {car.image.path}")
        else:
            print(f"  ✗ Главное изображение отсутствует")
        
        # Проверяем дополнительные изображения
        additional_images = car.images.all()
        print(f"  Дополнительных изображений: {additional_images.count()}")
        
        for img in additional_images:
            if img.image:
                print(f"    - {img.image.name} (главное: {img.is_main})")
                if not os.path.exists(img.image.path):
                    print(f"    ⚠ Файл не найден: {img.image.path}")
            else:
                print(f"    ✗ Изображение без файла")
        
        # Если есть главное изображение, но нет записи в CarImage
        if car.image and not car.images.filter(is_main=True).exists():
            print(f"  🔧 Создаю запись CarImage для главного изображения...")
            CarImage.objects.create(
                car=car,
                image=car.image,
                is_main=True
            )
            print(f"  ✓ Запись создана")


def assign_images_to_cars():
    """Присваивает изображения автомобилям на основе их ID"""
    print("\nПрисваивание изображений автомобилям...")
    
    # Получаем все файлы изображений
    media_cars_dir = Path('media/cars')
    if not media_cars_dir.exists():
        print("Папка media/cars не найдена!")
        return
    
    image_files = list(media_cars_dir.glob('*.webp'))
    print(f"Найдено файлов изображений: {len(image_files)}")
    
    # Получаем автомобили без изображений
    cars_without_images = Car.objects.filter(image='')
    print(f"Автомобилей без изображений: {cars_without_images.count()}")
    
    # Присваиваем изображения по порядку
    for i, car in enumerate(cars_without_images):
        if i < len(image_files):
            image_file = image_files[i]
            print(f"Присваиваю {image_file.name} к {car.brand} {car.model}")
            
            # Создаем относительный путь для Django
            relative_path = f'cars/{image_file.name}'
            
            # Обновляем главное изображение
            car.image = relative_path
            car.save()
            
            # Создаем запись в CarImage
            CarImage.objects.create(
                car=car,
                image=relative_path,
                is_main=True
            )
            
            print(f"  ✓ Изображение присвоено")
        else:
            print(f"Нет больше изображений для {car.brand} {car.model}")


def main():
    """Основная функция"""
    print("=== Проверка и исправление изображений ===\n")
    
    # Проверяем текущее состояние
    check_and_fix_images()
    
    # Спрашиваем пользователя о присваивании изображений
    response = input("\nПрисвоить изображения автомобилям без изображений? (y/n): ")
    if response.lower() == 'y':
        assign_images_to_cars()
        print("\nПроверка после исправления:")
        check_and_fix_images()
    
    print("\n=== Готово ===")


if __name__ == '__main__':
    main() 