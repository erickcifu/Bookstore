from django.db import models

class Libros(models.Model):
    name = models.CharField(max_length=100)
    Fecha_creacion= models.DateTimeField()
    Descripcion = models.TextField()
    def __str__(self):
        return self.name

class Autores(models.Model):
    name = models.CharField(max_length=100)
    Fecha_Nacimiento = models.DateTimeField()
    category = models.ForeignKey(
        Libros, related_name="Libros", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
