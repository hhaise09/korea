from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Car, Category, Order


def car_list(request):
    """Список всех автомобилей"""
    cars = Car.objects.filter(is_available=True)
    
    # Поиск
    search_query = request.GET.get('search')
    if search_query:
        cars = cars.filter(
            Q(brand__icontains=search_query) |
            Q(model__icontains=search_query)
        )
    
    # Сортировка
    sort_by = request.GET.get('sort', 'created_at')
    if sort_by == 'price':
        cars = cars.order_by('price')
    elif sort_by == 'price_desc':
        cars = cars.order_by('-price')
    elif sort_by == 'year':
        cars = cars.order_by('-year')
    else:
        cars = cars.order_by('-created_at')
    
    context = {
        'cars': cars,
        'search_query': search_query,
        'sort_by': sort_by,
    }
    return render(request, 'shop/car_list.html', context)


def car_detail(request, car_id):
    """Детальная страница автомобиля"""
    car = get_object_or_404(Car, id=car_id, is_available=True)
    
    context = {
        'car': car,
    }
    return render(request, 'shop/car_detail.html', context)


@login_required
def order_car(request, car_id):
    """Оформление заказа на автомобиль"""
    car = get_object_or_404(Car, id=car_id, is_available=True)
    
    if request.method == 'POST':
        comment = request.POST.get('comment', '')
        
        # Проверяем, нет ли уже заказа на этот автомобиль от этого пользователя
        existing_order = Order.objects.filter(user=request.user, car=car, status__in=['new', 'confirmed', 'processing'])
        
        if existing_order.exists():
            messages.error(request, 'У вас уже есть активный заказ на этот автомобиль.')
        else:
            Order.objects.create(
                user=request.user,
                car=car,
                comment=comment
            )
            messages.success(request, f'Заказ на {car.brand} {car.model} успешно оформлен!')
            return redirect('shop:car_detail', car_id=car.id)
    
    context = {
        'car': car,
    }
    return render(request, 'shop/order_car.html', context)


@login_required
def my_orders(request):
    """Мои заказы"""
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    
    context = {
        'orders': orders,
    }
    return render(request, 'shop/my_orders.html', context)
