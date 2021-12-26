from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from rest_framework.serializers import Serializer
from .models import Customer, Student, Financial, Result, Course, Customer_access
from .forms import StudentForm, ResultForm, FinancialForm, CourseForm, CustomerForm,CustomerAccessForm
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import studentSerializer, academicSerializer
from rest_framework.permissions import IsAuthenticated



def home(request):
    return render(request,'mainapp/home.html', {})

# Viewing Info Functions...

def all_students(request):
    student_list = Student.objects.all()
    financial_list = Financial.objects.all()
    course_list = Course.objects.all()
    result_list = Result.objects.all()
    return render(request, 'mainapp/student_list.html',
    {"student_list": student_list, 
    "financial_list": financial_list,
    "course_list": course_list,
    "result_list": result_list
    })

def all_customers(request):
    customer_list = Customer.objects.all()
    return render(request, 'mainapp/customer_list.html',
    {"customer_list": customer_list,})

def show_customer(request, customer_id):
    customer = Customer.objects.get(pk=customer_id)
    return render(request, 'mainapp/show_customer.html',
    {"customer": customer})

def show_student(request, student_id):
    student = Student.objects.get(pk=student_id)
    return render(request, 'mainapp/show_student.html',
    {"student": student})

def show_academic(request, academic_id):
    academic = Result.objects.get(pk=academic_id)
    return render(request, 'mainapp/show_academic.html',
    {"academic": academic})

def show_financial(request, financial_id):
    financial = Financial.objects.get(pk=financial_id)
    return render(request, 'mainapp/show_financial.html',
    {"financial": financial})


# Add Functions....

def add_student(request):
    submitted = False
    if request.method == "POST":
        student_form = StudentForm(request.POST)
        if student_form.is_valid():
            student_form.save()
            return HttpResponseRedirect('/add_student?submitted=True')
    else:
        student_form = StudentForm   
        if 'submitted' in request.GET:
            submitted = True
    
    return render(request,'mainapp/add_student.html', 
    {"student_form": student_form, 
    "submitted": submitted})

def add_result(request):
    submitted = False
    if request.method == "POST":
        result_form = ResultForm(request.POST)
        if result_form.is_valid:
            result_form.save()
            return HttpResponseRedirect('/add_result?submitted=True')
    else:
        result_form = ResultForm    
        if 'submitted' in request.GET:
            submitted = True
    
    return render(request,'mainapp/add_result.html', 
    {"submitted": submitted, 
    "result_form": result_form})

def add_financial(request):
    submitted = False
    if request.method == "POST":
        financial_form = FinancialForm(request.POST)
        if financial_form.is_valid:
            financial_form.save()
            return HttpResponseRedirect('/add_financial?submitted=True')
    else:
        financial_form = FinancialForm    
        if 'submitted' in request.GET:
            submitted = True
    
    return render(request,'mainapp/add_financial.html', 
    {"submitted": submitted, 
    "financial_form": financial_form})

def add_course(request):
    submitted = False
    if request.method == "POST":
        course_form = CourseForm(request.POST)
        if course_form.is_valid:
            course_form.save()
            return HttpResponseRedirect('/add_course?submitted=True')
    else:
        course_form = CourseForm    
        if 'submitted' in request.GET:
            submitted = True
    
    return render(request,'mainapp/add_course.html', 
    {"submitted": submitted, 
    "course_form": course_form})

def add_customer(request):
    submitted = False
    if request.method == "POST":
        customer_form = CustomerForm(request.POST)
        if customer_form.is_valid():
            customer_form.save()
            return HttpResponseRedirect('/add_customer?submitted=True')
    else:
        customer_form = CustomerForm   
        if 'submitted' in request.GET:
            submitted = True
    
    return render(request,'mainapp/add_customer.html', 
    {"customer_form": customer_form, 
    "submitted": submitted})


#Update Functions....

def update_customer(request, customer_id):
    customer = Customer.objects.get(pk=customer_id)
    form = CustomerForm(request.POST or None, instance= customer)
    if form.is_valid():
        form.save()
        return redirect('list_customers')
    return render(request, 'mainapp/update_customer.html',
    {"customer": customer,
    "form": form,
    })

def customer_access(request):
    submitted = False
    if request.method == "POST":
        customerAccess_form = CustomerAccessForm(request.POST)
        if customerAccess_form.is_valid():
            customerAccess_form.save()
            return HttpResponseRedirect('/customer_access?submitted=True')
    else:
        customerAccess_form = CustomerAccessForm   
        if 'submitted' in request.GET:
            submitted = True
    
    return render(request,'mainapp/customer_access.html', 
    {"customerAccess_form": customerAccess_form, 
    "submitted": submitted})

def update_customerAccess(request, customer_id):
    customer_access = Customer_access.objects.get(pk=customer_id)
    form = CustomerAccessForm(request.POST or None, instance= customer_access)
    if form.is_valid():
        form.save()
        return redirect('list_customers')
    return render(request, 'mainapp/update_customerAccess.html',
    {"customer": customer_access,
    "form": form,
    })


#Delete Functions....

def delete_customer(request, customer_id):
    customer = Customer.objects.get(pk=customer_id)
    customer.delete()
    return redirect('list_customers')


#API ...

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        "Nothing"
    }
    return Response(api_urls)

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def studentApi(request, pk):
    try:
        personal = Student.objects.get(nsu_id=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = studentSerializer(personal, many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def academicApi(request, pk):
    try:
        academic = Result.objects.get(id=pk)
    except Result.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = academicSerializer(academic, many=False)
    return Response(serializer.data)
