import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AwardsView from '../views/AwardsView.vue'

const routes = [
  { path: '/', name: 'home', component: HomeView },
  { path: '/awards', name: 'awards', component: AwardsView },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
