<template>
  <div>
    <TransitionRoot as="template" :show="sideBarOpen">
      <Dialog as="div" class="relative z-40 lg:hidden" @close="$emit('closeSideBar')">
        <TransitionChild
          as="template"
          enter="transition-opacity ease-linear duration-300"
          enter-from="opacity-0"
          enter-to="opacity-100"
          leave="transition-opacity ease-linear duration-300"
          leave-from="opacity-100"
          leave-to="opacity-0"
        >
          <div class="fixed inset-0 bg-gray-600 bg-opacity-75" />
        </TransitionChild>

        <div class="fixed inset-0 flex z-40">
          <TransitionChild
            as="template"
            enter="transition ease-in-out duration-300 transform"
            enter-from="-translate-x-full"
            enter-to="translate-x-0"
            leave="transition ease-in-out duration-300 transform"
            leave-from="translate-x-0"
            leave-to="-translate-x-full"
          >
            <DialogPanel class="relative flex-1 flex flex-col max-w-xs w-full pt-5 pb-4 bg-white">
              <TransitionChild
                as="template"
                enter="ease-in-out duration-300"
                enter-from="opacity-0"
                enter-to="opacity-100"
                leave="ease-in-out duration-300"
                leave-from="opacity-100"
                leave-to="opacity-0"
              >
                <div class="absolute top-0 right-0 -mr-12 pt-2">
                  <button
                    type="button"
                    class="ml-1 flex items-center justify-center h-10 w-10 rounded-full focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white"
                    @click="$emit('closeSideBar')"
                  >
                    <span class="sr-only">Close sidebar</span>
                    <XIcon class="h-6 w-6 text-white" aria-hidden="true" />
                  </button>
                </div>
              </TransitionChild>
              <div class="flex-shrink-0 flex items-center px-4">
                <img class="h-8 w-auto" src="..\..\src\assets\pm_logo.png" alt="PMDash" />
                <h1 id="mobile-headline" class="pl-2 font-semibold text-gray-500 uppercase tracking-wider">PMDash</h1>
              </div>
              <div class="mt-5 flex-1 h-0 overflow-y-auto">
                <nav class="px-2">
                  <!-- <div class="space-y-1">
                    <a
                      v-for="item in navigation"
                      :key="item.name"
                      :href="item.href"
                      :class="[
                        item.current ? 'bg-gray-100 text-gray-900' : 'text-gray-600 hover:text-gray-900 hover:bg-gray-50',
                        'group flex items-center px-2 py-2 text-base leading-5 font-medium rounded-md',
                      ]"
                      :aria-current="item.current ? 'page' : undefined"
                    >
                      <component
                        :is="item.icon"
                        :class="[
                          item.current ? 'text-gray-500' : 'text-gray-400 group-hover:text-gray-500',
                          'mr-3 flex-shrink-0 h-6 w-6',
                        ]"
                        aria-hidden="true"
                      />
                      {{ item.name }}
                    </a>
                  </div> -->
                  <div class="mt-8">
                    <div class="flex flex-row items-center">
                      <h3
                        id="mobile-teams-headline"
                        class="pl-3 text-base font-semibold text-gray-500 uppercase tracking-wider"
                      >
                        Teams
                      </h3>
                    </div>
                    <div class="mt-1 space-y-1" role="group" aria-labelledby="mobile-teams-headline">
                      <a
                        v-for="team in pmdashStore.teams"
                        :key="team.name"
                        class="group flex items-center px-3 py-2 text-base leading-5 font-medium text-gray-600 rounded-md hover:text-gray-900 hover:bg-gray-50 relative"
                      >
                        <span :class="[team.bgColorClass, 'w-2.5 h-2.5 mr-4 rounded-full']" aria-hidden="true" />
                        <span class="truncate">
                          {{ team.name }}
                        </span>
                        <Menu as="div" class="flex-shrink-0 pr-2 ml-auto">
                          <MenuButton
                            class="w-8 h-8 text-2xl inline-flex items-center justify-center rounded-full hover:bg-gray-300 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-purple-500"
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
                                    $emit('openTeamModal', {
                                      modalName: 'team-modal',
                                      mode: ModalMode.edit,
                                      uuid: team._id,
                                    })
                                  "
                                >
                                  <div
                                    class="flex flex-row content-center justify-end"
                                    :class="[
                                      active ? 'bg-gray-100 text-gray-900' : 'text-gray-700',
                                      'block px-4 py-2 text-sm',
                                    ]"
                                  >
                                    Edit Team
                                    <component
                                      :is="PencilIcon"
                                      aria-hidden="true"
                                      class="text-gray-700 mr-3 flex-shrink-0 h-5 w-5 ml-2"
                                    />
                                  </div>
                                </MenuItem>
                              </div>
                              <div class="py-1">
                                <MenuItem v-slot="{ active }">
                                  <div
                                    class="flex flex-row content-center justify-end"
                                    :class="[
                                      active ? 'bg-gray-100 text-gray-900' : 'text-gray-700',
                                      'block px-4 py-2 text-sm',
                                    ]"
                                  >
                                    Delete Team
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
                      </a>
                    </div>
                  </div>
                </nav>
              </div>
            </DialogPanel>
          </TransitionChild>
          <div class="flex-shrink-0 w-14" aria-hidden="true">
            <!-- Dummy element to force sidebar to shrink to fit close icon -->
          </div>
        </div>
      </Dialog>
    </TransitionRoot>

    <!-- Static sidebar for desktop -->
    <div
      class="hidden lg:flex lg:flex-col lg:w-64 lg:fixed lg:inset-y-0 lg:border-r lg:border-gray-200 lg:pt-5 lg:pb-4 lg:bg-gray-100"
    >
      <div class="flex items-center flex-shrink-0 px-6 justify-center">
        <img class="h-12 w-auto" src="..\..\src\assets\pm_logo.png" alt="PMDash" />
        <h1 id="desktop-headline" class="px-3 text-xl font-semibold text-gray-500 uppercase tracking-wider">PMDash</h1>
      </div>
      <!-- Sidebar component, swap this element with another sidebar if you like -->
      <div class="mt-6 h-0 flex-1 flex flex-col overflow-y-auto">
        <!-- Sidebar Search -->
        <div class="px-3 mt-4">
          <label for="search" class="sr-only">Search</label>
          <div class="mt-1 relative rounded-md shadow-sm">
            <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none" aria-hidden="true">
              <SearchIcon class="mr-3 h-4 w-4 text-gray-400" aria-hidden="true" />
            </div>
            <input
              id="search"
              v-model="searchTerm"
              type="text"
              name="search"
              class="focus:ring-indigo-500 focus:border-indigo-500 block w-full pl-9 sm:text-sm border-gray-300 rounded-md"
              placeholder="Search"
              @keyup.enter="search()"
            />
          </div>
        </div>
        <!-- Navigation -->
        <nav class="px-3 mt-6">
          <!-- <div class="space-y-1">
            <a
              v-for="item in navigation"
              :key="item.name"
              :href="item.href"
              :class="[
                item.current ? 'bg-gray-200 text-gray-900' : 'text-gray-700 hover:text-gray-900 hover:bg-gray-50',
                'group flex items-center px-2 py-2 text-sm font-medium rounded-md',
              ]"
              :aria-current="item.current ? 'page' : undefined"
            >
              <component
                :is="item.icon"
                :class="[
                  item.current ? 'text-gray-500' : 'text-gray-400 group-hover:text-gray-500',
                  'mr-3 flex-shrink-0 h-6 w-6',
                ]"
                aria-hidden="true"
              />
              {{ item.name }}
            </a>
          </div> -->
          <div class="mt-8">
            <!-- Secondary navigation -->
            <div class="flex flex-row items-center justify-center">
              <h3 id="desktop-teams-headline" class="text-base font-semibold text-gray-500 uppercase tracking-wider">
                Teams
              </h3>
            </div>
            <div class="mt-1 space-y-1" role="group" aria-labelledby="desktop-teams-headline">
              <a
                v-for="team in pmdashStore.teams"
                :key="team.name"
                class="group flex items-center px-3 py-2 text-sm font-medium text-gray-700 rounded-md hover:text-gray-900 hover:bg-gray-50 relative"
              >
                <span :class="[team.bgColorClass, 'w-2.5 h-2.5 mr-4 rounded-full']" aria-hidden="true" />
                <span class="truncate">
                  {{ team.name }}
                </span>
                <Menu as="div" class="flex-shrink-0 pr-2 ml-auto">
                  <MenuButton
                    class="w-8 h-8 text-2xl inline-flex items-center justify-center rounded-full hover:bg-gray-300 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-purple-500"
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
                            $emit('openTeamModal', {
                              modalName: 'team-modal',
                              mode: ModalMode.edit,
                              uuid: team._id,
                            })
                          "
                        >
                          <div
                            class="flex flex-row content-center justify-end"
                            :class="[active ? 'bg-gray-100 text-gray-900' : 'text-gray-700', 'block px-4 py-2 text-sm']"
                          >
                            Edit Team
                            <component
                              :is="PencilIcon"
                              aria-hidden="true"
                              class="text-gray-700 mr-3 flex-shrink-0 h-5 w-5 ml-2"
                            />
                          </div>
                        </MenuItem>
                      </div>
                      <div class="py-1">
                        <MenuItem v-slot="{ active }" @click="deleteTeam(team['_id'])">
                          <div
                            class="flex flex-row content-center justify-end"
                            :class="[active ? 'bg-gray-100 text-gray-900' : 'text-gray-700', 'block px-4 py-2 text-sm']"
                          >
                            Delete Team
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
              </a>
            </div>
          </div>
        </nav>
      </div>
      <div>
        <button
          type="button"
          class="w-28 mx-4 py-2 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-slate-600 hover:bg-slate-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-slate-500 sm:ml-3"
          @click="
            $emit('openTeamModal', {
              modalName: 'team-modal',
              mode: ModalMode.create,
            })
          "
        >
          Create Team
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';

