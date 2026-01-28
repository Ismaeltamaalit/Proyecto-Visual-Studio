<script setup>
import { ref } from 'vue'
import { Form, Field, ErrorMessage } from 'vee-validate'
import { schema } from '../schemas/ValidacionesSchema.js';
import { errorMessages } from 'vue/compiler-sfc';
import {useRegistrarStore} from '../stores/RegistrarStore.js'



const nombre = ref('')
const email = ref('')
const RegistrarStore= useRegistrarStore();  
const onSubmit = (values) => {
  console.log('Registro:', values)
  alert('Formulario enviado: ' + values.nombre + ' — ' + values.email)
  nombre.value = ''
  email.value = ''
}
</script>

<template>
    <h2>Formulario de registro</h2>
    <Form :validation-schema="schema" @submit="onSubmit" >
      <div class="form">
        <label for="nombre">Nombre</label>
        <Field name="nombre" id="nombre" v-model="nombre" type="text" placeholder="Introducir su nombre" />
        <errorMessages name="nombre"></errorMessages>
      </div>

      <div class="form">
        <label for="email">Email</label>
        <Field name="correo" id="correo" v-model="email" type="email" placeholder="Introduzca su email" />
        <errorMessages name="correo"></errorMessages>
      </div>

      <div>
        <button type="submit">REGISTRAR</button>
      </div>
    </Form>
</template>

<style scoped>
.form{
  margin-bottom: 10px;
}
input {
  display:block;
  width:100%;
  padding:6px 8px;
  box-sizing:border-box;
  margin-top:4px;
}
button {
  padding:8px 12px;
  background:#1e66f5;
  color:white;
  border:none;
  border-radius:4px;
  cursor:pointer;
}
</style>