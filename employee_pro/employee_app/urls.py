from django.urls import path
from .views import add_department,add_employee,add_address,add_document,employee_list

urlpatterns =[
    path('add-department/', add_department, name='add_department_url'),
    path('add-employee/',add_employee, name='add_employee_url'),
    path('add-address/',add_address,name='add_address_url'),
    path('add-document/',add_document,name='add_document_url'),
    path('employee-list/',employee_list,name='employee_list_url')
]