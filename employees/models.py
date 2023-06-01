from django.db import models

class Employee(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    birthdate = models.DateField()
    position = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.fname} {self.lname}'

class Car(models.Model):
    car_model = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.car_model} ({self.manufacturer})"
    
class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('Bought', 'Bought'),
        ('Repair', 'Repair'),
        ('Consult', 'Consult'),
    ]

    TRANSACTION_STATUS = [
        ('Fully paid', 'Fully paid'),
        ('Partially paid', 'Partially paid'),
        ('NA', 'NA'),
    ]

    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    t_type = models.CharField(max_length=50, choices=TRANSACTION_TYPES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    t_status = models.CharField(max_length=50, choices=TRANSACTION_STATUS)
    date = models.DateField()

    def __str__(self):
        return f"{self.fname} {self.lname} - {self.car.car_model}"