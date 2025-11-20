let numeros = []; 
let num; // 
let sumaTotal=0;

do {
    
    num = Number(prompt("Introduce un número (Introduce 0 para salir):")); 
    
    
    if (num !== 0) {
        numeros.push(num); 
    }
} while (num !== 0); 

console.log("Solo se sumarán numeros impares.");

for(let i=0; i<numeros.length;i++){
    let valor=numeros[i];
    if(numeros[i] % 2 !==0){
    sumaTotal +=valor;
    }
    console.log("El valor en la posicion "+i+" es: "+valor);
}

console.log(numeros.length);
console.log("La suma total de la cadena de numeros insertada es:"+sumaTotal);
