const cookie= document.cookie = "intentos=+1; expires=fecha; secure";


  const vehiculo= document.getElementById("tipoVehiculo");
  const formulario=document.getElementById("formulario")

  vehiculo.addEventListener("formdata", seleccion());

  function seleccion(vehiculo) {
    if (formulario.value=="errores") {
      focus.vehiculo;
    }
  }

  //

   const matricula=document.getElementById("matricula");
   const nombreFoco=document.getElementById("nombre");

   matricula.addEventListener("focus", matriculaFoco());
   nombre.addEventListener("focus", nombreFoco());


  function matriculaFoco(){
    matricula.toUpperCase;
  }

  function nombreFoco(){
    nombre.toUpperCase;
  }

  //

  const regexNombre=/\w/;

  const nombre=document.getElementById("nombre");

  let comprobacion=regexNombre.test(regexNombre, nombre);

  if (comprobacion!=true) {
 alert("solo letras")
  }