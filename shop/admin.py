from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import Category, Car, CarImage, Order


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


class CarImageInline(admin.TabularInline):
    model = CarImage
    extra = 1
    fields = ['image', 'is_main', 'image_preview']
    readonly_fields = ['image_preview']
    
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 50px; max-width: 50px;" />',
                obj.image.url
            )
        return "Нет изображения"
    image_preview.short_description = 'Предварительный просмотр'


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model', 'year', 'price', 'is_available', 'created_at', 'image_preview']
    list_filter = ['brand', 'year', 'transmission', 'fuel_type', 'is_available', 'created_at']
    search_fields = ['brand', 'model']
    list_editable = ['price', 'is_available']
    prepopulated_fields = {}
    inlines = [CarImageInline]
    readonly_fields = ['image_preview', 'created_at']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('brand', 'model', 'year', 'price', 'is_available')
        }),
        ('Технические характеристики', {
            'fields': ('mileage', 'transmission', 'fuel_type')
        }),
        ('Изображение', {
            'fields': ('image', 'image_preview')
        }),
        ('Дополнительно', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 100px; max-width: 100px;" />',
                obj.image.url
            )
        return "Нет изображения"
    image_preview.short_description = 'Главное изображение'
    
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # Если это новое изображение, обновляем главное изображение
        if obj.image:
            # Убеждаемся, что есть запись в CarImage для главного изображения
            main_image, created = CarImage.objects.get_or_create(
                car=obj,
                is_main=True,
                defaults={'image': obj.image}
            )
            if not created and main_image.image != obj.image:
                main_image.image = obj.image
                main_image.save()


@admin.register(CarImage)
class CarImageAdmin(admin.ModelAdmin):
    list_display = ['car', 'is_main', 'image_preview']
    list_filter = ['is_main', 'car__brand']
    search_fields = ['car__brand', 'car__model']
    readonly_fields = ['image_preview']
    
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 100px; max-width: 100px;" />',
                obj.image.url
            )
        return "Нет изображения"
    image_preview.short_description = 'Предварительный просмотр'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'car', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['user__username', 'car__brand', 'car__model']
    readonly_fields = ['created_at', 'updated_at']
    list_editable = ['status']
    
    fieldsets = (
        ('Информация о заказе', {
            'fields': ('user', 'car', 'status')
        }),
        ('Дополнительно', {
            'fields': ('comment', 'created_at', 'updated_at')
        }),
    )
