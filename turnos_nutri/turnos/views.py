from datetime import date
from .models import Paciente
from django.shortcuts import render
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Turno, HistorialClinico, PerfilProfesional
from django.contrib.admin.views.decorators import staff_member_required
from .forms import TurnoForm, HistorialClinicoForm, PerfilProfesionalForm
Paciente = get_user_model()


# Create your views here.
def home(request):
    return render(request, 'home.html')


""" Login """
@login_required
def agendar_turno(request):
    if request.method == 'POST':
        form = TurnoForm(request.POST)
        if form.is_valid():
            turno = form.save(commit=False)
            turno.nombre = request.user.get_full_name()
            turno.correo = request.user.email
            turno.save()
            return redirect('confirmacion')
    else:
        form = TurnoForm()
    return render(request, 'agendar_turno.html', {'form': form})


def confirmacion(request):
    return render(request, 'confirmacion.html')


""" Paciente """
def nuevo_paciente(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        contacto = request.POST.get('contacto')
        motivo = request.POST.get('motivo', '')
        mensaje = f"Nuevo paciente:\nNombre: {nombre}\nContacto: {contacto}\nMotivo: {motivo}"

        send_mail(
            'Nuevo paciente desde la web',
            mensaje,
            'prueba.proyectos.lopa@gmail.com',  # Remitente
            ['martu6lopardo@gmail.com'],  # Destinatario
        )

        return render(request, 'confirmacion.html', {
            'mensaje': 'Gracias por tu interés. En breve recibirás una respuesta para agendar tu primer turno.'
        })

    return render(request, 'nuevo_paciente.html')


""" Turnos"""
@login_required

def listar_turnos(request):
    # Mostrar todos los turnos del usuario logueado
    turnos = request.user.turno_set.all()  # Asumiendo relación inversa
    return render(request, 'profesional/listar_pacientes.html', {'pacientes': turnos})


def turnos(request):
    turnos = Turno.objects.all().order_by('fecha', 'hora')
    form = TurnoForm()
    if request.method == 'POST':
        form = TurnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('turnos')
    return render(request, 'clinica/turnos.html', {'turnos': turnos, 'form': form})


""" Vista profesional """
@staff_member_required
def vista_profesional(request):
    turnos = Turno.objects.all()
    return render(request, 'profesional/listar_turnos.html', {'turnos': turnos})


def perfil_profesional(request):
    perfil, created = PerfilProfesional.objects.get_or_create(id=1)
    if request.method == 'POST':
        form = PerfilProfesionalForm(request.POST, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('perfil_profesional')
    else:
        form = PerfilProfesionalForm(instance=perfil)
    return render(request, 'clinica/perfil_profesional.html', {'form': form})


@staff_member_required
def dashboard_profesional(request):
    # Obtener fecha actual
    hoy = date.today()

    turnos_hoy = Turno.objects.filter(fecha=hoy).order_by('fecha')

    return render(request, 'profesional/dashboard.html', {'turnos_hoy': turnos_hoy})


@staff_member_required
def listar_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'profesional/listar_pacientes.html', {'pacientes': pacientes})


@staff_member_required
def historial_paciente(request, paciente_id):
    paciente = Paciente.objects.get(id=paciente_id)
    turnos = paciente.turno_set.all()
    return render(request, 'profesional/historial_paciente.html', {'paciente': paciente, 'turnos': turnos})


def historial_clinico(request):
    historiales = HistorialClinico.objects.all().order_by('-fecha')
    form = HistorialClinicoForm()
    if request.method == 'POST':
        form = HistorialClinicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('historial_clinico')
    return render(request, 'clinica/historial_clinico.html', {'historiales': historiales, 'form': form})


@staff_member_required
def crear_paciente(request):
    Paciente = get_user_model()
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        password = request.POST.get('password') or '123456'

        paciente = Paciente.objects.create_user(username=email, email=email, password=password, first_name=nombre)
        
        return redirect('listar_pacientes')
    
    return render(request, 'profesional/crear_paciente.html')