"""Users models."""

# Django
from django.contrib.auth.models import User
from django.db import models


class Process(models.Model):
    user = models.CharField(max_length=500)
    name_owner = models.CharField(max_length=200)
    comments = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=20)
    picture = models.ImageField(blank=True, null=True)
    planes = models.ImageField(blank=True, null=True)
    fuerzas_horizontales = models.CharField(max_length=200)
    fuerzas_verticales = models.IntegerField(blank=True, null=True)
    value_type_construccion = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=500)
    type_construccion = models.CharField(max_length=200)
    type_property = models.IntegerField(blank=True, null=True)
    irregular_long = models.CharField(max_length=200)
    irregular_plant = models.CharField(max_length=200)
    val_irregular_long = models.IntegerField(blank=True, null=True)
    val_irregular_plant = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    floors = models.IntegerField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    height_floors = models.IntegerField(blank=True, null=True)


    cordenada_x = models.IntegerField(blank=True, null=True)
    cordenada_y = models.IntegerField(blank=True, null=True)
    type_suelo=models.CharField(max_length=200)


    viga_weight=models.IntegerField(blank=True, null=True)
    columna_weight=models.IntegerField(blank=True, null=True)
    placa_weight=models.IntegerField(blank=True, null=True)
    cubierta_weight=models.IntegerField(blank=True, null=True)
    piso_weight=models.IntegerField(blank=True, null=True)
    recubrimiento_weight=models.IntegerField(blank=True, null=True)
    weight_muro=models.IntegerField(blank=True, null=True)
    weight_divisorio=models.IntegerField(blank=True, null=True)
    enchape_weight=models.IntegerField(blank=True, null=True)
    ocupacion_weight=models.IntegerField(blank=True, null=True)
    cubierta_viva_weight=models.IntegerField(blank=True, null=True)
    weight_particiones=models.IntegerField(blank=True, null=True)
    weight_ventanas=models.IntegerField(blank=True, null=True)
    fa=models.IntegerField(blank=True, null=True)
    fv=models.IntegerField(blank=True, null=True)
    Espesor_deposito=models.CharField(max_length=200, blank=True, null=True)
    Periodo_suelo=models.CharField(max_length=200, blank=True, null=True)
    descripcion_geotecnica=models.CharField(max_length=200, blank=True, null=True)
    velocidad_onda=models.CharField(max_length=200, blank=True, null=True)
    Humedad_Promedio=models.CharField(max_length=200, blank=True, null=True)
    Efectos_relacionados=models.CharField(max_length=200, blank=True, null=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

class ResultPdf(models.Model):
    process = models.OneToOneField(Process, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    result_pdf = models.TextField()

class AisModel(models.Model):
    option_confined_walls = models.IntegerField()
    option_detail = models.IntegerField()
    option_mooring = models.IntegerField()
    option_characteristics = models.IntegerField()
    option_mezzanine = models.IntegerField()
    option_cover = models.IntegerField()
    option_floor = models.IntegerField()
    option_wall = models.IntegerField()
    option_height = models.IntegerField()
    option_quality = models.IntegerField()
    option_location = models.IntegerField()
    option_materials = models.IntegerField()
    option_base = models.IntegerField()
    option_soil = models.IntegerField()
    option_environment = models.IntegerField()
