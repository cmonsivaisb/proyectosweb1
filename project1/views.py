from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from .models import Proyecto
from .forms import ProyectoForm
from rest_framework import generics,permissions
from project1.serializers import ProyectoSerializer
from project1.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User


class ProyectoListAPIView(generics.ListAPIView):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer
    permission_classes = [permissions.AllowAny]  # No requiere autenticación

class ProyectoAuthListAPIView(generics.ListAPIView):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer
    permission_classes = [IsAuthenticated]  # Requiere autenticación

class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

def lista_proyectos(request):
    """
    Vista para mostrar una lista de proyectos.

    Args:
        request (HttpRequest): La solicitud HTTP.

    Returns:
        HttpResponse: La respuesta HTTP que muestra la lista de proyectos.
    """
    proyectos = Proyecto.objects.all()
    return render(request, 'proyectos/lista_proyectos.html', {'proyectos': proyectos})

def detalle_proyecto(request, proyecto_id):
    """
    Vista para mostrar detalles de un proyecto.

    Args:
        request (HttpRequest): La solicitud HTTP.
        proyecto_id (int): El ID del proyecto a mostrar.

    Returns:
        HttpResponse: La respuesta HTTP que muestra los detalles del proyecto.
    """
    proyecto = get_object_or_404(Proyecto, pk=proyecto_id)
    return render(request, 'proyectos/detalle_proyecto.html', {'proyecto': proyecto})

@staff_member_required
def crear_proyecto(request):
    """
    Vista para crear un nuevo proyecto (solo para administradores).

    Args:
        request (HttpRequest): La solicitud HTTP.

    Returns:
        HttpResponse: La respuesta HTTP que muestra el formulario de creación de proyectos.
    """
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_proyectos')
    else:
        form = ProyectoForm()
    return render(request, 'proyectos/crear_proyecto.html', {'form': form})

@staff_member_required
def editar_proyecto(request, proyecto_id):
    """
    Vista para editar un proyecto existente (solo para administradores).

    Args:
        request (HttpRequest): La solicitud HTTP.
        proyecto_id (int): El ID del proyecto a editar.

    Returns:
        HttpResponse: La respuesta HTTP que muestra el formulario de edición de proyectos.
    """
    proyecto = get_object_or_404(Proyecto, pk=proyecto_id)
    if request.method == 'POST':
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            return redirect('lista_proyectos')
    else:
        form = ProyectoForm(instance=proyecto)
    return render(request, 'proyectos/editar_proyecto.html', {'form': form, 'proyecto': proyecto})

@staff_member_required
def borrar_proyecto(request, proyecto_id):
    """
    Vista para confirmar la eliminación de un proyecto (solo para administradores).

    Args:
        request (HttpRequest): La solicitud HTTP.
        proyecto_id (int): El ID del proyecto a eliminar.

    Returns:
        HttpResponse: La respuesta HTTP que muestra la confirmación de eliminación.
    """
    proyecto = get_object_or_404(Proyecto, pk=proyecto_id)
    if request.method == 'POST':
        proyecto.delete()
        return redirect('lista_proyectos')
    return render(request, 'proyectos/borrar_proyecto.html', {'proyecto': proyecto})

