import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import DashboardRoute from './routers/DashboardRouter'
import UserRoute from './routers/UserRouter'

const routes: Array<RouteRecordRaw> = [...UserRoute, ...DashboardRoute]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach(() => {
  setTimeout(() => {
    window.scrollTo(0, 0)
  }, 100)
})

export default router
