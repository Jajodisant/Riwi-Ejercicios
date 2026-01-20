/* 
lista = [10,5,30,10,20,5,30,30,30,50,25,11,1,11]; // 10,5,30,20

const eliminarDuplicados = lista.reduce( (a,b) => {
    if (a.eliminados.includes(b)){
        a.duplicados.push(b);
    }else{
        a.eliminados.push(b);
    }
    return a;
},{duplicados : [], eliminados:[]})

console.log(eliminarDuplicados.eliminados);
console.log(eliminarDuplicados.duplicados);
// console.log([...new Set(lista)]); otra forma de hacerlo


console.log("con set")
const borrado = [...lista,new Set(lista)]
console.log(borrado)


 */


let array = [1,2,3,4,5,6,6,6,7,8,9,9];
let sinRepetidos = [];

for (let i = 0; i < array.length; i++){
    var existe = false;

    for( let j= 0; i < sinRepetidos.length; i++){
        if( array[i] === sinRepetidos[j]){
            existe=true;
            break;
        }
    }
    if(!existe){
        sinRepetidos.push(array[i]);
    }
}

console.log(sinRepetidos)