import { defineStore } from 'pinia';
import { PMDASH_API_CLIENT } from '../clients/axios-client';
import Task from '../models/task';

export const useTaskStore = defineStore('daseboard', {
  state: () => ({
    task: {} as Task,
    taskList: [] as Task[],
  }),
  getters: {
    // finishedTodos(state) {
    //   return state.todos.filter((todo) => todo.isFinished)
    // },
    // unfinishedTodos(state) {
    //   return state.todos.filter((todo) => !todo.isFinished)
    // },
    // filteredTodos(): ToDo[] {
    //   if (this.filter === Filter.finished) {
    //     return this.finishedTodos
    //   } else if (this.filter === Filter.unfinished) {
    //     return this.unfinishedTodos
    //   }
    //   return this.todos
    // },
  },
  actions: {
    async searchTaskByID(uuid: string) {
      const resp = await PMDASH_API_CLIENT.get(`tasks/search-by-id?uuid${uuid}`);
      console.log(resp);
    },
    async searchAllTasksOfProject(uuid: string) {
      const resp = await PMDASH_API_CLIENT.get(`tasks/search-all?uuid${uuid}`);
      console.log(resp);
    },
    async createTask(task: Task) {
      const resp = await PMDASH_API_CLIENT.post(`tasks/create`);
      console.log(resp);
    },
    async updateTask(uuid: string, {}) {
      const resp = await PMDASH_API_CLIENT.patch(`tasks/update?uuid=${uuid}`);
      console.log(resp);
    },
    async deleteTask(uuid: string) {
      const resp = await PMDASH_API_CLIENT.delete(`tasks/delete?uuid=${uuid}`);
      console.log(resp);
    },
  },
});
