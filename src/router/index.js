import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import RegisterView from '../views/RegisterView.vue'
import Edit from '../views/Edit.vue'


const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  { 
    path: '/product/:id', 
    component: Edit 
  },
  { 
    path: '/register', 
    component: RegisterView 
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
