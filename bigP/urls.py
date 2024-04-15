"""bigP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.show,name='main'),
    path('studentlogin/',views.slogin,name='slogin'),
    path('StudentRegister/',views.sregester,name='sregester'),
    path('forgetPassword/',views.forgetpassword,name='forget'),
    path('AdminLogin/',views.admin,name='admin'),
    path('Register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.slogout,name='slogout'),
    path('viewprofile/',views.viewprofile,name='viewprofile'),
    path('smodify/',views.smodify,name='smodify'),
    path('Supdate/',views.update,name='update'),
    path('updatepassword/',views.password,name='fp'),
    path('adminlogin/',views.adlogin,name='adlogin'),
    path('adminlogout/',views.alogout,name='alogout'),
    path('viewdeatils/',views.viewdeatils,name='viewdeatils'),
    path('adminhome/',views.adhome,name='adhome'),
    path('deletestudent/',views.sdelete,name='ds'),
    path('delete/',views.delete,name='delete'),
    path('app3/', include('app3.urls'))
]
