from django import forms
from .models import Employee
from .models import Car

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['fname', 'lname', 'birthdate', 'position', 'contact']

class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('car_model', 'manufacturer')