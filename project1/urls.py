from django.urls import path
from . import views
from rest_framework import permissions

urlpatterns = [
    path('', views.lista_proyectos, name='lista_proyectos'),
    path('proyecto/<int:proyecto_id>/', views.detalle_proyecto, name='detalle_proyecto'),
    path('proyecto/crear/', views.crear_proyecto, name='crear_proyecto'),
    path('proyecto/editar/<int:proyecto_id>/', views.editar_proyecto, name='editar_proyecto'),
    path('proyecto/borrar/<int:proyecto_id>/', views.borrar_proyecto, name='borrar_proyecto'),
    path('api/proyectos/', views.ProyectoListAPIView.as_view(), name='proyecto-list'),
    path('api/proyectos/auth/', views.ProyectoAuthListAPIView.as_view(), name='proyecto-auth-list'),
    path('api/user/<int:pk>/', views.UserDetailAPIView.as_view(), name='user-detail'),

]