$(document).ready(function () {
    //Esta sección es para llamar la barra de navegación en distintas páginas
    $(function(){
        $('#navbar').load('static/tienda/navbar.html')
    })

    //Esta es para llamar el footer
    $(function(){
        $('#barraFooter').load('barrafooter.html')
    })

    //Esta sección es para cambiar apariencia de botones en hover
    $('#botonEscogerCiudad').mouseover(function () { 
        $('#botonEscogerCiudad').addClass('boton-hover')

        $('#botonEscogerCiudad').removeClass('boton')
    });

    $('#botonEscogerCiudad').mouseleave(function () { 
        $('#botonEscogerCiudad').addClass('boton')

        $('#botonEscogerCiudad').removeClass('boton-hover')
    });

    $('#attachImageButton').mouseover(function () { 
        $('#attachImageButton').addClass('boton-hover')

        $('#attachImageButton').removeClass('boton')
    });

    $('#attachImageButton').mouseleave(function () { 
        $('#attachImageButton').addClass('boton')

        $('#attachImageButton').removeClass('boton-hover')
    });

    $('#botonPedir').mouseover(function () { 
        $('#botonPedir').addClass('boton-hover')

        $('#botonPedir').removeClass('boton')
    });

    $('#botonPedir').mouseleave(function () { 
        $('#botonPedir').addClass('boton')

        $('#botonPedir').removeClass('boton-hover')
    });

    
    //------------------------------------------------------------

    // Esta sección es para aceptar una imagen y validarla
    $('#attachImageButton').click(function () {
        $('#fileInput').click();
    });

    $('#fileInput').change(function () {
        var archivosPermitidos = /(\.jpg|\.jpeg|\.png)$/i;
        var fileName = $(this).val().split('\\').pop();
        if (!archivosPermitidos.exec(fileName)) {
            alert('Tipo de archivo inválido. Sólo .jpeg, jpg, or .png');
            this.value = '';
            return false;
        }
    });
    //-----------------------------------------------------------------------
    
});