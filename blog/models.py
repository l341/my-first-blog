# Agregan algo de otros archivos
from django.db import models
from django.utils import timezone

# Esta linea define nuestro modelo, es un objeto
# class -> se esta definiendo un objeto
# Post -> nombre del modelo (empieza con matuscula)
# models.Model -> indica que Post en un modelo de Django
# para que lo guarde en una base de datos
class Post(models.Model):

    # Relacion (link) con otro modelo
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    # Define texto con un numero limitado de caracteres
    title = models.CharField(max_length=200)

    # Texto sin limite
    text = models.TextField()

    # Fecha y hora
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
