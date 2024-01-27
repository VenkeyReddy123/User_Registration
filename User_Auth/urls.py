"""
URL configuration for User_Auth project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app1.views import *
from django.conf.urls.static import static 
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('User_Auth/',User_Auth,name='User_Auth'),
    path('Auther_View/',Auther_View,name='Auther_View'),
    path('HomePage/',HomePage,name='HomePage'),
    path('LoginPage/',LoginPage,name='LoginPage'),
    path('ProfilePage/',ProfilePage,name='ProfilePage'),
    path('LogoutPage/',LogoutPage,name='LogoutPage'),
    path('ChangePassword/',ChangePassword,name='ChangePassword'),
    # path('ResetPassword.html/',ResetPassword,name='ResetPassword.html'),
    path('ResetPasswordPage/',ResetPasswordPage,name='ResetPasswordPage'),
    path('OtpPage/',OtpPage,name='OtpPage')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
