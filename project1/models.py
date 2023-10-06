from django.db import models

class Proyecto(models.Model):
    """
    Representa un proyecto en la base de datos.

    :param nombre: El nombre del proyecto.
    :type nombre: str
    :param project_manager: El nombre del project manager.
    :type project_manager: str
    :param descripcion: La descripción del proyecto.
    :type descripcion: str
    :param desarrolladores: Relación con los desarrolladores involucrados en el proyecto.
    :type desarrolladores: ManyToManyField
    """
    nombre = models.CharField(max_length=100)
    project_manager = models.CharField(max_length=100)
    descripcion = models.TextField()
    desarrolladores = models.ManyToManyField('Desarrollador', blank=True)

    def __str__(self):
        """
        Retorna una representación legible en cadena del objeto Proyecto.

        :return: Una cadena con el nombre del proyecto.
        :rtype: str
        """
        return self.nombre

class Desarrollador(models.Model):
    """
    Representa un desarrollador en la base de datos.

    :param nombre: El nombre del desarrollador.
    :type nombre: str
    :param apellido: El apellido del desarrollador.
    :type apellido: str
    """
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    def __str__(self):
        """
        Retorna una representación legible en cadena del objeto Desarrollador.

        :return: Una cadena con el nombre y apellido del desarrollador.
        :rtype: str
        """
        return f'{self.nombre} {self.apellido}'
