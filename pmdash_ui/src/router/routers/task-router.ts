import { RouteRecordRaw } from 'vue-router';
import CreateEditTask from '../../views/CreateEditTask.vue';
import ViewTask from '../../views/ViewTask.vue';

const TaskRouter: Array<RouteRecordRaw> = [
  {
    path: '/task/:uuid',
    name: 'Task',
    component: ViewTask,
  },
  {
    path: '/create-task',
    name: 'Create-Task',
    component: CreateEditTask,
  },
  {
    path: '/edit-task/:uuid',
    name: 'Edit-Task',
    component: CreateEditTask,
  },
];

export default TaskRouter;
