"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from demo import views

urlpatterns = [
    path('', views.index),
    path('chat_gpt/', views.chat_gpt),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('p1/', views.p1_view, name='p1'),
    path('p2/', views.p2_view, name='p2'),
    path('p3/', views.p3_view, name='p3'),
    path('p4/', views.p4_view, name='p4'),


]
