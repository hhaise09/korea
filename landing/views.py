from django.shortcuts import render
from shop.models import Car


def landing_page(request):
    """Главная страница лендинга"""
    # Получаем несколько автомобилей для демонстрации на лендинге
    featured_cars = Car.objects.filter(is_available=True).order_by('-created_at')[:6]
    
    context = {
        'featured_cars': featured_cars,
    }
    return render(request, 'landing/landing.html', context)
