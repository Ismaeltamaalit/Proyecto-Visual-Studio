 function llama(){
        petition("https://jsonplaceholder.typicode.com/users");
      }


      function petition (url) {
        http_request=new XMLHttpRequest();
        http_request.overrrideMimeType('text/json');
        http_request.onreadystatechange=respuesta;
        http_request.open('GET', url, true);

      }

      function respuesta(){
        if(http_request.readyState==4){
          if(http_request.status==200){
            var json=http_request.responseJSON;
            var datos=json.querySelectorAll("name", "phone");
            for(let i=0; i<nombres.length;i++){
              console.log(datos[i].textContent);
            }
          }else{
            console.log('Hubo problemas con la peticion')
          }
        }
      }