import { Dialog, DialogPanel, TransitionChild, TransitionRoot } from '@headlessui/vue';
import { XIcon } from '@heroicons/vue/outline';
import { SearchIcon } from '@heroicons/vue/solid';
import { usePMDashStore } from '../stores/pmdash-store';
import { useProjectStore } from '../stores/project-store';
import { Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/vue';
import { TrashIcon, PencilIcon } from '@heroicons/vue/outline';
import { ModalMode } from '../enums/modal-mode';

const pmdashStore = usePMDashStore();
const projectStore = useProjectStore();

defineProps<{ sideBarOpen: boolean }>();
defineEmits(['openSideBar', 'closeSideBar', 'openTeamModal']);

// const navigation = [
//   { name: 'Home', href: '#', icon: HomeIcon, current: true },
//   { name: 'My tasks', href: '#', icon: ViewListIcon, current: false },
//   { name: 'Recent', href: '#', icon: ClockIcon, current: false },
// ];

const searchTerm = ref('test');

const search = () => {
  projectStore.searchAllProjects(searchTerm.value, ['title', 'application', 'description', 'initials', 'status']);
  searchTerm.value = '';
};

const deleteTeam = async (uuid: string) => {
  await pmdashStore.deleteTeam(uuid);
  await pmdashStore.fetchAllTeams();
};
</script>

<style scoped></style>
