from django.db import models
from django.db.models.fields.reverse_related import ManyToOneRel
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Student(models.Model):
    nsu_id = models.CharField(max_length=10, primary_key= True)
    full_name = models.CharField(max_length=50)
    program_name = models.CharField(max_length=100)
    personal_email = models.EmailField(max_length=50)
    cell_phone = models.CharField(max_length=15)
    nid = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    m = "Male"
    f = "Female"
    sex_choices = (
        (m, "Male"),
        (f, "Female")
    )
    sex = models.CharField(max_length=7, choices=sex_choices)
    blood_group = models.CharField(max_length=5)
    citizenship = models.CharField(max_length=20)
    marital_status = models.CharField(max_length=10)
    current_address = models.TextField(blank=True)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    parent_address = models.TextField(blank=True)
    parent_phone = models.CharField(max_length=15)
    
    def __str__(self):
        return self.nsu_id
    

class Financial(models.Model):
    student = models.OneToOneField(Student,on_delete=models.CASCADE)
    source = models.CharField(max_length=20)
    est_available_yearly = models.FloatField()

class Course(models.Model):
    course_code = models.CharField(max_length=6)
    course_credit = models.IntegerField()
    course_title = models.CharField(max_length=35)

    def __str__(self):
        return self.course_code

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.FloatField()
    year = models.CharField(max_length=4)
    semester = models.CharField(max_length=6)

class Customer(models.Model):
    name = models.CharField(max_length=30)
    bin = models.CharField(max_length=15)
    email = models.EmailField(max_length=40)

    def __str__(self):
        return self.name

class Customer_access(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key= True)
    student_name = models.BooleanField(default= False)
    student_id = models.BooleanField(default= False)
    program_name = models.BooleanField(default= False)
    student_email = models.BooleanField(default= False)
    student_cell = models.BooleanField(default= False)
    student_nid = models.BooleanField(default= False)
    student_dob = models.BooleanField(default= False)
    student_sex = models.BooleanField(default= False)
    student_bloodGroup = models.BooleanField(default= False)
    student_citizenship = models.BooleanField(default= False)
    student_maritalStatus = models.BooleanField(default= False)
    student_currentAddress = models.BooleanField(default= False)
    student_fatherName = models.BooleanField(default= False)
    student_motherName = models.BooleanField(default= False)
    student_parentAddress = models.BooleanField(default= False)
    student_parentPhone = models.BooleanField(default= False)
    Academic_Information = models.BooleanField(default=False)

    