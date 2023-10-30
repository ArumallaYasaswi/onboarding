from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.employee_list, name='employee_list'),
    path('employee/<int:employee_id>/', views.employee_detail, name='employee_detail'),
    path('employeeupdate/<int:employee_id>/', views.update_employee, name='employee_update'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('mark_onboarded/<int:employee_id>/', views.mark_onboarded, name='mark_onboarded'),
]
