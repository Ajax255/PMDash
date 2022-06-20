import { defineStore } from 'pinia';
import { PMDASH_API_CLIENT } from '../clients/axios-client';
import Project from '../models/project';

export const useProjectStore = defineStore('Project', {
  state: () => ({
    project: {} as Project,
    projectList: [] as Project[],
  }),
  getters: {},
  actions: {
    async fetchProject(uuid: string) {
      const resp = await PMDASH_API_CLIENT.get(`projects/fetch-by-id?uuid${uuid}`);
      console.log(resp);
    },
    async fetchAllProjects(uuid: string) {
      const resp = await PMDASH_API_CLIENT.get(`projects/fetch-all?uuid${uuid}`);
      console.log(resp);
    },
    async createProject(project: Project) {
      const resp = await PMDASH_API_CLIENT.post(`projects/create`);
      console.log(resp);
    },
    async updateProject(uuid: string, {}) {
      const resp = await PMDASH_API_CLIENT.patch(`projects/update?uuid=${uuid}`);
      console.log(resp);
    },
    async deleteProject(uuid: string) {
      const resp = await PMDASH_API_CLIENT.delete(`projects/delete?uuid=${uuid}`);
      console.log(resp);
    },
  },
});
