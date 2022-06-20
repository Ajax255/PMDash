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
    async searchMemberByID(uuid: string) {
      const resp = await PMDASH_API_CLIENT.get(`pmdash/search-member?uuid=${uuid}`);
      console.log(resp);
    },
    async searchAllMembers() {
      const resp = await PMDASH_API_CLIENT.get(`pmdash/search-all-members`);
      console.log(resp);
    },
    async searchTeamByID(uuid: string) {
      const resp = await PMDASH_API_CLIENT.get(`pmdash/search-team?uuid=${uuid}`);
      console.log(resp);
    },
    async searchAllTeams() {
      const resp = await PMDASH_API_CLIENT.get(`pmdash/search-all-teams`);
      console.log(resp);
    },
    async createMember(member: Member) {
      const resp = await PMDASH_API_CLIENT.post(`pmdash/create-member`);
      console.log(resp);
    },
    async updateMember(uuid: string, {}) {
      const resp = await PMDASH_API_CLIENT.patch(`pmdash/update-member?uuid=${uuid}`);
      console.log(resp);
    },
    async deleteMember(uuid: string) {
      const resp = await PMDASH_API_CLIENT.delete(`pmdash/delete-member?uuid=${uuid}`);
      console.log(resp);
    },
    async createTeam(team: Team) {
      const resp = await PMDASH_API_CLIENT.post(`pmdash/create-team`);
      console.log(resp);
    },
    async updateTeam(uuid: string, {}) {
      const resp = await PMDASH_API_CLIENT.patch(`pmdash/update-team?uuid=${uuid}`);
      console.log(resp);
    },
    async deleteTeam(uuid: string) {
      const resp = await PMDASH_API_CLIENT.delete(`pmdash/delete-team?uuid=${uuid}`);
      console.log(resp);
    },
  },
});
