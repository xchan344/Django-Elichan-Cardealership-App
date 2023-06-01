from django import forms
from .models import Employee
from .models import Car
from .models import Transaction

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['fname', 'lname', 'birthdate', 'position', 'contact']

class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('car_model', 'manufacturer')

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'