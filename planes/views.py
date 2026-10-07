from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import PlanEntrenamiento
from .forms import PlanForm


def inicio(request):
    """Página principal con estadísticas."""
    total = PlanEntrenamiento.objects.count()
    activos = PlanEntrenamiento.objects.filter(activo=True).count()
    return render(request, 'planes/inicio.html', {
        'total': total,
        'activos': activos,
    })


def lista(request):
    """Listado de todos los planes."""
    planes = PlanEntrenamiento.objects.all()
    return render(request, 'planes/lista.html', {'planes': planes})


def crear(request):
    """Formulario para crear un plan nuevo."""
    if request.method == 'POST':
        form = PlanForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Plan creado correctamente.")
            return redirect('planes:lista')
    else:
        form = PlanForm()
    return render(request, 'planes/crear.html', {'form': form})


def editar(request, pk):
    """Formulario para editar un plan existente."""
    plan = get_object_or_404(PlanEntrenamiento, pk=pk)
    if request.method == 'POST':
        form = PlanForm(request.POST, instance=plan)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Plan actualizado correctamente.")
            return redirect('planes:lista')
    else:
        form = PlanForm(instance=plan)
    return render(request, 'planes/editar.html', {'form': form, 'plan': plan})


def eliminar(request, pk):
    """Confirmación y eliminación de un plan."""
    plan = get_object_or_404(PlanEntrenamiento, pk=pk)
    if request.method == 'POST':
        plan.delete()
        messages.success(request, "🗑️ Plan eliminado correctamente.")
        return redirect('planes:lista')
    return render(request, 'planes/eliminar.html', {'plan': plan})