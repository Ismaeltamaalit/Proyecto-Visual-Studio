<script setup>
import BarraLateral from '../components/barraLateral.vue';
import Tareas from '../components/tareas.vue';
import Contador from '../components/contador.vue';
</script>

<template>
  <div class="layout">
    <BarraLateral />
    <main class="contenido">
      <!-- Mostrar Tareas por defecto (primer hijo). Al hacer click en la barra lateral
           con href="#contador" se mostrará la sección con id="contador" -->
      <section id="tareas">
        <Tareas />
      </section>

      <section id="contador">
        <Contador />
      </section>
    </main>
  </div>
</template>

<style scoped>
.layout {
  display: flex;
  gap: 1rem;
  align-items: flex-start;
  padding: 1rem;
  box-sizing: border-box;
}

.contenido {
  flex: 1;
  min-width: 0;
  background: #fafafa;
  padding: 1rem;
  border-radius: 6px;
  box-shadow: 0 1px 6px rgba(0,0,0,0.03);
}

/* ocultar todas las secciones y mostrar solo la que sea :target.
   además mostrar la primera sección por defecto (Tareas) si no hay hash */
.contenido > section { display: none; padding: 0.5rem 0; }
.contenido > section:target { display: block; }

/* en móvil apilar */
@media (max-width: 800px) {
  .layout { flex-direction: column; padding: 0.5rem; }
  .contenido { padding: 0.75rem; }
}
</style>