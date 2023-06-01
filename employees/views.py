from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Car
from .forms import CarModelForm

#employees page
def employees(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employees.html', {'employees': employees})

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employees')
    else:
        form = EmployeeForm()
    return render(request, 'employees/add_employee.html', {'form': form})

def edit_employee(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employees')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'edit_employee.html', {'form': form, 'employee_id': employee_id, 'employee': employee})

def delete_employee(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    employee.delete()
    return redirect('employees')

def transactions(request):
    return render(request, 'transactions.html')

def cars(request):
    return render(request, 'cars.html')

def logout(request):
    return render(request, 'logout.html')

#cars page
def cars(request):
    cars = Car.objects.all()
    return render(request, 'cars.html', {'cars': cars})

def add_car_model(request):
    if request.method == 'POST':
        form = CarModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cars')
    else:
        form = CarModelForm()
    
    return render(request, 'add_car_model.html', {'form': form})

def edit_car_model(request, pk):
    car = get_object_or_404(Car, pk=pk)
    
    if request.method == 'POST':
        form = CarModelForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('cars')
    else:
        form = CarModelForm(instance=car)
    
    return render(request, 'edit_car_model.html', {'form': form})

def delete_car_model(request, pk):
    car = get_object_or_404(Car, pk=pk)
    car.delete()
    return redirect('cars')