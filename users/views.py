"""Users views."""

# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Exception
from django.db.utils import IntegrityError

# Models
from django.contrib.auth.models import User
from users.models import Profile
from users.models import Process
from users.area import areas
from users.config import *
# Forms
from users.forms import ProfileForm
from matplotlib.path import Path

from django.http import HttpResponse


import socket




def login_view(request):
    """Login view."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('calculate_process')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username and password'})

    return render(request, 'users/login.html')


def signup(request):
    """Sign up view."""
    if request.method == 'POST':

        username = request.POST['username']
        passwd = request.POST['passwd']
        passwd_confirmation = request.POST['passwd_confirmation']

        if passwd != passwd_confirmation:
            return render(request, 'users/signup.html', {'error': 'Password confirmation does not match'})

        try:
            user = User.objects.create_user(username=username, password=passwd)
        except IntegrityError:
            return render(request, 'users/signup.html', {'error': 'Username is already in user'})

        user.email = request.POST['email']
        user.save()

        profile = Profile(user=user)
        profile.save()

        return redirect('login')

    return render(request, 'users/signup.html')

def new(request):
    if request.method == 'POST':
        return render(request, 'users/signup.html')
    else:
        return render(request, 'users/signup.html')

def page(request):
    if request.method == 'GET':
        return render(request, 'index.html')

def info(request):
    if request.method == 'GET':
        return render(request, 'info.html')

def info_construccion(request):
    if request.method == 'GET':
        return render(request, 'info_construccion.html')

@login_required
def stadistic(request):
    print(request.method)
    if request.method == 'GET':
        return render(request, 'stadistic.html')

@login_required
def calculate_process(request):
    if request.method == 'GET':
        return render(request, 'users/weight_calculation.html')

    if request.method == 'POST':
        response = request.POST

        option_floor = response.get('option_floor')
        obersation_floor = response.get('obersation_floor')
        option_wall = response.get('option_wall')
        observation_wall = response.get('observation_wall')
        option_height = response.get('option_height')
        observation_height = response.get('observation_height')
        option_quality = response.get('option_quality')
        obersation_quality = response.get('obersation_quality')
        option_location = response.get('option_location')
        observation_location = response.get('observation_location')
        option_materials = response.get('option_materials')
        observation_materials = response.get('observation_materials')
        option_confined_walls = response.get('option_confined_walls')
        obersation_confined_walls = response.get('obersation_confined_walls')
        option_detail = response.get('option_detail')
        observation_detail = response.get('observation_detail')
        option_mooring = response.get('option_mooring')
        observation_mooring = response.get('observation_mooring')
        option_characteristics = response.get('option_characteristics')
        obersation_characteristics = response.get('obersation_characteristics')
        option_mezzanine = response.get('option_mezzanine')
        observation_mezzanine = response.get('observation_mezzanine')
        option_cover = response.get('option_cover')
        observation_cover = response.get('observation_cover')
        option_base = response.get('option_base')
        obersation_base = response.get('obersation_base')
        option_soil = response.get('option_soil')
        observation_soil = response.get('observation_soil')
        option_environment = response.get('option_environment')
        observation_environment = response.get('observation_environment')

        if (
            not option_confined_walls
            or not option_detail
            or not option_mooring
            or not option_characteristics
            or not option_mezzanine
            or not option_cover
            or not option_floor
            or not option_wall
            or not option_height
            or not option_quality
            or not option_location
            or not option_materials
            or not option_base
            or not option_soil
            or not option_environment
        ):
            return HttpResponse({'Error': 'Missing data'})

        qualification_structural = (
            (
                int(option_confined_walls) +
                int(option_detail) +
                int(option_mooring) +
                int(option_characteristics) +
                int(option_mezzanine) +
                int(option_cover)
            )/6
        )*PORCENT_STRUCTURAL

        qualification_geometry =  (
            (int(option_floor)+ int(option_wall)+ int(option_height))/3
        )*PORCENT_GEOMETRY

        qualification_constructive =  (
            (int(option_quality) + int(option_location) + int(option_materials))/3
        )*PORCENT_CONSTRUCTIVE

        qualification_base = int(option_base)*PORCENT_BASE
        qualification_soil = int(option_soil)*PORCENT_SOIL
        qualification_environment = int(option_environment)*PORCENT_ENVIRONMENT

        vulnerability_result = round(((
            qualification_structural +
            qualification_geometry +
            qualification_constructive +
            qualification_base +
            qualification_soil +
            qualification_environment
        )/2)*100)

        form = ProfileForm(request.POST, request.FILES)
        form.is_valid()
        data = form.cleaned_data

        user = request.user
        val_irregular_long = None
        val_irregular_plant = None

        if data['irregular_plant'] == 'Irregularidad_torsional':
            val_irregular_plant = 0.9
        if data['irregular_plant'] == "Irregularidad_torsional_extrema":
            val_irregular_plant = 0.8
        if data['irregular_plant'] == "Retrocesos_excesivos_en_las_esquinas":
            val_irregular_plant = 0.9
        if data['irregular_plant'] == "Discontinuidades_en_el_diafragma":
            val_irregular_plant = 0.9
        if data['irregular_plant'] == "Desplazamientos_del_plano_de_accion_de_elementos_verticales":
            val_irregular_plant = 0.8
        if data['irregular_plant'] == "Sistemas_no_paralelos":
            val_irregular_plant = 0.9


        if data['irregular_long'] == 'Piso_flexible_(Irregularidad_en_rigidez)':
            val_irregular_long = 0.9
        if data['irregular_long'] == "Piso_flexible_(Irregularidad_extrema_en_rigidez)":
            val_irregular_long = 0.8
        if data['irregular_long'] == "Irregularidad_en_la_distribucion_de_las_masas":
            val_irregular_long = 0.9
        if data['irregular_long'] == "Irregularidad_geometrica":
            val_irregular_long = 0.9
        if data['irregular_long'] == "Desplazamientos_dentro_del_plano_de_accion":
            val_irregular_long = 0.8
        if data['irregular_long'] == "Piso_debil_Discontinuidad_en_la_resistencia":
            val_irregular_long = 0.9
        if data['irregular_long'] == "Piso_debil_Discontinuidad_extrema_en_la_resistencia":
            val_irregular_long = 0.8

        cordenada_x = data['cordenada_x']
        cordenada_y = data['cordenada_y']

        type_suelo = None

        for name_area in areas:
            p = Path(areas[name_area])
            response = p.contains_points([[cordenada_x, cordenada_y]])
            if response:
                type_suelo = name_area

        if not type_suelo:
            return render(
                request,
                'index.html',
                {
                    'message': 'La vivienda no esta en Bogotá',
                    'result': 0,
                    'status': 'error',
                    'process': 1
                }
            )

        fa = None
        fv = None

        if type_suelo =='Cerros':
            fa = 1.35
            fv = 1.3

        if type_suelo == 'Piedemonte_A':
            fa = 1.65
            fv = 2

        if type_suelo == 'Piedemonte_B':
            fa = 1.95
            fv = 1.7

        if type_suelo == 'Piedemonte_C':
            fa = 1.8
            fv = 1.78

        if type_suelo == 'Lacustre_50':
            fa = 1.4
            fv = 2.9

        if type_suelo == 'Lacustre_100':
            fa = 1.3
            fv = 3.2

        if type_suelo == 'Lacustre_200':
            fa = 1.2
            fv = 3.5

        if type_suelo == 'Lacustre_300':
            fa = 1.05
            fv = 2.9

        if type_suelo == 'Lacustre_500':
            fa = 0.95
            fv = 2.7

        if type_suelo == 'Lacustre_Aluvial_200':
            fa = 1.1
            fv = 2.8

        if type_suelo == 'Lacustre_Aluvial_300':
            fa = 1.1
            fv = 2.5

        if type_suelo == 'Aluvial_50':
            fa = 1.35
            fv = 1.8

        if type_suelo == 'Aluvial_100':
            fa = 1.2
            fv = 2.1

        if type_suelo == 'Aluvial_200':
            fa = 1.01
            fv = 2.1

        if type_suelo == 'Aluvial_300':
            fa = 0.95
            fv = 2.1

        process = Process(
            user=user,
            type_construccion=data['type_construccion'],
            type_property=data['type_property'],
            fuerzas_horizontales=data['fuerzas_horizontales'],
            fuerzas_verticales=data['fuerzas_horizontales'],
            picture=data['picture'],
            val_irregular_long=val_irregular_long,
            val_irregular_plant=val_irregular_plant,
            planes=data['planes'],
            floors=data['floors'],
            email=data['email'],
            phone_number=data['phone_number'],
            comments=data['comments'],
            name_owner=data['name_owner'],
            address=data['address'],
            cordenada_x=data['cordenada_x'],
            cordenada_y=data['cordenada_y'],
            type_suelo=type_suelo,
            fa=fa,
            fv=fv
        )

        process.save()

        if vulnerability_result <= 15:
            result = 'Baja'
        elif vulnerability_result <= 35:
            result = 'Media'
        else:
            result = 'Alta!'

        return render(
            request,
            'index.html',
            {
                'message': 'Proceso correcto',
                'result': f'El valor del resultado es {vulnerability_result} lo que indica que la vulnerabilidad es {result}',
                'status': 'success',
                'process': 1
            }
        )


@login_required
def logout_view(request):
    """Logout a user."""
    logout(request)
    return redirect('page')

def weight(request):
    return render(request, 'users/weight_calculation.html')
