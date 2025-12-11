// ==========================
// 1) Calculadora básica
// ==========================


/*


explico aqui que he hecho, basicamente he codigo, primero,  una 
validacion que alerta si no has insertado un numero valido
cojo para hacer el switch con las diferentes operaciones, 
"operacion" y entre comillas las operaciones, para capturar las opciones
tuve que convertir en numeros a y b para la primera porque
concatenaba solo esa, el primer ejercicio funciona

*/
function calcular(a, b, operacion) {

    if(isNaN(a)|| isNaN(b)){
        alert("INSERTA UN NUMERO VALIDO");
        
    }else{
        switch(operacion){
        case "sumar" :
            a=parseInt(a);
            b=parseInt(b);
        return a+b;
        break;

        case "restar":
       return a-b;
        break;

        case "multiplicar":
        return a*b;
        break;

        case "dividir":
        return a/b;
        break;

        
    }
    }


    
    

}

function Calculadora() {
    const a = document.getElementById('calcA').value;
    const b = document.getElementById('calcB').value;
    const op = document.getElementById('calcOp').value;
    const r = calcular(a, b, op);
    document.getElementById('calcOut').textContent = 'Resultado: ' + r;
}