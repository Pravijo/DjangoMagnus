from django.contrib import admin
from .models import Employee,Pets,Car

# Register your models here.
admin.site.register(Employee)
admin.site.register(Pets)
admin.site.register(Car)