<template>
  <!-- @click="sidebarOpen = true" -->
  <div class="min-h-full">
    <div v-if="loading === true">loading</div>
    <div v-else-if="loadingError === true">Failed to fetch data please reload page</div>
    <div v-else>
      <side-bar
        :side-bar-open="sideBarOpen"
        @open-side-bar="sideBarOpen = true"
        @close-side-bar="sideBarOpen = false"
        @open-team-modal="openEditModal"
      />
      <!-- Main column -->
      <div class="lg:pl-64 flex flex-col">
        <!-- Search header -->
        <div class="sticky top-0 z-10 flex-shrink-0 flex h-16 bg-white border-b border-gray-200 lg:hidden">
          <button
            type="button"
            class="px-4 border-r border-gray-200 text-gray-500 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-purple-500 lg:hidden"
            @click="sideBarOpen = true"
          >
            <span class="sr-only">Open sidebar</span>
            <MenuAlt1Icon class="h-6 w-6" aria-hidden="true" />
          </button>
          <div class="flex-1 flex justify-between px-4 sm:px-6 lg:px-8">
            <div class="flex-1 flex">
              <form class="w-full flex md:ml-0" action="#" method="GET">
                <label for="search-field" class="sr-only">Search</label>
                <div class="relative w-full text-gray-400 focus-within:text-gray-600">
                  <div class="absolute inset-y-0 left-0 flex items-center pointer-events-none">
                    <SearchIcon class="h-5 w-5" aria-hidden="true" />
                  </div>
                  <input
                    id="search-field"
                    name="search-field"
                    class="block w-full h-full pl-8 pr-3 py-2 border-transparent text-gray-900 placeholder-gray-500 focus:outline-none focus:ring-0 focus:border-transparent focus:placeholder-gray-400 sm:text-sm"
                    placeholder="Search"
                    type="search"
                  />
                </div>
              </form>
            </div>
          </div>
        </div>
        <main class="flex-1">
          <!-- Page title & actions -->
          <div class="border-b border-gray-200 px-4 py-4 sm:flex sm:items-center sm:justify-between sm:px-6 lg:px-8">
            <div class="flex-1 min-w-0">
              <h1 class="text-lg font-medium leading-6 text-gray-900 sm:truncate">PM Dashboard</h1>
            </div>
            <div class="mt-4 flex sm:mt-0 sm:ml-4">
              <button
                type="button"
                class="order-0 inline-flex items-center px-4 py-2 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-purple-600 hover:bg-purple-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-purple-500 sm:order-1 sm:ml-3"
                @click="openModal('project-modal', ModalMode.create)"
              >
                Create Project
              </button>
              <button
                type="button"
                class="order-0 inline-flex items-center px-4 py-2 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-green-700 hover:bg-green-800 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-600 sm:order-1 ml-3"
                @click="openModal('task-modal', ModalMode.create)"
              >
                Create Task
              </button>
            </div>
          </div>
          <project-table @open-project-modal="openEditModal" />
        </main>
      </div>
    </div>
    <project-modal :show-project-modal="showProjectModal" @close-project-modal="closeModal('project-modal')" />
    <task-modal :show-task-modal="showTaskModal" @close-task-modal="closeModal('task-modal')" />
    <team-modal :show-team-modal="showTeamModal" @close-team-modal="closeModal('team-modal')" />
    <member-modal :show-member-modal="showMemberModal" @close-member-modal="closeModal('member-modal')" />
  </div>
</template>

<script setup lang="ts">
import { ref, onBeforeMount } from 'vue';
import { MenuAlt1Icon } from '@heroicons/vue/outline';
import { SearchIcon } from '@heroicons/vue/solid';

import { usePMDashStore } from '../stores/pmdash-store';
import { useProjectStore } from '../stores/project-store';
import { useTaskStore } from '../stores/task-store';

import ProjectTable from '../components/ProjectTable.vue';
import SideBar from '../components/SideBar.vue';

import ProjectModal from '../components/ProjectModal.vue';
import TaskModal from '../components/TaskModal.vue';
import TeamModal from '../components/TeamModal.vue';
import MemberModal from '../components/MemberModal.vue';
import { ModalMode } from '../enums/modal-mode';
import Project from '../models/project';
import Task from '../models/task';
import Member from '../models/member';

