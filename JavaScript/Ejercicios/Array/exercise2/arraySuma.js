lista = [2, 4, 6, 8, 10];
suma = 0;

// Usando for tradicional
for (let i = 0; i< lista.length; i++){
    suma = suma + lista[i];
    console.log (`${i +1}. La suma es: ${suma}`)
}

// usando metodo reduce
console.log('--- Usando reduce() ---');
sumaReducida = lista.reduce((cont, elemento) => cont + elemento, 0);
console.log(`La suma total es: ${sumaReducida}`);
