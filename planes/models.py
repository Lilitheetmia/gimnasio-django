from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError


class PlanEntrenamiento(models.Model):
    NIVELES = [
        ('principiante', 'Principiante'),
        ('intermedio', 'Intermedio'),
        ('avanzado', 'Avanzado'),
    ]

    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre del plan")
    descripcion = models.TextField(max_length=500, verbose_name="Descripción")
    nivel = models.CharField(max_length=20, choices=NIVELES, default='principiante')
    duracion_semanas = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(52)],
        verbose_name="Duración (semanas)"
    )
    precio = models.DecimalField(
        max_digits=8, decimal_places=2,
        validators=[MinValueValidator(0.01)],
        verbose_name="Precio mensual"
    )
    cupos_disponibles = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(200)],
        verbose_name="Cupos disponibles"
    )
    entrenador = models.CharField(max_length=80, verbose_name="Entrenador a cargo")
    activo = models.BooleanField(default=True, verbose_name="¿Activo?")
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Plan de Entrenamiento"
        verbose_name_plural = "Planes de Entrenamiento"
        ordering = ['-creado_en']

    def __str__(self):
        return f"{self.nombre} ({self.get_nivel_display()})"

    def clean(self):
        if self.precio is not None and self.precio <= 0:
            raise ValidationError({'precio': 'El precio debe ser mayor a cero.'})
        if self.cupos_disponibles is not None and self.cupos_disponibles < 0:
            raise ValidationError({'cupos_disponibles': 'Los cupos no pueden ser negativos.'})