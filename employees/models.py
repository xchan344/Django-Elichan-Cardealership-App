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