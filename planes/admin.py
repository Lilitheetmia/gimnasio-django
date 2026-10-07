from django.contrib import admin
from .models import PlanEntrenamiento


@admin.register(PlanEntrenamiento)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nivel', 'precio', 'cupos_disponibles', 'entrenador', 'activo')
    list_filter = ('nivel', 'activo')
    search_fields = ('nombre', 'entrenador')