<template>
  <TransitionRoot as="template" :show="showProjectModal">
    <Dialog as="div" class="relative z-10" @close="$emit('closeProjectModal')">
      <TransitionChild
        as="template"
        enter="ease-out duration-300"
        enter-from="opacity-0"
        enter-to="opacity-100"
        leave="ease-in duration-200"
        leave-from="opacity-100"
        leave-to="opacity-0"
      >
        <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
      </TransitionChild>

      <div class="fixed z-10 inset-0 overflow-y-auto">
        <div class="flex items-end sm:items-center justify-center min-h-full p-4 text-center sm:p-0">
          <TransitionChild
            as="template"
            enter="ease-out duration-300"
            enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
            enter-to="opacity-100 translate-y-0 sm:scale-100"
            leave="ease-in duration-200"
            leave-from="opacity-100 translate-y-0 sm:scale-100"
            leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
          >
            <DialogPanel
              class="relative bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:max-w-lg sm:w-full"
            >
              <form class="space-y-8 divide-y divide-gray-200" @submit.prevent="onSubmit()">
                <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
                  <div class="space-y-6">
                    <div class="space-y-8 divide-y divide-gray-200 sm:space-y-5">
                      <div>
                        <div>
                          <h3
                            v-if="projectStore.projectMode === ModalMode.create"
                            class="text-lg leading-6 font-medium text-gray-900"
                          >
                            New Project
                          </h3>
                          <h3
                            v-if="projectStore.projectMode === ModalMode.edit"
                            class="text-lg leading-6 font-medium text-gray-900"
                          >
                            Edit Project
                          </h3>
                          <!-- <p class="mt-1 max-w-2xl text-sm text-gray-500">
                              This information will be displayed publicly so be careful what you share.
                            </p> -->
                        </div>

                        <div class="mt-6 sm:mt-5 space-y-6 sm:space-y-5">
                          <div class="sm:grid sm:grid-cols-3 sm:gap-4 sm:items-start sm:border-t sm:border-gray-200 sm:pt-5">
                            <label for="title" class="block text-sm font-medium text-gray-700 sm:mt-px sm:pt-2">
                              Title
                            </label>
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
                            <label for="members" class="block text-sm font-medium text-gray-700 sm:mt-px sm:pt-2">
                              Memebers
                            </label>
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
                  </div>
                </div>
                <div class="bg-gray-50 px-4 py-3 sm:px-6 sm:flex sm:flex-row-reverse">
                  <button
                    type="button"
                    class="mt-3 w-full inline-flex justify-center rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-base font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:mt-0 sm:ml-3 sm:w-auto sm:text-sm"
                    @click="$emit('closeProjectModal')"
                  >
                    Cancel
                  </button>

                  <button
                    type="submit"
                    class="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-indigo-600 text-base font-medium text-white hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:ml-3 sm:w-auto sm:text-sm"
                  >
                    Save
                  </button>
                </div>
              </form>
            </DialogPanel>
          </TransitionChild>
        </div>
      </div>
    </Dialog>
  </TransitionRoot>
</template>

<script setup lang="ts">
import { useProjectStore } from '../stores/project-store';
import { Dialog, DialogPanel, TransitionChild, TransitionRoot } from '@headlessui/vue';
import { ModalMode } from '../enums/modal-mode';

defineProps<{ showProjectModal: boolean }>();
const emit = defineEmits(['closeProjectModal']);
const projectStore = useProjectStore();

const onSubmit = () => {
  if (projectStore.projectMode === ModalMode.edit) {
    updateProject();
    emit('closeProjectModal');
  } else if (projectStore.projectMode === ModalMode.create) {
    createProject();
    emit('closeProjectModal');
  } else {
    emit('closeProjectModal');
  }
};

const createProject = async () => {
  await projectStore.createProject(projectStore.project);
  await projectStore.fetchAllProjects();
};

const updateProject = async () => {
  await projectStore.updateProject(projectStore.project._id, projectStore.project);
  await projectStore.fetchAllProjects();
};
</script>

<style scoped></style>
