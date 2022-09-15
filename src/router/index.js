import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import RegisterView from '../views/RegisterView.vue'
import EditView from '../views/EditView.vue'
import RelatorioView from '../views/RelatorioView.vue'
import TrocasView from '../views/TrocasView.vue'




const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  { 
    path: '/product/:id', 
    component: EditView 
  },
  { 
    path: '/register', 
    component: RegisterView 
  },
  { 
    path: '/relatorios', 
    component: RelatorioView 
  },
  { 
    path: '/trocas', 
    component: TrocasView
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
