
console.log("conectado..");

url= "https://pokeapi.co/";
fetch(url)
    .then(res =>{
        if(!res.ok) throw new Error('error en la peticion');
        return res.json();
    })
.catch(err => console.error(err));
