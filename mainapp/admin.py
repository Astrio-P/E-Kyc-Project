from django.contrib import admin
from .models import Student, Financial, Course, Result, Customer, Customer_access

# Register your models here.

admin.site.register(Student)
admin.site.register(Financial)
admin.site.register(Course)
admin.site.register(Result)
admin.site.register(Customer)
admin.site.register(Customer_access)
