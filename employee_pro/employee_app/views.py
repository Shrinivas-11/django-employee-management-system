from django.shortcuts import render,redirect
from .forms import DepartmentForm,EmployeeForm,AddressForm,DocumentForm
from .models import Employee
from django.http import HttpResponse

def add_department(request):
    department = DepartmentForm()
    template_name='employee_app/department.html'
    if request.method =='POST':
        department = DepartmentForm(request.POST)
        if department.is_valid():
            department.save()
            return redirect('employee_list_url')
    context = {'department':department}
    return render (request, template_name, context)

def add_employee(request):
    employee = EmployeeForm()
    template_name ='employee_app/employee.html'
    if request.method =='POST':
        employee = EmployeeForm(request.POST)
        if employee.is_valid():
            employee.save()
            return redirect('employee_list_url')
    context = {'employee':employee}
    return render (request,template_name, context )


def add_address(request):
    address = AddressForm()
    template_name ='employee_app/address.html'
    if request.method == 'POST':
        address = AddressForm(request.POST)
        if address.is_valid():
            address.save()
            return redirect('employee_list_url')
    context = {'address':address}
    return render (request,template_name, context )
    

def add_document(request):
    document = DocumentForm()
    template_name = 'employee_app/document.html'
    if request.method == 'POST':
        document = DocumentForm(request.POST, request.FILES)
        if document.is_valid():
            document.save()
            return redirect('employee_list_url')
    context= {'document':document}
    return render (request, template_name, context )



def employee_list(request):
    # Get all employees
    employees = Employee.objects.all()
    template_name = 'employee_app/employee_list.html'
    context = {'employees':employees}
    return render (request, template_name, context)
    



    




