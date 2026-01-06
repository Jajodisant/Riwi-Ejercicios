function abrirModal(id) {
    document.getElementById(id).style.display = "block";
}

function cerrarModal(id) {
    document.getElementById(id).style.display = "none";
}

// Cerrar haciendo clic fuera del modal
window.onclick = function(event) {
    const modales = document.querySelectorAll('.modal');
    modales.forEach(modal => {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    });
};
