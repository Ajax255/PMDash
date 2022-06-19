import { RouteRecordRaw } from 'vue-router';
import PageNotFound from '../../views/PageNotFound.vue';

const UserRouter: Array<RouteRecordRaw> = [
  // {
  //   path: "/login",
  //   name: "login",
  //   component: () => import("@/views/auth/Login.vue")
  // },
  // {
  //   path: "/password-reset",
  //   name: "password-reset",
  //   component: () => import("@/views/auth/PasswordReset.vue")
  // },
  {
    path: '/page-not-found',
    name: 'Page-Not-Found',
    component: PageNotFound,
  },
  {
    path: '/:pathMatch(.*)*',
    redirect: '/page-not-found',
  },
];
export default UserRouter;
