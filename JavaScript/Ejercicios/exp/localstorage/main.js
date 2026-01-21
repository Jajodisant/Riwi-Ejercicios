// Ejemplo simple
localStorage.setItem("nombre", "Juan");
alert(localStorage.getItem("nombre"));

//con array de objetos
const list =[{
    id: 123,
    name: "sara",
    lastname: "jrasz"
},
{
    id: 456,
    name: "alejandra",
    lastname: "wilson"
}]


let guardar = JSON.stringify(list)
localStorage.setItem("users", guardar);

let recuperar = JSON.parse(localStorage.setItem("users"))
console.log(recuperar)

