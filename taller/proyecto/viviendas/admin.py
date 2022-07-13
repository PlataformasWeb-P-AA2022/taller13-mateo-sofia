from django.contrib import admin
from viviendas.models import Edificio, Departamento

class EdificioAdmin(admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str) 
    # de la clase 
    list_display = ('nombre', 'direccion', 'ciudad', 'tipo')
    search_fields = ('nombre', 'direccion', 'ciudad')


admin.site.register(Edificio, EdificioAdmin)

class DepartamentoAdmin(admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str) 
    # de la clase 
    list_display = ('nombre_propietario', 'costo_departamento', 'num_cuartos' ,'edificio')
    # se agrega el atributo 
    # raw_id_fields que permite acceder a una interfaz 
    # para buscar los estudiantes y seleccionar el que 
    # se desee
    raw_id_fields = ('edificio',)

admin.site.register(Departamento, DepartamentoAdmin)
