from django import forms
from django.forms import ModelForm, widgets
from .models import Student, Financial, Course, Result, Customer, Customer_access

#Creating Student form
class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = "__all__" #('nsu_id',)

        '''
        labels = {
            'nsu_id' : ''
        }

        widgets = {
            'nsu_id' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'NSU ID'})
        }
        '''

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
