"""dringo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include

from dringo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('einloggen/', views.login_request, name="login"),
    path('ausloggen/', views.logout_request, name="logout"),
    path('new/', views.new_case, name="new_case"),
    path('', views.home, name="index"),
    path('', include('patient.urls')),
    path('', include('role.urls')),
    path('', include('emergency.urls')),
]
