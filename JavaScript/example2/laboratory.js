
// Punto 1
let nombre = prompt("¿Cuál es tu nombre?");
let edad = Number(prompt("¿Cuántos años tienes?"));
let correo = prompt("¿Cuál es tu correo electrónico?");

let estado = prompt("¿Estás activo? (true/false)").toLowerCase();
//estado = Boolean(estado) // Convertir edad a booleano
estado = estado === "true";
//ingresoDatos();    

console.log(typeof nombre + " " + nombre); // string
console.log(typeof edad + " " + edad);   // number  
console.log(typeof correo + " " + correo) ; // string
console.log(typeof estado + " " +  estado); // boolean




// Punto 2

validarEdad(edad);

//&& estado != false || estado != 0 || estado != null || estado != undefined || estado != NaN
if (nombre != "" && estado == true) {       
    console.log("Usuario activo con nombre registrado.");    
}else{
     console.log("Usuario con estado inactivo o sin nombre registrado.");
}

// Punto 3

contraseñaIngresada= prompt("Por favor, ingresa una contraseña (mínimo 8 caracteres):");
intento = 0;

validarContraseña(contraseñaIngresada , intento);


// Punto 4 -- funciones

/* function ingresoDatos() {
    let nombre = prompt("¿Cuál es tu nombre?");
    let edad = Number(prompt("¿Cuántos años tienes?"));
    let correo = prompt("¿Cuál es tu correo electrónico?");

    let estado = prompt("¿Estás activo? (true/false)").toLowerCase();
    // estado = Boolean(estado) // Convertir edad a booleano
    estado = estado === "true";
    
    console.log(typeof nombre + " " + nombre); // string
    console.log(typeof edad + " " + edad);   // number  
    console.log(typeof correo + " " + correo) ; // string
    console.log(typeof estado + " " +  estado); // boolean
    
    return console.log(` 
    El nombre del usuario es: ${nombre},
    La edad del usuario es: ${edad},
    El correo del usuario es: ${correo},
    El estado del usuario es: ${estado}.    
    `)

   
}
 */


function validarEdad(edad) {
    if (edad >= 18) {
       return console.log(`${nombre} es mayor de edad.`);
    }else {
        return console.log(`${nombre} es menor de edad.`);
    }
}

function validarContraseña(contraseña , intento) {
    contraseñaGuardada = "Segura123";
    while (intento < 2 ) {
   
        if (contraseña === contraseñaGuardada) {
            console.log("Contraseña correcta. Acceso concedido.");  
            break;
        }else {
            console.log("Contraseña incorrecta. Intenta de nuevo.");
            contraseñaIngresada = prompt("Por favor, ingresa una contraseña (mínimo 8 caracteres):");
            
        }
    
        intento++;
        if (intento == 2) {
            console.log("Has agotado todos los intentos. Acceso denegado.");   
            break;         
        }

    }   
   
}

