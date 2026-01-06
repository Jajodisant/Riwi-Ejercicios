function mostrarGlobo(event) {
    const globo = document.getElementById("globo");
    const contenedor = document.querySelector(".contenedor-imagen");

    // Coordenadas dentro del contenedor
    const rect = contenedor.getBoundingClientRect();

    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;

    // Posicionar el globo cerca del clic
    globo.style.left = (x + 10) + "px";
    globo.style.top = (y - 20) + "px";

    globo.querySelector(".globo-img").src = imgSrc;
    globo.querySelector(".globo-texto").textContent = texto;

    globo.style.display = "block";
}

function cerrarGlobo(event) {
    event.stopPropagation(); // Evita que el clic llegue al window
    const globo = document.getElementById("globo");
    globo.style.display = "none";
}

const globo = document.getElementById("globo");
globo.addEventListener("click", function(e) {
    e.stopPropagation();
});

// Ocultar globo al hacer clic fuera
window.addEventListener("click", function (e) {
    const globo = document.getElementById("globo");
    if (!globo.contains(e.target) && e.target.tagName !== "AREA") {
        globo.style.display = "none";
    }
});

