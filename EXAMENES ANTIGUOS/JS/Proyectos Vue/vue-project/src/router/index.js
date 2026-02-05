import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      redirect: '/tareas'
    },
    {
      path: '/contador',
      name: 'contador',
      component: () => import('../modules/contador/components/contador.vue')
    },
    {
      path: '/tareas',
      name: 'tareas',
      component: () => import('../modules/tareas/components/tareas.vue')
    },
    {
      path: '/registrar',
      name: 'registrar',
      component: () => import('../modules/registro/views/RegistroVista.vue')
    }
  ],
})

export default router