const pmdashStore = usePMDashStore();
const projectStore = useProjectStore();
const taskStore = useTaskStore();

const loading = ref(true);
const loadingError = ref(false);

const sideBarOpen = ref(false);
const showProjectModal = ref(false);
const showTaskModal = ref(false);
const showTeamModal = ref(false);
const showMemberModal = ref(false);

const getData = async () => {
  try {
    loading.value = true;
    pmdashStore.fetchAllMembers();
    pmdashStore.fetchAllTeams();
    projectStore.fetchAllProjects();
  } catch (error) {
    loadingError.value = true;
  } finally {
    loading.value = false;
  }
};

const openEditModal = (payload: { modalName: string; mode: ModalMode; uuid: string }) => {
  console.log('rans');
  openModal(payload.modalName, payload.mode, payload.uuid);
};

const openModal = (modalName: string, mode: ModalMode, uuid?: string) => {
  switch (modalName) {
    case 'project-modal': {
      setupProjectModal(mode, uuid);
      break;
    }
    case 'task-modal': {
      setupTaskModal(mode, uuid);
      break;
    }
    case 'team-modal': {
      setupTeamModal(mode, uuid);
      break;
    }
    case 'member-modal': {
      setupMemberModal(mode, uuid);
      break;
    }
    default: {
      //Do nothing
      break;
    }
  }
};

const setupProjectModal = async (mode: ModalMode, uuid?: string) => {
  if ((mode === ModalMode.edit || mode === ModalMode.view) && uuid) {
    await projectStore.searchForProject(uuid, ['_id']);
  } else {
    projectStore.project = new Project();
  }

  if (mode === ModalMode.edit && uuid) {
    projectStore.projectMode = ModalMode.edit;
  } else if (mode === ModalMode.create) {
    projectStore.projectMode = ModalMode.create;
  } else {
    projectStore.projectMode = ModalMode.view;
  }

  showProjectModal.value = true;
};

const setupTaskModal = async (mode: ModalMode, uuid?: string) => {
  if ((mode === ModalMode.edit || mode === ModalMode.view) && uuid) {
    await taskStore.searchForTask(uuid, ['_id']);
  } else {
    taskStore.task = new Task();
  }

  if (mode === ModalMode.edit && uuid) {
    taskStore.taskMode = ModalMode.edit;
  } else if (mode === ModalMode.create) {
    taskStore.taskMode = ModalMode.create;
  } else {
    taskStore.taskMode = ModalMode.view;
  }

  showTaskModal.value = true;
};

const setupTeamModal = async (mode: ModalMode, uuid?: string) => {
  if ((mode === ModalMode.edit || mode === ModalMode.view) && uuid) {
    await pmdashStore.searchForTeam(uuid, ['_id']);
  } else {
    projectStore.project = new Project();
  }

  if (mode === ModalMode.edit && uuid) {
    pmdashStore.teamMode = ModalMode.edit;
  } else if (mode === ModalMode.create) {
    pmdashStore.teamMode = ModalMode.create;
  } else {
    pmdashStore.teamMode = ModalMode.view;
  }

  showTeamModal.value = true;
};

const setupMemberModal = async (mode: ModalMode, uuid?: string) => {
  if ((mode === ModalMode.edit || mode === ModalMode.view) && uuid) {
    await pmdashStore.searchForMember(uuid, ['_id']);
  } else {
    pmdashStore.member = new Member();
  }

  if (mode === ModalMode.edit && uuid) {
    pmdashStore.memberMode = ModalMode.edit;
  } else if (mode === ModalMode.create) {
    pmdashStore.memberMode = ModalMode.create;
  } else {
    pmdashStore.memberMode = ModalMode.view;
  }

  showMemberModal.value = true;
};

const closeModal = (modalName: string) => {
  switch (modalName) {
    case 'project-modal': {
      showProjectModal.value = false;
      break;
    }
    case 'task-modal': {
      showTaskModal.value = false;
      break;
    }
    case 'team-modal': {
      showTeamModal.value = false;
      break;
    }
    case 'member-modal': {
      showMemberModal.value = false;
      break;
    }
    default: {
      //Do nothing
      break;
    }
  }
};

onBeforeMount(() => {
  getData();
});
</script>

<style scoped></style>
