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

