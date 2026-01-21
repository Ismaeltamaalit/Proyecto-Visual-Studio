<script setup>

</script>

<template>
<div class="sidebar">
<h2>Barra Lateral</h2>
<ul>
    <li><RouterLink to="/contador">Contador </RouterLink></li>
    <li><RouterLink to="/tareas">Tareas </RouterLink></li>

</ul>
</div>
</template>

<style scoped>
.sidebar{
    width: 200px;
    background-color: aquamarine;
    padding:20px;
}
</style>