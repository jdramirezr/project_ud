$(document).ready(function(){
    $('#type_construccion').html('<option selected></option><option name="Muros_de_carga" value="Muros_de_carga">Muros de carga</option><option name="Sistema_combinado" value="Sistema_combinado">Sistema combinado</option><option name="Sistema_portico" value="Sistema_portico">Sistema portico</option><option name="Sistema_dual" value="Sistema_dual">Sistema dual</option>')
    $('#type_construccion').click(function( date ) {
        event.preventDefault();
        console.log('&&&&&&&&&&&&&&&&&&')
        console.log($('#type_construccion').serialize().split("=")[1])
        if ($('#type_construccion').serialize().split("=")[1] == "Muros_de_carga"){
            $("#fuerzas_verticales").html('<option style="display:none">')
            $("#fuerzas_horizontales").html('<option style="display:none"><option value=1> Paneles de cortante de madera</option><option value=2>Muros de concreto con capacidad especial de disipación de energía (DES)</option><option value=3> Muros de concreto con capacidad moderada de disipación de energía (DMO)</option><option value=4>Muros de concreto con capacidad mínima de disipación de energía (DMI)</option><option value=5> Muros de mampostería reforzada de bloque de perforación vertical (DES) con todas las celdas rellenas</option> <option value=6>Muros de mampostería reforzada de bloque de perforación vertical (DMO)</option> <option value=7>Muros de mampostería parcialmente reforzada de bloque de perforación vertical</option> <option value=8>Muros de mampostería confinada</option> <option value=9>Muros de mampostería de cavidad reforzada</option> <option value=10>Muros de mampostería no reforzada (no tiene capacidad de disipación de energía)</option> <option value=11>Pórticos de acero estructural con diagonales concéntricas (DES)</option> <option value=12>Pórticos con diagonales de concreto con capacidad moderada de disipación de energía (DMO)</option><option value=13>Pórticos de madera con diagonales</option>')

        }
        if ($('#type_construccion').serialize().split("=")[1] == "Sistema_combinado"){
            $("#fuerzas_verticales").html('<option style="display:none">')
            $("#fuerzas_horizontales").html('<option style="display:none"><option value=14>Pórticos de acero con diagonales excéntricas si las conexiones con las columnas por fuera del vínculo son resistentes a momento</option><option value=15>Pórticos de acero con diagonales excéntricas si las conexiones con las columnas por fuera del vínculo no son resistentes a momento</option><option value=16>Pórticos de acero con diagonales excéntricas si el vínculo no se conecta a la columna</option><option value=17>Pórticos de acero con diagonales excéntricas si el vínculo tiene conexión resistente a momento con la columna</option><option value=18>Muros de concreto con capacidad especial de disipación de energía (DES)</option><option value=19>Muros de concreto con capacidad moderada de disipación de energía (DMO)</option><option value=20>Muros de concreto con capacidad mínima de disipación de energía (DMI)</option><option value=21>Muros de mampostería reforzada de bloque de perforación vertical (DES) con todas las celdas rellenas</option><option value=22>Muros de mampostería reforzada de bloque de perforación vertical (DMO)</option><option value=23>Muros de mampostería confinada (DMO — capacidad moderada de disipación de energía</option><option value=24>Muros de mampostería de cavidad reforzada  (DES — capacidad especial de disipación de energía)</option><option value=25>Muros de cortante con placa de acero (DES)</option><option value=26>Muros de cortante compuestos con placa de acero y concreto</option><option value=27>Muros de concreto reforzado (DES) mixtos con elementos de acero</option><option value=28>Muros de concreto reforzado (DMO) mixtos con elementos de acero</option><option value=29>Muros de concreto reforzado (DMI ) mixtos con elementos de acero</option><option value=30>Pórticos de acero con diagonales concéntricas (DES)</option><option value=31>Pórticos de acero con diagonales concéntricas (DMI)</option><option value=32>Pórticos mixtos con diagonales concéntricas (DES)</option><option value=33>Pórticos mixtos con diagonales concéntricas (DMI)</option><option value=34>Pórticos de acero con diagonales concéntricas restringidas a pandeo, con conexiones viga-columna resistentes a momento</option><option value=35>Pórticos de acero con diagonales concéntricas restringidas a pandeo, con conexiones viga-columna no resistentes a momento</option><option value=36>Pórticos de concreto con diagonales concéntricas con capacidad moderada de disipación de energía (DMO)</option>')

        }
        if ($('#type_construccion').serialize().split("=")[1] == "Sistema_portico"){
            $("#fuerzas_verticales").html('<option style="display:none">')
            $("#fuerzas_horizontales").html('<option style="display:none"><option value=37>Pórticos resistentes a momentos con capacidad especial de disipación de energía (DES) De concreto</option><option value=38>Pórticos resistentes a momentos con capacidad especial de disipación de energía (DES) De acero</option><option value=39>Pórticos resistentes a momentos con capacidad especial de disipación de energía (DES) Mixtos</option><option value=40>Pórticos resistentes a momentos con capacidad especial de disipación de energía (DES) De acero con cerchas dúctiles</option><option value=41>Pórticos resistentes a momentos con capacidad moderada de disipación de energía (DMO) De concreto</option><option value=42>Pórticos resistentes a momentos con capacidad moderada de disipación de energía (DMO) De acero</option><option value=43>Pórticos resistentes a momentos con capacidad moderada de disipación de energía (DMO) Mixtos  con  conexiones  rígidas</option><option value=44>Pórticos resistentes a momentos con capacidad mínima de disipación de energía (DMI) De concreto</option><option value=45>Pórticos resistentes a momentos con capacidad mínima de disipación de energía (DMI) De acero</option><option value=46>Pórticos resistentes a momentos con capacidad mínima de disipación de energía (DMI) Mixtos con conexiones totalmente restringidas a momento</option><option value=47>Pórticos resistentes a momentos con capacidad mínima de disipación de energía (DMI) Mixtos con conexiones parcialmente restringidas a momento</option><option value=48>Pórticos resistentes a momentos con capacidad mínima de disipación de energía (DMI) De acero con cerchas no dúctiles</option><option value=49>Pórticos resistentes a momentos con capacidad mínima de disipación de energía (DMI) De acero con perfiles de lámina doblada en frío y perfiles tubulares estructurales PTE que no cumplen los requisitos de F.2.2.4 para perfiles no esbeltos</option><option value=50>Pórticos losa-columna (incluye reticular celulado) De concreto con capacidad moderada de disipación de energía (DMO)</option<option value=51>Pórticos losa-columna (incluye reticular celulado) De concreto con capacidad mínima de disipación de energía (DMI)</option><option value=52>Estructuras de péndulo invertido, Pórticos de acero resistentes a momento con capacidad especial de disipación de energía (DES)</option><option value=53>Estructuras de péndulo invertido, Pórticos de concreto con capacidad especial de disipación de energía (DES)</option><option value=54>Estructuras de péndulo invertido, Pórticos de acero resistentes a momento con capacidad moderada de disipación de energía (DMO)</option>')
        }
        if ($('#type_construccion').serialize().split("=")[1] == "Sistema_dual"){
            $("#fuerzas_verticales").html('<option style="display:none">')
            $("#fuerzas_horizontales").html('<option style="display:none"><option value=55>Muros de concreto con capacidad especial de disipación de energía (DES)</option><option value=56>Muros de concreto con capacidad moderada de disipación de energía (DMO)</option><option value=57>Muros de mampostería reforzada de bloque de perforación vertical (DES) con todas las celdas rellenas</option><option value=58>Muros de mampostería reforzada de bloque de perforación vertical (DMO)</option><option value=59>Muros de cortante con placa de acero (DES)</option><option value=60>Muros de cortante mixtos con placa de acero</option><option value=61>Muros de concreto reforzado (DES) mixtos con elementos de acero</option><option value=62>Muros de concreto reforzado (DMI) mixtos con elementos de acero</option><option value=63>Pórticos de acero con diagonales excéntricas si las conexiones con las columnas por fuera del vínculo son resistentes a momento</option><option value=64>Pórticos de acero con diagonales excéntricas si las conexiones con las columnas por fuera del vínculo no son resistentes a momento</option><option value=61>Muros de concreto reforzado (DES) mixtos con elementos de acero</option><option value=62>Muros de concreto reforzado (DMI) mixtos con elementos de acero</option><option value=63>Pórticos de acero con diagonales excéntricas si las conexiones con las columnas por fuera del vínculo son resistentes a momento</option><option value=64>Pórticos de acero con diagonales excéntricas si las conexiones con las columnas por fuera del vínculo no son resistentes a momento</option><option value=65>De acero con capacidad especial de disipación de energía (DES)</option><option value=66>De acero con capacidad mínima de disipación de energía (DMI)</option><option value=67>De concreto con capacidad moderada de disipación de energía (DMO)</option><option value=68>Pórticos mixtos con diagonales concéntricas (DES)</option><option value=69>Pórticos de acero con diagonales concéntricas restringidas al pandeo</option><option value=70>Pórticos de acero con diagonales concéntricas (DES)</option><option value=71>Pórticos mixtos con diagonales concéntricas (DES)</option><option value=72>Pórticos con diagonales concéntricas que resistan solo a tensión</option>')

        }

    })

    $('#fuerzas_horizontales').click(function( date ) {
        event.preventDefault();
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '1') {
            $("#fuerzas_verticales").html('<option value=3.0>Muros ligeros de madera laminada</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '2') {
            $("#fuerzas_verticales").html('<option value=5.0>El mismo</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '3') {
            $("#fuerzas_verticales").html('<option value=4.0>El mismo</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '4') {
            $("#fuerzas_verticales").html('<option value=2.5>El mismo</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '5') {
            $("#fuerzas_verticales").html('<option value=3.5>El mismo</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '6') {
            $("#fuerzas_verticales").html('<option value=2.5>El mismo</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '7') {
            $("#fuerzas_verticales").html('<option value=2.0>El mismo</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '8') {
            $("#fuerzas_verticales").html('<option value=2.0>El mismo</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '9') {
            $("#fuerzas_verticales").html('<option value=4.0>El mismo</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '10') {
            $("#fuerzas_verticales").html('<option value=1.0>El mismo</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '11') {
            $("#fuerzas_verticales").html('<option value=5.0>El mismo</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '12') {
            $("#fuerzas_verticales").html('<option value=3.5>El mismo</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '13') {
            $("#fuerzas_verticales").html('<option value=2.0>El mismo</option>')
        }




        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '14') {
            $("#fuerzas_verticales").html('<option value=7.0>pórticos de acero resistentes a momentos con capacidad mínima de disipación de energía (DMI)</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '15') {
            $("#fuerzas_verticales").html('<option value=6.0>pórticos de acero resistentes a momentos con capacidad mínima de disipación de energía (DMI)</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '16') {
            $("#fuerzas_verticales").html('<option value=6.0>pórticos de acero no resistentes a momentos</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '17') {
            $("#fuerzas_verticales").html('<option value=5.0>pórticos de acero resistentes a momentos con capacidad mínima de disipación de energía (DMI)</option>')
        }


        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '18') {
            $("#fuerzas_verticales").html('<option value=7.0>pórticos de concreto con capacidad especial de disipación de energía (DES)</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '19') {

            $("#fuerzas_verticales").html('<option style="display:none"><option value=5.0>pórticos de concreto con capacidad moderada de disipación de energía (DMO)</option><option value=3.5>pórticos losa-columna con capacidad moderada de disipación de energía (DMO)</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '20') {
            $("#fuerzas_verticales").html('<option style="display:none"><option value=2.5>pórticos de concreto con capacidad mínima de disipación de energía (DMI)</option><option value=2.0>pórticos losa-columna con capacidad mínima de disipación de energía (DMI)</option>')
        }

        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '21') {
            $("#fuerzas_verticales").html('<option value=4.5>pórticos de concreto con capacidad especial de disipación de energía (DES)</option>')
        }

        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '22') {
            $("#fuerzas_verticales").html('<option style="display:none"><option value=3.5>pórticos de concreto con capacidad especial de disipación de energía (DES)</option><option value=2.5>pórticos de concreto con capacidad moderada de disipación de energía (DMO)</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '23') {
            $("#fuerzas_verticales").html('<option style="display:none"><option value=2.0>pórticos de concreto con capacidad moderada de disipación de energía (DMO)</option><option value=2.0>pórticos de concreto con capacidad mínima de disipación de energía (DMI)</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '24') {
            $("#fuerzas_verticales").html('<option style="display:none"><option value=4.0>pórticos de concreto con capacidad moderada de disipación de energía (DMO)</option><option value=2.0>pórticos de concreto con capacidad mínima de disipación de energía (DMI)</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '25') {
            $("#fuerzas_verticales").html('<option value=7.0>pórticos de acero resistente o no a momentos</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '26') {
            $("#fuerzas_verticales").html('<option value=6.5>pórticos de acero resistente o no a momentos</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '27') {
            $("#fuerzas_verticales").html('<option value=6.0>pórticos de acero resistente o no a momentos</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '28') {
            $("#fuerzas_verticales").html('<option value=5.5>pórticos de acero resistente o no a momentos</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '29') {
            $("#fuerzas_verticales").html('<option value=5.0>pórticos de acero resistente o no a momentos</option>')
        }


        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '30') {
            $("#fuerzas_verticales").html('<option value=5.0>pórticos de acero no resistentes a momentos</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '31') {
            $("#fuerzas_verticales").html('<option value=4.0>pórticos de acero no resistentes a momentos</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '32') {
            $("#fuerzas_verticales").html('<option value=5.0>pórticos de acero resistentes o no a momentos</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '33') {
            $("#fuerzas_verticales").html('<option value=3.0>pórticos de acero resistentes o no a momentos</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '34') {
            $("#fuerzas_verticales").html('<option value=7.0>pórticos de acero no resistentes a momentos</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '35') {
            $("#fuerzas_verticales").html('<option value=6.0>pórticos de acero no resistentes a momentos</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '36') {
            $("#fuerzas_verticales").html('<option value=6.0>pórticos de concreto con capacidad moderada de disipación de energía (DMO)</option>')
        }




        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '37') {
            $("#fuerzas_verticales").html('<option value=7.0>El mismo</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '38') {
            $("#fuerzas_verticales").html('<option value=7.0>El mismo</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '39') {
            $("#fuerzas_verticales").html('<option value=7.0>Pórticos de acero o mixtos resistentes o no a momentos</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '40') {
            $("#fuerzas_verticales").html('<option value=6.0>Pórticos de acero resistentes o no a momentos</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '41') {
            $("#fuerzas_verticales").html('<option value=5.0>El mismo</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '42') {
            $("#fuerzas_verticales").html('<option value=5.0>El mismo</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '43') {
            $("#fuerzas_verticales").html('<option value=5.0>Pórticos de acero o mixtos resistentes o no a momentos</option>')
        }





        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '44') {
            $("#fuerzas_verticales").html('<option value=2.5>El mismo</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '45') {
            $("#fuerzas_verticales").html('<option value=3.0>El mismo</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '46') {
            $("#fuerzas_verticales").html('<option value=3.0>Pórticos de acero o mixtos resistentes o no a momentos</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '47') {
            $("#fuerzas_verticales").html('<option value=6.0>Pórticos de acero o mixtos resistentes o no a momentos</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '48') {
            $("#fuerzas_verticales").html('<option value=1.5>El mismo</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '49') {
            $("#fuerzas_verticales").html('<option value=1.5>El mismo</option>')
        }



        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '50') {
            $("#fuerzas_verticales").html('<option value=2.5>El mismo</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '51') {
            $("#fuerzas_verticales").html('<option value=1.5>El mismo</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '52') {
            $("#fuerzas_verticales").html('<option value=2.5>El mismo</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '53') {
            $("#fuerzas_verticales").html('<option value=2.5>El mismo</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '54') {
            $("#fuerzas_verticales").html('<option value=1.5>El mismo</option>')
        }


        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '55') {
            $("#fuerzas_verticales").html('<option style="display:none"><option value=8.0>pórticos de concreto con capacidad especial de disipación de energía (DES)</option><option value=8.0>pórticos de acero resistentes a momentos con capacidad especial de disipación de energía (DES)</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '56') {
            $("#fuerzas_verticales").html('<option style="display:none"><option value=6.0>pórticos de concreto con capacidad moderada de disipación de energía (DMO)</option><option value=6.0>pórticos de acero resistentes a momentos con capacidad moderada de disipación de energía (DMO)</option>')
        }

        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '57') {
            $("#fuerzas_verticales").html('<option style="display:none"><option value=5.5>pórticos de concreto con capacidad especial de disipación de energía (DES)</option><option value=5.5>pórticos de acero resistentes a momentos con capacidad especial de disipación de energía (DES)</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '58') {
            $("#fuerzas_verticales").html('<option style="display:none"><option value=4.5>pórticos de concreto con capacidad especial de disipación de energía (DES)</option><option value=4.5>pórticos de acero resistentes a momentos con capacidad especial de disipación de energía (DES)</option><option value=3.5>pórticos de acero resistentes a momentos con capacidad moderada de disipación de energía (DMO)</option><option value=3.5>pórticos de concreto con capacidad moderada de disipación de energía (DMO)</option>')
        }


        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '59') {
            $("#fuerzas_verticales").html('<option value=7.0>pórticos de acero con alma llena, con conexiones rígidas (DES)</option>')
        }

        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '60') {
            $("#fuerzas_verticales").html('<option value=6.5>pórticos de acero con alma llena, con conexiones rígidas (DES)</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '61') {
            $("#fuerzas_verticales").html('<option value=6.0>pórticos de acero con alma llena, con conexiones rígidas (DES)</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '62') {
            $("#fuerzas_verticales").html('<option style="display:none"><option value=5.0>pórticos de acero con alma llena, con conexiones rígidas (DES)</option><option value=4.0>pórticos de acero con alma llena, con conexiones rígidas (DMO)</option>')
        }



        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '63') {
            $("#fuerzas_verticales").html('<option style="display:none"><option value=8.0>pórticos de acero resistentes a momentos con capacidad especial de disipación de energía (DES)</option><option value=6.0>pórticos de acero resistentes a momentos con capacidad moderada de disipación de energía (DMO)</option>')
        }

        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '64') {
            $("#fuerzas_verticales").html('<option style="display:none"><option value=7.0>pórticos de acero resistentes a momentos con capacidad especial de disipación de energía (DES)</option><option value=5.0>pórticos de acero resistentes a momentos con capacidad moderada de disipación de energía (DMO)</option>')
        }


        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '65') {
            $("#fuerzas_verticales").html('<option value=6.0>pórticos de acero resistentes a momentos con capacidad especial de disipación de energía (DES)</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '66') {
            $("#fuerzas_verticales").html('<option value=3.0>pórticos de acero resistentes a momentos con capacidad moderada de disipación de energía (DMO)</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '67') {
            $("#fuerzas_verticales").html('<option value=4.0>pórticos de concreto con capacidad moderada de disipación de energía (DMO)</option>')
        }


        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '68') {
            $("#fuerzas_verticales").html('<option value=6.0>pórticos de acero con alma llena con conexiones rígidas (DES)</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '69') {
            $("#fuerzas_verticales").html('<option value=7.0>pórticos de acero con alma llena con conexiones rígidas (DES)</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '70') {
            $("#fuerzas_verticales").html('<option value=6.0>pórticos de acero con alma llena con conexiones rígidas (DMO)</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '71') {
            $("#fuerzas_verticales").html('<option value=5.5>pórticos de acero con alma llena con conexiones rígidas (DMO)</option>')
        }
        if ($('#fuerzas_horizontales').serialize().split("=")[1] == '72') {
            $("#fuerzas_verticales").html('<option value=3.0>El mismo</option>')
        }


    })

    $('.more_information').on('click',function(){
        if ($('#irregular_plant').serialize().split("=")[1] == "Irregularidad_torsional"){
            Swal.fire({text:'La  irregularidad torsional existe cuando en una edificación con diafragma rígido, la máxima deriva de piso de un extremo de la estructura, calculada incluyendo la torsión accidental y medida perpendicularmente a un eje determinado, es más de 1.2 y menor o igual a 1.4 veces la deriva promedio de los dos extremos de la estructura, con respecto al mismo eje de referencia.'})
        }
        if ($('#irregular_plant').serialize().split("=")[1] == "Irregularidad_torsional_extrema"){
            Swal.fire({text:'La irregularidad torsional extrema existe cuando en una edificación con diafragma rígido, la máxima deriva de piso de un  extremo  de  la  estructura,  calculada  incluyendo  la  torsión  accidental  y medida  perpendicularmente  a  un  eje  determinado,  es  más  de  1.4  veces  la deriva promedio de los dos extremos de la estructura, con respecto al mismo eje de referencia.'})
        }
        if ($('#irregular_plant').serialize().split("=")[1] == "Retrocesos_excesivos_en_las_esquinas"){
            Swal.fire({text:'La configuración de una estructura se considera irregular cuando ésta tiene retrocesos excesivos en sus esquinas. Un retroceso en una esquina se considera excesivo cuando las proyecciones de la estructura, a ambos lados del retroceso, son mayores que el 15 por ciento de la dimensión de la planta de la estructura en la dirección del retroceso'})
        }
        if ($('#irregular_plant').serialize().split("=")[1] == "Discontinuidades_en_el_diafragma"){
            Swal.fire({text:'Cuando    el    diafragma    tiene discontinuidades  apreciables  o  variaciones  en  su  rigidez,  incluyendo  las causadas por aberturas, entradas, retrocesos o huecos con áreas mayores al 50  por  ciento  del  área  bruta  del  diafragma  o  existen  cambios  en  la  rigidez efectiva del diafragma de más del 50 por ciento, entre niveles consecutivos, la estructura se considera irregular.'})
        }
        if ($('#irregular_plant').serialize().split("=")[1] == "Desplazamientos_del_plano_de_accion_de_elementos_verticales"){
            console.log('Gfasd')
            Swal.fire({text:'La estructura  se  considera  irregular  cuando  existen  discontinuidades  en  las trayectorias  de  las  fuerzas  inducidas  por  los  efectos  sísmicos,  tales  como cuando se traslada el plano que contiene a un grupo de elementos verticales del  sistema  de  resistencia  sísmica,  en  una  dirección  perpendicular  a  él, generando  un  nuevo  plano.  Los  altillos  o  manzardas  de  un  solo  piso  se eximen de este requisito en la consideración de irregularidad.'})
        }
        if ($('#irregular_plant').serialize().split("=")[1] == "Sistemas_no_paralelos"){
            Swal.fire({text:'Cuando las direcciones de acción horizontal de los elementos  verticales  del  sistema  de  resistencia  sísmica  no  son  paralelas  o simétricas  con  respecto  a  los  ejes  ortogonales  horizontales  principales  del sistema de resistencia sísmica, la estructura se considera irregular.'})
        }



        if ($('#irregular_long').serialize().split("=")[1] == "Piso_flexible_(Irregularidad_en_rigidez)"){
            Swal.fire({text:'Cuando  la  rigidez  ante  fuerzas horizontales de un piso es menor del 70 por ciento pero superior o igual al 60 por  ciento  de  la  rigidez  del  piso  superior  o  menor  del  80  por  ciento  pero superior o igual al 70 por ciento del promedio de la rigidez de los tres pisos superiores, la estructura se considera irregular.'})
        }
        if ($('#irregular_long').serialize().split("=")[1] == "Piso_flexible_(Irregularidad_extrema_en_rigidez)"){
            Swal.fire({text:'Cuando  la rigidez  ante fuerzas horizontales de un piso es menor del 60 por ciento de la rigidez del piso superior o menor del 70 por ciento del promedio de la rigidez de los tres pisos superiores, la estructura se considera irregular.'})
        }
        if ($('#irregular_long').serialize().split("=")[1] == "Irregularidad_en_la_distribucion_de_las_masas"){
            Swal.fire({text:'Cuando la masa, de cualquier piso es mayor que 1.5 veces la masa de uno de los pisos contiguos, la  estructura  se  considera  irregular.  Se  exceptúa  el  caso  de  cubiertas  que sean más livianas que el piso de abajo.'})
        }
        if ($('#irregular_long').serialize().split("=")[1] == "Irregularidad_geometrica"){
            Swal.fire({text:'Cuando la dimensión horizontal del sistema de resistencia  sísmica  en  cualquier  piso  es  mayor  que  1.3  veces  la  misma dimensión  en  un  piso  adyacente,  la  estructura  se  considera  irregular.  Se exceptúa el caso de los altillos de un solo piso.'})
        }
        if ($('#irregular_long').serialize().split("=")[1] == "Desplazamientos_dentro_del_plano_de_accion"){
            Swal.fire({text:'La estructura se considera irregular  cuando  existen  desplazamientos  en  el  alineamiento  de  elementos verticales del sistema de resistencia sísmica, dentro del mismo plano que los contiene, y estos desplazamientos son mayores que la dimensión horizontal del elemento. Cuando los elementos  desplazados  solo sostienen la cubierta de la edificación sin otras cargas adicionales de tanques o equipos, se eximen de esta consideración de irregularidad.'})
        }
        if ($('#irregular_long').serialize().split("=")[1] == "Piso_debil_Discontinuidad_en_la_resistencia"){
            Swal.fire({text:'Cuando la resistencia del piso es menor del 80 por ciento de la del piso inmediatamente superior pero superior o igual al 65 por ciento, entendiendo la resistencia del piso como la suma de las resistencias de todos los elementos  que comparten el cortante del piso para la dirección considerada, la estructura se considera irregular.'})
        }
        if ($('#irregular_long').serialize().split("=")[1] == "Piso_debil_Discontinuidad_extrema_en_la_resistencia"){
            Swal.fire({text:'Cuando  la resistencia del piso es menor del 65 por ciento de la del piso inmediatamente superior, entendiendo la resistencia del piso como la suma de las resistencias de todos los elementos que comparten el cortante del piso para la dirección considerada, la estructura se considera irregular.'})
        }


    })


    $('#type_particiones').click(function( date ) {
        event.preventDefault();

        if ($('#type_particiones').serialize().split("=")[1] == "None"){
            $("#m2_particiones").attr("disabled", 'disabled');
        }
        else {
            $("#m2_particiones").removeAttr("disabled");
        }
    })

    $('#type_ventanas').click(function( date ) {
        event.preventDefault();

        if ($('#type_ventanas').serialize().split("=")[1] == "None"){

            $("#m2_ventanas").attr("disabled", 'disabled');


        }else {
            $("#m2_ventanas").removeAttr("disabled");
        }

    })

    $('#type_cubierta').click(function( date ) {
        event.preventDefault();

        if ($('#type_cubierta').serialize().split("=")[1] == "None"){
            $("#espesor_cubierta").attr("disabled", 'disabled');
            $("#m2_cubierta").attr("disabled", 'disabled');
        }else {
            $("#espesor_cubierta").removeAttr("disabled");
            $("#m2_cubierta").removeAttr("disabled");
        }

    })

    $('#type_piso').click(function( date ) {
        event.preventDefault();
        if ($('#type_piso').serialize().split("=")[1] == "None"){

            $("#m2_pisos").attr("disabled", 'disabled');
            $("#espesor_piso").attr("disabled", 'disabled');
        }else {
            $("#m2_pisos").removeAttr("disabled");
            $("#espesor_piso").removeAttr("disabled");
        }
    })


    $('#type_recubrimiento').click(function( date ) {
        event.preventDefault();
        if ($('#type_recubrimiento').serialize().split("=")[1] == "None"){

            $("#espesor_recubrimiento").attr("disabled", 'disabled');
            $("#m2_recubrimiento").attr("disabled", 'disabled');
        } else {
            $("#espesor_recubrimiento").removeAttr("disabled");
            $("#m2_recubrimiento").removeAttr("disabled");
        }

    })


    $('#type_enchape').click(function( date ) {
        event.preventDefault();

        if ($('#type_enchape').serialize().split("=")[1] == "None"){
            $("#espesor_enchape").attr("disabled", 'disabled');
            $("#m2_enchape").attr("disabled", 'disabled');
        }
        else {
            $("#espesor_enchape").removeAttr("disabled");
            $("#m2_enchape").removeAttr("disabled");
        }

    })

    alert('1111')

    $('#number_of_floors').change(function( date ) {

        event.preventDefault();
        var number = $('#number_of_floors').serialize().split("=")[1]

        var html = ''
        for (var i =0; i < parseInt(number) ; i++){
            html = html + `<div class="col-sm-4">
                <div class="form-group">
                    <label>Area piso 1:</label>
                    <input
                        class="form-control disable"
                        type="number"
                        name="area_floor_${i}"
                        id="area_floor_${i}"
                        step="0.01"
                        min="0"
                        required
                    >
                </div>

                </div>`
        }

        $("#div_floors").html(html)
    })

});

