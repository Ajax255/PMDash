import { createRouter, createWebHistory } from 'vue-router';
import PMDashRouter from './routers/pmdash-router';
import TaskRouter from './routers/task-router';
import ProjectRouter from './routers/project-router';
import UserRouter from './routers/user-router';

const routes = [...PMDashRouter, ...ProjectRouter, ...TaskRouter, ...UserRouter];

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
