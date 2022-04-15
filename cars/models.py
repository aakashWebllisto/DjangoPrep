
# Create your models here.

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Company(models.Model):
    make = models.CharField(max_length=100)

    def __str__(self):
        return self.make

class Car(models.Model):
    # make = models.CharField(max_length=200,)
    model_name = models.CharField(max_length=200,)
    condition = models.CharField(max_length=200,)
    year = models.PositiveIntegerField(blank=True, null=True)
    asking_price = models.FloatField(blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(10)])
    make = models.ForeignKey(Company, blank=True, null=True, on_delete=models.CASCADE)


    def __str__(self):
        if self.year:
            return f"{self.make} ({self.model_name})"
        return self.make
    
