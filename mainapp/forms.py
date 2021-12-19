from django import forms
from django.forms import ModelForm, widgets
from .models import Student, Personal, Financial, Course, Result, Customer, Customer_access

#Creating Student form
class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = "__all__" #('nsu_id',)

        labels = {
            'nsu_id' : ''
        }

        widgets = {
            'nsu_id' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'NSU ID'})
        }

#Creating Personal form
class PersonalForm(ModelForm):
    class Meta:
        model = Personal
        fields = "__all__"

        '''labels = {
            #'student' : '',
            'full_name' : '',
            'program_name' : '',
            'personal_email' : '',
            'cell_phone' : '',
            'nid' : '',
            'date_of_birth' : '',
            #'sex' : '',
            'blood_group' : '',
            'citizenship' : '',
            'marital_status' : '',
            'current_address' : '',
            'parent_phone' : '',
            'father_name' : '',
            'mother_name' : '',
            'parent_address' : '',
        }

        widgets = {
            #'student' : forms.TextInput(attrs={'class':'form-control'}),
            'full_name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Full Name'}),
            'program_name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Program Name'}),
            'personal_email' : forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
            'cell_phone' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone'}),
            'nid' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'NID'}),
            'date_of_birth' : forms.DateInput(attrs={'class':'form-control', 'placeholder':'Date of Birth'}),
            #'sex' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Sex'}),
            'blood_group' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Blood Group'}),
            'citizenship' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Citizenship'}),
            'marital_status' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Marital Status'}),
            'current_address' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Current Address'}),
            'parent_phone' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Parent Phone'}),
            'father_name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Fathers Name'}),
            'mother_name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Mothers Name'}),
            'parent_address' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Parent Address'}),
        }'''

#Creating Financial form
class FinancialForm(ModelForm):
    class Meta:
        model = Financial
        fields = "__all__"

#Creating Result form
class ResultForm(ModelForm):
    class Meta:
        model = Result
        fields = "__all__"

#Creating Course form
class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = "__all__"

#Creating Customer form
class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"

#Creating Customer access form
class CustomerAccessForm(ModelForm):
    class Meta:
        model = Customer_access
        fields = "__all__"
