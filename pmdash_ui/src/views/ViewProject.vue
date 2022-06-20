<template>
  <div v-if="loading === true">loading</div>
  <div v-else-if="loadingError === true">Failed to fetch data please reload page</div>
  <div v-else>
    <div>Project Task</div>
  </div>
</template>

<script setup lang="ts">
import { ref, onBeforeMount } from 'vue';
import { useRoute } from 'vue-router';
import { useProjectStore } from '../stores/project-store';

const route = useRoute();
const projectStore = useProjectStore();

const loading = ref(true);
const loadingError = ref(false);

const getData = async () => {
  try {
    loading.value = true;
    projectStore.fetchProject(route.params.uuid as string);
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
