from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='URL')
    description = models.TextField(blank=True, verbose_name='Описание')
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
    def __str__(self):
        return self.name


class Car(models.Model):
    TRANSMISSION_CHOICES = [
        ('manual', 'Механика'),
        ('automatic', 'Автомат'),
        ('robot', 'Робот'),
        ('cvt', 'Вариатор'),
    ]
    
    FUEL_CHOICES = [
        ('gasoline', 'Бензин'),
        ('diesel', 'Дизель'),
        ('hybrid', 'Гибрид'),
        ('electric', 'Электро'),
    ]
    
    brand = models.CharField(max_length=100, verbose_name='Марка')
    model = models.CharField(max_length=100, verbose_name='Модель')
    year = models.IntegerField(verbose_name='Год выпуска')
    mileage = models.IntegerField(verbose_name='Пробег (км)')
    transmission = models.CharField(max_length=20, choices=TRANSMISSION_CHOICES, verbose_name='Трансмиссия')
    fuel_type = models.CharField(max_length=20, choices=FUEL_CHOICES, verbose_name='Тип топлива')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    image = models.ImageField(upload_to='cars/', verbose_name='Главное изображение')
    is_available = models.BooleanField(default=True, verbose_name='Доступен')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    
    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"


class CarImage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='images', verbose_name='Автомобиль')
    image = models.ImageField(upload_to='cars/', verbose_name='Изображение')
    is_main = models.BooleanField(default=False, verbose_name='Главное изображение')
    
    class Meta:
        verbose_name = 'Изображение автомобиля'
        verbose_name_plural = 'Изображения автомобилей'
    
    def __str__(self):
        return f"Изображение {self.car.brand} {self.car.model}"


class Order(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новый'),
        ('confirmed', 'Подтвержден'),
        ('processing', 'В обработке'),
        ('completed', 'Завершен'),
        ('cancelled', 'Отменен'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Автомобиль')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new', verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    comment = models.TextField(blank=True, verbose_name='Комментарий')
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Заказ {self.id} - {self.car.brand} {self.car.model}"
