<script setup>
</script>

<template>
  <aside class="barra-lateral">
    <h3 class="titulo">Menú</h3>
    <nav>
      <ul>
        <li><router-link to="/tareas">Tareas</router-link></li>
        <li><router-link to="/contador">Contador</router-link></li>
        <li><router-link to="/registrar">Registrar</router-link></li>
      </ul>
    </nav>
  </aside>
</template>

<style scoped>
.barra-lateral {
  width: 220px;
  background: #fff;
  padding: 1rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
  border-right: 4px solid #1e66f5;
  box-sizing: border-box;
  position: sticky;
  top: 1rem;
  height: calc(100vh - 2rem);
  overflow: auto;
  border-radius: 6px;
}

.titulo {
  margin: 0 0 1rem 0;
  font-size: 1.05rem;
  color: #1e66f5;
  text-align: center;
}

.barra-lateral nav ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.barra-lateral nav li {
  margin: 0.6rem 0;
}

.barra-lateral a {
  display: block;
  padding: 0.45rem 0.6rem;
  color: #333;
  text-decoration: none;
  border-radius: 4px;
  transition: background-color .15s, color .15s;
}

.barra-lateral a:hover {
  background: #f0f6ff;
  color: #0f49d1;
}

@media (max-width: 800px) {
  .barra-lateral {
    position: static;
    width: 100%;
    height: auto;
    border-right: none;
    border-bottom: 4px solid #1e66f5;
    margin-bottom: 1rem;
  }
}
</style>