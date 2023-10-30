from django.contrib import admin
from .models import Employee  

# Register your models here.
@admin.register(Employee)  
class EmployeeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Employee._meta.fields]  
    search_fields = ('first_name', 'last_name', 'email')  
