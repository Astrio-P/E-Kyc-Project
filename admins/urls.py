from .import views
from django.urls import path, include

urlpatterns = [
    path('login_admin', views.login_admin, name='login' ),
    path('logout_admin', views.logout_admin, name = 'logout')
]
