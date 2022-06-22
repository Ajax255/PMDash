import { defineStore } from 'pinia';
import { PMDASH_API_CLIENT } from '../clients/axios-client';
import Member from '../models/member';
import Team from '../models/team';

export const usePMDashStore = defineStore('PMDash', {
  state: () => ({
    member: {} as Member,
    members: [] as Member[],
    memberMode: '',

    team: {} as Team,
    teams: [] as Team[],
    teamMode: '',
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
      this.member = resp.data;
      return resp;
    },
    async searchAllMembers(searchTerm: string, fields: string[]) {
      let url = `pmdash/search-all-members?searchTerm=${searchTerm}`;

      fields.forEach((field) => {
        url += `&fields=${field}`;
      });
      const resp = await PMDASH_API_CLIENT.get(url);
      this.members = resp.data;
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
    },
    async createTeam(team: Team) {
      const resp = await PMDASH_API_CLIENT.post(`pmdash/create-team`, JSON.stringify(team));
      return resp;
    },
    async searchForTeam(searchTerm: string, fields: string[]) {
      const resp = await PMDASH_API_CLIENT.get(`pmdash/search-for-team?searchTerm=${searchTerm}&fields=${fields}`);
      this.team = resp.data;
      return resp;
    },
    async searchAllTeams(searchTerm: string, fields: string[]) {
      let url = `pmdash/search-all-teams?searchTerm=${searchTerm}`;

      fields.forEach((field) => {
        url += `&fields=${field}`;
      });
      const resp = await PMDASH_API_CLIENT.get(url);
      this.teams = resp.data;
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
