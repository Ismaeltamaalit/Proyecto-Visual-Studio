      let btnAñadir=document.querySelector("#addItemButton");
      btn=document.getElementById("addItemButton");

      let btnBorrar=document.querySelector("#btnBorrar");
      btnBorrar.addEventListener("click", borrar);

      function anadir(){
        let ul =document.querySelector("shoppingList");
        if(ul==null){
          ul=document.createElement("ul");
                    document.body.appendChild(li);

        }
            let texto=prompt("texto para la lista");

             let txt=document.createTextNode(texto);

             let li= document.createElement("li");

             li.appendChild(txt);

             ul.append(li);

             document.getElementById("shoppingList").innerHTML="Elementos: "+ li.children.length;



      }

      function borrar(){
        let id=parseInt(prompt("elemento a eliminar"));

        var ul=document.getElementById("lista");

        var liBorrar=li.children[id-1];

        liBorrar.remove();
        document.getElementById("shoppingList").innerHTML="Elementos: "+ ul.children.length;
      }



      /**
       * He creado dos funciones una de borrar y otra de añadir,
       * ademas de llamar y relacionar los botones. 
       */