"""Users views."""

# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import FileResponse
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

# Exception
from django.db.utils import IntegrityError

# Models
from django.contrib.auth.models import User
from app.models import ResultPdf, Profile, AisModel
from app.models import Process
from app.area import areas
from app.config import *
# Forms
from app.forms import ProfileForm, IndiceForm
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
            return redirect('init_video')
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
        num_placa = response_weight.get('num_placa')


        placa_weight = []

        group_use = {
            1:1,
            1.1:2,
            1.25:3,
            1.5:4
        }
        #
        espeso_placa_facil = None
        espeso_placa = None

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
        placa_all = []
        placa_weight = 0
        count_placa = 1
        for num, placa in enumerate(type_placa):
            if placa == 'Placa_Maciza':
                placa_m = {}
                ancho_placo = float(placa_x.pop(0))
                espeso_placa = float(placa_z.pop(0))
                volumen = ancho_placo*float(placa_y.pop(0))*espeso_placa
                numero_placa = int(num_placa[num])
                placa_m['tipo_placa'] = placa.replace('_', ' ')
                total = volumen*numero_placa*DENSIDAD*GRAVEDAD
                placa_m['num'] = count_placa
                placa_m['volumen_placa'] = volumen
                placa_m['total_placa'] = round(total, 2)
                placa_m['numero_placa'] = numero_placa


                placa_weight += total
                placa_all.append(placa_m)

            if placa == 'Placa_Facil':
                placa_facil = type_placa_facil[0]

                if placa_facil == 'Placa':
                    placa_f = {}
                    ancho_placo = float(placa_x.pop(0))
                    espeso_placa_facil = float(z_placa_facil.pop(0))
                    volumen = ancho_placo*float(placa_y.pop(0))*espeso_placa_facil
                    numero_placa = int(num_placa[num])
                    total  = volumen*DENSIDAD*GRAVEDAD*numero_placa
                    placa_f['volumen_placa'] = volumen
                    placa_f['total_placa'] = round(total, 2)

                    p = placa.replace('_', ' ')
                    p_f = placa_facil.replace('_', ' ')
                    placa_f['tipo_placa'] = f'{p} - {p_f}'
                    placa_f['num'] = count_placa
                    placa_f['numero_placa'] = numero_placa

                    placa_weight += total
                    placa_all.append(placa_f)
                    type_placa_facil.pop(0)

                if placa_facil == 'Perfil_Metalico':
                    placa_fm = {}
                    ml_perfil = float(ml_perfil.pop(0))
                    numero_placa = int(num_placa[num])
                    total  = ml_perfil*4.47*GRAVEDAD*numero_placa
                    placa_fm['metro_lineal'] = ml_perfil
                    placa_fm['total_placa'] = round(total, 2)
                    placa_fm['peso_perfil_m2'] = 4.47
                    p = placa.replace('_', ' ')
                    p_f = placa_facil.replace('_', ' ')


                    placa_fm['tipo_placa'] = f'{p} - {p_f}'
                    placa_fm['num'] = count_placa
                    placa_fm['numero_placa'] = numero_placa

                    placa_weight += total
                    placa_all.append(placa_fm)

                    type_placa_facil.pop(0)

                if placa_facil == 'Bloquelon':
                    placa_fb = {}
                    ancho_placo = float(placa_x.pop(0))
                    area = ancho_placo*float(placa_y.pop(0))
                    numero_placa = int(num_placa[num])
                    total = area*53.57*GRAVEDAD*numero_placa
                    placa_fb['peso_bloquelon'] = 53.57
                    placa_fb['area_bloquelon'] = area
                    placa_fb['total_placa'] = round(total, 2)

                    p = placa.replace('_', ' ')
                    p_f = placa_facil.replace('_', ' ')

                    placa_fb['tipo_placa'] = f'{p} - {p_f}'
                    placa_fb['num'] = count_placa
                    placa_fb['numero_placa'] = numero_placa

                    placa_weight += total
                    placa_all.append(placa_fb)

                    type_placa_facil.pop(0)

            if placa == 'Placa_Aligerada':
                placa_a = {}
                vg_b_num = float(vg_b.pop(0))
                ancho_placo = float(placa_x.pop(0))
                m2 = ancho_placo*float(placa_y.pop(0))
                vigueta = (vg_b_num*float(vg_c.pop(0))*m2)/(
                    float(vg_a.pop(0))+vg_b_num
                )
                placa_superior=(float(vg_d.pop(0))+float(vg_e.pop(0)))*m2
                volumen = vigueta + placa_superior
                numero_placa = int(num_placa[num])
                total = volumen*DENSIDAD*GRAVEDAD*numero_placa
                placa_a['volumen_placa'] = volumen
                placa_a['total_placa'] = round(total, 2)

                placa_a['tipo_placa'] = placa.replace('_', ' ')
                placa_a['num'] = count_placa
                placa_a['numero_placa'] = numero_placa


                placa_weight += total
                placa_all.append(placa_a)

            count_placa += 1

        placa_weight = round(placa_weight, 2)

        ancho_viga = response_weight.get('ancho_viga')
        alto_viga = response_weight.get('alto_viga')
        largo_viga = response_weight.get('largo_viga')
        numero_viga = response_weight.get('numero_viga')

        vigas_total = []
        viga_weight = 0
        count = 1
        for num in range(len(numero_viga)):
            vigas = {}

            if espeso_placa:
                alto_viga_r = float(alto_viga[num])- espeso_placa
            elif espeso_placa_facil:
                alto_viga_r = float(alto_viga[num]) - espeso_placa_facil
            else:
                alto_viga_r = float(alto_viga[num])

            volumen = float(ancho_viga[num])*alto_viga_r*(float(largo_viga[num]))
            numero_vigas = int(numero_viga[num])
            total = volumen*numero_vigas*DENSIDAD*GRAVEDAD
            vigas['volumen_vigas'] = round(volumen, 2)
            vigas['numero_vigas'] = numero_vigas
            vigas['total_vigas'] = round(total,2)
            vigas['num'] = count
            viga_weight += total
            vigas_total.append(vigas)
            count += 1
        viga_weight = round(viga_weight,2)

        ancho_columna = response_weight.get('ancho_columna')
        alto_columna = response_weight.get('alto_columna')
        largo_columna = response_weight.get('largo_columna')
        numero_columna = response_weight.get('numero_columna')


        columnas_total = []
        columna_weight = 0
        count_columna = 1
        for num in range(len(numero_columna)):
            columnas = {}
            volumen = float(ancho_columna[num])*float(alto_columna[num])*float(largo_columna[num])
            numero_columnas = int(numero_columna[num])
            total = volumen*numero_columnas*DENSIDAD*GRAVEDAD
            columnas['volumen_columnas'] = round(volumen,2)
            columnas['numero_columnas'] = numero_columnas
            columnas['total_columnas'] = round(total,2)
            columnas['num'] = count_columna

            columna_weight += total
            columnas_total.append(columnas)
            count_columna += 1

        columna_weight = round(columna_weight, 2)

        tipo_muro_fachada = [
            'Mampostería de bloque de arcilla',
            'Mampostería de bloque de concreto',
            'Mampostería maciza de arcilla',
            'Mampostería maciza de concreto'
        ][int(response_weight.get('muro_fachada')[0])]
        muro_caracteristica = response_weight.get('muro_caracteristica')
        espesor = response_weight.get('espesor')
        m2_muros = float(response_weight.get('m2_muros')[0])
        weight_muro = eval(muro_caracteristica[0])[int(espesor[0])]*m2_muros
        valor_nsr_10 = eval(muro_caracteristica[0])[int(espesor[0])]

        muro_fachada = {
            'tipo_muro': tipo_muro_fachada,
            'valor_nsr_10': valor_nsr_10,
            'm2_muros': m2_muros,
            'weight_muro':round(weight_muro, 2)
        }


        tipo_mamposteria = [
            'Mampostería de bloque de arcilla',
            'Mampostería de bloque de concreto',
            'Mampostería maciza de arcilla',
            'Mampostería maciza de concreto',
        ][int(response_weight.get('muro_divisorio')[0])]

        muro_caracteristica_divisorio = response_weight.get('muro_caracteristica_divisorio')
        espesor_divisorio = response_weight.get('espesor_divisorio')
        m2_muros_divisorio = float(response_weight.get('m2_muros_divisorio')[0])
        weight_divisorio = eval(muro_caracteristica_divisorio[0])[int(espesor_divisorio[0])]*m2_muros_divisorio
        valor_nsr_10 = eval(muro_caracteristica_divisorio[0])[int(espesor_divisorio[0])]

        muro_divisorio = {
            'tipo_muro': tipo_mamposteria,
            'valor_nsr_10': valor_nsr_10,
            'm2_muros': m2_muros_divisorio,
            'weight_muro':round(weight_divisorio, 2)
        }


        type_particiones = response_weight.get('type_particiones')
        m2_particiones = response_weight.get('m2_particiones')
        particiones = {}
        weight_particiones = 0

        if  m2_particiones:
            m2_particiones = float(m2_particiones[0])
            weight_particiones = float(type_particiones[0])*m2_particiones

            name_particiones = {
                0.5:'Particiones móviles de acero (altura parcial)',
                0.2:'Particiones móviles de acero (altura total)',
                0.9:'Poste en madera o acero, yeso de 12 mm a cada lado'
            }

            particiones = {
                'tipo_particiones': name_particiones[float(type_particiones[0])],
                'valor_nsr_10': float(type_particiones[0]),
                'm2_particiones': m2_particiones,
                'weight_particiones': round(weight_particiones,2)

            }



        name_ventanas = {
            0.5:"Muros cortina de vidrio, entramado y marco",
            0.45:"Ventanas, vidrio, entramado y marco"
        }

        type_ventanas = response_weight.get('type_ventanas')
        m2_ventanas = response_weight.get('m2_ventanas')
        ventanas = {}
        weight_ventanas = 0
        if m2_ventanas:

            m2_ventanas = float(response_weight.get('m2_ventanas')[0])
            weight_ventanas = float(type_ventanas[0])*m2_ventanas

            ventanas = {
                'tipo_ventanas': name_ventanas[float(type_ventanas[0])],
                'm2_ventanas': m2_ventanas,
                'valor_nsr_10': float(type_ventanas[0]),
                'weight_ventanas': round(weight_ventanas, 2)
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
        cubierta_weight = 0
        cubierta = {}
        if m2_cubierta:
            m2_cubierta = float(response_weight.get('m2_cubierta')[0])

            if espesor_cubierta:
                cubierta_weight = float(type_cubierta[0])*float(espesor_cubierta[0])*m2_cubierta
            else:
                cubierta_weight = float(type_cubierta[0])*m2_cubierta

            cubierta = {
                'tipo_cubierta': name_cubierta[float(type_cubierta[0])],
                'valor_nsr_10': float(type_cubierta[0]),
                'm2_cubierta': m2_cubierta,
                'cubierta_weight': round(cubierta_weight, 2)

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
        piso = {}
        piso_weight = 0

        if m2_pisos:
            m2_pisos = float(response_weight.get('m2_pisos')[0])
            if espesor_piso:
                piso_weight = float(type_piso[0])*float(espesor_piso[0])*m2_pisos
            else:
                piso_weight = float(type_piso[0])*m2_pisos

            piso = {
                'tipo_piso': name_piso[float(type_piso[0])],
                'valor_nsr_10': float(type_piso[0]),
                'm2_pisos': m2_pisos,
                'piso_weight': round(piso_weight, 2)
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
        recubrimiento_weight = 0
        recubrimiento = {}

        if m2_recubrimiento:
            m2_recubrimiento = float(response_weight.get('m2_recubrimiento')[0])

            if espesor_recubrimiento:
                recubrimiento_weight = float(type_recubrimiento[0])*float(espesor_recubrimiento[0])*m2_recubrimiento
            else:
                recubrimiento_weight = float(type_recubrimiento[0])*m2_recubrimiento

            recubrimiento = {
                'tipo_recubrimiento': name_recubrimiento[float(type_recubrimiento[0])],
                'valor_nsr_10': float(type_recubrimiento[0]),
                'm2_recubrimiento': m2_recubrimiento,
                'recubrimiento_weight': round(recubrimiento_weight,2)
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
        enchape = {}
        enchape_weight = 0
        if m2_enchape:

            m2_enchape = float(response_weight.get('m2_enchape')[0])
            enchape_weight = float(type_enchape[0])*float(espesor_enchape[0])*m2_enchape

            enchape = {
                'tipo_enchape': name_enchape[float(type_enchape[0])],
                'valor_nsr_10': float(type_enchape[0]),
                'm2_enchape': m2_enchape,
                'enchape_weight': round(enchape_weight,2)
            }




        name_ocupacion = {
        "0": "Oficinas",
        "1": "Educativos",
        "2": "Comercio",
        "3": "Residencial",
        "4": "Almacenamiento",
        "5": "Garajes",
        }[response_weight.get('ocupacion')[0]]


        ocupacion_uso = response_weight.get('ocupacion_uso')
        m2_ocupacion = float(response_weight.get('m2_ocupacion')[0])
        ocupacion_weight = float(ocupacion_uso[0])*m2_ocupacion

        ocupacion = {
            'tipo_ocupacion': name_ocupacion,
            'valor_nsr_10': float(ocupacion_uso[0]),
            'm2_ocupacion': m2_ocupacion,
            'ocupacion_weight': round(ocupacion_weight, 2)
        }


        name_cubierta_viva = {
            1: "Cubiertas, Azoteas y Terrazas",
            5.0: "Cubiertas usadas para jardines de cubierta o para reuniones",
            0.35: "Cubiertas inclinadas con más de 15° de pendiente en estructura metálica o de madera con imposibilidad física de verse sometidas a cargas superiores a la aquí estipulada",
            0.5: "Cubiertas  inclinadas  con  pendiente  de  15°  o menos  en estructura metálica o de madera con imposibilidad física de verse sometidas a cargas superiores a la aquí estipulada",
        }
        cubierta_viva = response_weight.get('cubierta_viva')
        m2_cubierta_viva = float(response_weight.get('m2_cubierta_viva')[0])
        cubierta_viva_weight = float(cubierta_viva[0])*m2_cubierta_viva

        cubierta_viva = {
            'tipo_cubierta': name_cubierta_viva[float(cubierta_viva[0])],
            'valor_nsr_10': float(cubierta_viva[0]),
            'm2_cubierta_viva': m2_cubierta_viva,
            'cubierta_viva_weight': round(cubierta_viva_weight, 2)
        }

        weight_life = ocupacion_weight + cubierta_viva_weight

        form = ProfileForm(request.POST, request.FILES)
        form.is_valid()
        data = form.cleaned_data

        user = request.user
        val_irregular_long = 1
        val_irregular_plant = 1

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
                    'status': 'error'
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

        fuerzas_horizontales = {

                1:" Paneles de cortante de madera", 2:"Muros de concreto con capacidad especial de disipación de energía (DES)", 3:" Muros de concreto con capacidad moderada de disipación de energía (DMO)", 4:"Muros de concreto con capacidad mínima de disipación de energía (DMI)", 5:" Muros de mampostería reforzada de bloque de perforación vertical (DES) con todas las celdas rellenas" , 6:"Muros de mampostería reforzada de bloque de perforación vertical (DMO)" , 7:"Muros de mampostería parcialmente reforzada de bloque de perforación vertical" , 8:"Muros de mampostería confinada" , 9:"Muros de mampostería de cavidad reforzada" , 10:"Muros de mampostería no reforzada (no tiene capacidad de disipación de energía)" , 11:"Pórticos de acero estructural con diagonales concéntricas (DES)" , 12:"Pórticos con diagonales de concreto con capacidad moderada de disipación de energía (DMO)", 13:"Pórticos de madera con diagonales",
                14:"Pórticos de acero con diagonales excéntricas si las conexiones con las columnas por fuera del vínculo son resistentes a momento", 15:"Pórticos de acero con diagonales excéntricas si las conexiones con las columnas por fuera del vínculo no son resistentes a momento", 16:"Pórticos de acero con diagonales excéntricas si el vínculo no se conecta a la columna", 17:"Pórticos de acero con diagonales excéntricas si el vínculo tiene conexión resistente a momento con la columna", 18:"Muros de concreto con capacidad especial de disipación de energía (DES)", 19:"Muros de concreto con capacidad moderada de disipación de energía (DMO)", 20:"Muros de concreto con capacidad mínima de disipación de energía (DMI)", 21:"Muros de mampostería reforzada de bloque de perforación vertical (DES) con todas las celdas rellenas", 22:"Muros de mampostería reforzada de bloque de perforación vertical (DMO)", 23:"Muros de mampostería confinada (DMO — capacidad moderada de disipación de energía", 24:"Muros de mampostería de cavidad reforzada  (DES — capacidad especial de disipación de energía)", 25:"Muros de cortante con placa de acero (DES)", 26:"Muros de cortante compuestos con placa de acero y concreto", 27:"Muros de concreto reforzado (DES) mixtos con elementos de acero", 28:"Muros de concreto reforzado (DMO) mixtos con elementos de acero", 29:"Muros de concreto reforzado (DMI ) mixtos con elementos de acero", 30:"Pórticos de acero con diagonales concéntricas (DES)", 31:"Pórticos de acero con diagonales concéntricas (DMI)", 32:"Pórticos mixtos con diagonales concéntricas (DES)", 33:"Pórticos mixtos con diagonales concéntricas (DMI)", 34:"Pórticos de acero con diagonales concéntricas restringidas a pandeo, con conexiones viga-columna resistentes a momento", 35:"Pórticos de acero con diagonales concéntricas restringidas a pandeo, con conexiones viga-columna no resistentes a momento", 36:"Pórticos de concreto con diagonales concéntricas con capacidad moderada de disipación de energía (DMO)",
                37:"Pórticos resistentes a momentos con capacidad especial de disipación de energía (DES) De concreto", 38:"Pórticos resistentes a momentos con capacidad especial de disipación de energía (DES) De acero", 39:"Pórticos resistentes a momentos con capacidad especial de disipación de energía (DES) Mixtos", 40:"Pórticos resistentes a momentos con capacidad especial de disipación de energía (DES) De acero con cerchas dúctiles", 41:"Pórticos resistentes a momentos con capacidad moderada de disipación de energía (DMO) De concreto", 42:"Pórticos resistentes a momentos con capacidad moderada de disipación de energía (DMO) De acero", 43:"Pórticos resistentes a momentos con capacidad moderada de disipación de energía (DMO) Mixtos  con  conexiones  rígidas", 44:"Pórticos resistentes a momentos con capacidad mínima de disipación de energía (DMI) De concreto", 45:"Pórticos resistentes a momentos con capacidad mínima de disipación de energía (DMI) De acero", 46:"Pórticos resistentes a momentos con capacidad mínima de disipación de energía (DMI) Mixtos con conexiones totalmente restringidas a momento", 47:"Pórticos resistentes a momentos con capacidad mínima de disipación de energía (DMI) Mixtos con conexiones parcialmente restringidas a momento", 48:"Pórticos resistentes a momentos con capacidad mínima de disipación de energía (DMI) De acero con cerchas no dúctiles", 49:"Pórticos resistentes a momentos con capacidad mínima de disipación de energía (DMI) De acero con perfiles de lámina doblada en frío y perfiles tubulares estructurales PTE que no cumplen los requisitos de F.2.2.4 para perfiles no esbeltos", 50:"Pórticos losa-columna (incluye reticular celulado) De concreto con capacidad moderada de disipación de energía (DMO)", 51:"Pórticos losa-columna (incluye reticular celulado) De concreto con capacidad mínima de disipación de energía (DMI)", 52:"Estructuras de péndulo invertido, Pórticos de acero resistentes a momento con capacidad especial de disipación de energía (DES)", 53:"Estructuras de péndulo invertido, Pórticos de concreto con capacidad especial de disipación de energía (DES)", 54:"Estructuras de péndulo invertido, Pórticos de acero resistentes a momento con capacidad moderada de disipación de energía (DMO)",
                55:"Muros de concreto con capacidad especial de disipación de energía (DES)",56:"Muros de concreto con capacidad moderada de disipación de energía (DMO)",57:"Muros de mampostería reforzada de bloque de perforación vertical (DES) con todas las celdas rellenas",58:"Muros de mampostería reforzada de bloque de perforación vertical (DMO)",59:"Muros de cortante con placa de acero (DES)",60:"Muros de cortante mixtos con placa de acero",61:"Muros de concreto reforzado (DES) mixtos con elementos de acero",62:"Muros de concreto reforzado (DMI) mixtos con elementos de acero",63:"Pórticos de acero con diagonales excéntricas si las conexiones con las columnas por fuera del vínculo son resistentes a momento",64:"Pórticos de acero con diagonales excéntricas si las conexiones con las columnas por fuera del vínculo no son resistentes a momento",61:"Muros de concreto reforzado (DES) mixtos con elementos de acero",62:"Muros de concreto reforzado (DMI) mixtos con elementos de acero",63:"Pórticos de acero con diagonales excéntricas si las conexiones con las columnas por fuera del vínculo son resistentes a momento",64:"Pórticos de acero con diagonales excéntricas si las conexiones con las columnas por fuera del vínculo no son resistentes a momento",65:"De acero con capacidad especial de disipación de energía (DES)",66:"De acero con capacidad mínima de disipación de energía (DMI)",67:"De concreto con capacidad moderada de disipación de energía (DMO)",68:"Pórticos mixtos con diagonales concéntricas (DES)",69:"Pórticos de acero con diagonales concéntricas restringidas al pandeo",70:"Pórticos de acero con diagonales concéntricas (DES)",71:"Pórticos mixtos con diagonales concéntricas (DES)",72:"Pórticos con diagonales concéntricas que resistan solo a tensión",

        }

        fuerzas_verticales = {
            1:{3.0:"Muros ligeros de madera laminada", 'ausencia': 0.75},
            2:{5.0: "El mismo", 'ausencia': 1},
            3:{4.0: "El mismo", 'ausencia': 1},
            4:{2.5: "El mismo", 'ausencia': 1},
            5:{3.5: "El mismo", 'ausencia': 1},
            6:{2.5: "El mismo", 'ausencia': 0.75},
            7:{2.0: "El mismo", 'ausencia': 0.75},
            8:{2.0: "El mismo", 'ausencia': 0.75},
            9:{4.0: "El mismo", 'ausencia': 0.75},
            10:{1.0: "El mismo", 'ausencia': 0.75},
            11:{5.0: "El mismo", 'ausencia': 1},
            12:{3.5: "El mismo", 'ausencia': 1},
            13:{2.0: "El mismo", 'ausencia': 1},

            14:{7.0:"pórticos de acero resistentes a momentos con capacidad mínima de disipación de energía (DMI)", 'ausencia': 1},
            15:{6.0:"pórticos de acero resistentes a momentos con capacidad mínima de disipación de energía (DMI)", 'ausencia': 1},
            16:{6.0:"pórticos de acero no resistentes a momentos" , 'ausencia': 1},
            17:{5.0: "pórticos de acero resistentes a momentos con capacidad mínima de disipación de energía (DMI)" , 'ausencia': 1},

            18:{7.0: "pórticos de concreto con capacidad especial de disipación de energía (DES)" , 'ausencia': 1},
            19:{
                5.0:"pórticos de concreto con capacidad moderada de disipación de energía (DMO)",
                3.5:"pórticos losa-columna con capacidad moderada de disipación de energía (DMO)" ,
                'ausencia':1},
            20:{
                2.5:"pórticos de concreto con capacidad mínima de disipación de energía (DMI)",
                2.0:"pórticos losa-columna con capacidad mínima de disipación de energía (DMI)" ,
                'ausencia':1},

            21:{4.5:"pórticos de concreto con capacidad especial de disipación de energía (DES)" ,
            'ausencia':0.75},
            22:{
                3.5:"pórticos de concreto con capacidad especial de disipación de energía (DES)",
                2.5:"pórticos de concreto con capacidad moderada de disipación de energía (DMO)"
                , 'ausencia': 0.75},
            23:{
                2.0:"pórticos de concreto con capacidad moderada de disipación de energía (DMO)",
                2.0:"pórticos de concreto con capacidad mínima de disipación de energía (DMI)"
                , 'ausencia':0.75},
            24:{
                4.0:"pórticos de concreto con capacidad moderada de disipación de energía (DMO)",
                2.0:"pórticos de concreto con capacidad mínima de disipación de energía (DMI)"
                , 'ausencia': 0.75},

            25:{7.0:"pórticos de acero resistente o no a momentos" , 'ausencia': 1},
            26:{6.5:"pórticos de acero resistente o no a momentos" , 'ausencia': 1},
            27:{6.0:"pórticos de acero resistente o no a momentos" , 'ausencia': 1},
            28:{5.5: "pórticos de acero resistente o no a momentos" , 'ausencia': 1},
            29:{5.0: "pórticos de acero resistente o no a momentos" , 'ausencia': 1},
            30:{5.0:"pórticos de acero no resistentes a momentos" , 'ausencia': 1},
            31:{4.0:"pórticos de acero no resistentes a momentos" , 'ausencia': 1},
            32:{5.0:"pórticos de acero resistentes o no a momentos" , 'ausencia': 1},
            33:{3.0: "pórticos de acero resistentes o no a momentos" , 'ausencia': 1},
            34:{7.0: "pórticos de acero no resistentes a momentos" , 'ausencia': 1},
            35:{6.0: "pórticos de acero no resistentes a momentos" , 'ausencia': 1},
            36:{6.0: "pórticos de concreto con capacidad moderada de disipación de energía (DMO)" , 'ausencia':1},

            37:{7.0:"El mismo" , 'ausencia': 1},
            38:{7.0:"El mismo" , 'ausencia': 1},
            39:{7.0:"Pórticos de acero o mixtos resistentes o no a momentos" , 'ausencia': 1},
            40:{6.0:"Pórticos de acero resistentes o no a momentos" , 'ausencia': 1},
            41:{5.0: "El mismo" , 'ausencia': 1},
            42:{5.0: "El mismo" , 'ausencia': 1},
            43:{5.0: "Pórticos de acero o mixtos resistentes o no a momentos" , 'ausencia': 1},
            44:{2.5: "El mismo" , 'ausencia': 1},
            45:{3.0: "El mismo" , 'ausencia': 1},
            46:{3.0: "Pórticos de acero o mixtos resistentes o no a momentos" , 'ausencia': 1},
            47:{6.0: "Pórticos de acero o mixtos resistentes o no a momentos" , 'ausencia': 1},
            48:{1.5: "El mismo" , 'ausencia': 1},
            49:{1.5: "El mismo" , 'ausencia': 1},
            50:{2.5: "El mismo" , 'ausencia': 1},
            51:{1.5: "El mismo" , 'ausencia': 1},
            52:{2.5:"El mismo" , 'ausencia': 1},
            53:{2.5:"El mismo" , 'ausencia': 1},
            54:{1.5:"El mismo" , 'ausencia': 1},


            55:{
                8.0:"pórticos de concreto con capacidad especial de disipación de energía (DES)",
                8.0:"pórticos de acero resistentes a momentos con capacidad especial de disipación de energía (DES)" ,
                'ausencia':1
            },
            56:{
                6.0:"pórticos de concreto con capacidad moderada de disipación de energía (DMO)",
                6.0:"pórticos de acero resistentes a momentos con capacidad moderada de disipación de energía (DMO)" ,
                'ausencia': 1},
            57:{
                5.5:"pórticos de concreto con capacidad especial de disipación de energía (DES)",
                5.5:"pórticos de acero resistentes a momentos con capacidad especial de disipación de energía (DES)" ,
                'ausencia': 0.75},
            58:{
                4.5:"pórticos de concreto con capacidad especial de disipación de energía (DES)",
                4.5:"pórticos de acero resistentes a momentos con capacidad especial de disipación de energía (DES)",
                3.5:"pórticos de acero resistentes a momentos con capacidad moderada de disipación de energía (DMO)",
                3.5:"pórticos de concreto con capacidad moderada de disipación de energía (DMO)" ,
                'ausencia': 0.75
            },
            59:{7.0:"pórticos de acero con alma llena, con conexiones rígidas (DES)" , 'ausencia': 1},
            60:{6.5:"pórticos de acero con alma llena, con conexiones rígidas (DES)" , 'ausencia': 1},
            61:{6.0:"pórticos de acero con alma llena, con conexiones rígidas (DES)" , 'ausencia': 1},

            62:{5.0:"pórticos de acero con alma llena, con conexiones rígidas (DES)",
            4.0:"pórticos de acero con alma llena, con conexiones rígidas (DMO)" ,
             'ausencia': 1},
            63:{
                8.0:"pórticos de acero resistentes a momentos con capacidad especial de disipación de energía (DES)",
                6.0:"pórticos de acero resistentes a momentos con capacidad moderada de disipación de energía (DMO)" ,
            'ausencia':1},

            64:{7.0:"pórticos de acero resistentes a momentos con capacidad especial de disipación de energía (DES)",
            5.0:"pórticos de acero resistentes a momentos con capacidad moderada de disipación de energía (DMO)" ,
            'ausencia':1},



            65:{6.0:"pórticos de acero resistentes a momentos con capacidad especial de disipación de energía (DES)" , 'ausencia':1},
            66:{3.0:"pórticos de acero resistentes a momentos con capacidad moderada de disipación de energía (DMO)" , 'ausencia':1},
            67:{4.0:"pórticos de concreto con capacidad moderada de disipación de energía (DMO)" , 'ausencia':1},
            68:{6.0:"pórticos de acero con alma llena con conexiones rígidas (DES)" , 'ausencia':1},
            69:{7.0:"pórticos de acero con alma llena con conexiones rígidas (DES)" , 'ausencia':1},
            70:{6.0:"pórticos de acero con alma llena con conexiones rígidas (DMO)" , 'ausencia':1},
            71:{5.5:"pórticos de acero con alma llena con conexiones rígidas (DMO)" , 'ausencia':1},
            72:{3.0:"El mismo", 'ausencia': 1}
        }

        fuerzas_verticalees = {"Muros_de_carga":{}, "Sistema_combinado":{},"Sistema_portico":{}, "Sistema_dual":{}}
        weight_death = round((columna_weight + viga_weight + placa_weight + enchape_weight + recubrimiento_weight + piso_weight + cubierta_weight + weight_ventanas + weight_particiones + weight_divisorio  + weight_muro), 2)
        weight_other = round((enchape_weight + recubrimiento_weight + piso_weight + cubierta_weight + weight_ventanas + weight_particiones + weight_divisorio  + weight_muro),2)
        weight_all = round((weight_life + weight_death),2)


        r0 = float(data['fuerzas_verticales'])
        val_irregular_plant
        val_irregular_long
        ausencia = fuerzas_verticales[int(data['fuerzas_horizontales'])]['ausencia']

        Aa=0.15
        Av=0.20
        Ae=0.13

        r_prima = r0*val_irregular_plant*val_irregular_long*ausencia
        Cu = 1.75-(1.2*Av*fv)
        if Cu < 1.2:
            Cu = 1.2

        value_sistema = response_weight.get('value_sistema_estructural')[0]
        name_sistema = {
            '1':{'ct': 0.047, 'alpha': 0.9},
            '2':{'ct': 0.072, 'alpha': 0.8},
            '3':{'ct': 0.073, 'alpha': 0.75},
            '4':{'ct': 0.049 , 'alpha': 0.75},
            '5':{'ct': 0.06, 'alpha': 1}
        }
        Ct = name_sistema[value_sistema]['ct']
        Alpha = name_sistema[value_sistema]['alpha']
        H = data['height_floors']*data['floors']

        Ta = Ct*(H**Alpha)


        Cu_Ta = Cu*Ta
        To = (0.1*(Av*fv))/(Aa*fa)
        Tc = (0.48*(Av*fv))/(Aa*fa)

        Tl = 2.4*fv

        T = Ta
        if T <= 0.5:
            k = 1
        elif 0.5 >= T <= 2.5:
            k = 0.75+(0.5*T)
        else:
            k = 2.5
        I = data['type_property']
        T_x = [0.00, 0.06, 0.11, 0.17, 0.23, 0.28, 0.34, 0.40, 0.45, 0.51, 0.57, 0.62, 0.68, 0.74, 0.79, 0.85, 0.91, 0.96, 1.02, 1.08, 1.13, 1.19, 1.25, 1.30, 1.36, 1.41, 1.47, 1.53, 1.58, 1.64, 1.70, 1.75, 1.81, 1.87, 1.92, 1.98, 2.04, 2.09, 2.15, 2.21, 2.26, 2.32, 2.38, 2.43, 2.49]
        Sa_list = []
        Sa_all = {}

        for num, x in enumerate(T_x):

            if x <= T:
                Sa_all[f'Sa_{num}'] = 2.5*Aa*fa*I*(0.4 + (0.6*x)/T)
            if T <= x < Tc:
                Sa_all[f'Sa_{num}'] = 2.5*Aa*fa*I
            if Tc <= x < Tl:
                Sa_all[f'Sa_{num}'] = (1.2*Aa*fv*I)/x
            if Tl <= x:

                Sa_all[f'Sa_{num}'] = (1.2*Aa*fv*Tl*I)/x*x

        Sa = max(Sa_all.values())
        Vs = weight_all*Sa
        E = Vs/r_prima

        return render(
            request,
            'nsr_resutl.html',
            {
                'height':H,
                'fuerza_horizontal':fuerzas_horizontales[int(data['fuerzas_horizontales'])],
                'fuerza_vertical':fuerzas_verticales[int(data['fuerzas_horizontales'])][float(data['fuerzas_verticales'])],
                'type_construccion':data['type_construccion'].replace('_',' '),
                'grupo':group_use[data['type_property']],
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
                'weight_death': weight_death,
                'weight_life': weight_life,
                'weight_all': weight_all,
                'placa_all': placa_all,
                'densidad_concreto': f'{DENSIDAD} kg/m3',
                'weight_other': weight_other,
                'T_x':T_x,
                'Sa_list':Sa_list,
                'Sa_0': Sa_all['Sa_0'],
                'Sa_1': Sa_all['Sa_1'],
                'Sa_2': Sa_all['Sa_2'],
                'Sa_3': Sa_all['Sa_3'],
                'Sa_4': Sa_all['Sa_4'],
                'Sa_5': Sa_all['Sa_5'],
                'Sa_6': Sa_all['Sa_6'],
                'Sa_7': Sa_all['Sa_7'],
                'Sa_8': Sa_all['Sa_8'],
                'Sa_9': Sa_all['Sa_9'],
                'Sa_10': Sa_all['Sa_10'],
                'Sa_11': Sa_all['Sa_11'],
                'Sa_12': Sa_all['Sa_12'],
                'Sa_13': Sa_all['Sa_13'],
                'Sa_14': Sa_all['Sa_14'],
                'Sa_15': Sa_all['Sa_15'],
                'Sa_16': Sa_all['Sa_16'],
                'Sa_17': Sa_all['Sa_17'],
                'Sa_18': Sa_all['Sa_18'],
                'Sa_19': Sa_all['Sa_19'],
                'Sa_20': Sa_all['Sa_20'],
                'Sa_21': Sa_all['Sa_21'],
                'Sa_22': Sa_all['Sa_22'],
                'Sa_23': Sa_all['Sa_23'],
                'Sa_24': Sa_all['Sa_24'],
                'Sa_25': Sa_all['Sa_25'],
                'Sa_26': Sa_all['Sa_26'],
                'Sa_27': Sa_all['Sa_27'],
                'Sa_28': Sa_all['Sa_28'],
                'Sa_29': Sa_all['Sa_29'],
                'Sa_30': Sa_all['Sa_30'],
                'Sa_31': Sa_all['Sa_31'],
                'Sa_32': Sa_all['Sa_32'],
                'Sa_33': Sa_all['Sa_33'],
                'Sa_34': Sa_all['Sa_34'],
                'Sa_35': Sa_all['Sa_35'],
                'Sa_36': Sa_all['Sa_36'],
                'Sa_37': Sa_all['Sa_37'],
                'Sa_38': Sa_all['Sa_38'],
                'Sa_39': Sa_all['Sa_39'],
                'Sa_40': Sa_all['Sa_40'],
                'Sa_41': Sa_all['Sa_41'],
                'Sa_42': Sa_all['Sa_42'],
                'Sa_43': Sa_all['Sa_43'],
                'Sa_44': Sa_all['Sa_44'],
                'To': round(To, 2),
                'Tc': round(Tc, 2),
                'Tl': round(Tl, 2),
                'T': round(T, 2),
                'K':round(k, 2),
                'Sa': round(Sa, 2),
                'Vs': round(Vs,2),
                'E': round(Vs*r_prima,2),
                'r_prima': round(r_prima, 2)
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
    template_name = 'ais.html'
    context_object_name = 'aisprocess'

    def get_context_data(self, *arglas, **kwargs):
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


class Indice(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'indice.html')
    def post(self, request, *args, **kwargs):
        form = IndiceForm(request.POST)

        calification_1 = {0: 'A', 5: 'B', 25:'C', 45:'D'}
        calification_2 = {0: 'A', 5: 'B', 20:'C', 45:'D'}
        calification_3 = {0: 'A', 5: 'B', 15:'C', 45:'D'}
        calification_4 = {0: 'A', 15: 'B', 25:'C', 45:'D'}
        calification_5 = {0: 'A', 0: 'B', 25:'C', 45:'D'}

        if form.is_valid():
            data = form.cleaned_data
            organization = data['organization']
            quality = data['quality']
            number_of_floors = data['number_of_floors']
            cover_area = data['cover_area']
            area_x = data['area_x']
            area_y = data['area_y']
            height = data['height']
            diaphragm_thickness = data['diaphragm_thickness']
            mamposteria = data['mamposteria']
            position = data['position']
            diaphragm = data['diaphragm']
            a = data.get('a')
            b = data.get('b')
            L = data.get('L')
            wall_length = data['wall_length']
            wall_thickness = data['wall_thickness']
            cover_type = data['cover_type']
            elements = data['elements']
            status_conservation = data['status_conservation']


            if number_of_floors == 1:
                area_floor_1 = data['area_floor_1']
                Daa = area_floor_1*100

            if number_of_floors == 2:
                area_floor_1 = data['area_floor_1']
                area_floor_2 = data['area_floor_2']

                Daa = ((area_floor_2 - area_floor_1)/area_floor_1)*100

            if number_of_floors == 3:
                area_floor_1 = data['area_floor_1']
                area_floor_2 = data['area_floor_2']
                area_floor_3 = data['area_floor_3']

                Daa = ((area_floor_2 - area_floor_1)/area_floor_1)*100
                Daa2 = ((area_floor_3 - area_floor_2)/area_floor_2)*100

                Daa = max(Daa, Daa2)

            if number_of_floors == 4:
                area_floor_1 = data['area_floor_1']
                area_floor_2 = data['area_floor_2']
                area_floor_3 = data['area_floor_3']
                area_floor_4 = data['area_floor_4']
                print( area_floor_1, area_floor_2, area_floor_3, area_floor_4)
                print('///////////')
                Daa = ((area_floor_2 - area_floor_1)/area_floor_1)*100
                Daa2 = ((area_floor_3 - area_floor_2)/area_floor_2)*100
                Daa3 = ((area_floor_4 - area_floor_3)/area_floor_3)*100

                Daa = max(Daa, Daa2, Daa3)

            if number_of_floors == 5:
                area_floor_1 = data['area_floor_1']
                area_floor_2 = data['area_floor_2']
                area_floor_3 = data['area_floor_3']
                area_floor_4 = data['area_floor_4']
                area_floor_5 = data['area_floor_5']

                Daa = ((area_floor_2 - area_floor_1)/area_floor_1)*100
                Daa2 = ((area_floor_3 - area_floor_2)/area_floor_2)*100
                Daa3 = ((area_floor_4 - area_floor_3)/area_floor_3)*100
                Daa4 = ((area_floor_5 - area_floor_4)/area_floor_4)*100

                Daa = max(Daa, Daa2, Daa3, Daa4)

            Tk = ((area_x*mamposteria)+(area_y*mamposteria))/(area_x+area_y)
            Ps = 2.4*diaphragm_thickness

            if area_x < area_y:
                A = area_x
                B = area_y
            else:
                A = area_y
                B = area_x
            Ao = A/cover_area
            Y = B/A
            q = (((A+B)*height/cover_area)*1.85) + Ps
            C = ((Ao*Tk)/(q*height))* ((1+((q*height)/(1.5*Ao*Tk*(1+Y))))**0.5)
            alpha = C/0.15


            if alpha >= 1:
                resistance = 0
            elif 0.6 <= alpha < 1:
                resistance = 5
            elif 0.4 <= alpha < 0.6:
                resistance = 25
            elif alpha < 0.4:
                resistance = 45

            B1 = ''
            B2 = ''
            if a and not b:
                B1 = a/L

                if B1 >= 0.8:
                    plan_configuration = 0
                elif 0.8 > B1 >= 0.6:
                    plan_configuration = 5
                elif 0.6 > B1 >= 0.4:
                    plan_configuration = 25
                elif 0.4 > B1:
                    plan_configuration = 45

                B1 = round(B1,2)

            elif b and not a:
                B2 = b/L

                if B2 < 0.1:
                    plan_configuration = 0
                elif 0.1 < B2 <= 0.2:
                    plan_configuration = 5
                elif 0.2 < B2 <= 0.3:
                    plan_configuration = 25
                elif 0.3 < B2:
                    plan_configuration = 45

                B2 = round(B2,2)
            else:
                B1 = a/L
                B2 = b/L

                if B1 >= 0.8 or B2 < 0.1:
                    plan_configuration = 0
                elif 0.8 > B1 >= 0.6 or 0.1 < B2 <= 0.2:
                    plan_configuration = 5
                elif 0.6 > B1 >= 0.4 or 0.2 < B2 <= 0.3:
                    plan_configuration = 25
                elif 0.4 > B1 or 0.3 < B2:
                    plan_configuration = 45

                B1 = round(B1,2)
                B2 = round(B2,2)



            print(Daa)
            print('/////////////////////////////////')
            if Daa < 0 and abs(Daa) < 10:
                elevation_configuration = 0
            elif Daa < 0 and  10 <= abs(Daa) < 20:
                elevation_configuration = 5
            elif Daa < 0 and abs(Daa) >= 20:
                elevation_configuration = 25
            elif Daa >= 0:
                elevation_configuration = 45


            Ls = wall_length/wall_thickness

            if Ls < 15:
                maximum_distance = 0
            elif 15 <= Ls < 18:
                maximum_distance = 5
            elif 18 <= Ls < 25:
                maximum_distance = 25
            elif Ls >= 25:
                maximum_distance = 45


            score_1 = organization*1
            score_2 = quality*0.25
            score_3 = resistance*1.5
            score_4 = position*0.75
            score_5 = diaphragm*1
            score_6 = plan_configuration*0.5
            score_7 = elevation_configuration*1
            score_8 = maximum_distance*0.25
            score_9 = cover_type*1
            score_10 = elements*0.25
            score_11 = status_conservation*1

            total = (
                score_1 +
                score_2 +
                score_3 +
                score_4 +
                score_5 +
                score_6 +
                score_7 +
                score_8 +
                score_9 +
                score_10 +
                score_11
            )

            total_porcentage = total/382.5*100
            return render(
                request,
                'indice_result.html',
                {
                    'calification_1':calification_2[organization],
                    'calification_2':calification_1[quality],
                    'calification_3':calification_1[resistance],
                    'calification_4':calification_1[position],
                    'calification_5':calification_3[diaphragm],
                    'calification_6':calification_1[plan_configuration],
                    'calification_7':calification_1[elevation_configuration],
                    'calification_8':calification_1[maximum_distance],
                    'calification_9':calification_4[cover_type],
                    'calification_10':calification_5[elements],
                    'calification_11':calification_1[status_conservation],
                    'score_1':round(score_1),
                    'score_2':round(score_2),
                    'score_3':round(score_3),
                    'score_4':round(score_4),
                    'score_5':round(score_5),
                    'score_6':round(score_6),
                    'score_7':round(score_7),
                    'score_8':round(score_8),
                    'score_9':round(score_9),
                    'score_10':round(score_10),
                    'score_11':round(score_11),
                    'total': round(total, 3),
                    'number_of_floors': number_of_floors,
                    'cover_area': round(cover_area, 1),
                    'area_x': round(area_x, 1),
                    'area_y': round(area_y, 1),
                    'height': round(height, 1),
                    'Tk': round(Tk, 1),
                    'mamposteria': round(mamposteria, 1),
                    'B1': B1,
                    'B2': B2,
                    'Daa': round(Daa,1),
                    'Ls': round(Ls),
                    'total_porcentage': round(total_porcentage),
                }
            )

        print(form.errors)
        print('RRRRRRRRRRRRRRRRRRRRRR')
        return render(request, 'indice.html')