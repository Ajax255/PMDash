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
      console.log('members: ', this.members);
    },
    async createMember(member: Member) {
      const resp = await PMDASH_API_CLIENT.post(`pmdash/create-member`, member);
      console.log(resp);
    },
    async searchForMember(uuid: string) {
      const resp = await PMDASH_API_CLIENT.get(`pmdash/search-for-member?uuid=${uuid}`);
      console.log(resp);
    },
    async searchAllMembers() {
      const resp = await PMDASH_API_CLIENT.get(`pmdash/search-all-members`);
      console.log(resp);
    },
    async updateMember(uuid: string, {}) {
      const resp = await PMDASH_API_CLIENT.put(`pmdash/update-member?uuid=${uuid}`);
      console.log(resp);
    },
    async deleteMember(uuid: string) {
      const resp = await PMDASH_API_CLIENT.delete(`pmdash/delete-member?uuid=${uuid}`);
      console.log(resp);
    },

    // team endpoint calls
    async fetchAllTeams() {
      const resp = await PMDASH_API_CLIENT.get(`pmdash/fetch-all-teams`);
      this.teams = resp.data;
      console.log('teams: ', this.teams);
    },
    async createTeam(team: Team) {
      const resp = await PMDASH_API_CLIENT.post(`pmdash/create-team`, team);
      console.log(resp);
    },
    async searchForTeam(uuid: string) {
      const resp = await PMDASH_API_CLIENT.get(`pmdash/search-for-team?uuid=${uuid}`);
      console.log(resp);
    },
    async searchAllTeams() {
      const resp = await PMDASH_API_CLIENT.get(`pmdash/search-all-teams`);
      console.log(resp);
    },
    async updateTeam(uuid: string, {}) {
      const resp = await PMDASH_API_CLIENT.put(`pmdash/update-team?uuid=${uuid}`);
      console.log(resp);
    },
    async deleteTeam(uuid: string) {
      const resp = await PMDASH_API_CLIENT.delete(`pmdash/delete-team?uuid=${uuid}`);
      console.log(resp);
    },
  },
});
