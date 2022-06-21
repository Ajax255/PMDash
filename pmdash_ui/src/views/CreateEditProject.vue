<template>
  <div class="space-y-6">
    <div v-if="loading === true">loading</div>
    <div v-else-if="loadingError === true">Failed to fetch data please reload page</div>
    <div v-else>
      <form class="space-y-8 divide-y divide-gray-200" @submit.prevent="onSubmit()">
        <div class="space-y-8 divide-y divide-gray-200 sm:space-y-5">
          <div>
            <div>
              <h3 v-if="!route.params.uuid" class="text-lg leading-6 font-medium text-gray-900">New Project</h3>
              <h3 v-else class="text-lg leading-6 font-medium text-gray-900">Edit Project</h3>
              <!-- <p class="mt-1 max-w-2xl text-sm text-gray-500">
                This information will be displayed publicly so be careful what you share.
              </p> -->
            </div>

            <div class="mt-6 sm:mt-5 space-y-6 sm:space-y-5">
              <div class="sm:grid sm:grid-cols-3 sm:gap-4 sm:items-start sm:border-t sm:border-gray-200 sm:pt-5">
                <label for="title" class="block text-sm font-medium text-gray-700 sm:mt-px sm:pt-2"> Title </label>
                <div class="mt-1 sm:mt-0 sm:col-span-2">
                  <input
                    id="title"
                    v-model="projectStore.project.title"
                    type="text"
                    class="max-w-lg block w-full shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:max-w-xs sm:text-sm border-gray-300 rounded-md"
                  />
                </div>
              </div>

              <div class="sm:grid sm:grid-cols-3 sm:gap-4 sm:items-start sm:border-t sm:border-gray-200 sm:pt-5">
                <label for="application" class="block text-sm font-medium text-gray-700 sm:mt-px sm:pt-2">
                  Area of Application
                </label>
                <div class="mt-1 sm:mt-0 sm:col-span-2">
                  <select
                    id="application"
                    v-model="projectStore.project.application"
                    autocomplete="application"
                    class="max-w-lg block focus:ring-indigo-500 focus:border-indigo-500 w-full shadow-sm sm:max-w-xs sm:text-sm border-gray-300 rounded-md"
                  >
                    <option>Software Engineering</option>
                    <option>Human Resources</option>
                    <option>Costumer Success</option>
                  </select>
                </div>
              </div>

              <div class="sm:grid sm:grid-cols-3 sm:gap-4 sm:items-start sm:border-t sm:border-gray-200 sm:pt-5">
                <label for="discription" class="block text-sm font-medium text-gray-700 sm:mt-px sm:pt-2">
                  Discription
                </label>
                <div class="mt-1 sm:mt-0 sm:col-span-2">
                  <textarea
                    id="discription"
                    v-model="projectStore.project.description"
                    rows="3"
                    class="max-w-lg shadow-sm block w-full focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm border border-gray-300 rounded-md"
                  />
                  <p class="mt-2 text-sm text-gray-500">Describe your project</p>
                </div>
              </div>

              <div class="sm:grid sm:grid-cols-3 sm:gap-4 sm:items-start sm:border-t sm:border-gray-200 sm:pt-5">
                <label for="members" class="block text-sm font-medium text-gray-700 sm:mt-px sm:pt-2"> Memebers </label>
                <div class="mt-1 sm:mt-0 sm:col-span-2">
                  <select
                    id="members"
                    class="max-w-lg block focus:ring-indigo-500 focus:border-indigo-500 w-full shadow-sm sm:max-w-xs sm:text-sm border-gray-300 rounded-md"
                  >
                    <option>Anthony</option>
                    <option>Gage</option>
                    <option>Corbin</option>
                  </select>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="pt-5">
          <div class="flex justify-end">
            <button
              type="button"
              class="bg-white py-2 px-4 border border-gray-300 rounded-md shadow-sm text-sm font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
              @click="router.push({ path: '/' })"
            >
              Cancel
            </button>
            <button
              type="submit"
              class="ml-3 inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
            >
              Save
            </button>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive, onBeforeMount } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import Project from '../models/project';
import { useProjectStore } from '../stores/project-store';

const route = useRoute();
const router = useRouter();
const projectStore = useProjectStore();

const loading = ref(true);
const loadingError = ref(false);
const getData = async () => {
  try {
    loading.value = true;
    if (route.params.uuid) {
      await projectStore.searchForProject(route.params.uuid as string, ['_id']);
    } else {
      projectStore.project = new Project();
    }
  } catch (error) {
    loadingError.value = true;
  } finally {
    loading.value = false;
  }
};

const onSubmit = () => {
  if (route.params.uuid) {
    updateProject();
  } else {
    createProject();
  }
};

const createProject = async () => {
  await projectStore.createProject(projectStore.project);
  router.push({ path: '/' });
};

const updateProject = async () => {
  const res = await projectStore.updateProject(route.params.uuid as string, projectStore.project);
  router.push({ path: '/' });
  console.log(res);
};

onBeforeMount(() => {
  getData();
});
</script>

<style scoped></style>
