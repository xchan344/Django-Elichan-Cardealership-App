from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .forms import EmployeeForm, CarModelForm, TransactionForm
from .models import Employee, Car, Transaction
from .models import Transaction, Car
from django.db.models import Count
import json
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate

#login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage')  # Replace 'homepage' with the URL name of your desired homepage
    else:
        form = AuthenticationForm()
    return render(request, 'employees/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Replace 'login' with the URL name of your login view
    else:
        form = UserCreationForm()
    return render(request, 'employees/register.html', {'form': form})

#homepage
def homepage(request):
    # Calculate transactions per car model
    transactions_data = (
        Transaction.objects
        .values('car__car_model')
        .annotate(transaction_count=Count('id'))
        .order_by('car__car_model')
    )

    # Convert transactions_data to JSON
    transactions_data_json = json.dumps(list(transactions_data))

    context = {
        'transactions_data': transactions_data_json
    }
    return render(request, 'homepage.html', context)

#links
def transactions(request):
    return render(request, 'transactions.html')

def cars(request):
    return render(request, 'cars.html')

def logout(request):
    return render(request, 'logout.html')

# Employees
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
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employees')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'edit_employee.html', {'form': form, 'employee_id': employee_id, 'employee': employee})

def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    employee.delete()
    return redirect('employees')

# Cars
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

# Transactions
def transactions(request):
    fname = request.GET.get('fname')
    lname = request.GET.get('lname')
    car_id = request.GET.get('car')
    t_type = request.GET.get('t_type')
    t_status = request.GET.get('t_status')

    transactions = Transaction.objects.all()

    if fname:
        transactions = transactions.filter(fname__icontains=fname)
    if lname:
        transactions = transactions.filter(lname__icontains=lname)
    if car_id:
        transactions = transactions.filter(car_id=car_id)
    if t_type:
        transactions = transactions.filter(t_type=t_type)
    if t_status:
        transactions = transactions.filter(t_status=t_status)

    cars = Car.objects.all()

    context = {
        'transactions': transactions,
        'cars': cars,
        'fname': fname,
        'lname': lname,
        'selected_car': int(car_id) if car_id else None,
        'selected_t_type': t_type,
        'selected_t_status': t_status,
    }

    return render(request, 'transactions.html', context)

def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transactions')
    else:
        form = TransactionForm()

    cars = Car.objects.all()

    return render(request, 'add_transaction.html', {'form': form, 'cars': cars})

def edit_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('transactions')
    else:
        form = TransactionForm(instance=transaction)

    cars = Car.objects.all()

    context = {
        'form': form,
        'cars': cars,
    }
    return render(request, 'edit_transaction.html', context)

def delete_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id)
    transaction.delete()
    return redirect('transactions')
