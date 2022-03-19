from .import views
from django.urls import path, include

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('login', views.login_admin, name='login' ),
    path('logout', views.logout_admin, name = 'logout'),
    path('register_user', views.register_user, name='register_user'),
]
