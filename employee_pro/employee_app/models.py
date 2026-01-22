from django.db import models

# Create your models here.



class Department(models.Model):                          #(Parent)
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name
    

class Employee(models.Model):                                #(emp => dep == one to many)  (child of Department and parent of Address and doc)
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)   #Link Employee table to the Department table.

    def __str__(self):
        return f"{self.f_name} {self.l_name} {self.id}"
    

class Address(models.Model):                           #(Child of Emp)                        
    city = models.CharField(max_length=50)
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return f"Employee Address {self.employee}"
    
class Document(models.Model):                       #(Child of Emp)     
    title = models.CharField(max_length=50)
    file = models.FileField(upload_to='employee_files/')
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name='documents')

    def __str__(self):
        return self.title
    
