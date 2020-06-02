from django.urls import path
from . import views

app_name = 'apps'

urlpatterns = [
    path('create_application/', views.create_application, name='create_application'),
    path('view_application/', views.view_applications, name='view_application'),
]