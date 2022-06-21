import { defineStore } from 'pinia';
import { PMDASH_API_CLIENT } from '../clients/axios-client';
import Member from '../models/member';
import Team from '../models/team';

export const usePMDashStore = defineStore('PMDash', {
  state: () => ({
    members: [] as Member[],
    teams: [] as Team[],
  }),
  getters: {},
  actions: {
    // member endpoint calls
    async fetchAllMembers() {
      const resp = await PMDASH_API_CLIENT.get(`pmdash/fetch-all-members`);
      this.members = resp.data;
      return resp;
    },
    async createMember(member: Member) {
      const resp = await PMDASH_API_CLIENT.post(`pmdash/create-member`, JSON.stringify(member));
      return resp;
    },
    async searchForMember(searchTerm: string, fields: string[]) {
      const resp = await PMDASH_API_CLIENT.get(`pmdash/search-for-member?searchTerm=${searchTerm}&fields=${fields}`);
      return resp;
    },
    async searchAllMembers() {
      const resp = await PMDASH_API_CLIENT.get(`pmdash/search-all-members`);
      return resp;
    },
    async updateMember(uuid: string, member: Member) {
      const resp = await PMDASH_API_CLIENT.put(`pmdash/update-member/${uuid}`, member);
      return resp;
    },
    async deleteMember(uuid: string) {
      const resp = await PMDASH_API_CLIENT.delete(`pmdash/delete-member/${uuid}`);
      return resp;
    },

    // team endpoint calls
    async fetchAllTeams() {
      const resp = await PMDASH_API_CLIENT.get(`pmdash/fetch-all-teams`);
      this.teams = resp.data;
      console.log('teams: ', this.teams);
    },
    async createTeam(team: Team) {
      const resp = await PMDASH_API_CLIENT.post(`pmdash/create-team`, JSON.stringify(team));
      return resp;
    },
    async searchForTeam(uuid: string, fields: string[]) {
      const resp = await PMDASH_API_CLIENT.get(`pmdash/search-for-team?uuid=${uuid}&fields=${fields}`);
      return resp;
    },
    async searchAllTeams(searchTerm: string, fields: string[]) {
      const resp = await PMDASH_API_CLIENT.get(`pmdash/search-all-teams?searchTerm=${searchTerm}&fields=${fields}`);
      return resp;
    },
    async updateTeam(uuid: string, team: Team) {
      const resp = await PMDASH_API_CLIENT.put(`pmdash/update-team/${uuid}`, team);
      return resp;
    },
    async deleteTeam(uuid: string) {
      const resp = await PMDASH_API_CLIENT.delete(`pmdash/delete-team/${uuid}`);
      return resp;
    },
  },
});
