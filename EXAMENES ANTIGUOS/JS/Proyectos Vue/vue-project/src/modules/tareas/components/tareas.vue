<script setup>
import { ref } from 'vue';

const tareas=ref([]);

const nuevaTarea= ref('');

const addTarea=()=>{
    tareas.value.push(nuevaTarea.value)
    nuevaTarea.value='';
}

const borrarTarea=(indice)=>{
    tareas.value.splice(indice,1);
}
</script>

<template>
<h2> Lista de tareas</h2>
<input type="text" v-model="nuevaTarea" @keyup.enter="addTarea" >
<ul>
    <li v-for="(tarea, index) in tareas " :key="index">
        {{ tarea }}
    <button @click="borrarTarea(index)">Borrar tareaa</button>

    </li>
</ul>
</template>

<style scoped>

</style>