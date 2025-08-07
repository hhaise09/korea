#!/usr/bin/env python
"""
Скрипт для проверки готовности проекта к деплою на Render
"""
import os
import sys
from pathlib import Path

def check_files():
    """Проверяет наличие всех необходимых файлов"""
    print("🔍 Проверка файлов для деплоя...")
    
    required_files = [
        'requirements.txt',
        'manage.py',
        'build.sh',
        'gunicorn.conf.py',
        'korean_cars_shop/settings.py',
        'korean_cars_shop/wsgi.py',
        'korean_cars_shop/urls.py',
        'shop/models.py',
        'shop/admin.py',
        'shop/views.py',
        'shop/urls.py',
        'landing/views.py',
        'landing/urls.py',
        'templates/base.html',
        'templates/shop/car_list.html',
        'templates/shop/car_detail.html',
        'static/css/style.css',
    ]
    
    missing_files = []
    for file_path in required_files:
        if not Path(file_path).exists():
            missing_files.append(file_path)
        else:
            print(f"  ✅ {file_path}")
    
    if missing_files:
        print(f"\n❌ Отсутствуют файлы:")
        for file in missing_files:
            print(f"  - {file}")
        return False
    else:
        print("  ✅ Все необходимые файлы на месте")
        return True

def check_export_data():
    """Проверяет экспортированные данные"""
    print("\n📦 Проверка экспортированных данных...")
    
    export_dir = Path('export_data')
    if not export_dir.exists():
        print("  ❌ Папка export_data не найдена")
        return False
    
    cars_data_file = export_dir / 'cars_data.json'
    if not cars_data_file.exists():
        print("  ❌ Файл cars_data.json не найден")
        return False
    
    images_dir = export_dir / 'images'
    if not images_dir.exists():
        print("  ❌ Папка images не найдена")
        return False
    
    # Подсчитываем изображения
    image_files = list(images_dir.glob('*.jpg'))
    print(f"  ✅ Найдено {len(image_files)} изображений")
    
    # Проверяем размер файла с данными
    file_size = cars_data_file.stat().st_size
    print(f"  ✅ Размер файла данных: {file_size} байт")
    
    return True

def check_settings():
    """Проверяет настройки Django"""
    print("\n⚙️ Проверка настроек Django...")
    
    try:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'korean_cars_shop.settings')
        import django
        django.setup()
        
        from django.conf import settings
        
        # Проверяем ключевые настройки
        checks = [
            ('DEBUG', settings.DEBUG),
            ('SECRET_KEY', bool(settings.SECRET_KEY)),
            ('ALLOWED_HOSTS', bool(settings.ALLOWED_HOSTS)),
            ('STATIC_URL', settings.STATIC_URL),
            ('MEDIA_URL', settings.MEDIA_URL),
            ('DATABASES', bool(settings.DATABASES)),
        ]
        
        for setting_name, value in checks:
            if value:
                print(f"  ✅ {setting_name}: OK")
            else:
                print(f"  ❌ {setting_name}: НЕ НАСТРОЕН")
                return False
        
        return True
        
    except Exception as e:
        print(f"  ❌ Ошибка проверки настроек: {e}")
        return False

def check_models():
    """Проверяет модели Django"""
    print("\n🗄️ Проверка моделей...")
    
    try:
        from shop.models import Car, CarImage, Order
        
        # Проверяем количество записей
        cars_count = Car.objects.count()
        images_count = CarImage.objects.count()
        orders_count = Order.objects.count()
        
        print(f"  ✅ Автомобилей в БД: {cars_count}")
        print(f"  ✅ Изображений в БД: {images_count}")
        print(f"  ✅ Заказов в БД: {orders_count}")
        
        return True
        
    except Exception as e:
        print(f"  ❌ Ошибка проверки моделей: {e}")
        return False

def main():
    """Основная функция проверки"""
    print("🚀 ПРОВЕРКА ГОТОВНОСТИ К ДЕПЛОЮ НА RENDER")
    print("=" * 50)
    
    checks = [
        ("Файлы проекта", check_files),
        ("Экспортированные данные", check_export_data),
        ("Настройки Django", check_settings),
        ("Модели и данные", check_models),
    ]
    
    all_passed = True
    
    for check_name, check_func in checks:
        try:
            if not check_func():
                all_passed = False
        except Exception as e:
            print(f"  ❌ Ошибка в проверке {check_name}: {e}")
            all_passed = False
    
    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 ВСЕ ПРОВЕРКИ ПРОЙДЕНЫ!")
        print("✅ ПРОЕКТ ГОТОВ К ДЕПЛОЮ НА RENDER!")
        print("\n📋 Следующие шаги:")
        print("1. Закоммитьте все изменения в git")
        print("2. Загрузите на GitHub")
        print("3. Создайте Web Service на Render")
        print("4. Настройте переменные окружения")
        print("5. Дождитесь успешного деплоя")
    else:
        print("❌ НЕКОТОРЫЕ ПРОВЕРКИ НЕ ПРОЙДЕНЫ")
        print("Исправьте ошибки перед деплоем")
    
    print("\n📖 Подробная инструкция в файле DEPLOY_READY.md")

if __name__ == '__main__':
    main() 