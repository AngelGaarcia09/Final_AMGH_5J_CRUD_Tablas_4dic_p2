from django.db import models

# Create your models here.
class Troca(models.Model):
    color = models.CharField(max_length=100)
    id_troca=models.PositiveIntegerField(primary_key=True)
    año=models.PositiveIntegerField()
    modelo=models.CharField(max_length=50)
    marca=models.CharField(max_length=50)
    precio=models.DecimalField(max_digits=10, decimal_places=2)
    tipo_llantas=models.CharField(max_length=100)
    id_sucursal=models.IntegerField(default=1)

    def __str__(self):
        return self.modelo