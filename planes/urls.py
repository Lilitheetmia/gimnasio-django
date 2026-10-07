from django.urls import path
from . import views

app_name = 'planes'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('planes/', views.lista, name='lista'),
    path('planes/crear/', views.crear, name='crear'),
    path('planes/editar/<int:pk>/', views.editar, name='editar'),
    path('planes/eliminar/<int:pk>/', views.eliminar, name='eliminar'),
]