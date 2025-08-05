from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.car_list, name='car_list'),
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),
    path('car/<int:car_id>/order/', views.order_car, name='order_car'),
    path('my-orders/', views.my_orders, name='my_orders'),
] 