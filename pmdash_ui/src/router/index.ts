import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';
import DashboardRoute from './routers/dashboard-router';
import UserRoute from './routers/user-router';

const routes = [...UserRoute, ...DashboardRoute];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach(() => {
  setTimeout(() => {
    window.scrollTo(0, 0);
  }, 100);
});

export default router;
