from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from .models import Proyecto
from .forms import ProyectoForm
from rest_framework import generics, permissions
from project1.serializers import ProyectoSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User  # Importa la clase User desde el módulo correcto

@login_required
def lista_proyectos(request):
    """
    Vista para mostrar una lista de proyectos.

    :param request: La solicitud HTTP.
    :type request: HttpRequest

    :return: La respuesta HTTP que muestra la lista de proyectos.
    :rtype: HttpResponse
    """
    proyectos = Proyecto.objects.all()
    return render(request, 'proyectos/lista_proyectos.html', {'proyectos': proyectos})

@login_required
def detalle_proyecto(request, proyecto_id):
    """
    Vista para mostrar detalles de un proyecto.

    :param request: La solicitud HTTP.
    :type request: HttpRequest
    :param proyecto_id: El ID del proyecto a mostrar.
    :type proyecto_id: int

    :return: La respuesta HTTP que muestra los detalles del proyecto.
    :rtype: HttpResponse
    """
    proyecto = get_object_or_404(Proyecto, pk=proyecto_id)
    return render(request, 'proyectos/detalle_proyecto.html', {'proyecto': proyecto})

@staff_member_required
def crear_proyecto(request):
    """
    Vista para crear un nuevo proyecto (solo para administradores).

    :param request: La solicitud HTTP.
    :type request: HttpRequest

    :return: La respuesta HTTP que muestra el formulario de creación de proyectos.
    :rtype: HttpResponse
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

    :param request: La solicitud HTTP.
    :type request: HttpRequest
    :param proyecto_id: El ID del proyecto a editar.
    :type proyecto_id: int

    :return: La respuesta HTTP que muestra el formulario de edición de proyectos.
    :rtype: HttpResponse
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

    :param request: La solicitud HTTP.
    :type request: HttpRequest
    :param proyecto_id: El ID del proyecto a eliminar.
    :type proyecto_id: int

    :return: La respuesta HTTP que muestra la confirmación de eliminación.
    :rtype: HttpResponse
    """
    proyecto = get_object_or_404(Proyecto, pk=proyecto_id)
    if request.method == 'POST':
        proyecto.delete()
        return redirect('lista_proyectos')
    return render(request, 'proyectos/borrar_proyecto.html', {'proyecto': proyecto})

class ProyectoListAPIView(generics.ListAPIView):
    """
    Vista de API para listar proyectos (sin autenticación).

    :param generics: Clase genérica de la API.
    :type generics: generics.ListAPIView
    """
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer
    permission_classes = [permissions.AllowAny]

class ProyectoAuthListAPIView(generics.ListAPIView):
    """
    Vista de API para listar proyectos (requiere autenticación).

    :param generics: Clase genérica de la API.
    :type generics: generics.ListAPIView
    """
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer
    permission_classes = [IsAuthenticated]

class UserDetailAPIView(generics.RetrieveAPIView):
    """
    Vista de API para obtener detalles de usuario (requiere autenticación).

    :param generics: Clase genérica de la API.
    :type generics: generics.RetrieveAPIView
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
