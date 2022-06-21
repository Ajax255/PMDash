import { defineStore } from 'pinia';
import { PMDASH_API_CLIENT } from '../clients/axios-client';
import Project from '../models/project';

export const useProjectStore = defineStore('Project', {
  state: () => ({
    project: {} as Project,
    projects: [] as Project[],
  }),
  getters: {},
  actions: {
    async fetchAllProjects() {
      const resp = await PMDASH_API_CLIENT.get('projects/fetch-all-projects');
      this.projects = resp.data;
    },
    async createProject(project: Project) {
      const resp = await PMDASH_API_CLIENT.post('projects/create', JSON.stringify(project));
    },
    // async def search_for_one(searchTerm: str, fields: list[str]):
    async searchForProject(uuid: string, fields: string[]) {
      const resp = await PMDASH_API_CLIENT.get(`projects/search-for-project?searchTerm=${uuid}&fields=${fields}`);
      this.project = resp.data;
    },
    async searchAllProjects(uuid: string) {
      const resp = await PMDASH_API_CLIENT.get(`projects/search-all-projects?uuid${uuid}`);
      console.log(resp);
    },
    async updateProject(uuid: string, project: Project) {
      console.log('Project', project);
      const resp = await PMDASH_API_CLIENT.put(`projects/update/${uuid}`, project);
      console.log(resp);
    },
    async deleteProject(uuid: string) {
      const resp = await PMDASH_API_CLIENT.delete(`projects/delete/${uuid}`);
      console.log(resp);
    },
  },
});
