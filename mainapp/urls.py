from django.urls import path
from .import views
from rest_framework.authtoken import views as authviews

urlpatterns = [
    path('', views.home, name="home"),
    path('api-token-auth/', authviews.obtain_auth_token),
    path('api/', views.apiOverview, name="api-overview"),
    path('api/student/<str:pk>', views.studentApi, name="student-api"),
    path('api/academic/<str:pk>', views.academicApi, name="academic-api"),
    path('students', views.all_students, name="list_students"),
    path('show_student/<student_id>', views.show_student, name="show_student"),
    path('show_academic/<academic_id>', views.show_academic, name="show_academic"),
    path('show_financial/<financial_id>', views.show_financial, name="show_financial"),
    path('customers', views.all_customers, name="list_customers"),
    path('add_student', views.add_student, name="add-student"),
    path('add_result', views.add_result, name="add_result"),
    path('add_course', views.add_course, name="add_course"),
    path('add_financial', views.add_financial, name="add_financial"),
    path('add_customer', views.add_customer, name="add_customer"),
    path('customer_access', views.customer_access, name="customer_access"),
    path('show_customer/<customer_id>', views.show_customer, name="show_customer"),
    path('update_customer/<customer_id>', views.update_customer, name="update_customer"),
    path('delete_customer/<customer_id>', views.delete_customer, name="delete_customer"),
    path('update_customerAccess/<customer_id>', views.update_customerAccess, name="update_customerAccess"),
]