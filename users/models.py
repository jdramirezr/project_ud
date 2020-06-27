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
    Width_x_placa = models.IntegerField(blank=True, null=True)
    Width_y_placa = models.IntegerField(blank=True, null=True)
    thickness_placa = models.IntegerField(blank=True, null=True)
    ancho_viga = models.IntegerField(blank=True, null=True)
    alto_viga = models.IntegerField(blank=True, null=True)
    largo_viga = models.IntegerField(blank=True, null=True)
    numero_viga = models.IntegerField(blank=True, null=True)
    ancho_columna = models.IntegerField(blank=True, null=True)
    alto_columna = models.IntegerField(blank=True, null=True)
    largo_columna = models.IntegerField(blank=True, null=True)
    numero_columna = models.IntegerField(blank=True, null=True)
    cordenada_x = models.IntegerField(blank=True, null=True)
    cordenada_y = models.IntegerField(blank=True, null=True)
    type_suelo=models.CharField(max_length=200)
    fa=models.IntegerField(blank=True, null=True)
    fv=models.IntegerField(blank=True, null=True)

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
