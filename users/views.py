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
# Forms
from users.forms import ProfileForm
from geopy.geocoders import Nominatim
from matplotlib.path import Path

from googlemaps import Client as GoogleMaps
from django.http import HttpResponse


import socket



@login_required
def update_profile(request):
    """Update a user's profile view."""
    profile = request.user

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        data = form.cleaned_data
        if form.is_valid():
            data = form.cleaned_data
            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()

            return redirect('update_profile')

    else:
        form = ProfileForm()

    return render(
        request=request,
        template_name='users/update_profile.html',
        context={
            'profile': profile,
            'user': request.user,
            'form': form,
            'lat': 4.715757,
            'long': -74.1095727
        }
    )


def login_view(request):
    """Login view."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('update_profile')
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

def calculate_address(request):

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        print(form.is_valid())
        data = form.cleaned_data
        print(data)
        if form.is_valid():
            print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
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
                return render(request, 'users/finish.html', {'message': 'La vivienda no esta en Bogotá', 'status': 'error'})

            print(type_suelo)

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
            print(fa, fv)
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
            print(process)
            return render(request, 'users/finish.html', {'message': 'Proceso correcto', 'status': 'success'})


    #     geolocator = Nominatim(user_agent="users")
    #     location = geolocator.geocode(request.POST['address'])
    #     if location:
    #         print('7777777777777777777777777777777777777777777777')
    #         print(a,b)
    #         a = location.latitude
    #         b = location.longitude
    #         return render(request, 'users/update_profile.html', {'lat': a, 'long': b})
    #     return render(request, 'users/update_profile.html', {'error': 'No se pudo encontrar la direccion'})

    # else:
    #     return render(request, 'users/update_profile.html', {'error': 'No se pudo encontrar la direccion'})

@login_required
def logout_view(request):
    """Logout a user."""
    logout(request)
    return redirect('login')
