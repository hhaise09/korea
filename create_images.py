#!/usr/bin/env python
"""
Скрипт для создания изображений автомобилей
"""

import os

def create_car_image(brand, model, year, price, filename):
    """Создает SVG изображение для автомобиля"""
    
    svg_content = f'''<svg width="400" height="250" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="250" fill="#f8f8f8"/>
  <rect x="50" y="100" width="300" height="100" fill="#333" rx="10"/>
  <rect x="60" y="110" width="280" height="80" fill="#666" rx="5"/>
  <circle cx="100" cy="180" r="15" fill="#000"/>
  <circle cx="300" cy="180" r="15" fill="#000"/>
  <text x="200" y="140" text-anchor="middle" fill="#fff" font-family="Arial" font-size="16" font-weight="bold">{brand} {model}</text>
  <text x="200" y="160" text-anchor="middle" fill="#ccc" font-family="Arial" font-size="12">{year} • {price:,} ₽</text>
</svg>'''
    
    # Создаем папку если не существует
    os.makedirs('static/images/cars', exist_ok=True)
    
    # Сохраняем файл
    with open(f'static/images/cars/{filename}', 'w', encoding='utf-8') as f:
        f.write(svg_content)
    
    print(f"✅ Создано изображение: {filename}")

def create_all_images():
    """Создает изображения для всех автомобилей"""
    
    cars = [
        ('Hyundai', 'Sonata', 2022, 2500000, 'hyundai-sonata.svg'),
        ('Kia', 'Rio', 2021, 1800000, 'kia-rio.svg'),
        ('Genesis', 'G80', 2023, 4500000, 'genesis-g80.svg'),
        ('Hyundai', 'Tucson', 2022, 3200000, 'hyundai-tucson.svg'),
        ('Kia', 'Sportage', 2021, 2800000, 'kia-sportage.svg'),
        ('Genesis', 'GV70', 2023, 5200000, 'genesis-gv70.svg'),
        ('Hyundai', 'Santa Fe', 2022, 3800000, 'hyundai-santa-fe.svg'),
        ('Kia', 'K5', 2021, 2200000, 'kia-k5.svg'),
        ('Genesis', 'G90', 2023, 6500000, 'genesis-g90.svg'),
        ('Hyundai', 'Elantra', 2022, 1900000, 'hyundai-elantra.svg'),
        ('Kia', 'Sorento', 2021, 3500000, 'kia-sorento.svg'),
        ('Genesis', 'GV80', 2023, 5800000, 'genesis-gv80.svg'),
    ]
    
    for brand, model, year, price, filename in cars:
        create_car_image(brand, model, year, price, filename)
    
    print(f"\n🎉 Создано {len(cars)} изображений автомобилей!")

if __name__ == '__main__':
    create_all_images() 