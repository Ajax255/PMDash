import { RouteRecordRaw } from 'vue-router';
import CreateEditProject from '../../views/CreateEditProject.vue';
import ViewProject from '../../views/ViewProject.vue';

const ProjectRouter: Array<RouteRecordRaw> = [
  {
    path: '/project/:uuid',
    name: 'View-Project',
    component: ViewProject,
  },
  {
    path: '/create-project',
    name: 'Create-Project',
    component: CreateEditProject,
  },
  {
    path: '/edit-project/:uuid',
    name: 'Edit-Project',
    component: CreateEditProject,
  },
];
export default ProjectRouter;
