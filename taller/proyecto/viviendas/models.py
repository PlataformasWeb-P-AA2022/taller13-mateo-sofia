from django.db import models

# Create your models here.

class Edificio(models.Model):
    opciones_tipos = (
        ('residencial','Residencial'),
        ('comercial','Comercial'),
        )

    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30, choices=opciones_tipos)

    def __str__(self):
        return "%s %s %s %s" % (self.nombre,
                self.direccion,
                self.ciudad,
                self.tipo)

    def obtener_costo_departametos_edificio(self):
        valor = [d.costo_departamento for d in self.departamentos.all()]
        valor = sum(valor)
        return valor

    def obtener_cantidad_cuartos(self):
        valor = [d.num_cuartos for d in self.departamentos.all()]
        valor = sum(valor)
        return valor


class Departamento(models.Model):
    nombre_propietario = models.CharField(max_length=100)
    costo_departamento = models.IntegerField('costo departamento')
    num_cuartos = models.IntegerField('numero de cuartos')
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE,
            related_name="departamentos")

    def __str__(self):
        return "%s %s %d" % (self.nombre_propietario,
         self.costo_departamento,self.num_cuartos)
