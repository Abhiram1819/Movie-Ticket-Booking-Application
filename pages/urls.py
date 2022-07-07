from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('register',views.register, name='register'),
    path('login',views.login, name='login'),
    path('home',views.home,name='home'),
    path('logout', views.logout, name= 'logout'),
    path('admin_login', views.admin_login, name='admin_login'),
    path('admin_page', views.admin_page, name='admin_page'),
]