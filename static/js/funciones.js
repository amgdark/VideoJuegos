function muestraModal(url, titulo){
    document.getElementById('formEliminar').action = url;
    document.getElementById('modalCuerpo').innerHTML = `¿Deseas eliminar el videojuego ${titulo}?`;
}

$("#id_estado").on('change', function(){   
    alert(this.value);

});