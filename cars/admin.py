from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Company, Car
admin.site.register(Car)
admin.site.register(Company)