$(document).ready(function(){
    console.log('///////')
    $(document).on ("click", '#type_placa', function( event ){
        event.preventDefault();
        console.log($('#type_placa').serialize().split("=")[1])
        if ($('#type_placa').serialize().split("=")[1] == "Placa_Facil"){
            $('#placa_0').html('<div class="col-sm-2"><div class="form-group"><label>Tipo de Placa:</label><select class="form-control" name="type_placa" id="type_placa" required><option name="Placa_Aligerada" value="Placa_Aligerada">Aligerada</option><option name="Placa_Maciza" value="Placa_Maciza">Maciza</option><option name="Placa_Facil" value="Placa_Facil" selected>Facil</option></select></div></div><div class="col-sm-1"><div class="form-group"><label>Tipo:</label><select class="form-control" name="type_placa_facil" id="type_placa_facil" required><option selected></option><option name="Placa" value="Placa">Placa</option><option name="Bloquelon" value="Bloquelon">Bloquelon</option><option name="Perfil_Metalico" value="Perfil_Metalico">Perfil Metalico</option></select></div></div><div class="col-sm-2"><div class="form-group"><label>Ancho:</label><input class="form-control" type="number" name="placa_x_0" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Largo:</label><input class="form-control" type="number" name="placa_y_0" step=".001" min="0" required></div></div><div class="col-sm-1"><div class="form-group"><label>Cantidad:</label><input class="form-control" type="number" name="num_placa_0" min="0" required></div></div>')
        }
        if ($('#type_placa').serialize().split("=")[1] == "Placa_Maciza"){

            console.log("MACIZAAAAAAAAAAAAAAAAAAAAAAA")
            $('#placa_0').html('<div class="col-sm-2"><div class="form-group"><label>Tipo de Placa:</label><select class="form-control" name="type_placa" id="type_placa" required><option selected></option><option name="Placa_Aligerada" value="Placa_Aligerada">Aligerada</option><option name="Placa_Maciza" value="Placa_Maciza" selected>Maciza</option><option name="Placa_Facil" value="Placa_Facil">Facil</option></select></div></div><div class="col-sm-2"><div class="form-group"><label>Ancho:</label><input class="form-control" type="number" name="placa_x_0" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Largo:</label><input class="form-control" type="number" name="placa_y_0" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Cantidad:</label><input class="form-control" type="number" name="num_placa_0" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Espesor:</label><input class="form-control" type="number" name="_placa" min="0" required></div></div>')

        }
        if ($('#type_placa').serialize().split("=")[1] == "Placa_Aligerada"){

            console.log("ALIGERADAAAAAAAAAAAAAAA")
            $('#placa_0').html('<div class="col-sm-1"><div class="form-group"><label>Tipo:</label><select class="form-control" name="type_placa" id="type_placa" required><option selected></option><option name="Placa_Aligerada" value="Placa_Aligerada">Aligerada</option><option name="Placa_Maciza" value="Placa_Maciza">Maciza</option><option name="Placa_Facil" value="Placa_Facil">Facil</option></select></div></div><div class="col-sm-1"><div class="form-group"><label>Ancho:</label><input class="form-control" type="number" name="placa_x_0" step=".001" min="0" required></div></div><div class="col-sm-1"><div class="form-group"><label>Largo:</label><input class="form-control" type="number" name="placa_y_0" step=".001" min="0" required></div></div><div class="col-sm-1"><div class="form-group"><label>Cantidad:</label><input class="form-control" type="number" name="num_placa_0" min="0" required></div></div><div class="col-sm-1"><div class="form-group"><label>Medida a</label><input class="form-control" type="number" name="vg_a_0" step=".001" min="0" required></div></div><div class="col-sm-1"><div class="form-group"><label>Medida b</label><input class="form-control" type="number" name="vg_b_0" step=".001" min="0" required></div></div><div class="col-sm-1"><div class="form-group"><label>Medida c</label><input class="form-control" type="number" name="vg_c_0" min="0" required></div></div><div class="col-sm-1"><div class="form-group"><label>Medida d</label><input class="form-control" type="number" name="vg_a_0" step=".001" min="0" required></div></div><div class="col-sm-1"><div class="form-group"><label>Medida e</label><input class="form-control" type="number" name="vg_b_0" step=".001" min="0" required></div></div><div class="col-sm-1"><div class="form-group" id="p"><span class="more_information" id="info"><u>info</u></span></div></div>')
            $('#type_placa').html(`<option name="Placa_Aligerada" value="Placa_Aligerada" selected>Aligerada</option><option name="Placa_Maciza" value="Placa_Maciza">Maciza</option><option name="Placa_Facil" value="Placa_Facil">Facil</option>`)

        }




    })

    $(document).on ("click", '#info', function( event ){
        event.preventDefault();
        console.log('info!!!!!')
        var url="/static/images/placa.jpg";

        Swal.fire({
            imageUrl: url,
            imageWidth: 1500,
            imageHeight: 200,
            imageAlt: 'A tall image'
          })

    })




    $(document).on ("click", '#type_placa_facil', function( event ){
        if ($('#type_placa_facil').serialize().split("=")[1] == "Placa"){

            $('#placa_0').html('<div class="col-sm-2"><div class="form-group"><label>Tipo de Placa:</label><select class="form-control" name="type_placa" id="type_placa" required><option name="Placa_Aligerada" value="Placa_Aligerada">Aligerada</option><option name="Placa_Maciza" value="Placa_Maciza">Maciza</option><option name="Placa_Facil" value="Placa_Facil" selected>Facil</option></select></div></div><div class="col-sm-1"><div class="form-group"><label>Tipo:</label><select class="form-control" name="type_placa_facil" id="type_placa_facil" required><option name="Placa" value="Placa" selected>Placa</option><option name="Bloquelon" value="Bloquelon">Bloquelon</option><option name="Perfil_Metalico" value="Perfil_Metalico">Perfil Metalico</option></select></div></div><div class="col-sm-2"><div class="form-group"><label>Ancho:</label><input class="form-control" type="number" name="placa_x_0" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Largo:</label><input class="form-control" type="number" name="placa_y_0" step=".001" min="0" required></div></div><div class="col-sm-1"><div class="form-group"><label>Cantidad:</label><input class="form-control" type="number" name="num_placa_0" min="0" required></div></div><div class="col-sm-1"><div class="form-group"><label>Espesor:</label><input class="form-control" type="number" name="z_placa_facil" step=".001" min="0" required></div></div>')
        }
        if ($('#type_placa_facil').serialize().split("=")[1] == "Bloquelon"){
            $('#placa_0').html('<div class="col-sm-2"><div class="form-group"><label>Tipo de Placa:</label><select class="form-control" name="type_placa" id="type_placa" required><option name="Placa_Aligerada" value="Placa_Aligerada">Aligerada</option><option name="Placa_Maciza" value="Placa_Maciza">Maciza</option><option name="Placa_Facil" value="Placa_Facil" selected>Facil</option></select></div></div><div class="col-sm-1"><div class="form-group"><label>Tipo:</label><select class="form-control" name="type_placa_facil" id="type_placa_facil" required><option name="Placa" value="Placa">Placa</option><option name="Bloquelon" value="Bloquelon" selected>Bloquelon</option><option name="Perfil_Metalico" value="Perfil_Metalico">Perfil Metalico</option></select></div></div><div class="col-sm-2"><div class="form-group"><label>Ancho:</label><input class="form-control" type="number" name="placa_x_0" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Largo:</label><input class="form-control" type="number" name="placa_y_0" step=".001" min="0" required></div></div><div class="col-sm-1"><div class="form-group"><label>Cantidad:</label><input class="form-control" type="number" name="num_placa_0" min="0" required></div></div><div class="col-sm-1"><div class="form-group"><label>Peso/M2(kg)</label><input class="form-control" type="number" name="peso_bloquelon" step=".001" min="0" required></div></div>')

        }
        if ($('#type_placa_facil').serialize().split("=")[1] == "Perfil_Metalico"){
            $('#placa_0').html('<div class="col-sm-2"><div class="form-group"><label>Tipo de Placa:</label><select class="form-control" name="type_placa" id="type_placa" required><option name="Placa_Aligerada" value="Placa_Aligerada">Aligerada</option><option name="Placa_Maciza" value="Placa_Maciza">Maciza</option><option name="Placa_Facil" value="Placa_Facil" selected>Facil</option></select></div></div><div class="col-sm-1"><div class="form-group"><label>Tipo:</label><select class="form-control" name="type_placa_facil" id="type_placa_facil" required><option name="Placa" value="Placa">Placa</option><option name="Bloquelon" value="Bloquelon" >Bloquelon</option><option name="Perfil_Metalico" value="Perfil_Metalico" selected>Perfil Metalico</option></select></div></div><div class="col-sm-2"><div class="form-group"><label>Ancho:</label><input class="form-control" type="number" name="placa_x_0" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Largo:</label><input class="form-control" type="number" name="placa_y_0" step=".001" min="0" required></div></div><div class="col-sm-1"><div class="form-group"><label>Cantidad:</label><input class="form-control" type="number" name="num_placa_0" min="0" required></div></div><div class="col-sm-1"><div class="form-group"><label>Ml perfil</label><input class="form-control" type="number" name="ml_perfil" step=".001" min="0" required></div></div><div class="col-sm-1"><div class="form-group"><label>Peso/ml(kg)</label><input class="form-control" type="number" name="peso_ml_perfil" step=".001" min="0" required></div></div>')

        }

    })



    var count = 0
    $(document).on ("click", '#mas_placas', function( event ){
        console.log(count)
        count = count + 1
        if (count < 3){
            var element = $('#profile-box1').html()
            $('#profile-box1').html(`${element}<div class="row" id="placa_${count}"><div class="col-sm-2"><div class="form-group"><label>Tipo de Placa:</label><select class="form-control" name="type_placa_${count}" id="type_placa_${count}" required><option selected></option><option name="Placa_Aligerada" value="Placa_Aligerada">Aligerada</option><option name="Placa_Maciza" value="Placa_Maciza">Maciza</option><option name="Placa_Facil" value="Placa_Facil">Facil</option></select></div></div><div class="col-sm-2"><div class="form-group"><label>Ancho:</label><input class="form-control" type="number" name="placa_x_0" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Largo:</label><input class="form-control" type="number" name="placa_y_0" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Cantidad:</label><input class="form-control" type="number" name="num_placa_0" min="0" required></div></div>`)
        }
    })








    $(document).on ("click", '#type_placa_1', function( event ){
        event.preventDefault();
        console.log($('#type_placa_1').serialize().split("=")[1])
        if ($('#type_placa_1').serialize().split("=")[1] == "Placa_Facil"){
            $('#placa_1').html('<div class="col-sm-2"><div class="form-group"><label>Tipo de Placa:</label><select class="form-control" name="type_placa_1" id="type_placa_1" required><option name="Placa_Aligerada" value="Placa_Aligerada">Aligerada</option><option name="Placa_Maciza" value="Placa_Maciza">Maciza</option><option name="Placa_Facil" value="Placa_Facil" selected>Facil</option></select></div></div><div class="col-sm-1"><div class="form-group"><label>Tipo:</label><select class="form-control" name="type_placa_facil_1" id="type_placa_facil_1" required><option selected></option><option name="Placa" value="Placa">Placa</option><option name="Bloquelon" value="Bloquelon">Bloquelon</option><option name="Perfil_Metalico" value="Perfil_Metalico">Perfil Metalico</option></select></div></div><div class="col-sm-2"><div class="form-group"><label>Ancho:</label><input class="form-control" type="number" name="placa_x_0" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Largo:</label><input class="form-control" type="number" name="placa_y_0" step=".001" min="0" required></div></div><div class="col-sm-1"><div class="form-group"><label>Cantidad:</label><input class="form-control" type="number" name="num_placa_0" min="0" required></div></div>')
        }
        if ($('#type_placa_1').serialize().split("=")[1] == "Placa_Maciza"){

            console.log("MACIZAAAAAAAAAAAAAAAAAAAAAAA")
            $('#placa_1').html('<div class="col-sm-2"><div class="form-group"><label>Tipo de Placa:</label><select class="form-control" name="type_placa_1" id="type_placa_1" required><option selected></option><option name="Placa_Aligerada" value="Placa_Aligerada">Aligerada</option><option name="Placa_Maciza" value="Placa_Maciza" selected>Maciza</option><option name="Placa_Facil" value="Placa_Facil">Facil</option></select></div></div><div class="col-sm-2"><div class="form-group"><label>Ancho:</label><input class="form-control" type="number" name="placa_x_0" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Largo:</label><input class="form-control" type="number" name="placa_y_0" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Cantidad:</label><input class="form-control" type="number" name="num_placa_0" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Espesor:</label><input class="form-control" type="number" name="_placa" min="0" required></div></div>')

        }
        if ($('#type_placa_1').serialize().split("=")[1] == "Placa_Aligerada"){

            console.log("ALIGERADAAAAAAAAAAAAAAA")
            $('#placa_1').html('<div class="col-sm-1"><div class="form-group"><label>Tipo:</label><select class="form-control" name="type_placa_1" id="type_placa_1" required><option selected></option><option name="Placa_Aligerada" value="Placa_Aligerada">Aligerada</option><option name="Placa_Maciza" value="Placa_Maciza">Maciza</option><option name="Placa_Facil" value="Placa_Facil">Facil</option></select></div></div><div class="col-sm-1"><div class="form-group"><label>Ancho:</label><input class="form-control" type="number" name="placa_x_0" step=".001" min="0" required></div></div><div class="col-sm-1"><div class="form-group"><label>Largo:</label><input class="form-control" type="number" name="placa_y_0" step=".001" min="0" required></div></div><div class="col-sm-1"><div class="form-group"><label>Cantidad:</label><input class="form-control" type="number" name="num_placa_0" min="0" required></div></div><div class="col-sm-1"><div class="form-group"><label>Medida a</label><input class="form-control" type="number" name="vg_a_0" step=".001" min="0" required></div></div><div class="col-sm-1"><div class="form-group"><label>Medida b</label><input class="form-control" type="number" name="vg_b_0" step=".001" min="0" required></div></div><div class="col-sm-1"><div class="form-group"><label>Medida c</label><input class="form-control" type="number" name="vg_c_0" min="0" required></div></div><div class="col-sm-1"><div class="form-group"><label>Medida d</label><input class="form-control" type="number" name="vg_a_0" step=".001" min="0" required></div></div><div class="col-sm-1"><div class="form-group"><label>Medida e</label><input class="form-control" type="number" name="vg_b_0" step=".001" min="0" required></div></div><div class="col-sm-1"><div class="form-group" id="p"><span class="more_information" id="info"><u>info</u></span></div></div>')
            $('#type_placa_1').html(`<option name="Placa_Aligerada" value="Placa_Aligerada" selected>Aligerada</option><option name="Placa_Maciza" value="Placa_Maciza">Maciza</option><option name="Placa_Facil" value="Placa_Facil">Facil</option>`)

        }




    })


    $(document).on ("click", '#type_placa_facil_1', function( event ){
        if ($('#type_placa_facil_1').serialize().split("=")[1] == "Placa"){

            $('#placa_1').html('<div class="col-sm-2"><div class="form-group"><label>Tipo de Placa:</label><select class="form-control" name="type_placa_1" id="type_placa_1" required><option name="Placa_Aligerada" value="Placa_Aligerada">Aligerada</option><option name="Placa_Maciza" value="Placa_Maciza">Maciza</option><option name="Placa_Facil" value="Placa_Facil" selected>Facil</option></select></div></div><div class="col-sm-1"><div class="form-group"><label>Tipo:</label><select class="form-control" name="type_placa_facil_1" id="type_placa_facil_1" required><option name="Placa" value="Placa" selected>Placa</option><option name="Bloquelon" value="Bloquelon">Bloquelon</option><option name="Perfil_Metalico" value="Perfil_Metalico">Perfil Metalico</option></select></div></div><div class="col-sm-2"><div class="form-group"><label>Ancho:</label><input class="form-control" type="number" name="placa_x_0" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Largo:</label><input class="form-control" type="number" name="placa_y_0" step=".001" min="0" required></div></div><div class="col-sm-1"><div class="form-group"><label>Cantidad:</label><input class="form-control" type="number" name="num_placa_0" min="0" required></div></div><div class="col-sm-1"><div class="form-group"><label>Espesor:</label><input class="form-control" type="number" name="z_placa_facil" step=".001" min="0" required></div></div>')
        }
        if ($('#type_placa_facil_1').serialize().split("=")[1] == "Bloquelon"){
            $('#placa_1').html('<div class="col-sm-2"><div class="form-group"><label>Tipo de Placa:</label><select class="form-control" name="type_placa_1" id="type_placa_1" required><option name="Placa_Aligerada" value="Placa_Aligerada">Aligerada</option><option name="Placa_Maciza" value="Placa_Maciza">Maciza</option><option name="Placa_Facil" value="Placa_Facil" selected>Facil</option></select></div></div><div class="col-sm-1"><div class="form-group"><label>Tipo:</label><select class="form-control" name="type_placa_facil_1" id="type_placa_facil_1" required><option name="Placa" value="Placa">Placa</option><option name="Bloquelon" value="Bloquelon" selected>Bloquelon</option><option name="Perfil_Metalico" value="Perfil_Metalico">Perfil Metalico</option></select></div></div><div class="col-sm-2"><div class="form-group"><label>Ancho:</label><input class="form-control" type="number" name="placa_x_0" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Largo:</label><input class="form-control" type="number" name="placa_y_0" step=".001" min="0" required></div></div><div class="col-sm-1"><div class="form-group"><label>Cantidad:</label><input class="form-control" type="number" name="num_placa_0" min="0" required></div></div><div class="col-sm-1"><div class="form-group"><label>Peso/M2(kg)</label><input class="form-control" type="number" name="peso_bloquelon" step=".001" min="0" required></div></div>')

        }
        if ($('#type_placa_facil_1').serialize().split("=")[1] == "Perfil_Metalico"){
            $('#placa_1').html('<div class="col-sm-2"><div class="form-group"><label>Tipo de Placa:</label><select class="form-control" name="type_placa_1" id="type_placa_1" required><option name="Placa_Aligerada" value="Placa_Aligerada">Aligerada</option><option name="Placa_Maciza" value="Placa_Maciza">Maciza</option><option name="Placa_Facil" value="Placa_Facil" selected>Facil</option></select></div></div><div class="col-sm-1"><div class="form-group"><label>Tipo:</label><select class="form-control" name="type_placa_facil_1" id="type_placa_facil_1" required><option name="Placa" value="Placa">Placa</option><option name="Bloquelon" value="Bloquelon" >Bloquelon</option><option name="Perfil_Metalico" value="Perfil_Metalico" selected>Perfil Metalico</option></select></div></div><div class="col-sm-2"><div class="form-group"><label>Ancho:</label><input class="form-control" type="number" name="placa_x_0" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Largo:</label><input class="form-control" type="number" name="placa_y_0" step=".001" min="0" required></div></div><div class="col-sm-1"><div class="form-group"><label>Cantidad:</label><input class="form-control" type="number" name="num_placa_0" min="0" required></div></div><div class="col-sm-1"><div class="form-group"><label>Ml perfil</label><input class="form-control" type="number" name="ml_perfil" step=".001" min="0" required></div></div><div class="col-sm-1"><div class="form-group"><label>Peso/ml(kg)</label><input class="form-control" type="number" name="peso_ml_perfil" step=".001" min="0" required></div></div>')

        }

    })







    $(document).on ("click", '#type_placa_2', function( event ){
        event.preventDefault();
        console.log($('#type_placa_2').serialize().split("=")[1])
        if ($('#type_placa_2').serialize().split("=")[1] == "Placa_Facil"){
            $('#placa_2').html('<div class="col-sm-2"><div class="form-group"><label>Tipo de Placa:</label><select class="form-control" name="type_placa_2" id="type_placa_2" required><option name="Placa_Aligerada" value="Placa_Aligerada">Aligerada</option><option name="Placa_Maciza" value="Placa_Maciza">Maciza</option><option name="Placa_Facil" value="Placa_Facil" selected>Facil</option></select></div></div><div class="col-sm-1"><div class="form-group"><label>Tipo:</label><select class="form-control" name="type_placa_facil_2" id="type_placa_facil_2" required><option selected></option><option name="Placa" value="Placa">Placa</option><option name="Bloquelon" value="Bloquelon">Bloquelon</option><option name="Perfil_Metalico" value="Perfil_Metalico">Perfil Metalico</option></select></div></div><div class="col-sm-2"><div class="form-group"><label>Ancho:</label><input class="form-control" type="number" name="placa_x_0" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Largo:</label><input class="form-control" type="number" name="placa_y_0" step=".001" min="0" required></div></div><div class="col-sm-1"><div class="form-group"><label>Cantidad:</label><input class="form-control" type="number" name="num_placa_0" min="0" required></div></div>')
        }
        if ($('#type_placa_2').serialize().split("=")[1] == "Placa_Maciza"){

            console.log("MACIZAAAAAAAAAAAAAAAAAAAAAAA")
            $('#placa_2').html('<div class="col-sm-2"><div class="form-group"><label>Tipo de Placa:</label><select class="form-control" name="type_placa_2" id="type_placa_2" required><option selected></option><option name="Placa_Aligerada" value="Placa_Aligerada">Aligerada</option><option name="Placa_Maciza" value="Placa_Maciza" selected>Maciza</option><option name="Placa_Facil" value="Placa_Facil">Facil</option></select></div></div><div class="col-sm-2"><div class="form-group"><label>Ancho:</label><input class="form-control" type="number" name="placa_x_0" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Largo:</label><input class="form-control" type="number" name="placa_y_0" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Cantidad:</label><input class="form-control" type="number" name="num_placa_0" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Espesor:</label><input class="form-control" type="number" name="_placa" min="0" required></div></div>')

        }
        if ($('#type_placa_2').serialize().split("=")[1] == "Placa_Aligerada"){

            console.log("ALIGERADAAAAAAAAAAAAAAA")
            $('#placa_2').html('<div class="col-sm-1"><div class="form-group"><label>Tipo:</label><select class="form-control" name="type_placa_2" id="type_placa_2" required><option selected></option><option name="Placa_Aligerada" value="Placa_Aligerada">Aligerada</option><option name="Placa_Maciza" value="Placa_Maciza">Maciza</option><option name="Placa_Facil" value="Placa_Facil">Facil</option></select></div></div><div class="col-sm-1"><div class="form-group"><label>Ancho:</label><input class="form-control" type="number" name="placa_x_0" step=".001" min="0" required></div></div><div class="col-sm-1"><div class="form-group"><label>Largo:</label><input class="form-control" type="number" name="placa_y_0" step=".001" min="0" required></div></div><div class="col-sm-1"><div class="form-group"><label>Cantidad:</label><input class="form-control" type="number" name="num_placa_0" min="0" required></div></div><div class="col-sm-1"><div class="form-group"><label>Medida a</label><input class="form-control" type="number" name="vg_a_0" step=".001" min="0" required></div></div><div class="col-sm-1"><div class="form-group"><label>Medida b</label><input class="form-control" type="number" name="vg_b_0" step=".001" min="0" required></div></div><div class="col-sm-1"><div class="form-group"><label>Medida c</label><input class="form-control" type="number" name="vg_c_0" min="0" required></div></div><div class="col-sm-1"><div class="form-group"><label>Medida d</label><input class="form-control" type="number" name="vg_a_0" step=".001" min="0" required></div></div><div class="col-sm-1"><div class="form-group"><label>Medida e</label><input class="form-control" type="number" name="vg_b_0" step=".001" min="0" required></div></div><div class="col-sm-1"><div class="form-group" id="p"><span class="more_information" id="info"><u>info</u></span></div></div>')
            $('#type_placa_2').html(`<option name="Placa_Aligerada" value="Placa_Aligerada" selected>Aligerada</option><option name="Placa_Maciza" value="Placa_Maciza">Maciza</option><option name="Placa_Facil" value="Placa_Facil">Facil</option>`)

        }




    })


    $(document).on ("click", '#type_placa_facil_2', function( event ){
        if ($('#type_placa_facil_2').serialize().split("=")[1] == "Placa"){

            $('#placa_2').html('<div class="col-sm-2"><div class="form-group"><label>Tipo de Placa:</label><select class="form-control" name="type_placa_2" id="type_placa_2" required><option name="Placa_Aligerada" value="Placa_Aligerada">Aligerada</option><option name="Placa_Maciza" value="Placa_Maciza">Maciza</option><option name="Placa_Facil" value="Placa_Facil" selected>Facil</option></select></div></div><div class="col-sm-1"><div class="form-group"><label>Tipo:</label><select class="form-control" name="type_placa_facil_2" id="type_placa_facil_2" required><option name="Placa" value="Placa" selected>Placa</option><option name="Bloquelon" value="Bloquelon">Bloquelon</option><option name="Perfil_Metalico" value="Perfil_Metalico">Perfil Metalico</option></select></div></div><div class="col-sm-2"><div class="form-group"><label>Ancho:</label><input class="form-control" type="number" name="placa_x_0" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Largo:</label><input class="form-control" type="number" name="placa_y_0" step=".001" min="0" required></div></div><div class="col-sm-1"><div class="form-group"><label>Cantidad:</label><input class="form-control" type="number" name="num_placa_0" min="0" required></div></div><div class="col-sm-1"><div class="form-group"><label>Espesor:</label><input class="form-control" type="number" name="z_placa_facil" step=".001" min="0" required></div></div>')
        }
        if ($('#type_placa_facil_2').serialize().split("=")[1] == "Bloquelon"){
            $('#placa_2').html('<div class="col-sm-2"><div class="form-group"><label>Tipo de Placa:</label><select class="form-control" name="type_placa_2" id="type_placa_2" required><option name="Placa_Aligerada" value="Placa_Aligerada">Aligerada</option><option name="Placa_Maciza" value="Placa_Maciza">Maciza</option><option name="Placa_Facil" value="Placa_Facil" selected>Facil</option></select></div></div><div class="col-sm-1"><div class="form-group"><label>Tipo:</label><select class="form-control" name="type_placa_facil_2" id="type_placa_facil_2" required><option name="Placa" value="Placa">Placa</option><option name="Bloquelon" value="Bloquelon" selected>Bloquelon</option><option name="Perfil_Metalico" value="Perfil_Metalico">Perfil Metalico</option></select></div></div><div class="col-sm-2"><div class="form-group"><label>Ancho:</label><input class="form-control" type="number" name="placa_x_0" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Largo:</label><input class="form-control" type="number" name="placa_y_0" step=".001" min="0" required></div></div><div class="col-sm-1"><div class="form-group"><label>Cantidad:</label><input class="form-control" type="number" name="num_placa_0" min="0" required></div></div><div class="col-sm-1"><div class="form-group"><label>Peso/M2(kg)</label><input class="form-control" type="number" name="peso_bloquelon" step=".001" min="0" required></div></div>')

        }
        if ($('#type_placa_facil_2').serialize().split("=")[1] == "Perfil_Metalico"){
            $('#placa_2').html('<div class="col-sm-2"><div class="form-group"><label>Tipo de Placa:</label><select class="form-control" name="type_placa_2" id="type_placa_2" required><option name="Placa_Aligerada" value="Placa_Aligerada">Aligerada</option><option name="Placa_Maciza" value="Placa_Maciza">Maciza</option><option name="Placa_Facil" value="Placa_Facil" selected>Facil</option></select></div></div><div class="col-sm-1"><div class="form-group"><label>Tipo:</label><select class="form-control" name="type_placa_facil_2" id="type_placa_facil_2" required><option name="Placa" value="Placa">Placa</option><option name="Bloquelon" value="Bloquelon" >Bloquelon</option><option name="Perfil_Metalico" value="Perfil_Metalico" selected>Perfil Metalico</option></select></div></div><div class="col-sm-2"><div class="form-group"><label>Ancho:</label><input class="form-control" type="number" name="placa_x_0" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Largo:</label><input class="form-control" type="number" name="placa_y_0" step=".001" min="0" required></div></div><div class="col-sm-1"><div class="form-group"><label>Cantidad:</label><input class="form-control" type="number" name="num_placa_0" min="0" required></div></div><div class="col-sm-1"><div class="form-group"><label>Ml perfil</label><input class="form-control" type="number" name="ml_perfil" step=".001" min="0" required></div></div><div class="col-sm-1"><div class="form-group"><label>Peso/ml(kg)</label><input class="form-control" type="number" name="peso_ml_perfil" step=".001" min="0" required></div></div>')

        }

    })


    var count_vigas = 0
    $(document).on ("click", '#mas_vigas', function( event ){
        console.log(count_vigas)
        count_vigas = count_vigas + 1

        var element = $('#profile-box2').html()
        $('#profile-box2').html(`${element}<div class="row" id="viga_${count_vigas}"><div class="col-sm-2"><div class="form-group"><label>Ancho:</label><input class="form-control" type="number" name="ancho_viga_${count_vigas}" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Alto:</label><input class="form-control" type="number" name="alto_viga_${count_vigas}" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Largo:</label><input class="form-control" type="number" name="largo_viga_${count_vigas}" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label># de vigas:</label><input class="form-control" type="number" name="numero_viga_${count_vigas}" min="0" required></div></div>`)


    })

    var count_columnas = 0
    $(document).on ("click", '#mas_columnas', function( event ){
        console.log(count_columnas)
        count_columnas = count_columnas + 1
        var element = $('#profile-box3').html()
        $('#profile-box3').html(`${element}<div class="row" id="columna_${count_columnas}"><div class="col-sm-2"><div class="form-group"><label>Ancho:</label><input class="form-control" type="number" name="ancho_columna_${count_columnas}" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Alto:</label><input class="form-control" type="number" name="alto_columna_${count_columnas}" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Largo:</label><input class="form-control" type="number" name="largo_columna_${count_columnas}" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label># de columnas:</label><input class="form-control" type="number" name="numero_columna_${count_columnas}" min="0" required></div></div>`)


    })








});



