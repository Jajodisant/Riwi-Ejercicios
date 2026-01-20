
lista= [20,1,2,8,30,50,40,3,90]

let mayor = lista.reduce((a,b) =>  {
    /* a>b ? a:b */
    if(a>b){
        return a;
    }else{
        return b;
    }
})

console.log(mayor)