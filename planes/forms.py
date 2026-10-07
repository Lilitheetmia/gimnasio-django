from django import forms
from .models import PlanEntrenamiento


class PlanForm(forms.ModelForm):
    class Meta:
        model = PlanEntrenamiento
        fields = [
            'nombre', 'descripcion', 'nivel', 'duracion_semanas',
            'precio', 'cupos_disponibles', 'entrenador', 'activo'
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Full Body Principiante'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Describe brevemente el plan...'
            }),
            'nivel': forms.Select(attrs={'class': 'form-select'}),
            'duracion_semanas': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'max': 52
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0.01'
            }),
            'cupos_disponibles': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0,
                'max': 200
            }),
            'entrenador': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del entrenador'
            }),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'nombre': 'Nombre del plan',
            'descripcion': 'Descripción',
            'nivel': 'Nivel',
            'duracion_semanas': 'Duración (semanas)',
            'precio': 'Precio mensual ($)',
            'cupos_disponibles': 'Cupos disponibles',
            'entrenador': 'Entrenador a cargo',
            'activo': '¿Plan activo?',
        }

    # Validaciones personalizadas adicionales
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre', '').strip()
        if len(nombre) < 3:
            raise forms.ValidationError(
                "El nombre debe tener al menos 3 caracteres."
            )
        return nombre

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio is not None and precio <= 0:
            raise forms.ValidationError("El precio debe ser mayor que cero.")
        return precio

    def clean_duracion_semanas(self):
        d = self.cleaned_data.get('duracion_semanas')
        if d is not None and (d < 1 or d > 52):
            raise forms.ValidationError(
                "La duración debe estar entre 1 y 52 semanas."
            )
        return d

    def clean_cupos_disponibles(self):
        c = self.cleaned_data.get('cupos_disponibles')
        if c is not None and c < 0:
            raise forms.ValidationError("Los cupos no pueden ser negativos.")
        return c