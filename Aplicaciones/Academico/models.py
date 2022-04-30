from statistics import mode
from django.db import models

# Create your models here.
#compone un patone d aquitectua es una clase en django y ataves del 
# 	orm  nos pemite inteectua ataves del paadigma PO
class Curso(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=25)
    notas = models.PositiveSmallIntegerField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.notas) #ahoa vamos a cea una vista