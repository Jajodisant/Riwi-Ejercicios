
function Jugador(nombre){
    this.nombre = nombre;
    this.pv = 100;
    this.sp = 100;

    this.curar = function(jugadorObjetivo){
        
        if (this.sp >= 40){
            this.sp -= 40;
            jugadorObjetivo.pv += 20;
        }else{
            console.log(this.nombre, " " ,"no hay sp suficiente")
        }  
        this.estado(jugadorObjetivo)    
    }
    this.estado = function(jugadorObjetivo){
        console.info(this);
        console.info(jugadorObjetivo);
    }

    this.llenarSP =  function(){
        if(this.sp >= 0 &&  this.sp <100){           
            this.sp += 20;
            this.estado()
            console.log(this.nombre, this.sp," ", "Ha llenado");
        }else{
            console.log("sp estan llenos");
        }

    }

    this.tirarFlecha =  function(jugadorObjetivo){
        if(jugadorObjetivo.pv > 40){
            jugadorObjetivo.pv -=40;
        }else{
            jugadorObjetivo.pv =0;
            console.error(jugadorObjetivo.nombre +" "+ "murio noooooo!!!!");
        }
        this.estado(jugadorObjetivo)
    }
}

let gandalf = new Jugador("gandalf");
let legolas = new Jugador("legolas");

console.log(gandalf);
console.log(legolas);

gandalf.curar(legolas)

