// ==========================
// 2) Suma hasta N con filtro
// ==========================


/*
explico aqui que he hech


*/
function sumarHastaN(n, filtro, modo) {

    if(modo.value="for"){
        if(filtro="pares"){
           for(let i=0; i<=n;i++){
            n+=2;
        } 
        }else if(filtro="impares"){
            for(let i=0; i<=n;i++){
                n+=1;
            }
        }
        
    }else if(modo="while"){
        if(filtro="pares"){
          while(n<=n){
            n+=2;
          }
        }else if(filtro="impares"){
           while(n<=n){
            n+=1;
          }
        }
    }
    

}

function SumaHastaN() {
    const n = document.getElementById('sumN').value;
    const filtro = document.getElementById('sumFiltro').value;
    const modo = document.getElementById('sumModo').value;
    const r = sumarHastaN(n, filtro, modo);
    document.getElementById('sumOut').textContent = 'Suma: ' + r;
}