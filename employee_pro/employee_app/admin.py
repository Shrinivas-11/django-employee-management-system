from django.contrib import admin
from .models import Department,Employee,Address,Document

# Register your models here.

admin.site.register(Employee)
admin.site.register(Document)
admin.site.register(Address)
admin.site.register(Department)
