function setCookie(nombre, valor, dias) {
    const fecha = new Date();
    fecha.setTime(fecha.getTime() + (dias * 24 * 60 * 60 * 1000));
    document.cookie = `${nombre}=${valor}; expires=${fecha.toUTCString()}; path=/`;
}


function getCookie(nombre) {
    const cookies = document.cookie.split("; ");
    for (let cookie of cookies) {
        const [key, value] = cookie.split("=");
        if (key === nombre) {
            return value;
        }
    }
    return null;
}





const select = document.getElementById("idioma");
const texto = document.getElementById("texto");
const body = document.ge

// Diccionario de idiomas
const idiomas = {
    español: "hola a todos",
    ingles: "hello everyone"
};

// Cambiar idioma al seleccionar
select.addEventListener("change", () => {
    const idiomaSeleccionado = select.value;

    texto.textContent = idiomas[idiomaSeleccionado];

    // Guardar idioma en cookie por 30 días
    setCookie("idioma", idiomaSeleccionado, 30);
});


const idiomaGuardado = getCookie("idioma");

if (idiomaGuardado) {
    texto.textContent = idiomas[idiomaGuardado];
    select.value = idiomaGuardado;
}
