from django.db import models

class Venta(models.Model):
    nombre_aplicacion = models.CharField(max_length=100)
    id_tienda = models.IntegerField()
    monto_venta = models.FloatField()
    nombre_vista = models.CharField(max_length=100)

    def __str__(self):
        return f"Venta de {self.monto_venta} en la tienda {self.id_tienda}"
