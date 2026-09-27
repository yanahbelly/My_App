from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('appointment/', views.appointments_page, name='appointments'),
    path('support/', views.support_page, name='support'),
]