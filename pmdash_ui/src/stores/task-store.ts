import { defineStore } from 'pinia';
import { PMDASH_API_CLIENT } from '../clients/axios-client';
import Task from '../models/task';

export const useTaskStore = defineStore('daseboard', {
  state: () => ({
    task: {} as Task,
    tasks: [] as Task[],
    taskMode: '',
  }),
  getters: {},
  actions: {
    async fetchAllTasks() {
      const resp = await PMDASH_API_CLIENT.get(`tasks/fetch-all-tasks`);
      this.tasks = resp.data;
      return resp;
    },
    async createTask(task: Task) {
      const resp = await PMDASH_API_CLIENT.post(`tasks/create`, JSON.stringify(task));
      return resp;
    },
    async searchForTask(uuid: string, fields: string[]) {
      const resp = await PMDASH_API_CLIENT.get(`tasks/search-for-task?uuid${uuid}&fields=${fields}`);
      this.task = resp.data;
      return resp;
    },
    async searchAllTasks(searchTerm: string, fields: string[]) {
      let url = `tasks/search-all-tasks?searchTerm=${searchTerm}`;

      fields.forEach((field) => {
        url += `&fields=${field}`;
      });
      const resp = await PMDASH_API_CLIENT.get(url);
      this.tasks = resp.data;
      return resp;
    },
    async updateTask(uuid: string, task: Task) {
      const resp = await PMDASH_API_CLIENT.put(`tasks/update/${uuid}`, task);
      return resp;
    },
    async deleteTask(uuid: string) {
      const resp = await PMDASH_API_CLIENT.delete(`tasks/delete/${uuid}`);
      return resp;
    },
  },
});
