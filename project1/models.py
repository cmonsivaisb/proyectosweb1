from django.db import models

class Proyecto(models.Model):
    """
    Representa un proyecto en la base de datos.

    Attributes:
        nombre (str): El nombre del proyecto.
        project_manager (str): El nombre del project manager.
        descripcion (str): La descripción del proyecto.
        desarrolladores (ManyToManyField): Relación con los desarrolladores involucrados en el proyecto.
    """
    nombre = models.CharField(max_length=100)
    project_manager = models.CharField(max_length=100)
    descripcion = models.TextField()
    desarrolladores = models.ManyToManyField('Desarrollador', blank=True)

    def __str__(self):
        """
        Retorna una representación legible en cadena del objeto Proyecto.

        Returns:
            str: Una cadena con el nombre del proyecto.
        """
        return self.nombre

class Desarrollador(models.Model):
    """
    Representa un desarrollador en la base de datos.

    Attributes:
        nombre (str): El nombre del desarrollador.
        apellido (str): El apellido del desarrollador.
    """
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    def __str__(self):
        """
        Retorna una representación legible en cadena del objeto Desarrollador.

        Returns:
            str: Una cadena con el nombre y apellido del desarrollador.
        """
        return f'{self.nombre} {self.apellido}'
