<script setup>
import BarraLateral from '../components/barraLateral.vue';
</script>

<template>
  <div class="layout">
    <BarraLateral />
    <main class="contenido">
      <!-- aquí Vue Router renderizará la ruta activa -->
      <router-view />
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

@media (max-width: 800px) {
  .layout { flex-direction: column; padding: 0.5rem; }
  .contenido { padding: 0.75rem; }
}
</style>