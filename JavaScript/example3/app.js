const btnCambiarColor = document.getElementById('changeColor');
const titulo = document.getElementById('title');


btnCambiarColor.addEventListener('click', () => {
    titulo.style.color = titulo.style.color === 'blue' ? 'black' : 'blue';
});
