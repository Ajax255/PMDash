<template>
  <div>
    <!-- Pinned projects -->
    <div v-if="pinnedProjects.length > 0" class="px-4 mt-6 sm:px-6 lg:px-8">
      <h2 class="text-gray-500 text-xs font-medium uppercase tracking-wide">Pinned Projects</h2>
      <ul role="list" class="grid grid-cols-1 gap-4 sm:gap-6 sm:grid-cols-2 xl:grid-cols-4 mt-3">
        <li v-for="project in pinnedProjects" :key="project.title" class="relative col-span-1 flex shadow-sm rounded-md">
          <div
            :class="[
              project.bgColorClass,
              'flex-shrink-0 flex items-center justify-center w-16 text-white text-sm font-medium rounded-l-md',
            ]"
          >
            {{ project.initials }}
          </div>
          <div
            class="flex-1 flex items-center justify-between border-t border-r border-b border-gray-200 bg-white rounded-r-md truncate"
          >
            <div class="flex-1 px-4 py-2 text-sm truncate">
              <a href="#" class="text-gray-900 font-medium hover:text-gray-600">
                {{ project.title }}
              </a>
              <p class="text-gray-500">{{ project.members.length }} Members</p>
            </div>
            <Menu as="div" class="flex-shrink-0 pr-2">
              <MenuButton
                class="w-8 h-8 bg-white inline-flex items-center justify-center text-gray-400 rounded-full hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-purple-500"
              >
                <span class="sr-only">Open options</span>
                <DotsVerticalIcon class="w-5 h-5" aria-hidden="true" />
              </MenuButton>
              <transition
                enter-active-class="transition ease-out duration-100"
                enter-from-class="transform opacity-0 scale-95"
                enter-to-class="transform opacity-100 scale-100"
                leave-active-class="transition ease-in duration-75"
                leave-from-class="transform opacity-100 scale-100"
                leave-to-class="transform opacity-0 scale-95"
              >
                <MenuItems
                  class="z-10 mx-3 origin-top-right absolute right-10 top-3 w-48 mt-1 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 divide-y divide-gray-200 focus:outline-none"
                >
                  <div class="py-1">
                    <MenuItem v-slot="{ active }">
                      <a
                        href="#"
                        :class="[active ? 'bg-gray-100 text-gray-900' : 'text-gray-700', 'block px-4 py-2 text-sm']"
                        >View</a
                      >
                    </MenuItem>
                  </div>
                  <div class="py-1">
                    <MenuItem v-slot="{ active }">
                      <a
                        href="#"
                        :class="[active ? 'bg-gray-100 text-gray-900' : 'text-gray-700', 'block px-4 py-2 text-sm']"
                        >Removed from pinned</a
                      >
                    </MenuItem>
                    <MenuItem v-slot="{ active }">
                      <a
                        href="#"
                        :class="[active ? 'bg-gray-100 text-gray-900' : 'text-gray-700', 'block px-4 py-2 text-sm']"
                        >Share</a
                      >
                    </MenuItem>
                  </div>
                </MenuItems>
              </transition>
            </Menu>
          </div>
        </li>
      </ul>
    </div>

    <!-- Projects list (only on smallest breakpoint) -->
    <div class="mt-10 sm:hidden">
      <div class="px-4 sm:px-6">
        <h2 class="text-gray-500 text-xs font-medium uppercase tracking-wide">Projects</h2>
      </div>
      <ul role="list" class="mt-3 border-t border-gray-200 divide-y divide-gray-100">
        <li v-for="project in projectStore.projects" :key="project.title">
          <a href="#" class="group flex items-center justify-between px-4 py-4 hover:bg-gray-50 sm:px-6">
            <span class="flex items-center truncate space-x-3">
              <span :class="[project.bgColorClass, 'w-2.5 h-2.5 flex-shrink-0 rounded-full']" aria-hidden="true" />
              <span class="font-medium truncate text-sm leading-6">
                {{ project.title }}
                {{ ' ' }}
                <span class="truncate font-normal text-gray-500">in {{ project.application }}</span>
              </span>
            </span>
            <ChevronRightIcon class="ml-4 h-5 w-5 text-gray-400 group-hover:text-gray-500" aria-hidden="true" />
          </a>
        </li>
      </ul>
    </div>

    <div class="hidden mt-8 sm:block">
      <div class="align-middle inline-block min-w-full border-b border-gray-200">
        <table class="min-w-full">
          <thead>
            <tr class="border-t border-gray-200">
              <th
                class="px-6 py-3 border-b border-gray-200 bg-gray-50 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                scope="col"
              >
                <span class="lg:pl-2">Project</span>
              </th>
              <th
                class="px-6 py-3 border-b border-gray-200 bg-gray-50 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                scope="col"
              >
                Members
              </th>
              <th
                class="hidden md:table-cell px-6 py-3 border-b border-gray-200 bg-gray-50 text-right text-xs font-medium text-gray-500 uppercase tracking-wider"
                scope="col"
              >
                Last updated
              </th>
              <th
                class="pr-6 py-3 border-b border-gray-200 bg-gray-50 text-right text-xs font-medium text-gray-500 uppercase tracking-wider"
                scope="col"
              />
              <th
                class="pr-6 py-3 border-b border-gray-200 bg-gray-50 text-right text-xs font-medium text-gray-500 uppercase tracking-wider"
                scope="col"
              />
            </tr>
          </thead>
          <tbody class="bg-white divide-y divide-gray-100">
            <tr v-for="(project, index) in projectStore.projects" :key="index">
              <td class="px-6 py-3 max-w-0 w-full whitespace-nowrap text-sm font-medium text-gray-900">
                <div class="flex items-center space-x-3 lg:pl-2">
                  <div :class="[project.bgColorClass, 'flex-shrink-0 w-2.5 h-2.5 rounded-full']" aria-hidden="true" />
                  <a href="#" class="truncate hover:text-gray-600">
                    <span>
                      {{ project.title }}
                      {{ ' ' }}
                      <span class="text-gray-500 font-normal">in {{ project.application }}</span>
                    </span>
                  </a>
                </div>
              </td>
              <td class="px-6 py-3 text-sm text-gray-500 font-medium">
                <div class="flex items-center space-x-2">
                  <div class="flex flex-shrink-0 -space-x-1">
                    <img
                      v-for="member in project.members"
                      :key="member.handle"
                      class="max-w-none h-6 w-6 rounded-full ring-2 ring-white"
                      :src="member.imageUrl"
                      :alt="member.name"
                    />
                  </div>
                  <span
                    v-if="project.members.length > project.members.length"
                    class="flex-shrink-0 text-xs leading-5 font-medium"
                    >+{{ project.members.length }}</span
                  >
                  <span v-else class="flex-shrink-0 text-xs leading-5 font-medium">{{ project.members.length }}</span>
                </div>
              </td>
              <td class="hidden md:table-cell px-6 py-3 whitespace-nowrap text-sm text-gray-500 text-right">
                {{ showDate(project.created) }}
              </td>
              <td class="py-3 whitespace-nowrap text-right text-sm font-medium relative">
                <Menu as="div" class="flex-shrink-0 pr-2">
                  <MenuButton
                    class="w-8 h-8 text-2xl bg-white inline-flex items-center justify-center text-gray-400 rounded-full hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-purple-500"
                  >
                    <span class="sr-only">Open options</span>
                    &vellip;
                  </MenuButton>
                  <transition
                    enter-active-class="transition ease-out duration-100"
                    enter-from-class="transform opacity-0 scale-95"
                    enter-to-class="transform opacity-100 scale-100"
                    leave-active-class="transition ease-in duration-75"
                    leave-from-class="transform opacity-100 scale-100"
                    leave-to-class="transform opacity-0 scale-95"
                  >
                    <MenuItems
                      class="z-10 mx-3 absolute right-10 top-3 w-48 mt-1 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 divide-y divide-gray-200 focus:outline-none"
                    >
                      <div class="py-1">
                        <MenuItem
                          v-slot="{ active }"
                          @click="
                            $emit('openProjectModal', {
                              modalName: 'project-modal',
                              mode: ModalMode.edit,
                              uuid: project._id,
                            })
                          "
                        >
                          <div
                            class="flex flex-row content-center justify-end"
                            :class="[active ? 'bg-gray-100 text-gray-900' : 'text-gray-700', 'block px-4 py-2 text-sm']"
                          >
                            Edit Project
                            <component
                              :is="PencilIcon"
                              aria-hidden="true"
                              class="text-gray-700 mr-3 flex-shrink-0 h-5 w-5 ml-2"
                            />
                          </div>
                        </MenuItem>
                      </div>
                      <div class="py-1">
                        <MenuItem v-slot="{ active }" @click="deleteProject(project['_id'])">
                          <div
                            class="flex flex-row content-center justify-end"
                            :class="[active ? 'bg-gray-100 text-gray-900' : 'text-gray-700', 'block px-4 py-2 text-sm']"
                          >
                            Delete Project
                            <component
                              :is="TrashIcon"
                              aria-hidden="true"
                              class="text-gray-700 mr-3 flex-shrink-0 h-5 w-5 ml-2"
                            />
                          </div>
                        </MenuItem>
                      </div>
                    </MenuItems>
                  </transition>
                </Menu>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/vue';
import { ChevronRightIcon, DotsVerticalIcon } from '@heroicons/vue/solid';
import { useProjectStore } from '../stores/project-store';
import { TrashIcon, PencilIcon } from '@heroicons/vue/outline';
import { ModalMode } from '../enums/modal-mode';

defineEmits(['openProjectModal']);

const projectStore = useProjectStore();
const pinnedProjects = projectStore.projects.filter((project) => project.pinned);

const showDate = (date: any) => {
  return new Date(date.toLocaleString()).toLocaleString();
};

const deleteProject = async (uuid: string) => {
  await projectStore.deleteProject(uuid);
  await projectStore.fetchAllProjects();
};
</script>

<style scoped></style>
