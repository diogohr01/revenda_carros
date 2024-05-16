from django.db import models

# Create your models here.
class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=255)
    '''on_delete, ele protege os carros se acontecer de deletar a categoria'''
    '''related_name, ele coloca um nome na relação do carro com a marca(brand)'''
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    plate = models.CharField(max_length=10, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)
    
    
    '''Aqui eu puxei o objeto para buscar o nome do carro lançando no self.model'''
    def __str__(self):
        return self.model
    
 