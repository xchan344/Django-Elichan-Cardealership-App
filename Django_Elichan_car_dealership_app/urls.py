from django.contrib import admin
from django.urls import path, include
from employees.views import employees, add_employee, edit_employee, delete_employee, transactions, cars, logout
from django.conf import settings
from django.conf.urls.static import static
from employees import views

urlpatterns = [
    #employees
    path('employees/', views.employees, name='employees'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('edit_employee/<int:employee_id>/', views.edit_employee, name='edit_employee'),
    path('delete_employee/<int:employee_id>/', views.delete_employee, name='delete_employee'),
    path('transactions/', views.transactions, name='transactions'),
    path('cars/', views.cars, name='cars'),
    path('logout/', views.logout, name='logout'),
    #cars
    path('cars/', views.cars, name='cars'),
    path('add_car_model/', views.add_car_model, name='add_car_model'),
    path('edit_car_model/<int:pk>/', views.edit_car_model, name='edit_car_model'),
    path('delete_car/<int:pk>/', views.delete_car_model, name='delete_car_model'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
