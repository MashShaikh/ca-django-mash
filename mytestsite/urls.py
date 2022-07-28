"""mytestsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from WebApp import views
from django.contrib.auth import views as authentication_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.user,name='user'),
    path('<int:id>/',views.cv,name='cv'),
    path('list/',views.userList,name='list'),
    path('register/',views.register,name='register'),
    path('login/',authentication_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',authentication_views.LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('delete/<str:id>/', views.delete,name='delete'),
    path('profile/',views.profilepage,name='profile'),
]
    