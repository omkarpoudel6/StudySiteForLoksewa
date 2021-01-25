"""LoksewaPrepProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
# from Loksewa.views import test,questions,category
from Loksewa import views
from Users.views import Login,Signup,Logout,Home

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/',Login,name='login'),
    path('signup/',Signup,name='signup'),
    path('logout/',Logout,name='logout'),

    path('',Home,name='home'),

    path('test/',views.test,name='test'),
    path('questions/',views.questions,name='questions'),
    path('category/<int:id>/',views.category,name='category')
]
