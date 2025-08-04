from django import forms
from .models import Turno, HistorialClinico, PerfilProfesional


class TurnoForm(forms.ModelForm):
    class Meta:
        model = Turno
        fields = ['paciente', 'fecha', 'hora', 'tipo_consulta', 'notas']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time'}),
            'notas': forms.Textarea(attrs={'rows': '3'}),
        }


class HistorialClinicoForm(forms.ModelForm):
    class Meta:
        model = HistorialClinico
        fields = ['paciente', 'fecha', 'tipo_consulta', 'notas']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'tipo_consulta': forms.Textarea(attrs={'rows': 2}),
            'notas': forms.Textarea(attrs={'rows': 4}),
        }

class PerfilProfesionalForm(forms.ModelForm):
    class Meta:
        model = PerfilProfesional
        fields = [
            'nombre_completo', 'especialidad', 'email', 'telefono',
            'horario_semana_inicio', 'horario_semana_fin',
            'horario_sabado_inicio', 'horario_sabado_fin',
        ]
        widgets = {
            'horario_semana_inicio': forms.TimeInput(attrs={'type': 'time'}),
            'horario_semana_fin': forms.TimeInput(attrs={'type': 'time'}),
            'horario_sabado_inicio': forms.TimeInput(attrs={'type': 'time'}),
            'horario_sabado_fin': forms.TimeInput(attrs={'type': 'time'}),
        }
        