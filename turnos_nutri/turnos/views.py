from .models import Turno
from .forms import TurnoForm
from django.shortcuts import render
from django.shortcuts import redirect



# Create your views here.
def home(request):
    return render(request, 'home.html')


def agendar_turno(request):
    if request.method == 'POST':
        form = TurnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('confirmacion')
            #return render(request, 'turnos/turno_agendado.html', {'form': form})
    else:
        form = TurnoForm()
    return render(request, 'agendar_turno.html', {'form': form})


def confirmacion(request):
    return render(request, 'confirmacion.html')
