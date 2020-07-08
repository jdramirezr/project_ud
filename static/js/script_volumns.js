$(document).ready(function(){
    console.log('///////')
    $(document).on ("change", '#type_placa', function( event ){
        event.preventDefault();
        console.log($('#type_placa').serialize().split("=")[1])
        if ($('#type_placa').serialize().split("=")[1] == "Placa_Facil"){
            $('#placa_0').html('<div class="col-sm-2"><div class="form-group"><label>Tipo de Placa:</label><select class="form-control" name="type_placa" id="type_placa" required><option name="Placa_Aligerada" value="Placa_Aligerada">Aligerada</option><option name="Placa_Maciza" value="Placa_Maciza">Maciza</option><option name="Placa_Facil" value="Placa_Facil" selected>Facil</option></select></div></div><div class="col-sm-2"><div class="form-group"><label>Tipo:</label><select class="form-control" name="type_placa_facil" id="type_placa_facil" required><option selected></option><option name="Placa" value="Placa">Placa</option><option name="Bloquelon" value="Bloquelon">Bloquelon</option><option name="Perfil_Metalico" value="Perfil_Metalico">Perfil Metalico</option></select></div></div><div class="col-sm-2"><div class="form-group"><label>Ancho:</label><input class="form-control" type="number" name="placa_x" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Largo:</label><input class="form-control" type="number" name="placa_y" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Cantidad:</label><input class="form-control count" type="number" name="num_placa" min="0" required></div></div>')
        }
        if ($('#type_placa').serialize().split("=")[1] == "Placa_Maciza"){

            console.log("MACIZAAAAAAAAAAAAAAAAAAAAAAA")
            $('#placa_0').html('<div class="col-sm-2"><div class="form-group"><label>Tipo de Placa:</label><select class="form-control" name="type_placa" id="type_placa" required><option selected></option><option name="Placa_Aligerada" value="Placa_Aligerada">Aligerada</option><option name="Placa_Maciza" value="Placa_Maciza" selected>Maciza</option><option name="Placa_Facil" value="Placa_Facil">Facil</option></select></div></div><div class="col-sm-2"><div class="form-group"><label>Ancho:</label><input class="form-control" type="number" name="placa_x" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Largo:</label><input class="form-control" type="number" name="placa_y" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Cantidad:</label><input class="form-control count" type="number" name="num_placa" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Espesor:</label><input class="form-control" type="number" name="placa_z" min="0" required></div></div>')

        }
        if ($('#type_placa').serialize().split("=")[1] == "Placa_Aligerada"){

            console.log("ALIGERADAAAAAAAAAAAAAAA")
            $('#placa_0').html(`
            <div class="col-sm-2"><div class="form-group"><label>Tipo:</label><select class="form-control" name="type_placa" id="type_placa" required><option selected></option><option name="Placa_Aligerada" value="Placa_Aligerada">Aligerada</option><option name="Placa_Maciza" value="Placa_Maciza">Maciza</option><option name="Placa_Facil" value="Placa_Facil">Facil</option></select></div></div>
            <div class="col-sm-2"><div class="form-group"><label>Ancho:</label><input class="form-control" type="number" name="placa_x" step=".001" min="0" required></div></div>
            <div class="col-sm-2"><div class="form-group"><label>Largo:</label><input class="form-control" type="number" name="placa_y" step=".001" min="0" required></div></div>
            <div class="col-sm-2"><div class="form-group"><label>Cantidad:</label><input class="form-control count" type="number" name="num_placa" min="0" required></div></div>
            <div class="col-sm-2"><div class="form-group"><label>Medida A:</label><input class="form-control" type="number" name="vg_a" step=".001" min="0" required></div></div>
            <div class="col-sm-2"><div class="form-group"><label>Medida B:</label><input class="form-control" type="number" name="vg_b" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Medida C:</label><input class="form-control" type="number" name="vg_c" min="0" required></div></div>
            <div class="col-sm-2"><div class="form-group"><label>Medida D:</label><input class="form-control" type="number" name="vg_d" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Medida E:</label><input class="form-control" type="number" name="vg_e" step=".001" min="0" required></div></div>
            <div class="col-sm-2"><div class="form-group" id="p"><span class="more_information" id="info"><u>info</u></span></div></div>`)
            $('#type_placa').html(`<option name="Placa_Aligerada" value="Placa_Aligerada" selected>Aligerada</option><option name="Placa_Maciza" value="Placa_Maciza">Maciza</option><option name="Placa_Facil" value="Placa_Facil">Facil</option>`)

        }




    })

    $(document).on ("mouseover", '#info', function( event ){
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

            $('#placa_0').html('<div class="col-sm-2"><div class="form-group"><label>Tipo de Placa:</label><select class="form-control" name="type_placa" id="type_placa" required><option name="Placa_Aligerada" value="Placa_Aligerada">Aligerada</option><option name="Placa_Maciza" value="Placa_Maciza">Maciza</option><option name="Placa_Facil" value="Placa_Facil" selected>Facil</option></select></div></div><div class="col-sm-2"><div class="form-group"><label>Tipo:</label><select class="form-control" name="type_placa_facil" id="type_placa_facil" required><option name="Placa" value="Placa" selected>Placa</option><option name="Bloquelon" value="Bloquelon">Bloquelon</option><option name="Perfil_Metalico" value="Perfil_Metalico">Perfil Metalico</option></select></div></div><div class="col-sm-2"><div class="form-group"><label>Ancho:</label><input class="form-control" type="number" name="placa_x" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Largo:</label><input class="form-control" type="number" name="placa_y" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Cantidad:</label><input class="form-control count" type="number" name="num_placa" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Espesor:</label><input class="form-control" type="number" name="z_placa_facil" step=".001" min="0" required></div></div>')
        }
        if ($('#type_placa_facil').serialize().split("=")[1] == "Bloquelon"){
            $('#placa_0').html('<div class="col-sm-2"><div class="form-group"><label>Tipo de Placa:</label><select class="form-control" name="type_placa" id="type_placa" required><option name="Placa_Aligerada" value="Placa_Aligerada">Aligerada</option><option name="Placa_Maciza" value="Placa_Maciza">Maciza</option><option name="Placa_Facil" value="Placa_Facil" selected>Facil</option></select></div></div><div class="col-sm-2"><div class="form-group"><label>Tipo:</label><select class="form-control" name="type_placa_facil" id="type_placa_facil" required><option name="Placa" value="Placa">Placa</option><option name="Bloquelon" value="Bloquelon" selected>Bloquelon</option><option name="Perfil_Metalico" value="Perfil_Metalico">Perfil Metalico</option></select></div></div><div class="col-sm-2"><div class="form-group"><label>Ancho:</label><input class="form-control" type="number" name="placa_x" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Largo:</label><input class="form-control" type="number" name="placa_y" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Cantidad:</label><input class="form-control count" type="number" name="num_placa" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Peso/M2 (kg)</label><input class="form-control" type="number" name="peso_bloquelon" step=".001" min="0" required></div></div>')

        }
        if ($('#type_placa_facil').serialize().split("=")[1] == "Perfil_Metalico"){
            $('#placa_0').html('<div class="col-sm-2"><div class="form-group"><label>Tipo de Placa:</label><select class="form-control" name="type_placa" id="type_placa" required><option name="Placa_Aligerada" value="Placa_Aligerada">Aligerada</option><option name="Placa_Maciza" value="Placa_Maciza">Maciza</option><option name="Placa_Facil" value="Placa_Facil" selected>Facil</option></select></div></div><div class="col-sm-2"><div class="form-group"><label>Tipo:</label><select class="form-control" name="type_placa_facil" id="type_placa_facil" required><option name="Placa" value="Placa">Placa</option><option name="Bloquelon" value="Bloquelon" >Bloquelon</option><option name="Perfil_Metalico" value="Perfil_Metalico" selected>Perfil Metalico</option></select></div></div><div class="col-sm-2"><div class="form-group"><label>Cantidad:</label><input class="form-control count" type="number" name="num_placa" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Metro lineal perfil</label><input class="form-control" type="number" name="ml_perfil" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Peso/ml (kg)</label><input class="form-control" type="number" name="peso_ml_perfil" step=".001" min="0" required></div></div>')

        }

    })



    var count = 0
    $(document).on ("click", '#mas_placas', function( event ){
        console.log(count)
        count = count + 1
        if (count < 3){
            var element = $('#profile-box1').html()
            $('#profile-box1').html(`${element}<br></br><div class="row" id="placa_${count}"><div class="col-sm-3"><div class="form-group"><label>Tipo de Placa:</label><select class="form-control" name="type_placa" id="type_placa_${count}" required><option selected></option><option name="Placa_Aligerada" value="Placa_Aligerada">Aligerada</option><option name="Placa_Maciza" value="Placa_Maciza">Maciza</option><option name="Placa_Facil" value="Placa_Facil">Facil</option></select></div></div><div class="col-sm-3"><div class="form-group"><label>Ancho:</label><input class="form-control" type="number" name="placa_x" step=".001" min="0" required></div></div><div class="col-sm-3"><div class="form-group"><label>Largo:</label><input class="form-control" type="number" name="placa_y" step=".001" min="0" required></div></div><div class="col-sm-3"><div class="form-group"><label>Cantidad:</label><input class="form-control count" type="number" name="num_placa" min="0" required></div></div>`)
        }
    })








    $(document).on ("click", '#type_placa_1', function( event ){
        event.preventDefault();
        console.log($('#type_placa_1').serialize().split("=")[1])
        if ($('#type_placa_1').serialize().split("=")[1] == "Placa_Facil"){
            $('#placa_1').html('<div class="col-sm-2"><div class="form-group"><label>Tipo de Placa:</label><select class="form-control" name="type_placa" id="type_placa_1" required><option name="Placa_Aligerada" value="Placa_Aligerada">Aligerada</option><option name="Placa_Maciza" value="Placa_Maciza">Maciza</option><option name="Placa_Facil" value="Placa_Facil" selected>Facil</option></select></div></div><div class="col-sm-2"><div class="form-group"><label>Tipo:</label><select class="form-control" name="type_placa_facil" id="type_placa_facil_1" required><option selected></option><option name="Placa" value="Placa">Placa</option><option name="Bloquelon" value="Bloquelon">Bloquelon</option><option name="Perfil_Metalico" value="Perfil_Metalico">Perfil Metalico</option></select></div></div><div class="col-sm-2"><div class="form-group"><label>Ancho:</label><input class="form-control" type="number" name="placa_x" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Largo:</label><input class="form-control" type="number" name="placa_y" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Cantidad:</label><input class="form-control count" type="number" name="num_placa" min="0" required></div></div>')
        }
        if ($('#type_placa_1').serialize().split("=")[1] == "Placa_Maciza"){

            console.log("MACIZAAAAAAAAAAAAAAAAAAAAAAA")
            $('#placa_1').html('<div class="col-sm-2"><div class="form-group"><label>Tipo de Placa:</label><select class="form-control" name="type_placa" id="type_placa_1" required><option selected></option><option name="Placa_Aligerada" value="Placa_Aligerada">Aligerada</option><option name="Placa_Maciza" value="Placa_Maciza" selected>Maciza</option><option name="Placa_Facil" value="Placa_Facil">Facil</option></select></div></div><div class="col-sm-2"><div class="form-group"><label>Ancho:</label><input class="form-control" type="number" name="placa_x" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Largo:</label><input class="form-control" type="number" name="placa_y" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Cantidad:</label><input class="form-control count" type="number" name="num_placa" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Espesor:</label><input class="form-control" type="number" name="placa_z" min="0" required></div></div>')

        }
        if ($('#type_placa_1').serialize().split("=")[1] == "Placa_Aligerada"){

            console.log("ALIGERADAAAAAAAAAAAAAAA")
            $('#placa_1').html(`
            <div class="col-sm-2"><div class="form-group"><label>Tipo:</label><select class="form-control" name="type_placa" id="type_placa_1" required><option selected></option><option name="Placa_Aligerada" value="Placa_Aligerada">Aligerada</option><option name="Placa_Maciza" value="Placa_Maciza">Maciza</option><option name="Placa_Facil" value="Placa_Facil">Facil</option></select></div></div>
            <div class="col-sm-2"><div class="form-group"><label>Ancho:</label><input class="form-control" type="number" name="placa_x" step=".001" min="0" required></div></div>
            <div class="col-sm-2"><div class="form-group"><label>Largo:</label><input class="form-control" type="number" name="placa_y" step=".001" min="0" required></div></div>
            <div class="col-sm-2"><div class="form-group"><label>Cantidad:</label><input class="form-control count" type="number" name="num_placa" min="0" required></div></div>
            <div class="col-sm-2"><div class="form-group"><label>Medida A:</label><input class="form-control" type="number" name="vg_a" step=".001" min="0" required></div></div>
            <div class="col-sm-2"><div class="form-group"><label>Medida B:</label><input class="form-control" type="number" name="vg_b" step=".001" min="0" required></div></div>
            <div class="col-sm-2"><div class="form-group"><label>Medida C:</label><input class="form-control" type="number" name="vg_c" min="0" required></div></div>
            <div class="col-sm-2"><div class="form-group"><label>Medida D:</label><input class="form-control" type="number" name="vg_d" step=".001" min="0" required></div></div>
            <div class="col-sm-2"><div class="form-group"><label>Medida E:</label><input class="form-control" type="number" name="vg_e" step=".001" min="0" required></div></div>
            <div class="col-sm-2"><div class="form-group" id="p"><span class="more_information" id="info"><u>info</u></span></div></div>`)
            $('#type_placa_1').html(`<option name="Placa_Aligerada" value="Placa_Aligerada" selected>Aligerada</option><option name="Placa_Maciza" value="Placa_Maciza">Maciza</option><option name="Placa_Facil" value="Placa_Facil">Facil</option>`)

        }




    })


    $(document).on ("click", '#type_placa_facil_1', function( event ){
        if ($('#type_placa_facil_1').serialize().split("=")[1] == "Placa"){

            $('#placa_1').html('<div class="col-sm-2"><div class="form-group"><label>Tipo de Placa:</label><select class="form-control" name="type_placa" id="type_placa_1" required><option name="Placa_Aligerada" value="Placa_Aligerada">Aligerada</option><option name="Placa_Maciza" value="Placa_Maciza">Maciza</option><option name="Placa_Facil" value="Placa_Facil" selected>Facil</option></select></div></div><div class="col-sm-2"><div class="form-group"><label>Tipo:</label><select class="form-control" name="type_placa_facil" id="type_placa_facil_1" required><option name="Placa" value="Placa" selected>Placa</option><option name="Bloquelon" value="Bloquelon">Bloquelon</option><option name="Perfil_Metalico" value="Perfil_Metalico">Perfil Metalico</option></select></div></div><div class="col-sm-2"><div class="form-group"><label>Ancho:</label><input class="form-control" type="number" name="placa_x" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Largo:</label><input class="form-control" type="number" name="placa_y" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Cantidad:</label><input class="form-control count" type="number" name="num_placa" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Espesor:</label><input class="form-control" type="number" name="z_placa_facil" step=".001" min="0" required></div></div>')
        }
        if ($('#type_placa_facil_1').serialize().split("=")[1] == "Bloquelon"){
            $('#placa_1').html('<div class="col-sm-2"><div class="form-group"><label>Tipo de Placa:</label><select class="form-control" name="type_placa" id="type_placa_1" required><option name="Placa_Aligerada" value="Placa_Aligerada">Aligerada</option><option name="Placa_Maciza" value="Placa_Maciza">Maciza</option><option name="Placa_Facil" value="Placa_Facil" selected>Facil</option></select></div></div><div class="col-sm-2"><div class="form-group"><label>Tipo:</label><select class="form-control" name="type_placa_facil" id="type_placa_facil_1" required><option name="Placa" value="Placa">Placa</option><option name="Bloquelon" value="Bloquelon" selected>Bloquelon</option><option name="Perfil_Metalico" value="Perfil_Metalico">Perfil Metalico</option></select></div></div><div class="col-sm-2"><div class="form-group"><label>Ancho:</label><input class="form-control" type="number" name="placa_x" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Largo:</label><input class="form-control" type="number" name="placa_y" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Cantidad:</label><input class="form-control count" type="number" name="num_placa" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Peso/M2 (kg)</label><input class="form-control" type="number" name="peso_bloquelon" step=".001" min="0" required></div></div>')

        }
        if ($('#type_placa_facil_1').serialize().split("=")[1] == "Perfil_Metalico"){
            $('#placa_1').html('<div class="col-sm-2"><div class="form-group"><label>Tipo de Placa:</label><select class="form-control" name="type_placa" id="type_placa_1" required><option name="Placa_Aligerada" value="Placa_Aligerada">Aligerada</option><option name="Placa_Maciza" value="Placa_Maciza">Maciza</option><option name="Placa_Facil" value="Placa_Facil" selected>Facil</option></select></div></div><div class="col-sm-2"><div class="form-group"><label>Tipo:</label><select class="form-control" name="type_placa_facil" id="type_placa_facil_1" required><option name="Placa" value="Placa">Placa</option><option name="Bloquelon" value="Bloquelon" >Bloquelon</option><option name="Perfil_Metalico" value="Perfil_Metalico" selected>Perfil Metalico</option></select></div></div><div class="col-sm-2"><div class="form-group"><label>Cantidad:</label><input class="form-control count" type="number" name="num_placa" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Metro lineal perfil</label><input class="form-control" type="number" name="ml_perfil" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Peso/ml (kg)</label><input class="form-control" type="number" name="peso_ml_perfil" step=".001" min="0" required></div></div>')

        }

    })







    $(document).on ("click", '#type_placa_2', function( event ){
        event.preventDefault();
        console.log($('#type_placa_2').serialize().split("=")[1])
        if ($('#type_placa_2').serialize().split("=")[1] == "Placa_Facil"){
            $('#placa_2').html('<div class="col-sm-2"><div class="form-group"><label>Tipo de Placa:</label><select class="form-control" name="type_placa" id="type_placa_2" required><option name="Placa_Aligerada" value="Placa_Aligerada">Aligerada</option><option name="Placa_Maciza" value="Placa_Maciza">Maciza</option><option name="Placa_Facil" value="Placa_Facil" selected>Facil</option></select></div></div><div class="col-sm-2"><div class="form-group"><label>Tipo:</label><select class="form-control" name="type_placa_facil" id="type_placa_facil_2" required><option selected></option><option name="Placa" value="Placa">Placa</option><option name="Bloquelon" value="Bloquelon">Bloquelon</option><option name="Perfil_Metalico" value="Perfil_Metalico">Perfil Metalico</option></select></div></div><div class="col-sm-2"><div class="form-group"><label>Ancho:</label><input class="form-control" type="number" name="placa_x" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Largo:</label><input class="form-control" type="number" name="placa_y" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Cantidad:</label><input class="form-control count" type="number" name="num_placa" min="0" required></div></div>')
        }
        if ($('#type_placa_2').serialize().split("=")[1] == "Placa_Maciza"){

            console.log("MACIZAAAAAAAAAAAAAAAAAAAAAAA")
            $('#placa_2').html('<div class="col-sm-2"><div class="form-group"><label>Tipo de Placa:</label><select class="form-control" name="type_placa" id="type_placa" required><option selected></option><option name="Placa_Aligerada" value="Placa_Aligerada">Aligerada</option><option name="Placa_Maciza" value="Placa_Maciza" selected>Maciza</option><option name="Placa_Facil" value="Placa_Facil">Facil</option></select></div></div><div class="col-sm-2"><div class="form-group"><label>Ancho:</label><input class="form-control" type="number" name="placa_x" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Largo:</label><input class="form-control" type="number" name="placa_y" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Cantidad:</label><input class="form-control count" type="number" name="num_placa" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Espesor:</label><input class="form-control" type="number" name="placa_z" min="0" required></div></div>')

        }
        if ($('#type_placa_2').serialize().split("=")[1] == "Placa_Aligerada"){

            console.log("ALIGERADAAAAAAAAAAAAAAA")
            $('#placa_2').html(`
            <div class="col-sm-2"><div class="form-group"><label>Tipo:</label><select class="form-control" name="type_placa" id="type_placa_2" required><option selected></option><option name="Placa_Aligerada" value="Placa_Aligerada">Aligerada</option><option name="Placa_Maciza" value="Placa_Maciza">Maciza</option><option name="Placa_Facil" value="Placa_Facil">Facil</option></select></div></div>
            <div class="col-sm-2"><div class="form-group"><label>Ancho:</label><input class="form-control" type="number" name="placa_x" step=".001" min="0" required></div></div>
            <div class="col-sm-2"><div class="form-group"><label>Largo:</label><input class="form-control" type="number" name="placa_y" step=".001" min="0" required></div></div>
            <div class="col-sm-2"><div class="form-group"><label>Cantidad:</label><input class="form-control count" type="number" name="num_placa" min="0" required></div></div>
            <div class="col-sm-2"><div class="form-group"><label>Medida A:</label><input class="form-control" type="number" name="vg_a" step=".001" min="0" required></div></div>
            <div class="col-sm-2"><div class="form-group"><label>Medida B:</label><input class="form-control" type="number" name="vg_b" step=".001" min="0" required></div></div>
            <div class="col-sm-2"><div class="form-group"><label>Medida C:</label><input class="form-control" type="number" name="vg_c" min="0" required></div></div>
            <div class="col-sm-2"><div class="form-group"><label>Medida D:</label><input class="form-control" type="number" name="vg_d" step=".001" min="0" required></div></div>
            <div class="col-sm-2"><div class="form-group"><label>Medida E:</label><input class="form-control" type="number" name="vg_e" step=".001" min="0" required></div></div>
            <div class="col-sm-2"><div class="form-group" id="p"><span class="more_information" id="info"><u>info</u></span></div></div>`)

            $('#type_placa_2').html(`<option name="Placa_Aligerada" value="Placa_Aligerada" selected>Aligerada</option><option name="Placa_Maciza" value="Placa_Maciza">Maciza</option><option name="Placa_Facil" value="Placa_Facil">Facil</option>`)

        }




    })


    $(document).on ("click", '#type_placa_facil_2', function( event ){
        if ($('#type_placa_facil_2').serialize().split("=")[1] == "Placa"){

            $('#placa_2').html('<div class="col-sm-2"><div class="form-group"><label>Tipo de Placa:</label><select class="form-control" name="type_placa" id="type_placa_2" required><option name="Placa_Aligerada" value="Placa_Aligerada">Aligerada</option><option name="Placa_Maciza" value="Placa_Maciza">Maciza</option><option name="Placa_Facil" value="Placa_Facil" selected>Facil</option></select></div></div><div class="col-sm-2"><div class="form-group"><label>Tipo:</label><select class="form-control" name="type_placa_facil" id="type_placa_facil_2" required><option name="Placa" value="Placa" selected>Placa</option><option name="Bloquelon" value="Bloquelon">Bloquelon</option><option name="Perfil_Metalico" value="Perfil_Metalico">Perfil Metalico</option></select></div></div><div class="col-sm-2"><div class="form-group"><label>Ancho:</label><input class="form-control" type="number" name="placa_x" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Largo:</label><input class="form-control" type="number" name="placa_y" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Cantidad:</label><input class="form-control count" type="number" name="num_placa" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Espesor:</label><input class="form-control" type="number" name="z_placa_facil" step=".001" min="0" required></div></div>')
        }
        if ($('#type_placa_facil_2').serialize().split("=")[1] == "Bloquelon"){
            $('#placa_2').html('<div class="col-sm-2"><div class="form-group"><label>Tipo de Placa:</label><select class="form-control" name="type_placa" id="type_placa_2" required><option name="Placa_Aligerada" value="Placa_Aligerada">Aligerada</option><option name="Placa_Maciza" value="Placa_Maciza">Maciza</option><option name="Placa_Facil" value="Placa_Facil" selected>Facil</option></select></div></div><div class="col-sm-2"><div class="form-group"><label>Tipo:</label><select class="form-control" name="type_placa_facil" id="type_placa_facil_2" required><option name="Placa" value="Placa">Placa</option><option name="Bloquelon" value="Bloquelon" selected>Bloquelon</option><option name="Perfil_Metalico" value="Perfil_Metalico">Perfil Metalico</option></select></div></div><div class="col-sm-2"><div class="form-group"><label>Ancho:</label><input class="form-control" type="number" name="placa_x" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Largo:</label><input class="form-control" type="number" name="placa_y" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Cantidad:</label><input class="form-control count" type="number" name="num_placa" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Peso/M2 (kg)</label><input class="form-control" type="number" name="peso_bloquelon" step=".001" min="0" required></div></div>')

        }
        if ($('#type_placa_facil_2').serialize().split("=")[1] == "Perfil_Metalico"){
            $('#placa_2').html('<div class="col-sm-2"><div class="form-group"><label>Tipo de Placa:</label><select class="form-control" name="type_placa" id="type_placa_2" required><option name="Placa_Aligerada" value="Placa_Aligerada">Aligerada</option><option name="Placa_Maciza" value="Placa_Maciza">Maciza</option><option name="Placa_Facil" value="Placa_Facil" selected>Facil</option></select></div></div><div class="col-sm-2"><div class="form-group"><label>Tipo:</label><select class="form-control" name="type_placa_facil" id="type_placa_facil_2" required><option name="Placa" value="Placa">Placa</option><option name="Bloquelon" value="Bloquelon" >Bloquelon</option><option name="Perfil_Metalico" value="Perfil_Metalico" selected>Perfil Metalico</option></select></div></div><div class="col-sm-2"><div class="form-group"><label>Cantidad:</label><input class="form-control count" type="number" name="num_placa" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Metro lineal perfil</label><input class="form-control" type="number" name="ml_perfil" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Peso/ml (kg)</label><input class="form-control" type="number" name="peso_ml_perfil" step=".001" min="0" required></div></div>')

        }

    })


    var count_vigas = 0
    $(document).on ("click", '#mas_vigas', function( event ){
        console.log(count_vigas)
        count_vigas = count_vigas + 1

        var element = $('#profile-box2').html()
        $('#profile-box2').html(`${element}<div class="row" id="viga_${count_vigas}"><div class="col-sm-2"><div class="form-group"><label>Ancho:</label><input class="form-control" type="number" name="ancho_viga" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Alto:</label><input class="form-control" type="number" name="alto_viga" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Largo:</label><input class="form-control" type="number" name="largo_viga" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label># de vigas:</label><input class="form-control count" type="number" name="numero_viga" min="0" required></div><input type="hidden" name="count_vigas" value=${count_vigas}></div>`)


    })

    var count_columnas = 0
    $(document).on ("click", '#mas_columnas', function( event ){
        console.log(count_columnas)
        count_columnas = count_columnas + 1
        var element = $('#profile-box3').html()
        $('#profile-box3').html(`${element}<div class="row" id="columna_${count_columnas}"><div class="col-sm-2"><div class="form-group"><label>Ancho:</label><input class="form-control" type="number" name="ancho_columna" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Alto:</label><input class="form-control" type="number" name="alto_columna" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label>Largo:</label><input class="form-control" type="number" name="largo_columna" step=".001" min="0" required></div></div><div class="col-sm-2"><div class="form-group"><label># de columnas:</label><input class="form-control count" type="number" name="numero_columna" min="0" required></div></div>`)


    })




    $(document).on ("change", '#option_floor', function( event ){
        if ($('#option_floor').serialize().split("=")[1] == "0"){

            $('#info_descrip_floor').html('<ul><li>Forma geométrica de la edificación es regular y aproximadamente simetrica. </li><li>El largo es menor a 2.5 veces el ancho. </li><li>No tiene "entradas y salidas" como las que se muestran en las otras dos figuras, visto tanto en planta como en altura. </li></ul>')
            $('#info_img_floor').html('<img style="display: block;margin: auto;"  src="/static/images/1_floor.png">')

        }
        if ($('#option_floor').serialize().split("=")[1] == "1"){


            $('#info_descrip_floor').html('<ul><li>Presenta algunas irregularidades en planta o en altura no muy pronunciadas.</li></ul>')
            $('#info_img_floor').html('<img style="display: block;margin: auto;" src="/static/images/2_floor.png">')


        }
        if ($('#option_floor').serialize().split("=")[1] == "2"){

            $('#info_descrip_floor').html('<ul><li>El largo es mayor que 3.5 veces el ancho. </li><l1>La forma de la edificacion es irregular, con entradas y salidas abruptas.</li></ul>')
            $('#info_img_floor').html('<img style="display: block;margin: auto;" src="/static/images/3_floor.png">')


        }

    })


    $(document).on ("change", '#option_wall', function( event ){
        if ($('#option_wall').serialize().split("=")[1] == "0"){

            $('#info_img_wall').html('<img style="display: block; margin: auto;" src="/static/images/1_wall.png">')
            $('#info_descrip_wall').html('<ul><li>Existen muros estructurales en las dos direcciones principales de la vivienda y estyos son confinados o reforzados.</li><li>Hay una longitud totalizada de muros en cada una de las direcciones principales al menos igual al valor dado por:<ul><li>Lo=(Mo*Ap)/t</li><li>Ap: Area en m2 de la planta (si la cuebierta es liviana, lamina, asbesto, cemento, ap se puede multiplicar por 0.67).</li><li>t: espesor de muros.</li></ul></li></ul>')
        }
        if ($('#option_wall').serialize().split("=")[1] == "1"){

            $('#info_img_wall').html('<img style="display: block; margin: auto;" src="/static/images/2_wall.png">')
            $('#info_descrip_wall').html('<ul><li>La mayoria de los muros se concentran en una sola direccion aunque existen unos o varios en la otra direccion.</li><li>La longitud de muros en la direccion de menor cantidad de muros es ligeramente inferior a la calculada con la formula anterior.</li></ul>')

        }
        if ($('#option_wall').serialize().split("=")[1] == "2"){

            $('#info_img_wall').html('<img style="display: block; margin: auto;" src="/static/images/3_wall.png">')
            $('#info_descrip_wall').html('<ul><li>Mas del 70% de los muros estan en una sola direccion.</li><li>hay muy pocos muros confinados o reforzados.</li><li>La longitud total de muros estructurales en cualquier direccion es mucho menor que la calculada con la ecuacion anterior.</li></ul>')

        }

    })


    $(document).on ("change", '#option_height', function( event ){
        if ($('#option_height').serialize().split("=")[1] == "0"){

            $('#info_img_height').html('<img style="display: block; margin: auto;" src="/static/images/1_height.png">')
            $('#info_descrip_height').html('<ul><li>La mayoria de los muros estructurales son continuos desde la cimentacion hasta la cubierta</li></ul>')


        }
        if ($('#option_height').serialize().split("=")[1] == "1"){


            $('#info_img_height').html('<img style="display: block; margin: auto;" src="/static/images/2_height.png">')
            $('#info_descrip_height').html('<ul><li>Algunos muros representan discontinuidades desde la cimentacion hasta la cubierta</li></ul>')

        }
        if ($('#option_height').serialize().split("=")[1] == "2"){

            $('#info_img_height').html('<img style="display: block; margin: auto;" src="/static/images/3_height.png">')
            $('#info_descrip_height').html('<ul><li>La mayoria de los muros no son continuos en altura desde su cimentacion hasta la cubierta.</li><li>Cambios de alineacion en el sistema de muros en direcion vertical.</li><li>Cambio de sistema de muros en pisos superiores a culomnas en el iso inferior.</li></ul>')

        }

    })





    $(document).on ("change", '#option_quality', function( event ){
        if ($('#option_quality').serialize().split("=")[1] == "0"){

            $('#info_img_quality').html('<img style="display: block; margin: auto;" src="/static/images/1_quality.png">')
            $('#info_descrip_quality').html('<ul><li>El mortero de la mayoría de las pegas esta entre 0.7 y 1.3 cm. </li><li>Las juntas son uniformes y continuas.</li><li>Hay juntas de buena calidad verticales y horizontales rodeando cada unidad de mampostería.</li><li>El mortero es de buena calidad y presentan buena adherencia con la pieza de mampostería</li></ul>')


        }
        if ($('#option_quality').serialize().split("=")[1] == "1"){

            $('#info_img_quality').html('<img style="display: block; margin: auto;" src="/static/images/2_quality.png">')
            $('#info_descrip_quality').html('<ul><li>El espesor de la mayoria de las pegas es mayor a 1.3 cm o menos de 0.7 cm.</li><li>Las juntas no son uniformes.</li><li>No existen juntas verticales o son de mala calidad.</li></ul>')


        }
        if ($('#option_quality').serialize().split("=")[1] == "2"){

            $('#info_img_quality').html('<img style="display: block; margin: auto;" src="/static/images/3_quality.png">')
            $('#info_descrip_quality').html('<ul><li>La pega es muy pobre entre los bloques, casi inexistente.</li><li>Poca regularidad en la alineación de las piezas.</li><li>El mortero es de muy mala calidad o evidencia separación con las piezas de mampostería.</li><li>No existen juntas verticales y/o horizontales en zonas del muro.</li></ul>')

        }

    })


    $(document).on ("change", '#option_location', function( event ){
        if ($('#option_location').serialize().split("=")[1] == "0"){

            $('#info_img_location').html('<img style="display: block; margin: auto;" src="/static/images/1_location.png">')
            $('#info_descrip_location').html('<ul><li>Las unidades de mampostería están trabadas.</li><li>Las unidades de mampostería son de buena calidad. No presentan agrietamientos importantes, nos hay piezas deterioradas o rotas.</li><li>Las piezas están colocadas de manera uniforme y continua hilada tras hilada.</li></ul>')


        }
        if ($('#option_location').serialize().split("=")[1] == "1"){

            $('#info_img_location').html('<img style="display: block; margin: auto;" src="/static/images/2_location.png">')
            $('#info_descrip_location').html('<ul><li>Algunas piezas están trabadas, mientras otras no lo están Siendo la mayoría de la primera clase.</li><li>Algunas piezas presentan agrietamiento o deterioro.</li><li>Algunas piezas están colocadas de manera uniforme y continua hilada tras hilada.</li></ul>')


        }
        if ($('#option_location').serialize().split("=")[1] == "2"){

            $('#info_img_location').html('<img style="display: block; margin: auto;" src="/static/images/3_location.png">')
            $('#info_descrip_location').html('<ul><li>Las unidades de mampostería NO están trabadas (petaca).</li><li>Las unidades de mampostería son de muy mala calidad. Se presentan agrietamientos importantes con piezas deterioradas o rotas.</li><li>Las piezas no están colocadas de manera uniforme y continua hiladas tras hiladas.</li></ul>')


        }

    })


    $(document).on ("change", '#option_materials', function( event ){
        if ($('#option_materials').serialize().split("=")[1] == "0"){

            $('#info_img_materials').html('<img style="display: block; margin: auto;" src="/static/images/1_materials.png">')
            $('#info_descrip_materials').html('<ul><li>El mortero no se deja rayar o desmoronar con un clavo o herramienta metálicas.</li><li>El concreto tiene buen aspecto, sin hormigueros y el acero no esta expuesto.</li><li>En los elementos de confinamiento en concreto reforzado, hay estribos abundantes y por lo menos 3 a 4 barras No 3, en sentido longitudinal.</li><li>El ladrillo es de buena calidad, no esta muy fisurado, quebrado, ni despegado y resiste caídas de por lo menos 2 metros de alto sin desintegrarse ni deteriorarse en forma apreciable.</li></ul>')


        }
        if ($('#option_materials').serialize().split("=")[1] == "1"){

            $('#info_img_materials').html('<img style="display: block; margin: auto;" src="/static/images/2_materials.png">')
            $('#info_descrip_materials').html('<ul><li>Se cumplen varios de los requisitos mencionados anteriormente.</li></ul>')


        }
        if ($('#option_materials').serialize().split("=")[1] == "2"){

            $('#info_img_materials').html('<img style="display: block; margin: auto;" src="/static/images/3_materials.png">')
            $('#info_descrip_materials').html('<ul><li>No se cumples mas de dos requisitos de los mencionados anteriormente.</li></ul>')

        }

    })








    $(document).on ("change", '#option_confined_walls', function( event ){
        if ($('#option_confined_walls').serialize().split("=")[1] == "0"){

            $('#info_img_confined_walls').html('<img style="display: block; margin: auto;" src="/static/images/1_confined_walls.png">')
            $('#info_descrip_confined_walls').html('<ul><li>Todos los muros de mampostería de la vivienda están confinados con vigas y columnas de concreto reforzado alrededor de ellos.</li><li>El espaciamiento máximo entre elementos de confinamiento es del orden de 4m o la altura entre pisos.</li><li>Todos los elementos de confinamiento tienen refuerzo tanto longitudinal como transversal y esta adecuadamente dispuesto.</li><li>Las culatas y antepechos también están confinados.</li></ul>')


        }
        if ($('#option_confined_walls').serialize().split("=")[1] == "1"){

            $('#info_img_confined_walls').html('<img style="display: block; margin: auto;" src="/static/images/2_confined_walls.png">')
            $('#info_descrip_confined_walls').html('<ul><li>Algunos muros de la edificación no cumplen con los requisitos mencionados anteriormente.</li></ul>')


        }
        if ($('#option_confined_walls').serialize().split("=")[1] == "2"){

            $('#info_img_confined_walls').html('<img style="display: block; margin: auto;" src="/static/images/3_confined_walls.png">')
            $('#info_descrip_confined_walls').html('<ul><li>La mayoría de los muros de mampostería de la vivienda no tienen confinamiento mediante columnas y vigas de concreto reforzado.</li></ul>')

        }

    })


    $(document).on ("change", '#option_detail', function( event ){
        if ($('#option_detail').serialize().split("=")[1] == "0"){

            $('#info_img_detail').html('<img style="display: block; margin: auto;" src="/static/images/1_detail.png">')
            $('#info_descrip_detail').html('<ul><li>Las columnas y vigas tienen mas de 20 cm de espesor o mas de 400 cm2 de área transversal.</li><li>Las columnas y vigas tienen al menos 4 barras No 3 longitudinales y estribos espaciados a no mas de 10 a 15 cm.</li><li>Existe un buen contacto entre el muro de mampostería y los elementos de confinamiento.</li><li>El refuerzo longitudinal de las columnas y vigas debe estar adecuadamente anclado a sus extremos y a los elementos de la cimentación.</li></ul>')

        }
        if ($('#option_detail').serialize().split("=")[1] == "1"){

            $('#info_img_detail').html('<img style="display: block; margin: auto;" src="/static/images/2_detail.png">')
            $('#info_descrip_detail').html('<ul><li>No todas las columnas y vigas cumplen con los requisitos anteriores.</li></ul>')

        }
        if ($('#option_detail').serialize().split("=")[1] == "2"){


            $('#info_img_detail').html('<img style="display: block; margin: auto;" src="/static/images/3_detail.png">')
            $('#info_descrip_detail').html('<ul><li>La mayoría de las columnas y vigas de confinamiento no cumplen con los requisitos establecidos anteriormente.</li></ul>')

        }

    })


    $(document).on ("change", '#option_mooring', function( event ){
        if ($('#option_mooring').serialize().split("=")[1] == "0"){

            $('#info_img_mooring').html('<img style="display: block; margin: auto;" src="/static/images/1_mooring.png">')
            $('#info_descrip_mooring').html('<ul><li>Existen vigas de amarre o de corona en concreto reforzado en todos los muros, parapetos, fachadas y culatas en mamposteria.</li></ul>')


        }
        if ($('#option_mooring').serialize().split("=")[1] == "1"){

            $('#info_img_mooring').html('<img style="display: block; margin: auto;" src="/static/images/2_mooring.png">')
            $('#info_descrip_mooring').html('<ul><li>No todos los muros o elementos de mampostería disponen de vigas de amarre o de corona.</li></ul>')


        }
        if ($('#option_mooring').serialize().split("=")[1] == "2"){

            $('#info_img_mooring').html('<img style="display: block; margin: auto;" src="/static/images/3_mooring.png">')
            $('#info_descrip_mooring').html('<ul><li>La vivienda no dispone de vigas de amarre o corona en los muros de elementos de mampostería</li></ul>')


        }

    })






    $(document).on ("change", '#option_characteristics', function( event ){
        if ($('#option_characteristics').serialize().split("=")[1] == "0"){

            $('#info_img_characteristics').html('<img style="display: block; margin: auto;" src="/static/images/1_characteristics.png">')
            $('#info_descrip_characteristics').html('<ul><li>Las aberturas en los muros estructurales totalizan menos del 35% del area total del muro.</li><li>La longitud total de aberturas en el muro corresponde a menos de la mitad de la longitud total del muro.</li><li>Existe una distancia desde el borde del muro hasta la abertura adyacente igual a la altura de la misma o 50 cm, la que sea mayor.</li></ul>')



        }
        if ($('#option_characteristics').serialize().split("=")[1] == "1"){

            $('#info_img_characteristics').html('<img style="display: block; margin: auto;" src="/static/images/2_characteristics.png">')
            $('#info_descrip_characteristics').html('<ul><li>No se cumplen algunos de los anteriores requisitos en algunos de los muros de la vivienda.</li></ul>')



        }
        if ($('#option_characteristics').serialize().split("=")[1] == "2"){

            $('#info_img_characteristics').html('<img style="display: block; margin: auto;" src="/static/images/3_characteristics.png">')
            $('#info_descrip_characteristics').html('<ul><li>Muy pocos o ningún muro estructural de la vivienda cumple con los requisitos anteriores.</li></ul>')


        }

    })


    $(document).on ("change", '#option_mezzanine', function( event ){
        if ($('#option_mezzanine').serialize().split("=")[1] == "0"){
            $('#info_img_mezzanine').html('<img style="display: block; margin: auto;" src="/static/images/1_mezzanine.png">')
            $('#info_descrip_mezzanine').html('<ul><li>El entrepiso esta conformado por placas de concreto fundidas en el sitio o placas prefabricadas que funcionan de manera monolítica.</li><li>La placa de entrepiso se apoya de manera adecuada a los muros de soporte y proporciona continuidad y monolitismo.</li><li>La placa de entrepiso es continua, monolítica y uniforme en relación con los materiales que lo componen.</li></ul>')

        }
        if ($('#option_mezzanine').serialize().split("=")[1] == "1"){

            $('#info_img_mezzanine').html('<img style="display: block; margin: auto;" src="/static/images/2_mezzanine.png">')
            $('#info_descrip_mezzanine').html('<ul><li>La placa de entrepiso no cumple con alguna de las anteriores consideraciones.</li></ul>')

        }
        if ($('#option_mezzanine').serialize().split("=")[1] == "2"){

            $('#info_img_mezzanine').html('<img style="display: block; margin: auto;" src="/static/images/3_mezzanine.png">')
            $('#info_descrip_mezzanine').html('<ul><li>La placa de entrepiso no cumple con varias de las consideraciones anteriores.</li><li>Los entrepisos estan conformados por madera o combinaciones de materiales (guadua, mortero, madera, concreto) y no proporcionan las caracteristicas de continuidad y amarre deseados.</li></ul>')

        }

    })


    $(document).on ("change", '#option_cover', function( event ){
        if ($('#option_cover').serialize().split("=")[1] == "0"){


            $('#info_img_cover').html('<img style="display: block; margin: auto;" src="/static/images/1_cover.png">')
            $('#info_descrip_cover').html('<ul><li>Existen tornillos, alambres o conexiones similares que amarran el techo a los muros.</li><li>Hay arriostramiento de las vigas y la distancia entre vigas no es muy grande.</li><li>La cubierta es liviana y esta debidamente amarrada y apoyada a la estructura de cubierta.</li></ul>')


        }
        if ($('#option_cover').serialize().split("=")[1] == "1"){

            $('#info_img_cover').html('<img style="display: block; margin: auto;" src="/static/images/2_cover.png">')
            $('#info_descrip_cover').html('<ul><li>Algunos de los anteriores requisitos se cumplen.</li></ul>')



        }
        if ($('#option_cover').serialize().split("=")[1] == "2"){

            $('#info_img_cover').html('<img style="display: block; margin: auto;" src="/static/images/3_cover.png">')
            $('#info_descrip_cover').html('<ul><li>La mayoría de los requisitos mencionados anteriormente no se cumplen.</li><li>La cubierta es pesada y no esta debidamente soportada o arriostrada.</li></ul>')

        }

    })






    $(document).on ("change", '#option_base', function( event ){
        if ($('#option_base').serialize().split("=")[1] == "0"){

            $('#info_img_base').html('<img style="display: block; margin: auto;" src="/static/images/1_base.png">')
            $('#info_descrip_base').html('<ul><li>La cimentación esta conformada por vigas corridas en concreto reforzado bajo los muros estructurales.</li><li>Las vigas de cimentacion conforman anillos amarrados.</li><li>Las vigas de cimentacion en concreto reforzado cumplen los requisitos por la NSR-10 en el titulo E.</li></ul>')


        }
        if ($('#option_base').serialize().split("=")[1] == "1"){

            $('#info_img_base').html('<img style="display: block; margin: auto;" src="/static/images/2_base.png">')
            $('#info_descrip_base').html('<ul><li>La cimentación no esta debidamente amarrada.</li><li>No se cumplen algunos de los requerimientos anteriores.</li></ul>')


        }
        if ($('#option_base').serialize().split("=")[1] == "2"){

            $('#info_img_base').html('<img style="display: block; margin: auto;" src="/static/images/3_base.png">')
            $('#info_descrip_base').html('<ul><li>La edificación no cuenta con una cimentacion adecuada de acuerdo con los requisitos anteriores.</li></ul>')

        }

    })


    $(document).on ("change", '#option_soil', function( event ){
        if ($('#option_soil').serialize().split("=")[1] == "0"){


            $('#info_img_soil').html('<img style="display: block; margin: auto;" src="/static/images/1_soil.png">')
            $('#info_descrip_soil').html('<ul><li>El suelo de la fundación es duro. Esto se puede saber cuando alrededor de la edificación no existen hundimientos, cuando no se evidencien arboles o postes inclinados, no se siente vibración cuando pasa un vehículo pesado cerca de la vivienda o cuando en general las viviendas no presentan agrietamientos o daños generalizados, especialmente grietas en los pisos o hundimientos y desniveles en el mismo.</li></ul>')


        }
        if ($('#option_soil').serialize().split("=")[1] == "1"){

            $('#info_img_soil').html('<img style="display: block; margin: auto;" src="/static/images/2_soil.png">')
            $('#info_descrip_soil').html('<ul><li>El suelo de la fundación es de mediana resistencia. Se puede presentar en general algunos hundimientos y vibraciones por el paso de vehículos pesados. Se pueden identificar algunos daños generalizados en viviendas o manifestaciones de hundimientos pequeños.</li></ul>')


        }
        if ($('#option_soil').serialize().split("=")[1] == "2"){

            $('#info_img_soil').html('<img style="display: block; margin: auto;" src="/static/images/3_soil.png">')
            $('#info_descrip_soil').html('<ul><li>El suelo de la fundación es blando o es arena suelta. Se sabe por el hundimiento en las zonas vecinas, se siente la vibración al paso de vehículos pesados y la vivienda ha presentado asentamientos considerables en el tiempo de construcción. La mayoría de las viviendas de la zona presentan agrietamientos y/o hundimientos.</li></ul>')

        }

    })


    $(document).on ("change", '#option_environment', function( event ){
        if ($('#option_environment').serialize().split("=")[1] == "0"){

            $('#info_img_environment').html('<img style="display: block; margin: auto;" src="/static/images/1_environment.png">')
            $('#info_descrip_environment').html('<ul><li>La topografía donde se encuentra la vivienda es plana o muy poco inclinada.</li></ul>')


        }
        if ($('#option_environment').serialize().split("=")[1] == "1"){


            $('#info_img_environment').html('<img style="display: block; margin: auto;" src="/static/images/2_environment.png">')
            $('#info_descrip_environment').html('<ul><li>La topografía donde se encuentra la casa tiene un angulo entre 20 a 30 grados de inclinación con la horizontal.</li></ul>')


        }
        if ($('#option_environment').serialize().split("=")[1] == "2"){

            $('#info_img_environment').html('<img style="display: block; margin: auto;" src="/static/images/3_environment.png">')
            $('#info_descrip_environment').html('<ul><li>La vivienda se encuentra localizada en pendientes con una inclinación mayor de 30 grados con la horizontal.</li></ul>')


        }

    })



    $(document).on ("click", '#help', function( event ){
        var url="{% url 'info_construccion' %}"
        var text = '<p>Este método evaluá aspectos cualitativos de la vivienda,  en donde usted determinara bajo su criterio en qué estado  se encuentra la vivienda. <br></br>El estado se clasifica por Bueno, Regular y Malo el cual contará con una descripción y una imagen para explicar el item seleccionado.<br></br> El campo de Observaciones es opcional</p>'
        Swal.fire({
            title: 'Información de ayuda',
            html: text,
            footer: `<a href="/users/info_construccion" target="_blank">Ir al manual de la pagina</a>`
          })

    })

    $(document).on ("click", '#help_cuantitativo', function( event ){
        var url="{% url 'info_construccion' %}"
        var text = `<p>Este método evaluá aspectos cuantativos de la vivienda, 
        en donde usted tendrá que suministrar informacion exacta (dimension y tipo de elementos, sistema constructivo, etc..), la cual
        se procesara bajo los criterios de la NSR-10 Titulo A.10 y para determinar la fuerza equivalente</p>`
        Swal.fire({
            title: 'Información de ayuda',
            html: text,
            footer: `<a href="/users/info_construccion" target="_blank">Ir al manual de la pagina</a>`
          })

    })



    $(document).on ("change", '#muro_fachada', function( event ){
        if ($('#muro_fachada').serialize().split("=")[1] == "0"){
            $('#muro_caracteristica').html(`<option selected></option>
                    <option value="[1.8, 2.5, 3.1, 3.8, 4.4]">Pañetado en ambas caras</option>
                    <option value="[1.3, 2, 2.6 , 3.3, 3.9 ]">Sin pañetar</option>`
            )
        }
        if ($('#muro_fachada').serialize().split("=")[1] == "1"){
            $('#muro_caracteristica').html(`<option selected></option>
                    <option value="[1.4, 1.45, 1.9, 2.25, 2.6]">Sin relleno</option>
                    <option value="[1, 1.7, 2.25, 2.7, 3.15]">Relleno cada 1.2 m</option>
                    <option value="[1.8, 1.8, 2.3, 2.8, 3.3]">Relleno cada 1.0 m</option>
                    <option value="[1.8, 1.8, 2.4, 3, 3.45]">Relleno cada 0.8 m</option>
                    <option value="[2, 2, 2.6, 3.2, 3.75]">Relleno cada 0.6 m</option>
                    <option value="[2.2, 2.2, 2.9, 3.6, 4.3]">Relleno cada 0.4 m</option>
                    <option value="[3, 3, 4, 5, 6.1]">Todas las celdas llenas</option>`
            )
        }
        if ($('#muro_fachada').serialize().split("=")[1] == "2"){
            $('#muro_caracteristica').html(`
                    <option value="[1.9, 2.9, 3.8, 4.7, 5.5]" selected>Sin pañetar</option>`
            )


        }
        if ($('#muro_fachada').serialize().split("=")[1] == "3"){
            $('#muro_caracteristica').html(`
                    <option value="[2, 3.1, 4.2, 5.3, 6.4]" selected>Sin pañetar</option>`
            )



        }


    })

    $(document).on ("change", '#muro_divisorio', function( event ){
        if ($('#muro_divisorio').serialize().split("=")[1] == "0"){
            $('#muro_caracteristica_divisorio').html(`<option selected></option>
                    <option value="[1.8, 2.5, 3.1, 3.8, 4.4]">Pañetado en ambas caras</option>
                    <option value="[1.3, 2, 2.6 , 3.3, 3.9 ]">Sin pañetar</option>`
            )
        }
        if ($('#muro_divisorio').serialize().split("=")[1] == "1"){
            $('#muro_caracteristica_divisorio').html(`<option selected></option>
                    <option value="[1.4, 1.45, 1.9, 2.25, 2.6]">Sin relleno</option>
                    <option value="[1, 1.7, 2.25, 2.7, 3.15]">Relleno cada 1.2 m</option>
                    <option value="[1.8, 1.8, 2.3, 2.8, 3.3]">Relleno cada 1.0 m</option>
                    <option value="[1.8, 1.8, 2.4, 3, 3.45]">Relleno cada 0.8 m</option>
                    <option value="[2, 2, 2.6, 3.2, 3.75]">Relleno cada 0.6 m</option>
                    <option value="[2.2, 2.2, 2.9, 3.6, 4.3]">Relleno cada 0.4 m</option>
                    <option value="[3, 3, 4, 5, 6.1]">Todas las celdas llenas</option>`
            )
        }
        if ($('#muro_divisorio').serialize().split("=")[1] == "2"){
            $('#muro_caracteristica_divisorio').html(`
                    <option value="[1.9, 2.9, 3.8, 4.7, 5.5]" selected>Sin pañetar</option>`
            )


        }
        if ($('#muro_divisorio').serialize().split("=")[1] == "3"){
            $('#muro_caracteristica_divisorio').html(`
                    <option value="[2, 3.1, 4.2, 5.3, 6.4]" selected>Sin pañetar</option>`
            )



        }


    })




    $(document).on ("change", '#type_cubierta', function( event ){
        var html = `
            <label>Espesor (mm):</label>
            <input
                class="form-control"
                type="number"
                name="espesor_cubierta"
                required
                step=".001"
                min="0"
                disabled
            >`
        var html2 = `
            <label>Espesor (mm):</label>
            <input
                class="form-control"
                type="number"
                name="espesor_cubierta"
                required
                step=".001"
                min="0"
                required
            >`
        var type_cubierta = $('#type_cubierta').serialize().split("=")[1]
        if ( !(type_cubierta == "0.0020" || type_cubierta == "0.0060" || type_cubierta == "0.0100") ){
            $('#espesor_disable').html(html)
        }
        else {
            $('#espesor_disable').html(html2)

        }


    })






    $(document).on ("change", '#type_piso', function( event ){
        var html = `
            <label>Espesor (mm):</label>
            <input
                class="form-control"
                type="number"
                name="espesor_piso"
                required
                step=".001"
                min="0"
                disabled
            >`
        var html2 = `
            <label>Espesor (mm):</label>
            <input
                class="form-control"
                type="number"
                name="espesor_piso"
                required
                step=".001"
                min="0"
                required
            >`
        var type_piso = $('#type_piso').serialize().split("=")[1]
        if ( !(type_piso == "0.02" || type_piso == "0.03")){
            $('#piso_disable').html(html)
        }
        else {
            $('#piso_disable').html(html2)

        }


    })











    $(document).on ("change", '#type_recubrimiento', function( event ){
        var html = `
            <label>Espesor (mm):</label>
            <input
                class="form-control"
                type="number"
                name="espesor_recubrimiento"
                required
                step=".001"
                min="0"
                disabled
            >`
        var html2 = `
            <label>Espesor (mm):</label>
            <input
                class="form-control"
                type="number"
                name="espesor_recubrimiento"
                required
                step=".001"
                min="0"
                required
            >`
        var type_recubrimiento = $('#type_recubrimiento').serialize().split("=")[1]
        if ( !(type_recubrimiento == "0.01" || type_recubrimiento == "0.003")){
            $('#recubrimiento_disable').html(html)
        }
        else {
            $('#recubrimiento_disable').html(html2)

        }


    })




    $(document).on ("change", '#ocupacion', function( event ){
        if ($('#ocupacion').serialize().split("=")[1] == "0"){
            $('#ocupacion_uso').html(`<option selected></option>
                    <option value=3.0>Corredores y escaleras</option>
                    <option value=2.0>Oficinas</option>
                    <option value=5.0>Restaurantes</option>
                    `
            )
        }
        if ($('#ocupacion').serialize().split("=")[1] == "1"){
            $('#ocupacion_uso').html(`<option selected></option>
                    <option value=2.0>Salones de clase</option>
                    <option value=5.0>Corredores y escaleras</option>
                    <option value=2.0>Salones de lectura (Bibloceta)</option>
                    <option value=7.0>Estanterías (Bibloceta)</option>`
            )
        }
        if ($('#ocupacion').serialize().split("=")[1] == "2"){
            $('#ocupacion_uso').html(`<option selected></option>
                    <option value=5.0>Minorista</option>
                    <option value=6.0>Mayorista</option>`
            )


        }
        if ($('#ocupacion').serialize().split("=")[1] == "3"){
            $('#ocupacion_uso').html(`<option selected></option>
                    <option value=5.0>Balcones</option>
                    <option value=1.8>Cuartos privados y sus corredores</option>
                    <option value=3.0>Escaleras</option>`
            )
        }


        if ($('#ocupacion').serialize().split("=")[1] == "4"){
            $('#ocupacion_uso').html(`<option selected></option>
                    <option value=6.0>Liviano</option>
                    <option value=12.0>Pesado</option>`
            )
        }


        if ($('#ocupacion').serialize().split("=")[1] == "5"){
            $('#ocupacion_uso').html(`<option selected></option>
                    <option value=2.5>Garajes para automóviles de pasajeros</option>
                    <option value=5.0>Garajes para vehículos de carga de hasta 2.000 kg de capacidad.</option>`
            )
        }

    })















});


