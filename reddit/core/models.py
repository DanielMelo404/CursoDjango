from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Topico(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# Create your models here.
class Discusion(models.Model):
    topico = models.ForeignKey(Topico, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(null=True,blank=True)

    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo
    
class Comentario(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    discusion = models.ForeignKey(Discusion, on_delete=models.CASCADE)
    text = models.TextField(null=False,default=' ')
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.text[0:50]