"""User forms."""

# Django
from django import forms


class ProfileForm(forms.Form):
    """Profile form."""

    name_owner = forms.CharField(max_length=200, required=False)
    comments = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField(required=False)
    planes = forms.ImageField(required=False)
    address = forms.CharField(max_length=500, required=False)
    height_floors = forms.FloatField(required=False)
    Width_x_placa = forms.FloatField(required=False)
    Width_y_placa = forms.FloatField(required=False)
    thickness_placa = forms.FloatField(required=False)
    ancho_viga = forms.FloatField(required=False)
    alto_viga = forms.FloatField(required=False)
    largo_viga = forms.FloatField(required=False)
    numero_viga = forms.IntegerField(required=False)
    ancho_columna = forms.FloatField(required=False)
    alto_columna = forms.FloatField(required=False)
    largo_columna = forms.FloatField(required=False)
    numero_columna = forms.IntegerField(required=False)
    type_construccion = forms.CharField(max_length=200, required=False)
    fuerzas_horizontales = forms.CharField(max_length=200, required=False)
    fuerzas_verticales = forms.FloatField(required=False)
    type_property = forms.FloatField(required=False)
    irregular_long = forms.CharField(max_length=500, required=False)
    irregular_plant = forms.CharField(max_length=500, required=False)
    floors = forms.IntegerField(required=False)
    email = forms.EmailField(required=False)
    cordenada_x = forms.FloatField(required=False)
    cordenada_y = forms.FloatField(required=False)


class IndiceForm(forms.Form):
    organization = forms.IntegerField()
    quality = forms.IntegerField()
    number_of_floors = forms.IntegerField()
    cover_area = forms.FloatField()
    area_x = forms.FloatField()
    area_y = forms.FloatField()
    height = forms.FloatField()
    diaphragm_thickness = forms.FloatField()
    position = forms.IntegerField()
    diaphragm = forms.IntegerField()
    a = forms.FloatField()
    b = forms.FloatField()
    L = forms.FloatField()
    area_floor_1 = forms.FloatField(required=False)
    area_floor_2 = forms.FloatField(required=False)
    area_floor_3 = forms.FloatField(required=False)
    area_floor_4 = forms.FloatField(required=False)
    area_floor_5 = forms.FloatField(required=False)
    wall_length = forms.FloatField()
    wall_thickness = forms.FloatField()
    cover_type = forms.IntegerField()
    elements = forms.IntegerField()
    status_conservation = forms.IntegerField()
    mamposteria = forms.FloatField()