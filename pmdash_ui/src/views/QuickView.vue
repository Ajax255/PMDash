<template>
  <!-- @click="sidebarOpen = true" -->
  <div class="min-h-full">
    <div v-if="loading === true">loading</div>
    <div v-else-if="loadingError === true">Failed to fetch data please reload page</div>
    <div v-else>
      <side-bar />
      <!-- Main column -->
      <div class="lg:pl-64 flex flex-col">
        <!-- Search header -->
        <div class="sticky top-0 z-10 flex-shrink-0 flex h-16 bg-white border-b border-gray-200 lg:hidden">
          <button
            type="button"
            class="px-4 border-r border-gray-200 text-gray-500 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-purple-500 lg:hidden"
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
            <div class="flex items-center">
              <!-- Profile dropdown -->
              <Menu as="div" class="ml-3 relative">
                <div>
                  <MenuButton
                    class="max-w-xs bg-white flex items-center text-sm rounded-full focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-purple-500"
                  >
                    <span class="sr-only">Open user menu</span>
                    <img
                      class="h-8 w-8 rounded-full"
                      src="https://images.unsplash.com/photo-1502685104226-ee32379fefbe?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80"
                      alt=""
                    />
                  </MenuButton>
                </div>
                <transition
                  enter-active-class="transition ease-out duration-100"
                  enter-from-class="transform opacity-0 scale-95"
                  enter-to-class="transform opacity-100 scale-100"
                  leave-active-class="transition ease-in duration-75"
                  leave-from-class="transform opacity-100 scale-100"
                  leave-to-class="transform opacity-0 scale-95"
                >
                  <MenuItems
                    class="origin-top-right absolute right-0 mt-2 w-48 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 divide-y divide-gray-200 focus:outline-none"
                  >
                    <div class="py-1">
                      <MenuItem v-slot="{ active }">
                        <a
                          href="#"
                          :class="[active ? 'bg-gray-100 text-gray-900' : 'text-gray-700', 'block px-4 py-2 text-sm']"
                          >View profile</a
                        >
                      </MenuItem>
                      <MenuItem v-slot="{ active }">
                        <a
                          href="#"
                          :class="[active ? 'bg-gray-100 text-gray-900' : 'text-gray-700', 'block px-4 py-2 text-sm']"
                          >Settings</a
                        >
                      </MenuItem>
                      <MenuItem v-slot="{ active }">
                        <a
                          href="#"
                          :class="[active ? 'bg-gray-100 text-gray-900' : 'text-gray-700', 'block px-4 py-2 text-sm']"
                          >Notifications</a
                        >
                      </MenuItem>
                    </div>
                    <div class="py-1">
                      <MenuItem v-slot="{ active }">
                        <a
                          href="#"
                          :class="[active ? 'bg-gray-100 text-gray-900' : 'text-gray-700', 'block px-4 py-2 text-sm']"
                          >Get desktop app</a
                        >
                      </MenuItem>
                      <MenuItem v-slot="{ active }">
                        <a
                          href="#"
                          :class="[active ? 'bg-gray-100 text-gray-900' : 'text-gray-700', 'block px-4 py-2 text-sm']"
                          >Support</a
                        >
                      </MenuItem>
                    </div>
                    <div class="py-1">
                      <MenuItem v-slot="{ active }">
                        <a
                          href="#"
                          :class="[active ? 'bg-gray-100 text-gray-900' : 'text-gray-700', 'block px-4 py-2 text-sm']"
                          >Logout</a
                        >
                      </MenuItem>
                    </div>
                  </MenuItems>
                </transition>
              </Menu>
            </div>
          </div>
        </div>
        <main class="flex-1">
          <!-- Page title & actions -->
          <div class="border-b border-gray-200 px-4 py-4 sm:flex sm:items-center sm:justify-between sm:px-6 lg:px-8">
            <div class="flex-1 min-w-0">
              <h1 class="text-lg font-medium leading-6 text-gray-900 sm:truncate">Home</h1>
            </div>
            <div class="mt-4 flex sm:mt-0 sm:ml-4">
              <button
                type="button"
                class="order-1 ml-3 inline-flex items-center px-4 py-2 border border-gray-300 shadow-sm text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-purple-500 sm:order-0 sm:ml-0"
              >
                Share
              </button>
              <button
                type="button"
                class="order-0 inline-flex items-center px-4 py-2 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-purple-600 hover:bg-purple-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-purple-500 sm:order-1 sm:ml-3"
                @click="router.push({ path: '/create-project' })"
              >
                Create
              </button>
            </div>
          </div>
          <project-table />
        </main>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onBeforeMount } from 'vue';
import { useRouter } from 'vue-router';
import ProjectTable from '../components/ProjectTable.vue';
import SideBar from '../components/SideBar.vue';
import { Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/vue';
import { MenuAlt1Icon } from '@heroicons/vue/outline';
import { SearchIcon } from '@heroicons/vue/solid';
import { usePMDashStore } from '../stores/pmdash-store';

const router = useRouter();
const pmDashStore = usePMDashStore();

const loading = ref(true);
const loadingError = ref(false);

const getData = async () => {
  try {
    loading.value = true;
    pmDashStore.searchAllMembers();
    pmDashStore.searchAllTeams();
  } catch (error) {
    loadingError.value = true;
  } finally {
    loading.value = false;
  }
};

onBeforeMount(() => {
  getData();
});
</script>

<style scoped></style>
