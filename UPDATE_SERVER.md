# 🔄 Обновление данных на сервере Render

## Проблема
На сервере изображения не загружаются (ошибки 404). Это происходит потому, что:
1. Изображения не были правильно импортированы
2. Папка `media` не была создана на сервере
3. Форматы файлов не соответствуют ожидаемым

## ✅ Решение

### 1. Автоматическое исправление

Обновленные файлы теперь:
- ✅ Создают папку `media/cars` автоматически
- ✅ Используют правильные форматы файлов `.webp`
- ✅ Копируют файлы в правильные места

### 2. Загрузка исправлений на GitHub

```bash
# Добавьте все изменения
git add .

# Закоммитьте с описанием
git commit -m "Fix media folder creation and image import on Render"

# Загрузите на GitHub
git push origin main
```

### 3. Автоматическое обновление на Render

После загрузки на GitHub:
1. Render автоматически обнаружит изменения
2. Запустится новый деплой
3. `build.sh` создаст папку media и импортирует данные
4. Изображения будут доступны

## 🔧 Ручное исправление (если автоматическое не работает)

### Вариант 1: Через SSH на Render

1. Подключитесь к серверу Render через SSH
2. Выполните команды:

```bash
# Создаем папки
mkdir -p media/cars

# Очищаем старые данные
python manage.py shell
>>> from shop.models import Car, CarImage
>>> Car.objects.all().delete()
>>> CarImage.objects.all().delete()
>>> exit()

# Импортируем новые данные
python export_data.py import

# Соберите статические файлы
python manage.py collectstatic --noinput
```

### Вариант 2: Использование специального скрипта

```bash
# Запустите специальный скрипт исправления
python fix_server_images.py
```

### Вариант 3: Проверка и исправление через Django shell

```bash
python manage.py shell
```

```python
from shop.models import Car, CarImage
from pathlib import Path
import shutil

# Создаем папки
media_dir = Path('media')
media_dir.mkdir(exist_ok=True)
media_cars_dir = media_dir / 'cars'
media_cars_dir.mkdir(exist_ok=True)

# Проверяем данные
print(f"Автомобилей: {Car.objects.count()}")
print(f"Изображений: {CarImage.objects.count()}")

# Проверяем файлы
image_files = list(media_cars_dir.glob('*'))
print(f"Файлов в media/cars: {len(image_files)}")

# Если файлов нет, импортируем заново
if len(image_files) == 0:
    print("Импортируем данные...")
    import subprocess
    subprocess.run(['python', 'export_data.py', 'import'])
```

## 📊 Проверка результата

### После исправления проверьте:

1. **Файлы на сервере:**
```bash
ls -la media/cars/
# Должно быть 20 файлов .webp
```

2. **Данные в базе:**
```bash
python manage.py shell
>>> from shop.models import Car, CarImage
>>> Car.objects.count()  # Должно быть 9
>>> CarImage.objects.count()  # Должно быть 10
>>> Car.objects.first().image.name  # Должно быть 'cars/car_X_main.webp'
```

3. **Сайт в браузере:**
- ✅ https://korea-tisl.onrender.com/ - главная страница
- ✅ https://korea-tisl.onrender.com/shop/ - каталог с изображениями
- ✅ Никаких ошибок 404

## 🎯 Структура правильных данных

После исправления на сервере должны быть:
```
media/cars/
├── car_1_main.webp
├── car_1_image_1.webp
├── car_2_main.webp
├── car_2_image_2.webp
└── ... (всего 20 файлов)
```

## 🚨 Если проблема остается

1. **Проверьте логи в Render** - найдите точную ошибку
2. **Убедитесь, что все файлы загружены** - проверьте export_data/
3. **Проверьте переменные окружения** - ENVIRONMENT=production
4. **Создайте новый деплой** - с чистого состояния

## 📞 Поддержка

Если ничего не помогает:
1. Удалите старые данные через админку
2. Загрузите новые изображения через админку
3. Экспортируйте данные заново
4. Импортируйте на сервер

---

# 🎉 Результат

После исправления:
- ✅ Все изображения будут загружаться
- ✅ Никаких ошибок 404
- ✅ Красивый каталог автомобилей
- ✅ Работающие детальные страницы 