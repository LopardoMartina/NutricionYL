from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 

    # paciente
    path('agendar/', views.agendar_turno, name='agendar_turno'),
    path('confirmacion/', views.confirmacion, name='confirmacion'),
    path('nuevo_paciente/', views.nuevo_paciente, name='nuevo_paciente'),

    path('mis-turnos/', views.listar_turnos, name='listar_turnos'),
    
    # profesional
    path('profesional/', views.vista_profesional, name='vista_profesional'),
    path('profesional/dashboard/', views.dashboard_profesional, name='dashboard_profesional'),
    path('profesional/pacientes/', views.listar_pacientes, name='listar_pacientes'),
    path('profesional/pacientes/<int:paciente_id>/', views.historial_paciente, name='historial_paciente'),
    path('profesional/crear-paciente/', views.crear_paciente, name='crear_paciente'),

    # Para iniciar seccion
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
