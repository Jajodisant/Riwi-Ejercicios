

const url = 'https://api.themoviedb.org/3/discover/movie'
const token = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmNmQyYWY3NGM4NDlmMmQxMjMwYTZmYTg2MzcwMzgyZiIsIm5iZiI6MTcwNDk4Nzg4NC4xOTI5OTk4LCJzdWIiOiI2NWEwMGNlY2YwNjQ3YzAxMmJhNDU3MDUiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.c8VeTnSBbCkhF-z1VeRMWcAbOXzQTvJCbl3-4cDziCk'


const imageUrl = 'https://image.tmdb.org/t/p/original';

//captura de datos del html
const containerMovies = document.getElementById("container-Movies");
const prevBtn = document.getElementById('prev');
const nextBtn = document.getElementById('next');
const pageButtons = document.querySelectorAll('.flex.items-center.gap-2 button');

// para el paginado
let paginaActual = 1;
let totalPaginas = 500;


//autenticador
const headers ={
    "Authorization" : `Bearer ${token}`
}

/* fetch(url , {headers})
    .then(response => response.json())
    .then(data => console.log(data))
 */

async function getAllMovies(page = 1){
   const response = await fetch( `${url}?page=${page}` , { headers })
    
    if(!response.ok){
        throw new Error("Error al consultar pelicula");
    }
    const data =  await response.json();
    totalPaginas = data.total_pages; // Actualizar total páginas
    //console.log(data);
    //return data.results;

    return data.results.slice(0, 12); // Limita la cantidad de cards que le paso al redes para que pueda imprimir
}



//Funcion que permite renderizar en pantalla con el css de talwind
function renderMovies(movies){

        containerMovies.innerHTML = "";
        movies.forEach(element => {

            const poster = element.poster_path
            ? `${imageUrl}${element.poster_path}`
            : 'https://via.placeholder.com/300x450?text=No+Image';

            const cardMovie = document.createElement("div");

            cardMovie.innerHTML =`<div class="p-4 bg-white border border-gray-200 hover:-translate-y-1 transition duration-300 rounded-lg shadow shadow-black/10 max-w-80">
                    <img class="rounded-md max-h-40 w-full object-cover" src="${poster}" alt="officeImage">
                    <p class="text-gray-900 text-xl font-semibold ml-2 mt-4">
                        ${element.title}
                    </p>
                    <p class="text-zinc-400 text-sm/6 mt-2 ml-2 mb-2">
                        ${element.overview}
                    </p>
                    <button type="button" class="bg-indigo-600 hover:bg-indigo-700 transition cursor-pointer mt-4 mb-3 ml-2 px-6 py-2 font-medium rounded-md text-white text-sm">
                        Learn More
                    </button>
                </div>
            `
            containerMovies.appendChild(cardMovie)

        });
}



//carga la pagina teniendo en cuenta la pagina actual

async function cargarPagina(page){
    const movies = await getAllMovies(page);
    renderMovies(movies);

    paginaActual = page;


    // Actualizar botones numéricos activos
    pageButtons.forEach(btn => btn.classList.remove('text-indigo-500', 'border', 'border-indigo-200', 'rounded-full'));
    const index = page - 1;
    if (pageButtons[index]) {
        pageButtons[index].classList.add('text-indigo-500', 'border', 'border-indigo-200', 'rounded-full');
    }

    // Desactivar prev/next
    prevBtn.disabled = paginaActual === 1;
    nextBtn.disabled = paginaActual === totalPaginas;


}

function paginado(){
    
    prevBtn.addEventListener("click", () => {
        if(paginaActual > 1){
            cargarPagina(paginaActual - 1);
        }
    });

    nextBtn.addEventListener("click", () => {
        if(paginaActual < totalPaginas){
            cargarPagina(paginaActual + 1);
        }
    });

    pageButtons.forEach((btn, index) => {
    btn.addEventListener("click", () => {
        const page = index + 1; // número de página
        cargarPagina(page);
    });
});   
}


function filterFunction(){
    const inputFilter = document.getElementById("FilterText").toLowerCase();
    
   
}




async function main() {
   // movies = await getAllMovies();
    //console.log(movies);
    //renderMovies(movies);
    await cargarPagina(paginaActual);
    paginado(); // 👈 ESTO FALTABA
}

main()

