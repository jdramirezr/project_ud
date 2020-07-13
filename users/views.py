"""Users views."""

# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import FileResponse
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from reportlab.pdfgen import canvas
from werkzeug import FileWrapper

import io
from io import BytesIO
# Exception
from django.db.utils import IntegrityError

# Models
from django.contrib.auth.models import User
from users.models import ResultPdf, Profile, AisModel
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
        return render(request, 'video.html')

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

        response_weight = dict(response.lists())

        type_placa = response_weight.get('type_placa')
        placa_x = response_weight.get('placa_x')
        placa_y = response_weight.get('placa_y')

        plate_weight = []

        if 'Placa_Maciza' in type_placa:
            placa_z = response_weight.get('placa_z')

        if 'Placa_Aligerada' in type_placa:
            vg_a = response_weight.get('vg_a')
            vg_b = response_weight.get('vg_b')
            vg_c = response_weight.get('vg_c')
            vg_d = response_weight.get('vg_d')
            vg_e = response_weight.get('vg_e')

        if 'Placa_Facil' in type_placa:
            type_placa_facil = response_weight.get('type_placa_facil')

            if 'Placa' in type_placa_facil:
                z_placa_facil = response_weight.get('z_placa_facil')

            if 'Perfil_Metalico' in type_placa_facil:
                peso_ml_perfil = response_weight.get('peso_ml_perfil')
                ml_perfil = response_weight.get('ml_perfil')

            if 'Bloquelon' in type_placa_facil:
                peso_bloquelon = response_weight.get('peso_bloquelon')


        for placa in type_placa:
            if placa == 'Placa_Maciza':

                plate_weight.append(
                    float(placa_x.pop(0))*float(placa_y.pop(0))
                    *float(placa_z.pop(0))
                    *DENSIDAD*GRAVEDAD
                )

            if placa == 'Placa_Facil':
                placa_facil = type_placa_facil[0]

                if placa_facil == 'Placa':
                    plate_weight.append(
                        float(placa_x.pop(0))*float(placa_y.pop(0))
                        *float(z_placa_facil.pop(0))
                        *DENSIDAD*GRAVEDAD
                    )
                    type_placa_facil.pop(0)

                if placa_facil == 'Perfil_Metalico':
                    plate_weight.append(
                        float(peso_ml_perfil.pop(0))*
                        float(ml_perfil.pop(0))*
                        GRAVEDAD
                    )
                    type_placa_facil.pop(0)

                if placa_facil == 'Bloquelon':
                    plate_weight.append(float(placa_x.pop(0))
                    *float(placa_y.pop(0))*float(peso_bloquelon.pop(0))
                    *GRAVEDAD
                )
                    type_placa_facil.pop(0)

            if placa == 'Placa_Aligerada':
                vg_b_num = float(vg_b.pop(0))
                m2 = float(placa_x.pop(0))*float(placa_y.pop(0))
                vigueta = (vg_b_num*float(vg_c.pop(0))*m2*DENSIDAD*GRAVEDAD)/(
                    float(vg_a.pop(0))+vg_b_num
                )
                placa_superior=(float(vg_d.pop(0))+float(vg_e.pop(0)))*m2*DENSIDAD*GRAVEDAD
                plate_weight.append(vigueta+placa_superior)


        ancho_viga = response_weight.get('ancho_viga')
        alto_viga = response_weight.get('alto_viga')
        largo_viga = response_weight.get('largo_viga')
        numero_viga = response_weight.get('numero_viga')

        plate_weight = plate_weight + [
            float(ancho_viga[num])*
            float(alto_viga[num])*
            float(largo_viga[num])*
            int(numero_viga[num])*
            DENSIDAD*GRAVEDAD
            for num in range(len(numero_viga))
        ]


        ancho_columna = response_weight.get('ancho_columna')
        alto_columna = response_weight.get('alto_columna')
        largo_columna = response_weight.get('largo_columna')
        numero_columna = response_weight.get('numero_columna')

        plate_weight = plate_weight + [
            float(ancho_columna[num])*
            float(alto_columna[num])*
            float(largo_columna[num])*
            int(numero_columna[num])*
            DENSIDAD*GRAVEDAD
            for num in range(len(numero_columna))
        ]

        muro_caracteristica = response_weight.get('muro_caracteristica')
        espesor = response_weight.get('espesor')
        cantidad_muros = response_weight.get('cantidad_muros')
        m2_muros = response_weight.get('m2_muros')

        muro_caracteristica_divisorio = response_weight.get('muro_caracteristica_divisorio')
        espesor_divisorio = response_weight.get('espesor_divisorio')
        cantidad_muros_divisorio = response_weight.get('cantidad_muros_divisorio')
        m2_muros_divisorio = response_weight.get('m2_muros_divisorio')

        type_cubierta = response_weight.get('type_cubierta')
        espesor_cubierta = response_weight.get('espesor_cubierta')
        m2_cubierta = response_weight.get('m2_cubierta')

        type_piso = response_weight.get('type_piso')
        espesor_piso = response_weight.get('espesor_piso')
        m2_pisos = response_weight.get('m2_pisos')

        type_recubrimiento = response_weight.get('type_recubrimiento')
        espesor_recubrimiento = response_weight.get('espesor_recubrimiento')
        m2_recubrimiento = response_weight.get('m2_recubrimiento')

        type_enchape = response_weight.get('type_enchape')
        espesor_enchape = response_weight.get('espesor_enchape')
        m2_enchape = response_weight.get('m2_enchape')

        ocupacion_uso = response_weight.get('ocupacion_uso')
        m2_ocupacion = response_weight.get('m2_ocupacion')

        cubierta_viva = response_weight.get('cubierta_viva')
        m2_cubierta_viva = response_weight.get('m2_cubierta_viva')

        type_particiones = response_weight.get('type_particiones')
        m2_particiones = response_weight.get('m2_particiones')

        type_ventanas = response_weight.get('type_ventanas')
        m2_ventanas = response_weight.get('m2_ventanas')
        print(type_cubierta)
        print(espesor_cubierta)
        if espesor_cubierta:
            cubierta_weight = float(type_cubierta[0])*float(espesor_cubierta[0])*float(m2_cubierta[0])
        else:
            cubierta_weight = float(type_cubierta[0])*float(m2_cubierta[0])

        if espesor_piso:
            piso_weight = float(type_piso[0])*float(espesor_piso[0])*float(m2_pisos[0])
        else:
            piso_weight = float(type_piso[0])*float(m2_pisos[0])

        if espesor_recubrimiento:
            recubrimiento_weight = float(type_recubrimiento[0])*float(espesor_recubrimiento[0])*float(m2_recubrimiento[0])
        else:
            recubrimiento_weight = float(type_recubrimiento[0])*float(m2_recubrimiento[0])

        weight_muro = eval(muro_caracteristica[0])[int(espesor[0])]*int(cantidad_muros[0])*float(m2_muros[0])
        weight_divisorio = eval(muro_caracteristica_divisorio[0])[int(espesor_divisorio[0])]*int(cantidad_muros_divisorio[0])*float(m2_muros_divisorio[0])
        enchape_weight = float(type_enchape[0])*float(espesor_enchape[0])*float(m2_enchape[0])
        ocupacion_weight = float(ocupacion_uso[0])*float(m2_ocupacion[0])
        cubierta_viva_weight = float(cubierta_viva[0])*float(m2_cubierta_viva[0])
        weight_particiones = float(type_particiones[0])*float(m2_particiones[0])
        weight_ventanas = float(type_ventanas[0])*float(m2_ventanas[0])

        plate_weight.append(cubierta_weight)
        plate_weight.append(piso_weight)
        plate_weight.append(recubrimiento_weight)
        plate_weight.append(weight_muro)
        plate_weight.append(weight_divisorio)
        plate_weight.append(enchape_weight)
        plate_weight.append(ocupacion_weight)
        plate_weight.append(cubierta_viva_weight)
        plate_weight.append(weight_particiones)
        plate_weight.append(weight_ventanas)


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
            Espesor_deposito = '-'
            Periodo_suelo = '< 0.3'
            descripcion_geotecnica = 'Rocas sedimentarias y depósitos de ladera con espesores inferiores a 6 m'
            velocidad_onda = '> 750'
            Humedad_Promedio = '< 10'
            Efectos_relacionados = 'Topográfico'

        if type_suelo == 'Piedemonte_A':
            fa = 1.65
            fv = 2
            Espesor_deposito = '< 50'
            Periodo_suelo = '0.3-0.6'
            descripcion_geotecnica = 'Suelo coluvial y aluvial con intercalaciones de arcillas blandas: Bloques, cantos y gravas con matriz arcillo arenosas o areno arcillosa, capas de arcillas blandas.'
            velocidad_onda = '200 - 750'
            Humedad_Promedio = '10-80'
            Efectos_relacionados = 'Topográfico, amplificación'

        if type_suelo == 'Piedemonte_B':
            fa = 1.95
            fv = 1.7
            Espesor_deposito = '< 50'
            Periodo_suelo = '0.3-0.6'
            descripcion_geotecnica = 'Suelo coluvial y aluvial con espesor superior a 12 m:  Bloques, cantos y gravas con matriz arcillo arenosas o areno arcillosa'
            velocidad_onda = '300 - 750'
            Humedad_Promedio = '10-30'
            Efectos_relacionados = 'Topográfico, amplificación'

        if type_suelo == 'Piedemonte_C':
            fa = 1.8
            fv = 1.78
            Espesor_deposito = '< 50'
            Periodo_suelo = '0.3-0.6'
            descripcion_geotecnica = 'Suelo coluvial y aluvial con espesor superior a 12 m:  Bloques, cantos y gravas con matriz arcillo arenosas o areno arcillosa'
            velocidad_onda = '300 - 750'
            Humedad_Promedio = '10-30'
            Efectos_relacionados = 'Topográfico, amplificación'

        if type_suelo == 'Lacustre_50':
            fa = 1.4
            fv = 2.9
            Espesor_deposito = '< 50'
            Periodo_suelo = '1.0-1.5'
            descripcion_geotecnica = 'Suelo lacustre blando: Arcillas limosas o limos arcillosos, en algunos sectores con intercalaciones de lentes de turba'
            velocidad_onda = '< 175'
            Humedad_Promedio = '> 80'
            Efectos_relacionados = 'Amplificación'

        if type_suelo == 'Lacustre_100':
            fa = 1.3
            fv = 3.2
            Espesor_deposito = '50-100'
            Periodo_suelo = '1.5-2.5'
            descripcion_geotecnica = 'Suelo lacustre blando: Arcillas limosas o limos arcillosos, en algunos sectores con intercalaciones de lentes de turba'
            velocidad_onda = '< 175'
            Humedad_Promedio = '> 80'
            Efectos_relacionados = 'Amplificación'

        if type_suelo == 'Lacustre_200':
            fa = 1.2
            fv = 3.5
            Espesor_deposito = '100-200'
            Periodo_suelo = '2.5-3.5'
            descripcion_geotecnica = 'Suelo lacustre blando: Arcillas limosas o limos arcillosos, en algunos sectores con intercalaciones de lentes de turba'
            velocidad_onda = '< 175'
            Humedad_Promedio = '> 80'
            Efectos_relacionados = 'Amplificación'

        if type_suelo == 'Lacustre_300':
            fa = 1.05
            fv = 2.9
            Espesor_deposito = '200-300'
            Periodo_suelo = '3.4-4.5'
            descripcion_geotecnica = 'Suelo lacustre blando: Arcillas limosas o limos arcillosos, en algunos sectores con intercalaciones de lentes de turba'
            velocidad_onda = '< 175'
            Humedad_Promedio = '> 80'
            Efectos_relacionados = 'Amplificación'

        if type_suelo == 'Lacustre_500':
            fa = 0.95
            fv = 2.7
            Espesor_deposito = '300-500'
            Periodo_suelo = '4.5-6.5'
            descripcion_geotecnica = 'Suelo lacustre blando: Arcillas limosas o limos arcillosos, en algunos sectores con intercalaciones de lentes de turba'
            velocidad_onda = '< 175'
            Humedad_Promedio = '> 80'
            Efectos_relacionados = 'Amplificación'

        if type_suelo == 'Lacustre_Aluvial_200':
            fa = 1.1
            fv = 2.8
            Espesor_deposito = '100-200'
            Periodo_suelo = '2.0-3.0'
            descripcion_geotecnica = 'Suelo lacustre con intercalaciones de aluvial: Arcillas limosas o limos arcillosos con de lentes de turba y capas de arenas compactas'
            velocidad_onda = '< 200'
            Humedad_Promedio = '> 60'
            Efectos_relacionados = 'Amplificación'

        if type_suelo == 'Lacustre_Aluvial_300':
            fa = 1.1
            fv = 2.5
            Espesor_deposito = '200-300'
            Periodo_suelo = '3.0-4.0'
            descripcion_geotecnica = 'Suelo lacustre con intercalaciones de aluvial: Arcillas limosas o limos arcillosos con de lentes de turba y capas de arenas compactas'
            velocidad_onda = '< 200'
            Humedad_Promedio = '> 60'
            Efectos_relacionados = 'Amplificación'

        if type_suelo == 'Aluvial_50':
            fa = 1.35
            fv = 1.8
            Espesor_deposito = '< 50'
            Periodo_suelo = '0.4-0.8'
            descripcion_geotecnica = 'Suelo aluvial duro: Arcillas limosas o arenas arcillosos o limos arenosos, en algunos sectores se encuentran lentes de arenas limpias'
            velocidad_onda = '175 - 300'
            Humedad_Promedio = '25 - 50'
            Efectos_relacionados = 'Amplificación, licuación'

        if type_suelo == 'Aluvial_100':
            fa = 1.2
            fv = 2.1
            Espesor_deposito = '50-100'
            Periodo_suelo = '0.8-1.2'
            descripcion_geotecnica = 'Suelo aluvial duro: Arcillas limosas o arenas arcillosos o limos arenosos, en algunos sectores se encuentran lentes de arenas limpias'
            velocidad_onda = '175 - 300'
            Humedad_Promedio = '25 - 50'
            Efectos_relacionados = 'Amplificación, licuación'

        if type_suelo == 'Aluvial_200':
            fa = 1.01
            fv = 2.1
            Espesor_deposito = '100-200'
            Periodo_suelo = '1.2-2.5'
            descripcion_geotecnica = 'Suelo aluvial duro: Arcillas limosas o arenas arcillosos o limos arenosos, en algunos sectores se encuentran lentes de arenas limpias'
            velocidad_onda = '175 - 300'
            Humedad_Promedio = '25 - 50'
            Efectos_relacionados = 'Amplificación, licuación'

        if type_suelo == 'Aluvial_300':
            fa = 0.95
            fv = 2.1
            Espesor_deposito = '200-300'
            Periodo_suelo = '2.5-4.0'
            descripcion_geotecnica = 'Suelo aluvial duro: Arcillas limosas o arenas arcillosos o limos arenosos, en algunos sectores se encuentran lentes de arenas limpias'
            velocidad_onda = '175 - 300'
            Humedad_Promedio = '25 - 50'
            Efectos_relacionados = 'Amplificación, licuación'

        process = Process(
            user=user,
            type_construccion=data['type_construccion'],
            type_property=data['type_property'],
            fuerzas_horizontales=data['fuerzas_horizontales'],
            fuerzas_verticales=data['fuerzas_verticales'],
            # picture=data['picture'],
            val_irregular_long=val_irregular_long,
            val_irregular_plant=val_irregular_plant,
            # planes=data['planes'],
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
            result = 'BAJA'
        elif vulnerability_result <= 35:
            result = 'MEDIA'
        else:
            result = 'AlTA!'

        print('/////////////////////')
        print(data['height_floors'], data['floors'] )
        height = data['height_floors']*data['floors']

        comments = data['comments']
        if not comments:
            comments = ''


        if data['type_property'] == 1:
            group_use = 1
        elif data['type_property'] == 1.1:
            group_use = 2
        elif data['type_property'] == 1.25:
            group_use = 3
        else:
            group_use = 4

        result_pdf = f"{user};{data['name_owner']};{data['address']};{data['email']};{data['floors']};{height};{type_suelo};{Espesor_deposito};{Periodo_suelo};{descripcion_geotecnica};{velocidad_onda};{Humedad_Promedio};{Efectos_relacionados};{group_use};{data['type_construccion']};{data['irregular_plant']};{data['irregular_long']};{round(sum(plate_weight))};{comments};{result}"

        result_process_pdf = ResultPdf(process=process, result_pdf=result_pdf)
        result_process_pdf.save()

        return render(
            request,
            'index.html',
            {
                'message': 'Proceso correcto',
                'result': f'El valor del resultado es {vulnerability_result} lo que indica que la vulnerabilidad es {result}',
                'status': 'success',
                'process': 1,
                'footer': result_process_pdf.pk
            }
        )


def file_response(request, pk, file= "Hello world."):
    try:
        print(pk)
        result = ResultPdf.objects.get(pk=pk)
    except ResultPdf.DoesNotExist:
        raise Http404("El proceso no existe")

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)

    result = result.result_pdf.split(';')
    print(result)
    p.drawString(150, 750, 'RESULTADOS ANÁLISIS DE VULNERABILIDAD SÍSMICA')
    p.drawString(50, 710, 'Usuario:')
    p.drawString(80, 685, result[0])
    print(result[0], type(result[0]))

    p.drawString(50, 645, 'Información preliminar de la vivienda:')

    p.drawString(80, 620, f'Propietario de la vivienda: {result[1]}')
    p.drawString(80, 605, f'Dirección: {result[2]}')
    p.drawString(80, 590, f'Email: {result[3]}')
    p.drawString(80, 575, f'No de pisos: {result[4]}')
    p.drawString(80, 560, f'Altura de la edificación (m): {result[5]}')


    p.drawString(50, 520, 'Resultados del análisis de vulnerabilidad:')

    p.drawString(80, 495, f'Tipo de suelo: {result[6]}')
    p.drawString(80, 480, f'Espesor del depósito (m) {result[7]}')
    p.drawString(80, 465, f'Perido fundamental del suelo (s): {result[8]}')
    p.drawString(80, 450, f'Descropción geotécnica general: {result[9]}')
    p.drawString(80, 435, f'Velocidad de onda promedio 50 m Vs (m/s): {result[10]}')
    p.drawString(80, 420, f'Humedad Promedio 50 m Hn (%): {result[11]}')
    p.drawString(80, 405, f'Efectos de sitio relacionados: {result[12]}')
    p.drawString(80, 390, f'Grupo de uso: {result[13]}')
    p.drawString(80, 375, f'Tipo de sistema estructural: {result[14]}')
    p.drawString(80, 360, f'Irregularidad en planta: {result[15]}')
    p.drawString(80, 345, f'Irregulidad en altura: {result[16]}')
    p.drawString(80, 330, f'Peso de la estructura (kn): {result[17]}')
    p.drawString(80, 315, f'Comentarios: {result[18]}')
    p.drawString(80, 270, f'Índice de vulnerabilidad sísmica de la vivienda: {result[19]}')

    p.showPage()
    p.save()
    buffer.seek(0)

    w = FileWrapper(buffer)
    return FileResponse(w, as_attachment=True, filename=f'Proceso{pk}.pdf', content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")


@login_required
def logout_view(request):
    """Logout a user."""
    logout(request)
    return redirect('page')

def weight(request):
    return render(request, 'users/weight_calculation.html')


class Nsr10(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'users/nsr.html')

    def post(self, request, *args, **kwargs):
        response = request.POST

        response_weight = dict(response.lists())

        type_placa = response_weight.get('type_placa')
        placa_x = response_weight.get('placa_x')
        placa_y = response_weight.get('placa_y')

        placa_weight = []

        if 'Placa_Maciza' in type_placa:
            placa_z = response_weight.get('placa_z')

        if 'Placa_Aligerada' in type_placa:
            vg_a = response_weight.get('vg_a')
            vg_b = response_weight.get('vg_b')
            vg_c = response_weight.get('vg_c')
            vg_d = response_weight.get('vg_d')
            vg_e = response_weight.get('vg_e')

        if 'Placa_Facil' in type_placa:
            type_placa_facil = response_weight.get('type_placa_facil')

            if 'Placa' in type_placa_facil:
                z_placa_facil = response_weight.get('z_placa_facil')

            if 'Perfil_Metalico' in type_placa_facil:
                peso_ml_perfil = response_weight.get('peso_ml_perfil')
                ml_perfil = response_weight.get('ml_perfil')

            if 'Bloquelon' in type_placa_facil:
                peso_bloquelon = response_weight.get('peso_bloquelon')

        placa_facil_placa = []
        placa_facil_perfil = []
        placa_facil_bloquelon = []

        placa_aligerada = []
        placa_maciza = []

        placa_weight = 0

        for placa in type_placa:
            if placa == 'Placa_Maciza':
                placa = {}
                volumen = float(placa_x.pop(0))*float(placa_y.pop(0))*float(placa_z.pop(0))
                total = volumen*DENSIDAD*GRAVEDAD
                placa['volumen_placa'] = volumen
                placa['total_placa'] = total

                placa_weight += total
                placa_maciza.append(placa)

            if placa == 'Placa_Facil':
                placa_facil = type_placa_facil[0]

                if placa_facil == 'Placa':
                    placa = {}
                    volumen = float(placa_x.pop(0))*float(placa_y.pop(0))*float(z_placa_facil.pop(0))
                    total  = volumen*DENSIDAD*GRAVEDAD
                    placa['volumen_placa'] = volumen
                    placa['total_placa'] = total

                    placa_weight += total
                    placa_facil_placa.append(placa)


                    # placa_weight.append(
                    #     float(placa_x.pop(0))*float(placa_y.pop(0))
                    #     *float(z_placa_facil.pop(0))
                    #     *DENSIDAD*GRAVEDAD
                    # )

                    type_placa_facil.pop(0)

                if placa_facil == 'Perfil_Metalico':
                    placa = {}
                    volumen = float(peso_ml_perfil.pop(0))*float(ml_perfil.pop(0))
                    total  = volumen*GRAVEDAD
                    placa['volumen_placa'] = volumen
                    placa['total_placa'] = total


                    placa_weight += total
                    placa_facil_perfil.append(placa)

                    type_placa_facil.pop(0)

                if placa_facil == 'Bloquelon':
                    placa = {}
                    volumen = float(placa_x.pop(0))*float(placa_y.pop(0))*float(peso_bloquelon.pop(0))
                    total = volumen*GRAVEDAD
                    placa['volumen_placa'] = volumen
                    placa['total_placa'] = total


                    placa_weight += total
                    placa_facil_bloquelon.append(placa)

                    # placa_weight.append(
                    #     float(placa_x.pop(0))
                    # *float(placa_y.pop(0))*float(peso_bloquelon.pop(0))
                    # *GRAVEDAD
                    # )

                    type_placa_facil.pop(0)

            if placa == 'Placa_Aligerada':
                placa = {}
                vg_b_num = float(vg_b.pop(0))
                m2 = float(placa_x.pop(0))*float(placa_y.pop(0))
                vigueta = (vg_b_num*float(vg_c.pop(0))*m2)/(
                    float(vg_a.pop(0))+vg_b_num
                )
                placa_superior=(float(vg_d.pop(0))+float(vg_e.pop(0)))*m2
                volumen = vigueta + placa_superior

                total = volumen*DENSIDAD*GRAVEDAD
                placa['volumen_placa'] = volumen
                placa['total_placa'] = total


                placa_weight += total
                placa_aligerada.append(placa)



        ancho_viga = response_weight.get('ancho_viga')
        alto_viga = response_weight.get('alto_viga')
        largo_viga = response_weight.get('largo_viga')
        numero_viga = response_weight.get('numero_viga')

        # viga_weight = [
        #     float(ancho_viga[num])*
        #     float(alto_viga[num])*
        #     float(largo_viga[num])*
        #     int(numero_viga[num])*
        #     DENSIDAD*GRAVEDAD
        #     for num in range(len(numero_viga))
        # ]

        vigas_total = []
        viga_weight = 0

        for num in range(len(numero_viga)):
            vigas = {}
            volumen = float(ancho_viga[num])*float(alto_viga[num])*float(largo_viga[num])
            numero_vigas = int(numero_viga[num])
            total = volumen*numero_vigas*DENSIDAD*GRAVEDAD
            vigas['volumen_vigas'] = volumen
            vigas['numero_vigas'] = numero_vigas
            vigas['total_vigas'] = total

            viga_weight += total
            vigas_total.append(vigas)



        ancho_columna = response_weight.get('ancho_columna')
        alto_columna = response_weight.get('alto_columna')
        largo_columna = response_weight.get('largo_columna')
        numero_columna = response_weight.get('numero_columna')

        # columna_weight = [
        #     float(ancho_columna[num])*
        #     float(alto_columna[num])*
        #     float(largo_columna[num])*
        #     int(numero_columna[num])*
        #     DENSIDAD*GRAVEDAD
        #     for num in range(len(numero_columna))
        # ]
        columnas_total = []
        columna_weight = 0

        for num in range(len(numero_columna)):
            columnas = {}
            volumen = float(ancho_columna[num])*float(alto_columna[num])*float(largo_columna[num])
            numero_columnas = int(numero_columna[num])
            total = volumen*numero_columnas*DENSIDAD*GRAVEDAD
            columnas['volumen_columnas'] = volumen
            columnas['numero_columnas'] = numero_columnas
            columnas['total_columnas'] = total

            columna_weight += total
            columnas_total.append(columnas)
        print('/////////////////////////////////')
        print(response_weight.get('muro_fachada'))
        tipo_muro_fachada = [
            'Mampostería de bloque de arcilla',
            'Mampostería de bloque de concreto',
            'Mampostería maciza de arcilla',
            'Mampostería maciza de concreto'
        ][int(response_weight.get('muro_fachada')[0])]
        muro_caracteristica = response_weight.get('muro_caracteristica')
        espesor = response_weight.get('espesor')
        m2_muros = response_weight.get('m2_muros')
        weight_muro = eval(muro_caracteristica[0])[int(espesor[0])]*float(m2_muros[0])
        valor_nsr_10 = eval(muro_caracteristica[0])[int(espesor[0])]

        muro_fachada = {
            'tipo_muro': tipo_muro_fachada,
            'valor_nsr_10': valor_nsr_10,
            'm2_muros': m2_muros,
            'weight_muro':weight_muro
        }


        tipo_mamposteria = [
            'Mampostería de bloque de arcilla',
            'Mampostería de bloque de concreto',
            'Mampostería maciza de arcilla',
            'Mampostería maciza de concreto',
        ][int(response_weight.get('muro_divisorio')[0])]
        muro_caracteristica_divisorio = response_weight.get('muro_caracteristica_divisorio')
        espesor_divisorio = response_weight.get('espesor_divisorio')
        m2_muros_divisorio = response_weight.get('m2_muros_divisorio')
        weight_divisorio = eval(muro_caracteristica_divisorio[0])[int(espesor_divisorio[0])]*float(m2_muros_divisorio[0])
        valor_nsr_10 = eval(muro_caracteristica_divisorio[0])[int(espesor_divisorio[0])]

        muro_divisorio = {
            'tipo_muro': tipo_mamposteria,
            'valor_nsr_10': valor_nsr_10,
            'm2_muros': m2_muros_divisorio,
            'weight_muro':weight_divisorio
        }


        type_particiones = response_weight.get('type_particiones')
        m2_particiones = response_weight.get('m2_particiones')
        weight_particiones = float(type_particiones[0])*float(m2_particiones[0])

        name_particiones = {
            0.5:'Particiones móviles de acero (altura parcial)',
            0.2:'Particiones móviles de acero (altura total)',
            0.9:'Poste en madera o acero, yeso de 12 mm a cada lado'
        }

        particiones = {
            'tipo_particiones': name_particiones[float(type_particiones[0])],
            'valor_nsr_10': float(type_particiones[0]),
            'm2_particiones': m2_particiones,
            'weight_particiones': weight_particiones

        }

        name_ventanas = {
            0.5:"Muros cortina de vidrio, entramado y marco",
            0.45:"Ventanas, vidrio, entramado y marco"
        }

        type_ventanas = response_weight.get('type_ventanas')
        m2_ventanas = response_weight.get('m2_ventanas')
        weight_ventanas = float(type_ventanas[0])*float(m2_ventanas[0])

        ventanas = {
            'tipo_ventanas': name_ventanas[float(type_ventanas[0])],
            'm2_ventanas': m2_ventanas,
            'valor_nsr_10': float(type_ventanas[0]),
            'weight_ventanas': weight_ventanas
        }

        name_cubierta = {
            0.0020: "Cubiertas aislantes Fibra de vidrio",
            0.2: "Cubiertas corrugadas de asbesto-cemento",
            0.0060: "Entablado de madera",
            0.1: "Láminas de yeso, 12 mm",
            0.0100: "Madera laminada (según el espesor)",
            0.4: "Marquesinas, marco metálico, vidrio de 10 mm",
            0.15: "Tablillas (shingles) de madera",
            0.8: "Teja de arcilla, incluyendo el mortero",
        }
        type_cubierta = response_weight.get('type_cubierta')
        espesor_cubierta = response_weight.get('espesor_cubierta')
        m2_cubierta = response_weight.get('m2_cubierta')

        if espesor_cubierta:
            cubierta_weight = float(type_cubierta[0])*float(espesor_cubierta[0])*float(m2_cubierta[0])
        else:
            cubierta_weight = float(type_cubierta[0])*float(m2_cubierta[0])

        cubierta = {
            'tipo_cubierta': name_cubierta[float(type_cubierta[0])],
            'valor_nsr_10': float(type_cubierta[0]),
            'm2_cubierta': m2_cubierta,
            'cubierta_weight': cubierta_weight

        }

        name_piso = {
            0.02: "Acabado de piso en concreto",
            0.8: "Baldosa cerámica (20 mm) sobre 12 mm de mortero",
            1.1: "Baldosa sobre 25 mm de mortero",
            0.2: "Madera densa, 25 mm",
            0.03: "Pizarra",
            1.5: "Terrazzo (25 mm), concreto 50 mm",
            0.9: "Terrazzo (40 mm) directamente sobre la losa",
            1.5: "Terrazzo (25 mm) sobre afinado en concreto",
        }

        type_piso = response_weight.get('type_piso')
        espesor_piso = response_weight.get('espesor_piso')
        m2_pisos = response_weight.get('m2_pisos')

        if espesor_piso:
            piso_weight = float(type_piso[0])*float(espesor_piso[0])*float(m2_pisos[0])
        else:
            piso_weight = float(type_piso[0])*float(m2_pisos[0])

        piso = {
            'tipo_piso': name_piso[float(type_piso[0])],
            'valor_nsr_10': float(type_piso[0]),
            'm2_pisos': m2_pisos,
            'piso_weight':piso_weight
        }

        name_recubrimiento = {
            0.8: "Baldosín de cemento",
            0.01: "Madera laminada (según el espesor)",
            0.003: "Tableros de fibra (aislante)",
            0.1: "Tableros de yeso, 12 mm (aislante)",
        }

        type_recubrimiento = response_weight.get('type_recubrimiento')
        espesor_recubrimiento = response_weight.get('espesor_recubrimiento')
        m2_recubrimiento = response_weight.get('m2_recubrimiento')

        if espesor_recubrimiento:
            recubrimiento_weight = float(type_recubrimiento[0])*float(espesor_recubrimiento[0])*float(m2_recubrimiento[0])
        else:
            recubrimiento_weight = float(type_recubrimiento[0])*float(m2_recubrimiento[0])

        recubrimiento = {
            'tipo_recubrimiento': name_recubrimiento[float(type_recubrimiento[0])],
            'valor_nsr_10': float(type_recubrimiento[0]),
            'm2_recubrimiento': m2_recubrimiento,
            'recubrimiento_weight': recubrimiento_weight
        }

        name_enchape = {
                0.015:"Enchape cerámico",
                0.013:"Enchape en arenisca",
                0.015:"Enchape en caliza",
                0.017:"Enchape en granito",

        }
        type_enchape = response_weight.get('type_enchape')
        espesor_enchape = response_weight.get('espesor_enchape')
        m2_enchape = response_weight.get('m2_enchape')
        enchape_weight = float(type_enchape[0])*float(espesor_enchape[0])*float(m2_enchape[0])

        enchape = {
            'tipo_enchape': name_enchape[float(type_enchape[0])],
            'valor_nsr_10': float(type_enchape[0]),
            'm2_enchape': m2_enchape,
            'enchape_weight':enchape_weight
        }


        name_ocupacion = response_weight.get('ocupacion')
        ocupacion_uso = response_weight.get('ocupacion_uso')
        m2_ocupacion = response_weight.get('m2_ocupacion')
        ocupacion_weight = float(ocupacion_uso[0])*float(m2_ocupacion[0])

        ocupacion = {
            'tipo_ocupacion': name_ocupacion,
            'valor_nsr_10': float(ocupacion_uso[0]),
            'm2_ocupacion': m2_ocupacion,
            'ocupacion_weight': ocupacion_weight
        }


        name_cubierta_viva = {
            1: "Cubiertas, Azoteas y Terrazas",
            5.0: "Cubiertas usadas para jardines de cubierta o para reuniones",
            0.35: "Cubiertas inclinadas con más de 15° de pendiente en estructura metálica o de madera con imposibilidad física de verse sometidas a cargas superiores a la aquí estipulada",
            0.5: "Cubiertas  inclinadas  con  pendiente  de  15°  o menos  en estructura metálica o de madera con imposibilidad física de verse sometidas a cargas superiores a la aquí estipulada",
        }
        cubierta_viva = response_weight.get('cubierta_viva')
        m2_cubierta_viva = response_weight.get('m2_cubierta_viva')
        cubierta_viva_weight = float(cubierta_viva[0])*float(m2_cubierta_viva[0])

        cubierta_viva = {
            'tipo_cubierta': name_cubierta_viva[float(cubierta_viva[0])],
            'valor_nsr_10': float(cubierta_viva[0]),
            'm2_cubierta_viva': m2_cubierta_viva,
            'cubierta_viva_weight': cubierta_viva_weight
        }


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
            Espesor_deposito = '-'
            Periodo_suelo = '< 0.3'
            descripcion_geotecnica = 'Rocas sedimentarias y depósitos de ladera con espesores inferiores a 6 m'
            velocidad_onda = '> 750'
            Humedad_Promedio = '< 10'
            Efectos_relacionados = 'Topográfico'

        if type_suelo == 'Piedemonte_A':
            fa = 1.65
            fv = 2
            Espesor_deposito = '< 50'
            Periodo_suelo = '0.3-0.6'
            descripcion_geotecnica = 'Suelo coluvial y aluvial con intercalaciones de arcillas blandas: Bloques, cantos y gravas con matriz arcillo arenosas o areno arcillosa, capas de arcillas blandas.'
            velocidad_onda = '200 - 750'
            Humedad_Promedio = '10-80'
            Efectos_relacionados = 'Topográfico, amplificación'

        if type_suelo == 'Piedemonte_B':
            fa = 1.95
            fv = 1.7
            Espesor_deposito = '< 50'
            Periodo_suelo = '0.3-0.6'
            descripcion_geotecnica = 'Suelo coluvial y aluvial con espesor superior a 12 m:  Bloques, cantos y gravas con matriz arcillo arenosas o areno arcillosa'
            velocidad_onda = '300 - 750'
            Humedad_Promedio = '10-30'
            Efectos_relacionados = 'Topográfico, amplificación'

        if type_suelo == 'Piedemonte_C':
            fa = 1.8
            fv = 1.78
            Espesor_deposito = '< 50'
            Periodo_suelo = '0.3-0.6'
            descripcion_geotecnica = 'Suelo coluvial y aluvial con espesor superior a 12 m:  Bloques, cantos y gravas con matriz arcillo arenosas o areno arcillosa'
            velocidad_onda = '300 - 750'
            Humedad_Promedio = '10-30'
            Efectos_relacionados = 'Topográfico, amplificación'

        if type_suelo == 'Lacustre_50':
            fa = 1.4
            fv = 2.9
            Espesor_deposito = '< 50'
            Periodo_suelo = '1.0-1.5'
            descripcion_geotecnica = 'Suelo lacustre blando: Arcillas limosas o limos arcillosos, en algunos sectores con intercalaciones de lentes de turba'
            velocidad_onda = '< 175'
            Humedad_Promedio = '> 80'
            Efectos_relacionados = 'Amplificación'

        if type_suelo == 'Lacustre_100':
            fa = 1.3
            fv = 3.2
            Espesor_deposito = '50-100'
            Periodo_suelo = '1.5-2.5'
            descripcion_geotecnica = 'Suelo lacustre blando: Arcillas limosas o limos arcillosos, en algunos sectores con intercalaciones de lentes de turba'
            velocidad_onda = '< 175'
            Humedad_Promedio = '> 80'
            Efectos_relacionados = 'Amplificación'

        if type_suelo == 'Lacustre_200':
            fa = 1.2
            fv = 3.5
            Espesor_deposito = '100-200'
            Periodo_suelo = '2.5-3.5'
            descripcion_geotecnica = 'Suelo lacustre blando: Arcillas limosas o limos arcillosos, en algunos sectores con intercalaciones de lentes de turba'
            velocidad_onda = '< 175'
            Humedad_Promedio = '> 80'
            Efectos_relacionados = 'Amplificación'

        if type_suelo == 'Lacustre_300':
            fa = 1.05
            fv = 2.9
            Espesor_deposito = '200-300'
            Periodo_suelo = '3.4-4.5'
            descripcion_geotecnica = 'Suelo lacustre blando: Arcillas limosas o limos arcillosos, en algunos sectores con intercalaciones de lentes de turba'
            velocidad_onda = '< 175'
            Humedad_Promedio = '> 80'
            Efectos_relacionados = 'Amplificación'

        if type_suelo == 'Lacustre_500':
            fa = 0.95
            fv = 2.7
            Espesor_deposito = '300-500'
            Periodo_suelo = '4.5-6.5'
            descripcion_geotecnica = 'Suelo lacustre blando: Arcillas limosas o limos arcillosos, en algunos sectores con intercalaciones de lentes de turba'
            velocidad_onda = '< 175'
            Humedad_Promedio = '> 80'
            Efectos_relacionados = 'Amplificación'

        if type_suelo == 'Lacustre_Aluvial_200':
            fa = 1.1
            fv = 2.8
            Espesor_deposito = '100-200'
            Periodo_suelo = '2.0-3.0'
            descripcion_geotecnica = 'Suelo lacustre con intercalaciones de aluvial: Arcillas limosas o limos arcillosos con de lentes de turba y capas de arenas compactas'
            velocidad_onda = '< 200'
            Humedad_Promedio = '> 60'
            Efectos_relacionados = 'Amplificación'

        if type_suelo == 'Lacustre_Aluvial_300':
            fa = 1.1
            fv = 2.5
            Espesor_deposito = '200-300'
            Periodo_suelo = '3.0-4.0'
            descripcion_geotecnica = 'Suelo lacustre con intercalaciones de aluvial: Arcillas limosas o limos arcillosos con de lentes de turba y capas de arenas compactas'
            velocidad_onda = '< 200'
            Humedad_Promedio = '> 60'
            Efectos_relacionados = 'Amplificación'

        if type_suelo == 'Aluvial_50':
            fa = 1.35
            fv = 1.8
            Espesor_deposito = '< 50'
            Periodo_suelo = '0.4-0.8'
            descripcion_geotecnica = 'Suelo aluvial duro: Arcillas limosas o arenas arcillosos o limos arenosos, en algunos sectores se encuentran lentes de arenas limpias'
            velocidad_onda = '175 - 300'
            Humedad_Promedio = '25 - 50'
            Efectos_relacionados = 'Amplificación, licuación'

        if type_suelo == 'Aluvial_100':
            fa = 1.2
            fv = 2.1
            Espesor_deposito = '50-100'
            Periodo_suelo = '0.8-1.2'
            descripcion_geotecnica = 'Suelo aluvial duro: Arcillas limosas o arenas arcillosos o limos arenosos, en algunos sectores se encuentran lentes de arenas limpias'
            velocidad_onda = '175 - 300'
            Humedad_Promedio = '25 - 50'
            Efectos_relacionados = 'Amplificación, licuación'

        if type_suelo == 'Aluvial_200':
            fa = 1.01
            fv = 2.1
            Espesor_deposito = '100-200'
            Periodo_suelo = '1.2-2.5'
            descripcion_geotecnica = 'Suelo aluvial duro: Arcillas limosas o arenas arcillosos o limos arenosos, en algunos sectores se encuentran lentes de arenas limpias'
            velocidad_onda = '175 - 300'
            Humedad_Promedio = '25 - 50'
            Efectos_relacionados = 'Amplificación, licuación'

        if type_suelo == 'Aluvial_300':
            fa = 0.95
            fv = 2.1
            Espesor_deposito = '200-300'
            Periodo_suelo = '2.5-4.0'
            descripcion_geotecnica = 'Suelo aluvial duro: Arcillas limosas o arenas arcillosos o limos arenosos, en algunos sectores se encuentran lentes de arenas limpias'
            velocidad_onda = '175 - 300'
            Humedad_Promedio = '25 - 50'
            Efectos_relacionados = 'Amplificación, licuación'

        return render(
            request,
            'nsr_resutl.html',
            {
                'height':data['height_floors']*data['floors'],
                'type_construccion':data['type_construccion'].replace('_',' '),
                'type_property':data['type_property'],
                'floors':data['floors'],
                'comments':data['comments'],
                'cordenada_x':data['cordenada_x'],
                'cordenada_y':data['cordenada_y'],
                'irregularidad_planta':data['irregular_plant'].replace('_',' '),
                'irregularidad_long':data['irregular_long'].replace('_',' '),
                'height_floors':data['height_floors'],
                'type_suelo':type_suelo,
                'fa':fa,
                'fv':fv,
                'Espesor_deposito':Espesor_deposito,
                'Periodo_suelo':Periodo_suelo,
                'descripcion_geotecnica':descripcion_geotecnica,
                'velocidad_onda':velocidad_onda,
                'Humedad_Promedio':Humedad_Promedio,
                'Efectos_relacionados':Efectos_relacionados,
                'columnas_total': columnas_total,
                'columna_weight': columna_weight,
                'placa_facil_placa':placa_facil_placa,
                'placa_facil_perfil':placa_facil_perfil,
                'placa_facil_bloquelon':placa_facil_bloquelon,
                'placa_aligerada':placa_aligerada,
                'placa_maciza':placa_maciza,
                'placa_weight':placa_weight,
                'vigas_total': vigas_total,
                'viga_weight':  viga_weight,
                'columnas_total': columnas_total,
                'columna_weight': columna_weight,
                'muro_fachada': muro_fachada,
                'muro_divisorio': muro_divisorio,
                'particiones': particiones,
                'ventanas': ventanas,
                'cubierta': cubierta,
                'piso': piso,
                'recubrimiento': recubrimiento,
                'enchape': enchape,
                'ocupacion': ocupacion,
                'cubierta_viva': cubierta_viva,
            }
        )













class Ais(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'users/weight_calculation.html')

    def post(self, request, *args, **kwargs):
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


        ais = AisModel(
            option_confined_walls=option_confined_walls,
            option_detail=option_detail,
            option_mooring=option_mooring,
            option_characteristics=option_characteristics,
            option_mezzanine=option_mezzanine,
            option_cover=option_cover,
            option_floor=option_floor,
            option_wall=option_wall,
            option_height=option_height,
            option_quality=option_quality,
            option_location=option_location,
            option_materials=option_materials,
            option_base=option_base,
            option_soil=option_soil,
            option_environment=option_environment,
        )

        ais.save()

        return redirect('ais_detail', pk=ais.pk)


        # qualification_structural = (
        #     (
        #         int(option_confined_walls) +
        #         int(option_detail) +
        #         int(option_mooring) +
        #         int(option_characteristics) +
        #         int(option_mezzanine) +
        #         int(option_cover)
        #     )/6
        # )*PORCENT_STRUCTURAL

        # qualification_geometry =  (
        #     (int(option_floor)+ int(option_wall)+ int(option_height))/3
        # )*PORCENT_GEOMETRY

        # qualification_constructive =  (
        #     (int(option_quality) + int(option_location) + int(option_materials))/3
        # )*PORCENT_CONSTRUCTIVE

        # qualification_base = int(option_base)*PORCENT_BASE
        # qualification_soil = int(option_soil)*PORCENT_SOIL
        # qualification_environment = int(option_environment)*PORCENT_ENVIRONMENT

        # vulnerability_result = round(((
        #     qualification_structural +
        #     qualification_geometry +
        #     qualification_constructive +
        #     qualification_base +
        #     qualification_soil +
        #     qualification_environment
        # )/2)*100)

        # if vulnerability_result <= 15:
        #     result = 'BAJA'
        # elif vulnerability_result <= 35:
        #     result = 'MEDIA'
        # else:
        #     result = 'AlTA!'


        # return render(
        #     request,
        #     'index.html',
        #     {
        #         'message': 'Proceso correcto',
        #         'result': f'El valor del resultado es {vulnerability_result} lo que indica que la vulnerabilidad es {result}',
        #         'status': 'success',
        #         'process': 1,
        #     }
        # )

class AisDetail(LoginRequiredMixin, DetailView):
    model = AisModel
    template_name = 'nsr_resutl.html'
    context_object_name = 'aisprocess'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        aisprocess = context['aisprocess']

        qualification_structural = (
            (
                aisprocess.option_confined_walls +
                aisprocess.option_detail +
                aisprocess.option_mooring +
                aisprocess.option_characteristics +
                aisprocess.option_mezzanine +
                aisprocess.option_cover
            )/6
        )
        total_structural = qualification_structural*PORCENT_STRUCTURAL

        context['qualification_structural'] = qualification_structural
        context['PORCENT_STRUCTURAL'] = PORCENT_STRUCTURAL
        context['total_structural'] = total_structural

        qualification_geometry =  (
            aisprocess.option_floor + aisprocess.option_wall + aisprocess.option_height
        )/3
        total_geometry = qualification_geometry*PORCENT_GEOMETRY

        context['qualification_geometry'] = qualification_geometry
        context['PORCENT_GEOMETRY'] = PORCENT_GEOMETRY
        context['total_geometry'] = total_geometry


        qualification_constructive =  (
            aisprocess.option_quality + aisprocess.option_location + aisprocess.option_materials
        )/3

        total_constructive = qualification_constructive*PORCENT_CONSTRUCTIVE

        context['qualification_constructive'] = qualification_constructive
        context['PORCENT_CONSTRUCTIVE'] = PORCENT_CONSTRUCTIVE
        context['total_constructive'] = total_constructive

        total_base = aisprocess.option_base*PORCENT_BASE

        context['PORCENT_BASE'] = PORCENT_BASE
        context['total_base'] = total_base

        total_soil = aisprocess.option_soil*PORCENT_SOIL

        context['PORCENT_SOIL'] = PORCENT_SOIL
        context['total_soil'] = total_soil

        total_environment = aisprocess.option_environment*PORCENT_ENVIRONMENT

        context['PORCENT_ENVIRONMENT'] = PORCENT_ENVIRONMENT
        context['total_environment'] = total_environment


        vulnerability_result = round(((
            total_structural +
            total_geometry +
            total_constructive +
            total_base +
            total_soil +
            total_environment
        )/2)*100)

        context['vulnerability_result'] = vulnerability_result

        if vulnerability_result <= 15:
            context['result'] = 'BAJA'
        elif vulnerability_result <= 35:
            context['result']  = 'MEDIA'
        else:
            context['result']  = 'AlTA!'
        return context