from django.shortcuts import render, redirect
from .models import Employee
from django.urls import reverse
from .forms import EmployeeForm
from django.contrib.auth.decorators import login_required

@login_required
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})


@login_required
def employee_detail(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    return render(request, 'employee_detail.html', {'employee': employee})


@login_required
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'add_employee.html', {'form': form})


@login_required
def mark_onboarded(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    employee.is_onboarded = True
    employee.save()
    return redirect('employee_list')


@login_required
def update_employee(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect(reverse('employee_detail', kwargs={'employee_id': employee.id}))
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee_update.html', {'form': form, 'employee':employee})

