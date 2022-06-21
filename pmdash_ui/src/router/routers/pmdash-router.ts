import { RouteRecordRaw } from 'vue-router';
import QuickView from '../../views/QuickView.vue';
const PMDashRouter: Array<RouteRecordRaw> = [
  {
    path: '/',
    redirect: '/dashboard',
    component: QuickView,
    children: [
      {
        path: '/dashboard',
        name: 'dashboard',
        component: QuickView,
      },
    ],
  },
];
export default PMDashRouter;
