import { RouteRecordRaw } from 'vue-router'
import PageNotFound from '../../views/PageNotFound.vue'

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
    // the 404 route, when none of the above matches
    path: '/404',
    name: 'error-404',
    component: PageNotFound,
  },
  {
    path: '/:pathMatch(.*)*',
    redirect: '/404',
  },
]
export default UserRouter
