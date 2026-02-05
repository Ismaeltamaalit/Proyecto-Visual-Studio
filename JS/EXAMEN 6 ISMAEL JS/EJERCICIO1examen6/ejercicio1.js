 function anadir(){
          

          let botonDerecho=document.getElementById("btnRight");
          let botonIzquierdo=document.getElementById("btnLeft");

          if(botonDerecho.addEventListener("click", añadirDerecha)){
            objeto=document.getElementsByClassName("elemento");
            const tablaNueva=document.getElementById("destino");

            let elemento= document.createElement("li");
            var texto=document.createTextNode(elemento);

            tablaNueva= elemento.appendChild(texto);



          }

          if(botonIzquierdo.addEventListener("click", añadirIzquierda)){
            const tabla=document.getElementById("origen")
            texto=tabla;
            
            
            
          }

          function borrarElemento(){
            let texto=this.parentElement;
            texto.remove();
            
          }





        }