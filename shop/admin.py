from django.contrib import admin
from .models import Category, Car, CarImage, Order


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


class CarImageInline(admin.TabularInline):
    model = CarImage
    extra = 1


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model', 'year', 'price', 'is_available', 'created_at']
    list_filter = ['brand', 'year', 'transmission', 'fuel_type', 'is_available']
    search_fields = ['brand', 'model']
    list_editable = ['price', 'is_available']
    prepopulated_fields = {}
    inlines = [CarImageInline]
    fieldsets = (
        ('Основная информация', {
            'fields': ('brand', 'model', 'year', 'price', 'is_available')
        }),
        ('Технические характеристики', {
            'fields': ('mileage', 'transmission', 'fuel_type')
        }),
        ('Изображение', {
            'fields': ('image',)
        }),
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'car', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['user__username', 'car__brand', 'car__model']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Информация о заказе', {
            'fields': ('user', 'car', 'status')
        }),
        ('Дополнительно', {
            'fields': ('comment', 'created_at', 'updated_at')
        }),
    )
