$(document).ready(function () {
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

    $('#botonDonar').mouseover(function () { 
        $('#botonDonar').addClass('boton-hover')

        $('#botonDonar').removeClass('boton')
    });

    $('#botonDonar').mouseleave(function () { 
        $('#botonDonar').addClass('boton')

        $('#botonDonar').removeClass('boton-hover')
    });
    
    //------------------------------------------------------------

    // Esta sección es para aceptar una imagen y validarla NO SE USA
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