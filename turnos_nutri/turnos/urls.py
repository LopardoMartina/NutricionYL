from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('agendar/', views.agendar_turno, name='agendar_turno'),
    path('confirmacion/', views.confirmacion, name='confirmacion'),
]
