from django.db import models

class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self): #mostrar nome da cidade 
        return self.name

    class Meta: #mostrar "cidade" no plural
        verbose_name_plural = 'cities'