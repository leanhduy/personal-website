import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ProjectsView from '../views/ProjectsView.vue'
import AwardsView from '../views/AwardsView.vue'
import ExperienceView from '../views/ExperienceView.vue'

const routes = [
  { path: '/', name: 'home', component: HomeView },
  { path: '/projects', name: 'projects', component: ProjectsView },
  { path: '/awards', name: 'awards', component: AwardsView },
  { path: '/experiences', name: 'experiences', component: ExperienceView },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
