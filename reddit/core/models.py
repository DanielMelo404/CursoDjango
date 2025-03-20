from django.db import models

# Create your models here.
class Discusion(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(null=True,blank=True)
