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
    async searchProjectByID(uuid: string) {
      const resp = await PMDASH_API_CLIENT.get(`projects/search-by-id?uuid${uuid}`);
      console.log(resp);
    },
    async searchAllProjects(uuid: string) {
      const resp = await PMDASH_API_CLIENT.get(`projects/search-all?uuid${uuid}`);
      console.log(resp);
    },
    async createProject(project: Project) {
      console.log('createProject', project);
      const resp = await PMDASH_API_CLIENT.post(`projects/create`, project);
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
