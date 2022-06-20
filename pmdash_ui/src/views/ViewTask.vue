<template>
  <div v-if="loading === true">loading</div>
  <div v-else-if="loadingError === true">Failed to fetch data please reload page</div>
  <div v-else>
    <div>View Task</div>
  </div>
</template>

<script setup lang="ts">
import { ref, onBeforeMount } from 'vue';
import { useTaskStore } from '../stores/task-store';
import { useRoute } from 'vue-router';

const route = useRoute();
const taskStore = useTaskStore();

const loading = ref(true);
const loadingError = ref(false);

const getData = async () => {
  try {
    loading.value = true;
    taskStore.fetchTask(route.params.uuid as string);
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
