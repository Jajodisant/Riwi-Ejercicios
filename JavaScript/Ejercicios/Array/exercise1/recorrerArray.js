
// usando for tradicional y entries() para recorrer un array
console.log('--- Recorrer un array ---');
let lista = ['Manzana', 'Banana', 'Cereza', 'Dátil', 'Elderberry'];

//forma convencional
for (let i = 0; i < lista.length; i++){
    console.log(`${[i + 1]}. ${lista[i]}`);
}

//con entries
console.log('--- Usando entries() ---');

for (const [index, elemento] of lista.entries()){
    console.log(`${[index + 1]}. ${elemento}`);
}

// Output:
// 1. Manzana
// 2. Banana
// 3. Cereza
// 4. Dátil
// 5. Elderberry    

