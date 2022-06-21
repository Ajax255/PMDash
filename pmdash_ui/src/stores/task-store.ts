import { defineStore } from 'pinia';
import { PMDASH_API_CLIENT } from '../clients/axios-client';
import Task from '../models/task';

export const useTaskStore = defineStore('daseboard', {
  state: () => ({
    task: {} as Task,
    tasks: [] as Task[],
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
    async fetchAlltasks() {
      const resp = await PMDASH_API_CLIENT.get(`tasks/fetch-all-tasks`);
      this.tasks = resp.data;
      console.log('tasks: ', resp);
    },
    async createTask(task: Task) {
      const resp = await PMDASH_API_CLIENT.post(`tasks/create`, task);
      console.log(resp);
    },
    async searchForTask(uuid: string) {
      const resp = await PMDASH_API_CLIENT.get(`tasks/search-for-task?uuid${uuid}`);
      console.log(resp);
    },
    async searchAllTasks(uuid: string) {
      const resp = await PMDASH_API_CLIENT.get(`tasks/search-all-tasks?uuid${uuid}`);
      console.log(resp);
    },
    async updateTask(uuid: string, {}) {
      const resp = await PMDASH_API_CLIENT.put(`tasks/update?uuid=${uuid}`);
      console.log(resp);
    },
    async deleteTask(uuid: string) {
      const resp = await PMDASH_API_CLIENT.delete(`tasks/delete?uuid=${uuid}`);
      console.log(resp);
    },
  },
});
