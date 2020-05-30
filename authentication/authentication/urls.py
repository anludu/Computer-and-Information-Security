"""authentication URL Configuration

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
from django.conf.urls import url
from django.template.backends import django
from django.urls import path, include
from two_factor.urls import urlpatterns as tf

from django_otp.admin import OTPAdminSite


class OTPAdmin(OTPAdminSite):
    pass


from django.contrib import admin
from django.contrib.auth.models import User

from django_otp.plugins.otp_totp.models import TOTPDevice
from two_factor.admin import AdminSiteOTPRequired

admin_site = OTPAdmin(name='OTPAdmin')
admin_site.register(User)
admin_site.register(TOTPDevice)

urlpatterns = [

    url(r'^admin/', admin_site.urls),
    url(r'^dadmin/', admin.site.urls),
    path(r'', include(tf)),
]
