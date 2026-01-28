import { defineStore } from "pinia";
import { ref } from "vue";

const userRegistrarStore = defineStore('registrar', ()=> {
    const nombre=ref('')
    const correo=ref('')

    const guardarRegistro=(nombreFormulario, correoFormulario)=>{
        nombre.value=nombreFormulario
        correo.value=correoFormulario
    }
    return(nombre, correo, guardarRegistro)
})