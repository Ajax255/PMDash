import { RouteRecordRaw } from 'vue-router';
import QuickView from '../../views/QuickView.vue';
const PMDashRouter: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'dashboard',
    component: QuickView,
  },
];
export default PMDashRouter;
